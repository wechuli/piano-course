"""Build the course book (or a single unit) as a print-ready A4 PDF with LilyPond.

Usage:  python3 build.py [--vol N] [unit ids...]   e.g. python3 build.py --vol 2 1 2 3
Output: ../build/read-at-sight-volN[-unitM].pdf
"""
import importlib
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "content"))

from units import VOLUME1, VOLUME2, POSITIONS  # noqa: E402
from generator import generate_unit, lily_exercise  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "build")
TEXT_WIDTH = 86  # line width for wrapped text, in staff spaces (A4, staff size 22)

VOLUMES = {
    1: {"units": VOLUME1, "subtitle": "Volume 1  -  First Steps", "content": "unit",
        "blurb": ["Hundreds of short, new exercises at exactly your level,",
                  "with tips, checkpoints and real pieces along the way."],
        "extra": []},
    2: {"units": VOLUME2, "subtitle": "Volume 2  -  Moving Hands", "content": "v2unit",
        "blurb": ["Your hands leave home: shifts, stretches, new keys and minor keys,",
                  "with legato, staccato and dynamics to bring the music to life."],
        "skip": ["Why this book is built this way"],
        "extra": [
            ("What is new in Volume 2",
             "In Volume 1 each exercise stayed in one hand position. Now the hands move. A finger number in the "
             "middle of an exercise means: shift your hand now, so that finger lands on that note. You will also read "
             "slurs, staccato dots and dynamics, and play in G major, F major and three minor keys. "
             "Start this book when you can read both clefs in C and G positions, hands together, with eighth notes, "
             "rests and ties."),
        ]},
}


def lilypond_bin():
    try:
        import lilypond
        return str(lilypond.executable())
    except ImportError:
        return "lilypond"


def s(text):
    """Quote a Python string as a LilyPond/Scheme string literal."""
    return '"' + text.replace("\\", "\\\\").replace('"', '\\"') + '"'


def para(text, size=0):
    return f"\\override #'(line-width . {TEXT_WIDTH}) \\fontsize #{size} \\wordwrap-string #{s(text)}"


# ---------------------------------------------------------------- preamble
PREAMBLE = r"""
\version "2.24.0"
#(set-global-staff-size 22)

\paper {
  #(set-paper-size "a4")
  top-margin = 14\mm
  bottom-margin = 14\mm
  left-margin = 18\mm
  right-margin = 18\mm
  indent = 0
  ragged-bottom = ##t
  ragged-last-bottom = ##t
  print-first-page-number = ##f
  page-breaking = #ly:minimal-breaking
  markup-system-spacing = #'((basic-distance . 5) (padding . 1.2))
  score-markup-spacing = #'((basic-distance . 6) (padding . 2))
  markup-markup-spacing = #'((basic-distance . 1) (padding . 1.2))
  score-system-spacing = #'((basic-distance . 12) (padding . 2.5))
  system-system-spacing = #'((basic-distance . 12) (padding . 2.5))
  oddHeaderMarkup = \markup \fill-line {
    \unless \on-first-page \fontsize #-2 \italic "@@HEADER@@"
    \unless \on-first-page \fromproperty #'page:page-number-string
  }
  evenHeaderMarkup = \markup \fill-line {
    \unless \on-first-page \fromproperty #'page:page-number-string
    \unless \on-first-page \fontsize #-2 \italic "@@HEADER@@"
  }
  oddFooterMarkup = ##f
  evenFooterMarkup = ##f
}

\header { tagline = ##f }

\layout {
  indent = 0
  ragged-right = ##f
  \context { \Score
    \override BarNumber.break-visibility = ##(#f #f #f)
  }
  \context { \Staff
    \override Fingering.font-size = #-3
    \override TimeSignature.style = #'numbered
  }
}

#(define-markup-command (exLabel layout props txt) (string?)
  (interpret-markup layout props
    (markup #:line (#:override '(box-padding . 0.35) #:box (#:fontsize -2 #:transparent "M")
                    #:fontsize 1 #:bold txt))))
"""


def boxed_list(title, items, numbered=True):
    """A rounded box with a heading and wrapped list items that never overlap."""
    rows = []
    for i, t in enumerate(items):
        mark = f"{i + 1}." if numbered else "-"
        rows.append(f"\\vspace #0.5 \\line {{ \\bold \"{mark}\" \\override #'(baseline-skip . 3) "
                    f"\\override #'(line-width . {TEXT_WIDTH - 8}) \\wordwrap-string #{s(t)} }}")
    return (f"\\markup \\column {{ \\vspace #0.8 \\override #'(box-padding . 1.4) \\rounded-box "
            f"\\override #'(baseline-skip . 0) \\column {{ \\fontsize #2 \\bold {s(title)} "
            + " ".join(rows) + " } }")


def tempo_mk(bpm):
    return f"\\concat {{ \\general-align #Y #DOWN \\fontsize #-2 \\note {{4}} #UP \" = {bpm}\" }}"


# ---------------------------------------------------------------- keyboard diagram
COLORS = {"RH": ("(rgb-color 0.72 0.85 0.97)", "(rgb-color 0.22 0.42 0.72)"),
          "LH": ("(rgb-color 0.76 0.92 0.76)", "(rgb-color 0.18 0.52 0.28)"),
          "RH*": ("(rgb-color 0.90 0.95 1.0)", "(rgb-color 0.22 0.42 0.72)"),   # stretch keys
          "LH*": ("(rgb-color 0.91 0.97 0.91)", "(rgb-color 0.18 0.52 0.28)")}


def position_keys(pos_key):
    """List of (white_step, acc, finger, hand) for a five-finger position.
    acc is None, 'is' (black key above the step) or 'es' (black key below)."""
    pos = POSITIONS[pos_key]
    accs = pos.get("acc", {})
    out = []
    for i, st in enumerate(range(pos["low"], pos["high"] + 1)):
        finger = i + 1 if pos["hand"] == "RH" else 5 - i
        out.append((st, accs.get(st), finger, pos["hand"]))
    return out


def keyboard_markup(first, last, keys, labels):
    """Draw white keys first..last (diatonic steps); highlight keys with finger numbers."""
    w, h, bw, bh = 2.6, 10.0, 1.6, 6.2
    white_mark, black_mark = {}, {}
    for st, acc, finger, hand in keys:
        if acc is None:
            white_mark[st] = (finger, hand)
        else:
            below = st if acc == "is" else st - 1  # black key sits just above this white step
            black_mark[below] = (finger, hand)
    items = []
    whites = list(range(first, last + 1))
    for i, st in enumerate(whites):
        x0 = i * w
        items.append(f"\\translate #'({x0} . 0) \\filled-box #'(0 . {w}) #'(0 . {h}) #0")
        fill = COLORS[white_mark[st][1]][0] if st in white_mark else "white"
        items.append(f"\\translate #'({x0 + 0.12} . 0.12) \\with-color #{fill} "
                     f"\\filled-box #'(0 . {w - 0.24}) #'(0 . {h - 0.24}) #0")
    for i, st in enumerate(whites[:-1]):
        if st % 7 in (0, 1, 3, 4, 5):  # black key after C, D, F, G, A
            x0 = (i + 1) * w - bw / 2
            items.append(f"\\translate #'({x0} . {h - bh}) \\filled-box #'(0 . {bw}) #'(0 . {bh}) #0.1")
            if st in black_mark:
                finger, hand = black_mark[st]
                items.append(f"\\translate #'({x0 + 0.15} . {h - bh + 0.15}) \\with-color #{COLORS[hand][1]} "
                             f"\\filled-box #'(0 . {bw - 0.3}) #'(0 . {bh - 0.3}) #0.1")
                items.append(f"\\translate #'({x0 + bw / 2} . {h - bh + 0.9}) \\center-align "
                             f"\\with-color #white \\fontsize #-2 \\bold \"{finger}\"")
    for i, st in enumerate(whites):
        if st in white_mark:
            items.append(f"\\translate #'({i * w + w / 2} . 1.6) \\center-align \\fontsize #-1 "
                         f"\\bold \"{white_mark[st][0]}\"")
        if st in labels:
            items.append(f"\\translate #'({i * w + w / 2} . -2.2) \\center-align \\fontsize #-3 \"{labels[st]}\"")
    return "\\overlay {\n    " + "\n    ".join(items) + "\n  }"


def unit_positions(unit, content):
    if getattr(content, "KEYBOARD", None):
        return content.KEYBOARD
    from generator import hand_options
    first = unit["parts"][0]
    lh, rh = hand_options(first, "LH"), hand_options(first, "RH")
    if first["mode"] == "RH":
        return rh[:1]
    if first["mode"] == "LH":
        return lh[:1]
    return lh[:1] + rh[:1]


def note_name_markup(st, acc):
    letter = "CDEFGAB"[st % 7]
    if acc == "is":
        return f"\\concat {{ \"{letter}\" \\raise #0.6 \\fontsize #-3 \\sharp }}"
    if acc == "es":
        return f"\\concat {{ \"{letter}\" \\raise #0.4 \\fontsize #-3 \\flat }}"
    return f"\"{letter}\""


def note_map_score(pos_keys):
    """Small score showing each position's five notes, finger numbers and names."""
    from generator import lily_pitch
    rh, lh = [], []
    for pk in pos_keys:
        for st, acc, finger, hand in position_keys(pk):
            p = lily_pitch(st, {"cdefgab"[st % 7]: acc} if acc else None)
            name = note_name_markup(st, acc)
            if hand == "RH":
                rh.append(f"{p}1^\\markup \\bold \"{finger}\" _\\markup {name}")
            else:
                lh.append(f"{p}1_\\markup \\center-column {{ \\bold \"{finger}\" {name} }}")
    title = "Your five notes" if len(pos_keys) == 1 else "Your notes"
    nostime = "\\with { \\remove \"Time_signature_engraver\" }"
    if rh and lh:
        music = (f"\\new PianoStaff << \\new Staff {nostime} {{ \\clef treble \\cadenzaOn s1*{len(lh)} "
                 f"{' '.join(rh)} \\bar \"||\" }} \\new Staff {nostime} {{ \\clef bass \\cadenzaOn "
                 f"{' '.join(lh)} s1*{len(rh)} \\bar \"||\" }} >>")
    else:
        clef = "treble" if rh else "bass"
        music = f"\\new Staff {nostime} {{ \\clef {clef} \\cadenzaOn {' '.join(rh or lh)} \\bar \"||\" }}"
    return f"""\\score {{
  \\header {{ piece = \\markup \\fontsize #1 \\bold "{title}" }}
  {music}
  \\layout {{ ragged-right = ##t \\context {{ \\Staff \\override Accidental.font-size = #-1 }} }}
}}"""


# ---------------------------------------------------------------- front matter
def title_page(vol):
    V = VOLUMES[vol]
    kb = keyboard_markup(21, 35, [], {28: "Middle C"})
    return rf"""
\markup \column {{
  \vspace #10
  \fill-line {{ \fontsize #12 \bold "Read at Sight" }}
  \vspace #1
  \fill-line {{ \fontsize #4 \italic "A graded sight-reading course for piano" }}
  \vspace #2
  \fill-line {{ \fontsize #6 {s(V["subtitle"])} }}
  \vspace #6
  \fill-line {{ {kb} }}
  \vspace #12
  \fill-line {{ \override #'(line-width . 70) \fontsize #1 \center-column {{
    {s(V["blurb"][0])}
    {s(V["blurb"][1])}
  }} }}
  \vspace #2
  \fill-line {{ \fontsize #-1 \italic "Exercises generated to graded rules; pieces are original or public domain." }}
}}
\pageBreak
"""


HOW_TO = [
    ("Why this book is built this way",
     "You get better at sight-reading by reading a lot of new music that is easy for you, not by struggling through hard pieces. "
     "So every unit gives you many short exercises that use only what you have learned so far, plus a few real pieces."),
    ("The five rules",
     "1. Never stop: keep the beat going, even after a wrong note. "
     "2. Count out loud and use a metronome at the speed shown. "
     "3. Keep your eyes on the music, not your hands. "
     "4. Read the shape: up, down, or the same, and by how much. "
     "5. Play each exercise once, tick its box, and move on. Come back only after a few weeks."),
    ("Before every exercise: 10 seconds",
     "Check the clef and time signature. Find the first note and its finger number. "
     "Scan for the highest and lowest note, and for any bar that repeats an earlier one. Then count one bar in and play."),
    ("How each unit is laid out",
     "A unit opens with what is new, a keyboard picture of the hand position, and reading tips. "
     "Then come Parts A, B and C, which grow slightly harder. Pieces come next, and the unit ends with a checkpoint that tells you when to move on."),
    ("A daily routine (15-20 minutes)",
     "Warm up by playing the five notes of the hand position up and down, saying their names (2 minutes). "
     "Read 6-10 new exercises, one pass each (10 minutes). Play one piece, aiming for steady and musical (5 minutes)."),
]

OVERVIEW_NOTE = "Each unit adds exactly one new idea to everything before it."


def how_to_page(vol):
    V = VOLUMES[vol]
    out = ["\\markup \\column { \\fontsize #6 \\bold \"How to use this book\" \\vspace #1 }"]
    for head, body in V["extra"] + [h for h in HOW_TO if h[0] not in V.get("skip", [])]:
        out.append(f"\\markup \\column {{ \\fontsize #2 \\bold {s(head)} \\vspace #0.3 {para(body, 1)} \\vspace #0.6 }}")
    out.append("\\pageBreak")
    rows = []
    for u in V["units"]:
        rows.append(f"\\vspace #0.9 \\override #'(line-width . {TEXT_WIDTH}) \\fill-line {{ \\line {{ \\fontsize #2 \\bold "
                    f"\"Unit {u['id']}\" \\hspace #1 \\fontsize #2 {s(u['title'])} }} "
                    f"\\fontsize #2 \\page-ref #'unit{u['id']} \"00\" \" \" }}")
        rows.append(f"\\vspace #0.2 \\line {{ \\hspace #6 \\italic {s(u['new'])} }}")
    out.append("\\markup \\override #'(baseline-skip . 0) \\column { \\fontsize #6 \\bold \"Contents\" "
               "\\vspace #0.8 " + para(OVERVIEW_NOTE, 1) + " " + " ".join(rows) + " }")
    out.append("\\pageBreak")
    return "\n".join(out)


# ---------------------------------------------------------------- unit pages
def unit_pages(unit, vol=1):
    try:
        content = importlib.import_module(f"{VOLUMES[vol]['content']}{unit['id']:02d}")
    except ModuleNotFoundError:  # preview: exercises only, placeholder text
        import types
        content = types.SimpleNamespace(
            INTRO=["[Preview - unit text not written yet. Create content/unit%02d.py]" % unit["id"]],
            NEW_IDEAS=[], TIPS=["[tips go here]"], PART_NOTES={}, PIECES=[], CHECKPOINT=["[checkpoint goes here]"])
    out = [f"\\label #'unit{unit['id']}"]
    out.append(f"""\\markup \\column {{
  \\fontsize #3 \\italic "Unit {unit['id']}"
  \\vspace #0.6
  \\fontsize #7 \\bold {s(unit['title'])}
  \\vspace #0.5
  \\fontsize #0 \\italic {s('New: ' + unit['new'])}
  \\vspace #1
}}""")
    for p in content.INTRO:
        out.append(f"\\markup {para(p, 1)}")
    # Keyboard picture(s) of the hand position(s) used in this unit
    groups = getattr(content, "KEYBOARDS", None) or [unit_positions(unit, content)]
    for pos_keys in groups:
        keys = [k for pk in pos_keys for k in position_keys(pk)]
        hands_here = {POSITIONS[pk]["hand"] for pk in pos_keys}
        keys += [(st, None, f, h + "*") for st, f, h in getattr(content, "STRETCH", []) if h in hands_here]
        lo = min(k[0] for k in keys)
        hi = max(k[0] for k in keys)
        first_key = 21 if lo >= 21 else lo - 1
        last_key = 35 if hi <= 35 else hi + 1
        kb = keyboard_markup(first_key, last_key, keys, {28: "Middle C"})
        if len(pos_keys) == 1:
            caption = POSITIONS[pos_keys[0]]["label"] + ": finger numbers on the keys"
            if any(h in hands_here for _, _, h in getattr(content, "STRETCH", [])):
                caption += " (pale keys: stretches)"
        else:
            caption = " and ".join(POSITIONS[pk]["label"] for pk in pos_keys) + " (green: left hand, blue: right hand)"
        out.append(f"\\markup \\column {{ \\vspace #1 \\fill-line {{ {kb} }} \\vspace #3.2 "
                   f"\\fill-line {{ \\fontsize #-1 \\italic {s(caption)} }} \\vspace #0.5 }}")
        out.append(note_map_score(pos_keys))
    # New ideas
    for i, (head, body) in enumerate(content.NEW_IDEAS):
        lead = "\\vspace #0.5 \\fontsize #3 \\bold \"What is new\" \\vspace #0.3 " if i == 0 else ""
        out.append(f"\\markup \\override #'(line-width . {TEXT_WIDTH}) \\column {{ {lead}\\fontsize #1 \\bold {s(head)} {para(body, 0)} }}")
    # Tips box
    out.append(boxed_list("Reading tips", content.TIPS))
    out.append("\\pageBreak")

    # Exercise parts
    n = 0
    for part, exercises in generate_unit(unit, seed=vol * 1000 + unit["id"]):
        out.append(f"""\\markup \\column {{
  \\vspace #0.6
  \\line {{ \\fontsize #4 \\bold {s('Part ' + part['name'] + ': ' + part['title'])} \\hspace #3 \\fontsize #1 {tempo_mk(part['tempo'])} }}
  \\vspace #0.2
  {para(content.PART_NOTES.get(part['name'], ''), 0)}
  \\vspace #0.3
}}""")
        for ex in exercises:
            n += 1
            out.append(lily_exercise(part, ex, f"{unit['id']}.{n}"))
        out.append("\\pageBreak")

    # Pieces
    out.append(f"""\\markup \\column {{
  \\fontsize #5 \\bold "Pieces"
  \\vspace #0.3
  {para('Pieces are for playing more than once. Read each one first without stopping, like an exercise; then practise it until it sounds steady and musical.', 0)}
  \\vspace #0.5
}}""")
    for pc_ in content.PIECES:
        pkey = pc_.get('key', 'c \\major')
        prh = pc_['rh'].replace('\\break', '\\break \\noPageBreak')
        out.append(f"""\\score {{
  \\header {{
    piece = \\markup \\column {{
      \\line {{ \\fontsize #3 \\bold {s(pc_['title'])} \\hspace #2 \\fontsize #0 {tempo_mk(pc_['tempo'])} }}
      \\fontsize #-1 \\italic {s(pc_['credit'])}
      \\override #'(line-width . {TEXT_WIDTH}) \\fontsize #-1 \\wordwrap-string #{s(pc_['note'])}
    }}
  }}
  \\new PianoStaff <<
    \\new Staff {{ \\autoLineBreaksOff \\clef treble \\key {pkey} \\time {pc_['meter']} {prh} }}
    \\new Staff {{ \\clef bass \\key {pkey} \\time {pc_['meter']} {pc_['lh']} \\bar "|." }}
  >>
  \\layout {{ }}
}}""")
    # Checkpoint
    cp_title = getattr(content, "CHECKPOINT_TITLE", f"Checkpoint: ready for Unit {unit['id'] + 1}?")
    out.append(boxed_list(cp_title, content.CHECKPOINT, numbered=False))
    out.append("\\pageBreak")
    return "\n".join(out)


def build(unit_ids, vol=1, front=None):
    V = VOLUMES[vol]
    if front is None:
        front = 1 in unit_ids  # title + how-to pages belong at the start of the volume
    header = f"Read at Sight  -  Volume {vol}"
    parts = [PREAMBLE.replace("@@HEADER@@", header), "\\book {"]
    if front:
        parts.append(title_page(vol))
        parts.append(how_to_page(vol))
    for uid in unit_ids:
        unit = next(u for u in V["units"] if u["id"] == uid)
        parts.append(unit_pages(unit, vol))
    parts.append("}")
    os.makedirs(BUILD, exist_ok=True)
    name = f"read-at-sight-vol{vol}" + ("" if len(unit_ids) > 1 else f"-unit{unit_ids[0]}")
    ly = os.path.join(BUILD, name + ".ly")
    with open(ly, "w") as f:
        f.write("\n".join(parts))
    r = subprocess.run([lilypond_bin(), "-s", "--pdf", "-o", os.path.join(BUILD, name), ly],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit("LilyPond failed")
    warnings = [line for line in r.stderr.splitlines() if "warning" in line.lower()]
    for w in warnings:
        print("WARN:", w)
    print("built", os.path.join(BUILD, name + ".pdf"))


if __name__ == "__main__":
    args = sys.argv[1:]
    vol = 1
    if args and args[0] == "--vol":
        vol, args = int(args[1]), args[2:]
    ids = [int(x) for x in args] or [1]
    build(ids, vol)
