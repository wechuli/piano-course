"""Build the course book (or a single unit) as a print-ready A4 PDF with LilyPond.

Usage:  python3 build.py [--vol N] [unit ids...]   e.g. python3 build.py --vol 2 1 2 3
Output: ../build/read-at-sight-volN[-unitM].pdf
"""
import importlib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "content"))

from units import VOLUME1, VOLUME2, VOLUME3, VOLUME4, VOLUME5, VOLUME6, POSITIONS, CHORDS  # noqa: E402
from generator import generate_unit, lily_exercise, chord_fingers, lily_pitch, raised_pitch  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "build")
TEXT_WIDTH = 86  # line width for wrapped text, in staff spaces (A4, staff size 22)


def _layout_for(vol):
    """Volume 6 is set at staff size 20 (option "staff_size": four-staff systems must fit A4),
    so its text lines are measured in smaller staff spaces and need a larger width. Volumes 1-5
    keep the defaults (86 at staff size 22) and must stay byte-identical."""
    global TEXT_WIDTH
    TEXT_WIDTH = VOLUMES[vol].get("text_width", 86)

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
    3: {"units": VOLUME3, "subtitle": "Volume 3  -  Two Voices", "content": "v3unit",
        "blurb": ["The left hand gets its own music: broken chords, Alberti basses and real second voices,",
                  "in 6/8 time and in keys with up to two sharps or flats."],
        "skip": ["Why this book is built this way"],
        "extra": [
            ("What is new in Volume 3",
             "In Volumes 1 and 2 the left hand mostly held long notes while the right hand played the tune. Now both "
             "hands have something to say. The left hand plays broken chords and Alberti basses, then a melody of its "
             "own, and the right hand starts to play two notes at once. You will also meet 6/8 time, the keys of D "
             "major and B-flat major, and sharps and flats that are not in the key signature. "
             "Start this book when you can read Volume 2 music, with shifts, dotted rhythms and dynamics, in C, G and "
             "F major and their relative minors."),
        ]},
    4: {"units": VOLUME4, "subtitle": "Volume 4  -  Patterns and Keys", "content": "v4unit",
        "blurb": ["Chords in both hands, high and low notes, syncopation and sixteenths,",
                  "keys with three sharps or flats, and music that changes key."],
        "replace": {"How each unit is laid out":
                    "A unit opens with what is new, keyboard pictures of the hand positions or chord shapes, and reading tips. "
                    "Then come Parts A to D, which grow slightly harder. Pieces come next, and the unit ends with a checkpoint "
                    "that tells you when to move on."},
        "skip": ["Why this book is built this way"],
        "extra": [
            ("What is new in Volume 4",
             "Both hands now play chords, and the accompaniment falls into patterns you learn to read at a glance: "
             "held chords, oom-pah and waltz basses, chorales and after-beat chords. You will read ledger lines far "
             "above and below the staves, syncopated rhythms and sixteenth notes, the keys of A major, E-flat major, "
             "F-sharp minor and C minor, and music that moves into a new key. 2/4 time joins 3/4, 4/4 and 6/8. "
             "Start this book when you can read Volume 3 music: broken-chord and Alberti basses, 6/8, keys with two "
             "sharps or flats, and two independent voices."),
        ]},
    5: {"units": VOLUME5, "subtitle": "Volume 5  -  Repertoire Reading", "content": "v5unit",
        "blurb": ["Real piano music: two voices in one hand, chorales, chromatic notes, triplets,",
                  "every key, the pedal and ornaments, with pieces by Bach, Beethoven, Schumann and Chopin."],
        "replace": {
            "Before every exercise: 10 seconds":
                "Name the key (the key signature and the last bass note) and the time signature. Look at the left "
                "hand's pattern: held chords, a waltz, a broken chord, a second voice? Find the highest and lowest "
                "notes, any accidentals, and any bar that repeats an earlier one. Then count one bar in and play.",
            "How each unit is laid out":
                "A unit opens with what is new, short examples, and reading tips. Parts A to C (sometimes D) are "
                "generated exercises that practise the new idea. The pieces come next: in this volume they are the "
                "heart of each unit, and most are real music by the great composers. A checkpoint ends the unit.",
            "A daily routine (15-20 minutes)":
                "Warm up with the scale and the I, IV and V chords of the day's key (2 minutes). Read 4-6 new "
                "exercises, one pass each (8 minutes). Then read one piece, or a page of one, and practise a "
                "passage from it (8 minutes)."},
        "skip": ["Why this book is built this way"],
        "extra": [
            ("What is new in Volume 5",
             "This is the last volume. The hand positions of Volumes 1-4 give way to reading as pianists do: by key, "
             "by chord shape and by pattern. Finger numbers now appear only where a passage needs a particular "
             "fingering. You will read two voices in one hand, four-part chorales, chromatic notes, triplets and "
             "four new time signatures, every major and minor key, the sustain pedal, clef changes and ornaments. "
             "Most of the pieces are real music: Bach chorales and inventions, Beethoven, Schubert, Schumann, "
             "Chopin and Satie. Start this book when you can read Volume 4 music: chords in both hands, ledger "
             "lines, syncopation, sixteenths and keys with three sharps or flats."),
        ]},
    6: {"units": VOLUME6, "subtitle": "Volume 6  -  Reading Like a Professional", "content": "v6unit",
        "staff_size": 20, "text_width": 94,  # four-staff systems must fit A4 portrait
        "blurb": ["Three voices, cross-rhythms, changing meters and chromatic harmony; songs on three staves,",
                  "open score with C clefs, lead sheets, and transposing and simplifying at sight."],
        "replace": {
            "Before every exercise: 10 seconds":
                "Name the key (or mode) and the time signature, and check whether either changes. Count the "
                "staves and name each clef. Find the hardest bar and decide what you will drop from it if you "
                "must. Then count one bar in and play.",
            "How each unit is laid out":
                "A unit opens with what is new, short examples, and reading tips. Parts A to C are generated "
                "exercises that practise the new idea. The pieces come next: real music by the great composers, "
                "chosen because each needs exactly the unit's new skill. A checkpoint ends the unit.",
            "A daily routine (15-20 minutes)":
                "Warm up with the scale and the main chords of the day's key (2 minutes). Read 4-6 new "
                "exercises, one pass each (8 minutes). Then read one piece, or a page of one, keeping the beat "
                "and simplifying where you must (8 minutes)."},
        "skip": ["Why this book is built this way"],
        "extra": [
            ("What is new in Volume 6",
             "Volumes 1-5 taught you to read piano music. This volume teaches you to read music written for "
             "anyone: three-voice counterpoint, two rhythms at once, meters that change bar by bar, chromatic "
             "harmony, big textures, a singer's line above the piano, open score with alto and tenor clefs, and "
             "lead sheets with chord symbols. It also teaches the professional's two survival skills: "
             "simplifying at sight (dropping notes without losing the music) and transposing at sight. "
             "Start this book when you have passed the Volume 5 checkpoint: every key, triplets, the pedal, "
             "clef changes and ornaments."),
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
#(set-global-staff-size @@STAFF_SIZE@@)

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


def tempo_mk(bpm, unit="4"):
    return f"\\concat {{ \\general-align #Y #DOWN \\fontsize #-2 \\note {{{unit}}} #UP \" = {bpm}\" }}"


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
        if acc == "is" and st % 7 in (2, 6):  # E-sharp and B-sharp are white keys
            st, acc = st + 1, None
        elif acc == "es" and st % 7 in (0, 3):  # C-flat and F-flat too
            st, acc = st - 1, None
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


def chord_shapes(group):
    """The left hand's chord shapes in one key: [(label, name markup, [(step, acc, finger)], [lily names])].
    group = (title, lh position, lily key, key_acc[, minor]); in a minor key the chords are i, iv and V7,
    and V7's bottom note (the leading note) is raised."""
    title, lh, key, key_acc = group[:4]
    minor = len(group) > 4 and group[4]
    out = []
    for c in ("I", "IV", "V7"):
        notes = [POSITIONS[lh]["low"] + v for v in CHORDS[c]["voicing"]]
        accs = [key_acc.get("cdefgab"[st % 7]) for st in notes]
        lily = [lily_pitch(st, key_acc) for st in notes]
        if minor and c == "V7":
            accs[0] = {"es": None, None: "is"}[accs[0]]
            lily[0] = raised_pitch(notes[0], key_acc)
        root = {"I": notes[0], "IV": notes[1], "V7": notes[0] - 2}[c]  # C E G = C; C F A = F; B F G = G7
        root_acc = key_acc.get("cdefgab"[root % 7])
        name = note_name_markup(root, root_acc)
        if c == "V7":
            name = f"\\concat {{ {name} \"7\" }}"
        elif minor:
            name = f"\\concat {{ {name} \"m\" }}"
        label = c.lower() if minor and c != "V7" else c
        out.append((label, name, list(zip(notes, accs, chord_fingers(notes))), lily))
    return out


def chord_shapes_markup(group):
    """Three small keyboards (I, IV, V7) side by side for one key, left hand."""
    shapes = chord_shapes(group)
    steps = [st for _, _, ns, _ in shapes for st, _, _ in ns]
    lo, hi = min(steps) - 1, max(steps) + 1
    cells = []
    for c, name, ns, _ in shapes:
        kb = keyboard_markup(lo, hi, [(st, acc, f, "LH") for st, acc, f in ns], {})
        cells.append(f"\\center-column {{ {kb} \\vspace #0.6 \\line {{ \\bold {c} \\hspace #0.6 = \\hspace #0.6 {name} }} }}")
    return (f"\\markup \\column {{ \\vspace #0.8 \\fontsize #1 \\bold {s(group[0] + ': left-hand chord shapes')} \\vspace #0.6 "
            f"\\fill-line {{ {' '.join(cells)} }} \\vspace #0.6 }}")


def chord_map_score(groups):
    """All the chord shapes as block chords on one bass staff, key by key."""
    music = []
    for gi, group in enumerate(groups):
        if len(groups) >= 4 and gi and gi % 2 == 0:
            music.append("\\break")  # four or more keys: two keys per line
        music.append(f"\\key {group[2]}")
        for c, name, ns, lily in chord_shapes(group):
            inner = " ".join(lily)
            music.append(f"<{inner}>1^\\markup \\bold {c} _\\markup {name}")
        music.append('\\bar "||"')
    nostime = "\\with { \\remove \"Time_signature_engraver\" }"
    return f"""\\score {{
  \\header {{ piece = \\markup \\fontsize #1 \\bold "The same shapes on the staff" }}
  \\new Staff {nostime} {{ \\clef bass \\cadenzaOn {' '.join(music)} }}
  \\layout {{ ragged-right = ##f }}
}}"""


def example_score(exm):
    """A short example (Volume 5): title, music on one staff or a piano staff, and a caption."""
    staff = exm.get("staff", "piano")
    key = exm.get("key", "c \\major")
    time = exm.get("time")
    tsig = f"\\time {time} " if time else ""
    nost = "" if time else "\\with { \\remove \"Time_signature_engraver\" } "
    pre = "\\accidentalStyle modern \\set Staff.pedalSustainStyle = #'bracket "
    if staff == "piano":
        music = (f"\\new PianoStaff << \\new Staff {nost}{{ \\clef treble \\key {key} {tsig}{pre}{exm['rh']} }} "
                 f"\\new Staff {nost}{{ \\clef bass \\key {key} {tsig}{pre}{exm['lh']} }} >>")
    else:
        music = f"\\new Staff {nost}{{ \\clef {staff} \\key {key} {tsig}{pre}{exm['rh']} }}"
    cap = f"\\override #'(line-width . {TEXT_WIDTH}) \\fontsize #-1 \\wordwrap-string #{s(exm['text'])}" if exm.get("text") else ""
    return f"""\\score {{
  \\header {{ piece = \\markup \\column {{ \\fontsize #1 \\bold {s(exm['title'])} {cap} }} }}
  {music}
  \\layout {{ ragged-right = ##{'f' if exm.get('wide') else 't'} }}
}}"""


def key_picture(kp):
    """One octave of a key's scale on the keyboard, with the scale degrees on the keys (Volume 5).
    In a minor key the 7th is raised, as in the harmonic minor."""
    import gen5
    title, name, mode = kp
    k = gen5.Key(name, mode)
    start = 28 + k.tpc if k.tpc <= 2 else 21 + k.tpc
    keys, names = [], []
    for i in range(8):
        st = start + i
        alt = k.sig[st % 7] + (1 if mode == "minor" and i == 6 else 0)
        acc = {1: "is", -1: "es", 0: None}.get(alt)
        if alt == 2:  # a double sharp (F double-sharp, G-sharp minor's 7th) is the white key above
            keys.append((st + 1, None, str(i % 7 + 1), "RH"))
            names.append(f"\\concat {{ \"{'CDEFGAB'[st % 7]}\" \\raise #0.5 \\fontsize #-3 \\doublesharp }}")
        else:
            keys.append((st, acc, str(i % 7 + 1), "RH"))
            names.append(note_name_markup(st, acc))
    kb = keyboard_markup(start - 1, start + 8, keys, {})
    return (f"\\markup \\column {{ \\vspace #0.6 \\fill-line {{ \\fontsize #1 \\bold {s(title)} }} \\vspace #0.5 "
            f"\\fill-line {{ {kb} }} \\vspace #0.8 \\fill-line {{ \\line {{ \\italic \"Scale degrees on the keys:\" "
            f"{' '.join(names)} }} }} \\vspace #0.4 }}")


# ---------------------------------------------------------------- front matter
def title_page(vol):
    _layout_for(vol)
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
    _layout_for(vol)
    V = VOLUMES[vol]
    out = ["\\markup \\column { \\fontsize #6 \\bold \"How to use this book\" \\vspace #1 }"]
    how = [(h, V.get("replace", {}).get(h, b)) for h, b in HOW_TO if h not in V.get("skip", [])]
    for head, body in V["extra"] + how:
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
V6_CLEFS = {"treble": "treble", "bass": "bass", "treble_8": '"treble_8"', "alto": "alto", "tenor": "tenor"}
V6_GROUPS = {"piano": "PianoStaff", "choir": "ChoirStaff", "quartet": "StaffGroup"}


def piece_score_v6(pc_):
    """A Volume 6 piece. Besides "rh"/"lh" (two piano staves, as before), a piece may define
    "staves": a list of {name, clef, music}, plus "hand": "rh"/"lh" on the piano staves,
    "solo": True on a staff printed above the group (a singer or violin), "instrument" for a
    printed name, "lyrics" for an \\addlyrics line, and clef "chords" for a ChordNames line
    (lead sheets). "group" picks the bracket: piano (default), choir or quartet. "meter" may
    be left out when the music is unbarred (\\cadenzaOn)."""
    pkey = pc_.get("key", "c \\major")
    tpre = "\\once \\override Staff.TimeSignature.style = #'C " if pc_.get("cut") else ""
    tsig = f"\\time {pc_['meter']} " if pc_.get("meter") else "\\omit Staff.TimeSignature "
    staves = pc_.get("staves") or [{"name": "up", "clef": "treble", "music": pc_["rh"], "hand": "rh"},
                                   {"name": "down", "clef": "bass", "music": pc_["lh"], "hand": "lh"}]
    last_staff = [st for st in staves if st.get("clef") != "chords"][-1]
    solo_codes, group_codes = [], []
    first = True
    for st in staves:
        music = st["music"]
        if st.get("clef") == "chords":
            group_codes.append(f"\\new ChordNames {{ {music} }}")
            continue
        if not pc_.get("long"):
            music = music.replace("\\break", "\\break \\noPageBreak")
        pre = "\\accidentalStyle modern "
        if st.get("hand"):
            pre += "\\set Staff.pedalSustainStyle = #'bracket "
            if re.search(r"<[^>]*-\d", st["music"]):  # fingers beside chords
                pre = "\\set fingeringOrientations = #'(left) " + pre
        if st.get("instrument"):
            pre += f"\\set Staff.instrumentName = {s(st['instrument'] + ' ')} "
        endbar = ""
        if st is last_staff and "\\repeat volta" not in st["music"]:
            endbar = ' \\bar "|."'  # one staff ends the system (a repeat sign would be hidden)
        auto = "\\autoLineBreaksOff " if first else ""
        first = False
        code = (f'\\new Staff = "{st["name"]}" {{ {auto}\\clef {V6_CLEFS[st.get("clef", "treble")]} '
                f"\\key {pkey} {tpre}{tsig}{pre}{music}{endbar} }}")
        if st.get("lyrics"):
            code += (" \\addlyrics \\with { \\override VerticalAxisGroup.nonstaff-unrelatedstaff-spacing.padding = #1.5 }"
                     f" {{ {st['lyrics']} }}")
        (solo_codes if st.get("solo") else group_codes).append(code)
    body = (f"\\new {V6_GROUPS[pc_.get('group', 'piano')]} <<\n    "
            + "\n    ".join(group_codes) + "\n  >>")
    if solo_codes:
        body = "<<\n  " + "\n  ".join(solo_codes) + "\n  " + body + "\n  >>"
    return f"""\\score {{
  \\header {{
    piece = \\markup \\column {{
      \\line {{ \\fontsize #3 \\bold {s(pc_['title'])} \\hspace #2 \\fontsize #0 {tempo_mk(pc_['tempo'], pc_.get('tempo_unit', '4'))} }}
      \\fontsize #-1 \\italic {s(pc_['credit'])}
      \\override #'(line-width . {TEXT_WIDTH}) \\fontsize #-1 \\wordwrap-string #{s(pc_['note'])}
    }}
  }}
  {body}
  \\layout {{ }}
}}"""


def unit_pages(unit, vol=1):
    _layout_for(vol)
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
    groups = getattr(content, "KEYBOARDS", None)
    if groups is None:  # KEYBOARDS = [] draws no position keyboard (e.g. a unit about chord shapes)
        groups = [unit_positions(unit, content)] if vol < 5 else []  # Volume 5 has no hand positions
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
    for group in getattr(content, "CHORD_SHAPES", []):
        out.append(chord_shapes_markup(group))
    if getattr(content, "CHORD_SHAPES", None):
        out.append(chord_map_score(content.CHORD_SHAPES))
    # New ideas
    for i, (head, body) in enumerate(content.NEW_IDEAS):
        lead = "\\vspace #0.5 \\fontsize #3 \\bold \"What is new\" \\vspace #0.3 " if i == 0 else ""
        out.append(f"\\markup \\override #'(line-width . {TEXT_WIDTH}) \\column {{ {lead}\\fontsize #1 \\bold {s(head)} {para(body, 0)} }}")
    # Short examples (Volume 5): small scores with a caption, e.g. how an ornament is played
    for exm in getattr(content, "EXAMPLES", []):
        out.append(example_score(exm))
    for kp in getattr(content, "KEY_PICTURES", []):
        out.append(key_picture(kp))
    # Tips box
    out.append(boxed_list("Reading tips", content.TIPS))
    out.append("\\pageBreak")

    # Exercise parts
    n = 0
    if vol >= 6:
        import gen6
        gen_unit, emit = gen6.generate_unit, gen6.lily_exercise
    elif vol == 5:
        import gen5
        gen_unit, emit = gen5.generate_unit, gen5.lily_exercise
    else:
        gen_unit, emit = generate_unit, (lambda p, e, label: [lily_exercise(p, e, label)])
    for part, exercises in gen_unit(unit, seed=vol * 1000 + unit["id"]):
        out.append(f"""\\markup \\column {{
  \\vspace #0.6
  \\line {{ \\fontsize #4 \\bold {s('Part ' + part['name'] + ': ' + part['title'])} \\hspace #3 \\fontsize #1 {tempo_mk(part['tempo'], part.get('tempo_unit', '4'))} }}
  \\vspace #0.2
  {para(content.PART_NOTES.get(part['name'], ''), 0)}
  \\vspace #0.3
}}""")
        for ex in exercises:
            n += 1
            out.extend(emit(part, ex, f"{unit['id']}.{n}"))
        out.append("\\pageBreak")

    # Pieces
    out.append(f"""\\markup \\column {{
  \\fontsize #5 \\bold "Pieces"
  \\vspace #0.3
  {para('Pieces are for playing more than once. Read each one first without stopping, like an exercise; then practise it until it sounds steady and musical.', 0)}
  \\vspace #0.5
}}""")
    if vol >= 6:
        out.append("\\noPageBreak")  # keep the heading with the first piece
    for pc_ in content.PIECES:
        if vol >= 6:
            out.append(piece_score_v6(pc_))
            continue
        pkey = pc_.get('key', 'c \\major')
        prh = pc_['rh'] if pc_.get('long') else pc_['rh'].replace('\\break', '\\break \\noPageBreak')
        lpre = "\\set fingeringOrientations = #'(left) " if vol >= 4 else ""  # fingers beside LH chords
        rpre = lpre if re.search(r"<[^>]*-\d", pc_['rh']) else ""  # and RH chords that carry fingers
        tpre = ""
        sup, sdown = (' = "up"', ' = "down"') if vol >= 5 else ("", "")  # named, for cross-staff notes
        endbar = '\\bar "|." '
        if vol >= 5 and pc_['lh'].rstrip().endswith("}") and "\\repeat volta" in pc_['lh']:
            endbar = ""  # the piece ends with a repeat sign, which the final bar line would hide
        if vol >= 5:  # Volume 5: alla breve sign, bracket pedal marks, reminders after accidentals
            tpre = "\\once \\override Staff.TimeSignature.style = #'C " if pc_.get('cut') else ""
            rpre = "\\accidentalStyle modern " + rpre
            lpre = "\\accidentalStyle modern \\set Staff.pedalSustainStyle = #'bracket " + lpre
        out.append(f"""\\score {{
  \\header {{
    piece = \\markup \\column {{
      \\line {{ \\fontsize #3 \\bold {s(pc_['title'])} \\hspace #2 \\fontsize #0 {tempo_mk(pc_['tempo'], pc_.get('tempo_unit', '4'))} }}
      \\fontsize #-1 \\italic {s(pc_['credit'])}
      \\override #'(line-width . {TEXT_WIDTH}) \\fontsize #-1 \\wordwrap-string #{s(pc_['note'])}
    }}
  }}
  \\new PianoStaff <<
    \\new Staff{sup} {{ \\autoLineBreaksOff \\clef treble \\key {pkey} {tpre}\\time {pc_['meter']} {rpre}{prh} }}
    \\new Staff{sdown} {{ \\clef bass \\key {pkey} {tpre}\\time {pc_['meter']} {lpre}{pc_['lh']} {endbar}}}
  >>
  \\layout {{ }}
}}""")
    # Checkpoint
    cp_title = getattr(content, "CHECKPOINT_TITLE", f"Checkpoint: ready for Unit {unit['id'] + 1}?")
    out.append(boxed_list(cp_title, content.CHECKPOINT, numbered=False))
    out.append("\\pageBreak")
    return "\n".join(out)


def answers_pages(vol):
    """The Answers appendix (Volume 6): every transposing exercise written out in its target
    key, at the back of the book. No pages while no unit transposes."""
    import gen6
    scores = []
    for unit in VOLUMES[vol]["units"]:
        scores += gen6.answer_scores(unit, seed=vol * 1000 + unit["id"])
    if not scores:
        return ""
    head = f"""\\markup \\column {{
  \\fontsize #6 \\bold "Answers"
  \\vspace #0.4
  {para('The transposing exercises, written out in their target keys. Play first; check yourself here afterwards.', 0)}
  \\vspace #0.5
}}"""
    return "\n".join([head] + scores + ["\\pageBreak"])


def build(unit_ids, vol=1, front=None):
    _layout_for(vol)
    V = VOLUMES[vol]
    if front is None:
        front = 1 in unit_ids  # title + how-to pages belong at the start of the volume
    header = f"Read at Sight  -  Volume {vol}"
    parts = [PREAMBLE.replace("@@HEADER@@", header)
             .replace("@@STAFF_SIZE@@", str(V.get("staff_size", 22))), "\\book {"]
    if front:
        parts.append(title_page(vol))
        parts.append(how_to_page(vol))
    for uid in unit_ids:
        unit = next(u for u in V["units"] if u["id"] == uid)
        parts.append(unit_pages(unit, vol))
    if vol >= 6 and V["units"][-1]["id"] in unit_ids:
        app = answers_pages(vol)  # the appendix ends the book
        if app:
            parts.append(app)
    parts.append("}")
    os.makedirs(BUILD, exist_ok=True)
    name = f"read-at-sight-vol{vol}" + ("" if len(unit_ids) > 1 else f"-unit{unit_ids[0]}")
    ly = os.path.join(BUILD, name + ".ly")
    with open(ly, "w") as f:
        f.write("\n".join(parts))
    r = subprocess.run([lilypond_bin(), "-l", "WARNING", "--pdf", "-o", os.path.join(BUILD, name), ly],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-4000:])
        raise SystemExit("LilyPond failed")
    benign = ("has been compressed", "page must be compressed", "compressing over-full page")  # tighter page: harmless
    warnings = [line for line in r.stderr.splitlines() if "warning" in line.lower()
                and not any(b in line for b in benign)]
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
