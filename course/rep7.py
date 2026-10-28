"""Volume 7: the repertoire books (complete pieces from the Mutopia Project).

Volumes 1-6 retype short excerpts into content/*.py. Volume 7 prints complete pieces, so it uses
the Mutopia LilyPond sources themselves: each is copied into repertoire/<slug>/, upgraded with
convert-ly and cleaned (its \\header, \\paper and \\midi blocks and paper-size settings removed),
then compiled on its own inside a wrapper that adds the book's paper, page headers and the piece
heading. The book is assembled from the separate PDFs with continuous page numbers.

Usage (from course/):
  python3 rep7.py import SLUG MUTOPIA_PATH   copy, convert and clean one source
                                             (MUTOPIA_PATH: ftp/... main .ly file in a Mutopia clone,
                                              given by --mutopia DIR or $MUTOPIA)
  python3 rep7.py check [SLUG...]            compile pieces alone; print every warning (must be none)
  python3 rep7.py book A|B                   build "Read at Sight - Volume 7A.pdf" (or 7B)
  python3 rep7.py identical                  a finished book must not change (fingerprints7.json)
  python3 rep7.py fingerprint A|B            record a finished book's fingerprint
"""
import importlib
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
REP = os.path.join(ROOT, "repertoire")
OUT = os.path.join(ROOT, "build", "rep7")
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "content"))

import build  # noqa: E402  (shared text helpers: s, para, boxed_list, keyboard_markup)

STAFF_SIZE = 20
TEXT_WIDTH = 94          # as Volume 6 (staff size 20)
BENIGN = ("has been compressed", "page must be compressed", "compressing over-full page")
# Layout-quality messages from LilyPond's beam and slur solvers: the output is drawn, but the place
# must be looked at. `check` lists them as "look at"; they do not fail the build.
COSMETIC = ("may not find good beam slope", "weird stem size", "calculation-in-progress encountered for Slur",
            "calculation-in-progress encountered for PhrasingSlur", "this Voice needs a \\voiceXx",
            "cannot resolve rest collision", "encountered for VerticalAxisGroup.adjacent-pure-heights")
BOOKS = {"A": {"levels": (7, 8), "title": "Volume 7A  -  Repertoire, Levels 7-8"},
         "B": {"levels": (9, 10), "title": "Volume 7B  -  Repertoire, Levels 9-10"}}
SECTIONS = [1, 2, 3, 4, 5]
LOOK = {}  # wrapper name -> cosmetic messages of its last compile
OVERFULL = {}  # wrapper name -> LilyPond had to squeeze a page in its last compile
PAGE_COUNT = {}  # slug -> page count forced to avoid a nearly empty last page (see fit_piece)


# ---------------------------------------------------------------- LilyPond source surgery
def _skip_string(t, i):
    """t[i] == '"': return the index after the closing quote."""
    i += 1
    while i < len(t):
        if t[i] == "\\":
            i += 2
            continue
        if t[i] == '"':
            return i + 1
        i += 1
    return i


def _skip_comment(t, i):
    """t[i] == '%': return the index after the comment."""
    if t.startswith("%{", i):
        j = t.find("%}", i + 2)
        return len(t) if j < 0 else j + 2
    j = t.find("\n", i)
    return len(t) if j < 0 else j


def match_brace(t, i):
    """t[i] == '{': return the index after its matching '}' (strings and comments skipped)."""
    depth = 0
    while i < len(t):
        c = t[i]
        if c == '"':
            i = _skip_string(t, i)
            continue
        if c == "%":
            i = _skip_comment(t, i)
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i + 1
        i += 1
    raise ValueError("unbalanced braces")


def blocks(t, word):
    """Spans (start, end) of every `\\word { ... }` block outside strings and comments."""
    out, i = [], 0
    pat = re.compile(r"\\" + word + r"(?![A-Za-z])\s*\{")
    while i < len(t):
        c = t[i]
        if c == '"':
            i = _skip_string(t, i)
            continue
        if c == "%":
            i = _skip_comment(t, i)
            continue
        m = pat.match(t, i) if c == "\\" else None
        if m:
            end = match_brace(t, m.end() - 1)
            out.append((i, end))
            i = end
            continue
        i += 1
    return out


def cut(t, spans):
    for a, b in sorted(spans, reverse=True):
        t = t[:a] + t[b:]
    return t


def header_fields(t):
    """The string fields of the first \\header block (title, composer, maintainer, ...)."""
    sp = blocks(t, "header")
    if not sp:
        return {}
    h = t[sp[0][0]:sp[0][1]]
    return {k: v for k, v in re.findall(r'(\w+)\s*=\s*"((?:[^"\\]|\\.)*)"', h)}


KEEP_BREAKS = {"satie-gnossienne-1"}  # unbarred music: its line breaks are part of the source


def clean(t, keep_breaks=False):
    """Remove what the book sets itself: headers, paper blocks, paper and staff size, MIDI output.
    A \\score that only makes MIDI (no \\layout) is removed whole."""
    for word in ("book", "bookpart"):  # unwrap: the book's own heading must stay in the same output
        for a, b in sorted(blocks(t, word), reverse=True):
            body = t[a:b]
            inner = body[body.index("{") + 1:-1]
            t = t[:a] + inner + t[b:]
    # page geometry inside \layout blocks is the book's to set
    geom = re.compile(r"^[ \t]*(?:line-width|left-margin|right-margin|indent|short-indent|ragged-bottom|"
                      r"ragged-last-bottom|ragged-right|ragged-last|top-margin|bottom-margin)\s*=[^\n]*\n?", re.M)
    for a, b in sorted(blocks(t, "layout"), reverse=True):
        t = t[:a] + geom.sub("", t[a:b]) + t[b:]
    if not keep_breaks:  # the source's line and page breaks were made for its own page size
        brk = r"\\(?:break|pageBreak|noBreak|noPageBreak)(?![A-Za-z])"
        t = re.sub(r"%" + brk, "%", t)                 # in a comment: drop (never leave "%{", a block comment)
        t = re.sub(r"(?<![A-Za-z%])" + brk, "{}", t)
    t = cut(t, blocks(t, "header"))
    t = cut(t, blocks(t, "paper"))
    drop = []
    for a, b in blocks(t, "score"):
        body = t[a:b]
        if blocks(body, "midi") and not blocks(body, "layout"):
            drop.append((a, b))
    t = cut(t, drop)
    t = cut(t, blocks(t, "midi"))
    # fingerings written as text inside chords (<c-"5-4" e>) must be \finger in current LilyPond
    t = re.sub(r"<[^<>\n]*>", lambda m: re.sub(r'-"([0-9-]+)"', r'-\\finger "\1"', m.group(0)), t)
    t = re.sub(r"#\(set-global-staff-size[^)]*\)", "", t)
    t = re.sub(r"#\(set-default-paper-size[^)]*\)", "", t)
    return t


# ---------------------------------------------------------------- import
def lily_tools():
    lp = build.lilypond_bin()
    return lp, os.path.join(os.path.dirname(lp), "convert-ly")


def reclean(slugs=None):
    """Apply clean() again to imported sources (it is idempotent)."""
    for slug in sorted(os.listdir(REP)):
        if (slugs and slug not in slugs) or not os.path.isdir(os.path.join(REP, slug)):
            continue
        for f in os.listdir(os.path.join(REP, slug)):
            if f.endswith((".ly", ".ily")):
                p = os.path.join(REP, slug, f)
                t = open(p).read()
                c = clean(t, slug in KEEP_BREAKS)
                if c != t:
                    open(p, "w").write(c)
                    print("cleaned", slug, f)


def do_import(slug, path, mutopia):
    src = os.path.join(mutopia, path)
    sdir, main = os.path.split(src)
    dest = os.path.join(REP, slug)
    if os.path.exists(dest):
        shutil.rmtree(dest)
    def keep_only_sources(d, names):  # LilyPond sources only (Mutopia folders also hold PDFs, MIDI, Makefiles)
        return [n for n in names if not (os.path.isdir(os.path.join(d, n)) and not os.path.islink(os.path.join(d, n)))
                and not (n.endswith((".ly", ".ily")) and not os.path.islink(os.path.join(d, n)))]
    shutil.copytree(sdir, dest, ignore=keep_only_sources)
    files = [f for f in os.listdir(dest) if f.endswith((".ly", ".ily"))]
    fields = {}
    for f in files:
        fields.update({k: v for k, v in header_fields(open(os.path.join(dest, f), errors="replace").read()).items()
                       if k not in fields})
    _, cv = lily_tools()
    for f in files:
        subprocess.run([cv, "-e", "--loglevel=ERROR", f], cwd=dest, capture_output=True)
    for f in os.listdir(dest):
        if f.endswith(".ly~") or f.endswith(".ily~"):
            os.remove(os.path.join(dest, f))
    for f in files:
        p = os.path.join(dest, f)
        t = open(p, errors="replace").read()
        open(p, "w").write(clean(t, slug in KEEP_BREAKS))
    with open(os.path.join(dest, "SOURCE.txt"), "w") as o:
        o.write(f"main: {main}\nmutopia_path: {path}\n")
        for k in ("title", "mutopiatitle", "composer", "mutopiacomposer", "opus", "source", "maintainer",
                  "maintainerEmail", "license", "mutopiacopyright", "copyright", "footer"):
            if k in fields:
                o.write(f"{k}: {fields[k]}\n")
    print("imported", slug, "->", main, f"({len(files)} files)")


def source_info(slug):
    info = {}
    for line in open(os.path.join(REP, slug, "SOURCE.txt")):
        if ": " in line:
            k, v = line.rstrip("\n").split(": ", 1)
            info[k] = v
    return info


# ---------------------------------------------------------------- pieces
def pieces(book=None):
    """All Volume 7 pieces in book order (section, then the order in the content file)."""
    out = []
    for sec in SECTIONS:
        try:
            m = importlib.import_module(f"v7sec{sec:02d}")
        except ImportError:
            continue
        for pc in m.PIECES:
            pc = dict(pc, section=sec)
            if book is None or pc["level"] in BOOKS[book]["levels"]:
                out.append(pc)
    return out


def section_module(sec):
    return importlib.import_module(f"v7sec{sec:02d}")


def paper(first_page, header_text, first_header=True, page_count=None, top_padding=None):
    tight = page_count is not None  # fitting one page fewer: closer systems
    cond = "" if first_header else "\\unless \\on-first-page "
    return rf"""
\version "2.24.0"
#(set-global-staff-size {STAFF_SIZE})
\paper {{
  #(set-paper-size "a4")
  top-margin = 14\mm
  bottom-margin = 14\mm
  left-margin = 18\mm
  right-margin = 18\mm{"" if top_padding is None else f"\n  top-system-spacing.padding = {top_padding}"}
  indent = 0
  ragged-bottom = ##f
  ragged-last-bottom = ##t
  first-page-number = {first_page}{"" if not page_count else f"\n  page-count = {page_count}"}
  print-first-page-number = ##t
  markup-system-spacing = #'((basic-distance . 6) (padding . 1.5))
  score-markup-spacing = #'((basic-distance . 6) (padding . 2))
  markup-markup-spacing = #'((basic-distance . 1) (padding . 0.5))
  system-system-spacing = {"#'((basic-distance . 8) (minimum-distance . 6) (padding . 1) (stretchability . 12))" if tight else "#'((basic-distance . 12) (padding . 2) (stretchability . 12))"}
  oddHeaderMarkup = \markup \fill-line {{
    {cond}\fontsize #-2 \italic {build.s(header_text)}
    {cond}\fromproperty #'page:page-number-string
  }}
  evenHeaderMarkup = \markup \fill-line {{
    {cond}\fromproperty #'page:page-number-string
    {cond}\fontsize #-2 \italic {build.s(header_text)}
  }}
  oddFooterMarkup = ##f
  evenFooterMarkup = ##f
}}
\header {{ tagline = ##f }}
\layout {{
  \context {{ \Staff \override TimeSignature.style = #'numbered \remove "Instrument_name_engraver" }}
  \context {{ \PianoStaff \remove "Instrument_name_engraver" }}
}}
"""


def para(text, size=0, width=TEXT_WIDTH):
    return f"\\override #'(line-width . {width}) \\fontsize #{size} \\wordwrap-string #{build.s(text)}"


def piece_heading(pc):
    info = source_info(pc["slug"])
    lic = pc["licence"]
    src = (f"Source: Mutopia Project no. {pc['mutopia']}, typeset by {info.get('maintainer', 'unknown')} "
           f"({'public domain' if lic == 'PD' else lic}).")
    meta = f"Level {pc['level']}   ·   about {pc['minutes']} min"
    who = pc['composer'] + ' (' + pc['dates'] + ')' + ('  -  ' + pc['work'] if pc.get('work') else '')
    return rf"""\markup \column {{
  \fontsize #5 \bold {build.s(pc['title'])}
  \vspace #0.2
  {para(who, 1)}
  \vspace #0.1
  \fontsize #0 \italic {build.s(meta)}
  \vspace #0.4
  {para(pc['note'], -1)}
  \vspace #0.2
  {para(src, -2)}
  \vspace #0.6
}}
"""


def piece_file(pc, first_page, header_text, page_count=None):
    info = source_info(pc["slug"])
    # top_padding (piece option): room above each page's first system, for slurs that rise into the header
    return (paper(first_page, header_text, True, page_count, pc.get("top_padding")) + piece_heading(pc)
            + f'\\include "{info["main"]}"\n')


def compile_ly(code, name, include=None):
    """Write build/rep7/<name>.ly, compile it; return (pdf path, page count, warnings)."""
    os.makedirs(OUT, exist_ok=True)
    ly = os.path.join(OUT, name + ".ly")
    open(ly, "w").write(code)
    cmd = [lily_tools()[0], "-l", "WARNING", "-dno-point-and-click", "-o", os.path.join(OUT, name)]
    if include:
        cmd += ["-I", include]
    try:
        r = subprocess.run(cmd + [ly], capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return None, 0, [f"{name}: LilyPond took more than 10 minutes"]
    pdf = os.path.join(OUT, name + ".pdf")
    msg = re.compile(r"^(?:.*?:\d+:\d+: |)(?:warning|error|programming error|fatal error):")
    warns = [l for l in r.stderr.splitlines() if msg.match(l) and not any(b in l for b in BENIGN)]
    LOOK[name] = [l for l in warns if any(c in l for c in COSMETIC)]
    OVERFULL[name] = any(b in r.stderr for b in BENIGN)
    warns = [l for l in warns if not any(c in l for c in COSMETIC)]
    if r.returncode != 0 or not os.path.exists(pdf):
        return None, 0, warns or r.stderr.splitlines()[-5:]
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True,
                                                              text=True).stdout).group(1))
    return pdf, pages, warns


def compile_piece(pc, first_page=1, header_text="Read at Sight  -  Volume 7", page_count=None):
    # the wrapper's name must differ from every source file name, or \include finds the wrapper itself
    return compile_ly(piece_file(pc, first_page, header_text, page_count), "piece--" + pc["slug"],
                      os.path.join(REP, pc["slug"]))


def last_page_fill(pdf, n):
    """How far down the last page the music reaches (0-1)."""
    png = pdf[:-4] + "-last"
    subprocess.run(["pdftoppm", "-r", "20", "-png", "-singlefile", "-f", str(n), "-l", str(n), pdf, png], check=True)
    from PIL import Image
    im = Image.open(png + ".png").convert("L")
    w, h = im.size
    px = im.load()
    rows = [y for y in range(h) if any(px[x, y] < 128 for x in range(w))]
    os.remove(png + ".png")
    return (max(rows) + 1) / h if rows else 0


def fit_piece(pc, header_text="Read at Sight  -  Volume 7"):
    """Compile a piece; if its last page holds only a system or two, try one page fewer, and keep
    that only if LilyPond does not have to squeeze any page. Remembers the choice in PAGE_COUNT."""
    PAGE_COUNT.pop(pc["slug"], None)
    pdf, n, warns = compile_piece(pc, 1, header_text)
    if not pdf or warns or n < 2 or last_page_fill(pdf, n) > 0.4:
        return pdf, n, warns
    pdf2, n2, warns2 = compile_piece(pc, 1, header_text, n - 1)
    if pdf2 and not warns2 and n2 == n - 1 and not OVERFULL["piece--" + pc["slug"]]:
        PAGE_COUNT[pc["slug"]] = n - 1
        return pdf2, n2, warns2
    return compile_piece(pc, 1, header_text)


def check(slugs):
    bad = 0
    for pc in pieces():
        if slugs and pc["slug"] not in slugs:
            continue
        pdf, n, warns = fit_piece(pc)
        status = "OK" if pdf and not warns else "PROBLEM"
        bad += status != "OK"
        look = LOOK.get("piece--" + pc["slug"], [])
        print(f"{pc['slug']:28} {n:3} pp  {status}" + (" (one page saved)" if pc["slug"] in PAGE_COUNT else "")
              + (f"  (look at {len(look)} places)" if look else ""))
        for w in warns[:12]:
            print("   ", w)
    print("all OK" if not bad else f"{bad} with problems")
    return bad


# ---------------------------------------------------------------- front and back matter
def title_page(book):
    B = BOOKS[book]
    lo, hi = B["levels"]
    n = len(pieces(book))
    kb = build.keyboard_markup(21, 35, [], {28: "Middle C"})
    return rf"""\markup \column {{
  \vspace #10
  \fill-line {{ \fontsize #12 \bold "Read at Sight" }}
  \vspace #1
  \fill-line {{ \fontsize #4 \italic "A graded sight-reading course for piano" }}
  \vspace #2
  \fill-line {{ \fontsize #6 {build.s(B['title'])} }}
  \vspace #6
  \fill-line {{ {kb} }}
  \vspace #12
  \fill-line {{ \override #'(line-width . 70) \fontsize #1 \center-column {{
    {build.s(f'{n} complete pieces by the great keyboard composers,')}
    {build.s('from Bach to Debussy and Joplin, to learn and keep.')}
  }} }}
  \vspace #2
  \fill-line {{ \fontsize #-1 \italic "Scores from the Mutopia Project: public domain or Creative Commons (see the last page)." }}
}}
\pageBreak
"""


HOW_TO_7 = [
    ("What this book is",
     "Volumes 1-6 taught you to read. This book is music to learn and keep: complete pieces, not exercises. Each one "
     "will take from a few days to a few weeks. Every piece is printed in full, exactly as its composer wrote it."),
    ("Levels",
     "Each piece has a level. Level 7 pieces can be learned in days after Volume 6; Level 8 pieces take a week or two "
     "(faster passages, wider stretches, pedal and voicing matter). Book 7B continues with Levels 9 and 10. The index at "
     "the back lists this book's pieces by level: a suggested order."),
    ("How to learn a piece",
     "1. Read it through once at sight, slowly, without stopping, to hear what it is. "
     "2. Find the hard places and learn them first, hands separately, then together, slowly with a metronome. "
     "3. Learn the piece in sections of four to eight bars, joining each to the next. "
     "4. Raise the speed in small steps; never faster than you can play evenly. "
     "5. Then play it for someone. A piece is learned when you can play it steadily after a day away from it."),
    ("Keep reading",
     "Do not stop sight-reading while you learn these pieces. Ten minutes a day of new music at Level 6-7 keeps your reading "
     "growing: hymns, chorales, easier pieces by the composers in this book."),
    ("The sources",
     "The scores were engraved by volunteers of the Mutopia Project and are public domain or Creative Commons. The note "
     "above each piece names its source; the last page lists them all with their licences."),
]


def how_to_page():
    out = ["\\markup \\column { \\fontsize #6 \\bold \"How to use this book\" \\vspace #1 }"]
    for head, body in HOW_TO_7:
        out.append(f"\\markup \\column {{ \\fontsize #2 \\bold {build.s(head)} \\vspace #0.3 {para(body, 1)} \\vspace #0.6 }}")
    return "\n".join(out)


def contents_markup(book, pages):
    """pages: {slug: first page, ('sec', n): page}."""
    rows = []
    for sec in SECTIONS:
        ps = [p for p in pieces(book) if p["section"] == sec]
        if not ps:
            continue
        m = section_module(sec)
        rows.append(f"\\vspace #1.0 \\override #'(line-width . {TEXT_WIDTH}) \\fill-line {{ \\line {{ \\fontsize #2 \\bold "
                    f"{build.s(m.TITLE)} }} \\fontsize #2 \\bold {build.s(str(pages.get(('sec', sec), '00')))} }}")
        for p in ps:
            left = f"{p['composer']}: {p['title']}"
            rows.append(f"\\vspace #0.15 \\override #'(line-width . {TEXT_WIDTH}) \\fill-line {{ \\line {{ \\hspace #3 "
                        f"{build.s(left)} \\hspace #1 \\italic {build.s('(' + str(p['level']) + ')')} }} "
                        f"{build.s(str(pages.get(p['slug'], '00')))} }}")
    return ("\\markup \\override #'(baseline-skip . 0) \\column { \\fontsize #6 \\bold \"Contents\" \\vspace #0.6 "
            + para("Level in brackets. Sections follow history; within a section, pieces go from easier to harder by composer.", 0)
            + " " + " ".join(rows) + " }")


def section_page(sec, book):
    m = section_module(sec)
    ps = [p for p in pieces(book) if p["section"] == sec]
    items = " ".join(f"\\vspace #0.2 \\line {{ \\hspace #3 {build.s(p['composer'] + ': ' + p['title'])} "
                     f"\\italic {build.s('(Level ' + str(p['level']) + ')')} }}" for p in ps)
    return rf"""\markup \column {{
  \vspace #4
  \fontsize #2 \italic {build.s('Section ' + str(sec))}
  \fontsize #8 \bold {build.s(m.TITLE)}
  \vspace #1.5
  {para(m.INTRO, 1)}
  \vspace #1
  \fontsize #2 \bold "What it asks of you"
  \vspace #0.3
  {para(m.ASKS, 1)}
  \vspace #1.2
  \fontsize #2 \bold "In this section"
  \vspace #0.3
  {items}
}}
"""


def index_markup(book, pages):
    """One \\markup per line, so that the index can run onto a second page."""
    out = ["\\markup \\column { \\fontsize #6 \\bold \"Pieces by level\" \\vspace #0.6 "
           + para(f"A suggested order: start at the top of Level {BOOKS[book]['levels'][0]} and choose freely within a level. Mix the eras: a Baroque piece "
                  "trains the fingers and the ear for voices, a Romantic one the pedal and the singing tone.", 0) + " }"]
    for lev in BOOKS[book]["levels"]:
        ps = sorted((p for p in pieces(book) if p["level"] == lev), key=lambda p: pages[p["slug"]])
        out.append(f"\\markup \\column {{ \\vspace #0.6 \\fontsize #3 \\bold {build.s('Level ' + str(lev))} }}")
        for p in ps:
            out.append(f"\\markup \\override #'(line-width . {TEXT_WIDTH}) \\fill-line {{ \\line {{ \\hspace #3 "
                       f"{build.s(p['composer'] + ': ' + p['title'])} }} {build.s(str(pages[p['slug']]))} }}")
    return "\n".join(out)


LICENCE_TEXT = (
    "Every score in this book comes from the Mutopia Project (www.mutopiaproject.org), whose volunteers engrave public-domain "
    "music with LilyPond. Each source was upgraded to the current LilyPond version and set in this book's layout; the notes "
    "were not changed (a few engraving slips, such as unclosed slurs and zigzag beams, were corrected). Public-domain sources may be used freely. Sources under Creative Commons Attribution-ShareAlike (CC BY-SA) "
    "require credit (given below) and that adapted versions be shared under the same licence: this book's engravings of those "
    "pieces are therefore released under CC BY-SA 4.0. Sources under CC BY 3.0 require credit only.")


def licences_markup(book):
    """One \\markup per entry, so that the list can run onto a second page."""
    out = ["\\markup \\column { \\fontsize #6 \\bold \"Sources and licences\" \\vspace #0.6 "
           + para(LICENCE_TEXT, -1) + " \\vspace #0.4 }"]
    for p in pieces(book):
        info = source_info(p["slug"])
        lic = "public domain" if p["licence"] == "PD" else p["licence"]
        text = (p["composer"] + ": " + p["title"] + ". Mutopia no. " + str(p["mutopia"]) + ", typeset by "
                + info.get("maintainer", "unknown") + "; " + lic + ".")
        out.append(f"\\markup \\override #'(baseline-skip . 2.2) {para(text, -2)}")
    return "\n".join(out)


# ---------------------------------------------------------------- the book
def book_pdf(book):
    B = BOOKS[book]
    head = f"Read at Sight  -  {B['title']}"
    ps = pieces(book)
    # pass 1: page counts (they do not depend on the page numbers)
    counts = {}
    for p in ps:
        pdf, n, warns = fit_piece(p, head)
        if not pdf or warns:
            print("PROBLEM", p["slug"], *warns[:5], sep="\n  ")
            raise SystemExit(1)
        counts[p["slug"]] = n

    def matter(name, code, first, first_header=False):
        return compile_ly(paper(first, head, first_header) + code, name)

    _, n_front, _ = matter("front", title_page(book) + how_to_page(), 1)
    _, n_cont, _ = matter("contents", contents_markup(book, {}), n_front + 1)
    pages, page = {}, n_front + n_cont + 1
    order = []
    for sec in SECTIONS:
        sp = [p for p in ps if p["section"] == sec]
        if not sp:
            continue
        pages[("sec", sec)] = page
        order.append(("sec", sec, page))
        page += 1
        for p in sp:
            pages[p["slug"]] = page
            order.append(("piece", p, page))
            page += counts[p["slug"]]
    files = []
    f, _, _ = matter("front", title_page(book) + how_to_page(), 1)
    files.append(f)
    f, n, _ = matter("contents", contents_markup(book, pages), n_front + 1)
    assert n == n_cont, "contents length changed"
    files.append(f)
    for kind, x, first in order:
        if kind == "sec":
            f, n, w = matter(f"section{x}", section_page(x, book), first, True)
            assert n == 1 and not w, (x, n, w)
        else:
            f, n, w = compile_piece(x, first, head, PAGE_COUNT.get(x["slug"]))
            assert n == counts[x["slug"]] and not w, (x["slug"], n, w)
        files.append(f)
    f, n_idx, w = matter("index", index_markup(book, pages), page, True)
    files.append(f)
    f, n_lic, w = matter("licences", licences_markup(book), page + n_idx, True)
    files.append(f)
    out = os.path.join(ROOT, "build", f"Read at Sight - Volume 7{book}.pdf")
    subprocess.run(["pdfunite", *files, out], check=True)
    total = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", out], capture_output=True, text=True).stdout).group(1))
    print(f"built {out}: {total} pages, {len(ps)} pieces")


# ---------------------------------------------------------------- fingerprints
FP_FILE = os.path.join(HERE, "fingerprints7.json")


def fingerprint(book):
    """SHA-256 of everything a book is made of: its sources, headings and front and back matter."""
    import hashlib
    h = hashlib.sha256()
    head = f"Read at Sight  -  {BOOKS[book]['title']}"
    h.update((title_page(book) + how_to_page() + contents_markup(book, {}) + licences_markup(book)).encode())
    for sec in SECTIONS:
        if any(p["section"] == sec for p in pieces(book)):
            h.update(section_page(sec, book).encode())
    for p in pieces(book):
        h.update(piece_file(p, 1, head).encode())
        d = os.path.join(REP, p["slug"])
        for f in sorted(os.listdir(d)):
            h.update(f.encode() + open(os.path.join(d, f), "rb").read())
    return h.hexdigest()


def identical():
    import json
    stored = json.load(open(FP_FILE)) if os.path.exists(FP_FILE) else {}
    bad = 0
    for book, fp in sorted(stored.items()):
        same = fingerprint(book) == fp
        bad += not same
        print(f"Volume 7{book}: {'identical' if same else 'CHANGED'}")
    return bad


def record(book):
    import json
    stored = json.load(open(FP_FILE)) if os.path.exists(FP_FILE) else {}
    stored[book] = fingerprint(book)
    json.dump(stored, open(FP_FILE, "w"), indent=1, sort_keys=True)
    print(f"recorded Volume 7{book}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__)
    elif a[0] == "import":
        mut = os.environ.get("MUTOPIA", "")
        if "--mutopia" in a:
            i = a.index("--mutopia")
            mut = a[i + 1]
            a = a[:i] + a[i + 2:]
        do_import(a[1], a[2], mut)
    elif a[0] == "reclean":
        reclean(a[1:])
    elif a[0] == "check":
        sys.exit(1 if check(a[1:]) else 0)
    elif a[0] == "book":
        book_pdf(a[1])
    elif a[0] == "identical":
        sys.exit(1 if identical() else 0)
    elif a[0] == "fingerprint":
        record(a[1])
