"""Build "Before You Begin": a short guide to read before Volume 1 (habits, key and time
signatures, metronome, fingering, practice). Uses the shared page style of build.py.

Usage (from course/):  python3 before.py
Output: ../build/Read at Sight - Before You Begin.pdf
"""
import os
import re
import subprocess

import build
from build import s, para, keyboard_markup

OUT = os.path.join(build.BUILD, "Read at Sight - Before You Begin")

SECTIONS = [
    ("1. Keep your eyes on the music", [
        "Looking down to hunt for keys is the habit that most limits sight-reading: every glance down loses your "
        "place on the page, and the music stops while you find it again. The cure is to know the keyboard by touch.",
        "Find your place by the black keys. They come in groups of two and three, and you can feel them without "
        "looking: C is just left of every group of two, F just left of every group of three (see the picture).",
        "Feel distances instead of seeing them. In a five-finger position each finger sits over its own key, so a "
        "step is the next finger and a skip is every other finger. Read the distance on the page (step, skip, "
        "same note) and move by that distance.",
        "Glance down only when you must, and only with your eyes: before a large leap, or during a rest or long "
        "note. Look at the target key, not your hand, and look back up at once.",
        "Practise it on purpose: play the exercises of a unit you have finished with a cloth or a sheet of card held "
        "over your hands, or with the lights low. Wrong notes are fine; looking is not.",
    ]),
    ("2. Ten seconds before you play", [
        "Never start cold. Before every exercise or piece, check in this order: the clefs; the key signature (which "
        "notes are sharp or flat all the way through); the time signature (how to count); the speed; then scan for "
        "the highest and lowest notes, accidentals, rests, repeats and any bar that looks hard. Then count one bar "
        "out loud and start.",
    ]),
]

KEYS = [
    "Sharps: the last sharp is the leading note, so the key is one half step above it. One sharp (F-sharp): G "
    "major. Two sharps (C-sharp last): D major.",
    "Flats: one flat is F major; otherwise the second-to-last flat names the key. Two flats (B-flat, E-flat): "
    "B-flat major. Three flats: E-flat major.",
    "No sharps or flats: C major (or A minor).",
    "Major or minor? Every key signature belongs to a major key and to the minor key three half steps below it "
    "(G major and E minor share one sharp). Look at the last bass note, which is usually the key note, and for "
    "the raised seventh of the minor key appearing as an accidental (D-sharp in E minor, G-sharp in A minor).",
    "Then say it aloud before you play: 'one sharp, every F is F-sharp'. Most key-signature mistakes are an F "
    "or a B played natural halfway down the page, so look for those notes in your 10-second scan.",
]

TIMES = [
    "The top number is how many beats in a bar; the bottom number is which note gets one beat: 4 is a quarter "
    "note, 2 a half note, 8 an eighth note.",
    "4/4 (also written as C): four quarter-note beats. 3/4: three, with the accent on 1 (waltzes, minuets). "
    "2/4: two (marches).",
    "6/8 is felt in two, not six: two beats in each bar, each a dotted quarter split into three eighths. Count "
    "'1 2 3 4 5 6' slowly, then feel only 1 and 4. 2/2 (cut time) is felt in two half-note beats.",
    "Count out loud in the first weeks of every new rhythm. Counting aloud is the fastest way to stop "
    "guessing rhythms, and you can stop doing it once the counting runs in your head without effort.",
]

LATER = [
    ("3. The metronome: yes, but use it to keep going", [
        "Use it for every exercise. Sight-reading is mostly the skill of not stopping, and the metronome is what "
        "teaches it: it will not wait for you, so you learn to keep the beat and let a wrong note go.",
        "Set it slow enough that you never need to stop. The speeds in the books are targets; if you stumble more "
        "than once or twice in an exercise, go 10-20 beats per minute slower. A steady slow beat is worth far more "
        "than a fast one with stops.",
        "For a piece you are learning (not sight-reading), use it to find and fix uneven places, then turn it off "
        "and play musically. Raise the speed in small steps (4-8 beats per minute) only after two clean runs.",
        "If a click distracts you at first, count out loud instead, then add the metronome. Both together is best.",
    ]),
    ("4. Fingering: follow the book, then keep it the same", [
        "Use the finger numbers printed in the books (thumb is 1, little finger is 5, in both hands). They are "
        "chosen so that your hand is already in place for the notes that come next; what feels comfortable for one "
        "note often leaves you stuck two notes later.",
        "Where no number is printed, keep the hand position you were given: one finger per key in a five-finger "
        "position, and stay there until a new number tells you to move.",
        "Your own fingering is fine if it does three things: it lets you play the whole phrase without stopping, "
        "without twisting your hand, and the same way every time. Changing fingering from day to day is what makes "
        "pieces fail; once you choose one, write it in pencil and keep it.",
        "While sight-reading, never stop to correct a fingering. Keep going, and fix it next time.",
    ]),
    ("5. Reading habits that make the difference", [
        "Read ahead: while you play one beat, your eyes should already be on the next. Good readers look a beat or "
        "two ahead of their hands.",
        "Read shapes, not letter names: up or down, step or skip, and how far. Name notes only to find your starting "
        "position (and from landmark notes: middle C, treble G, bass F).",
        "Rhythm comes first. If you cannot play everything, drop notes, not beats. A wrong note in time sounds like "
        "music; a right note late does not.",
        "Do not go back. Never correct a wrong note during a run-through. Finish, then look at what went wrong.",
        "Play each exercise once, and move on. Reading something new every day is what trains reading; repeating "
        "the same exercise trains memory.",
    ]),
    ("6. Sitting and hands", [
        "Sit at the middle of the keyboard (middle C in front of you), far enough back that your elbows are a "
        "little in front of your body, at a height where your forearms are level with the keys.",
        "Keep your fingers gently curved, as if holding a ball, playing on the fingertips; wrists level, shoulders "
        "loose. If anything hurts or tightens, stop and shake it out. Tension is the first thing to fix, before speed.",
    ]),
    ("7. How to practise", [
        "Little and often beats long and seldom: 15-20 minutes every day does more than two hours once a week.",
        "Choose a level that feels easy. If you make more than two or three mistakes in an exercise, the material "
        "is too hard: go back a part or a unit. Sight-reading improves fastest on music you can almost play perfectly.",
        "Plateaus are normal. Some weeks nothing seems to improve, then it does. Keep the daily habit and trust it.",
        "Once a month, record yourself reading one new exercise and one piece. Listening back shows progress you "
        "cannot hear while playing.",
    ]),
]

QUICK = [
    "Eyes on the page; feel the black-key groups.",
    "Ten-second scan: clefs, key, time, speed, hard spots.",
    "Count one bar in, then never stop.",
    "Metronome slow enough that you keep going.",
    "Printed fingering, the same every time.",
    "Rhythm first: drop notes, not beats.",
    "Something new to read every day.",
]

KEY_EXAMPLE = r"""
\score {
  \new Staff \with { printKeyCancellation = ##f } {
    \set Staff.explicitKeySignatureVisibility = #end-of-line-invisible
    \omit Staff.TimeSignature \textLengthOn
    \key g \major g'1_\markup \center-column { "1 sharp" "G major" "(E minor)" } \bar "||"
    \key d \major d''1_\markup \center-column { "2 sharps" "D major" "(B minor)" } \bar "||"
    \key a \major a'1_\markup \center-column { "3 sharps" "A major" "(F-sharp minor)" } \bar "||"
    \key f \major f'1_\markup \center-column { "1 flat" "F major" "(D minor)" } \bar "||"
    \key bes \major bes'1_\markup \center-column { "2 flats" "B-flat major" "(G minor)" } \bar "||"
    \key ees \major ees''1_\markup \center-column { "3 flats" "E-flat major" "(C minor)" } \bar "||"
  }
  \layout { indent = 0 ragged-right = ##f \context { \Staff \override TextScript.font-size = #-2 } }
}
"""

TIME_EXAMPLE = r"""
\score {
  <<
    \new RhythmicStaff {
      \time 4/4 c4 c c c \bar "||"
      \time 3/4 c4 c c \bar "||"
      \time 6/8 c8 c c c c c | c4. c4. \bar "||"
      \time 2/2 c2 c \bar "|."
    }
    \addlyrics { \override LyricText.font-size = #-1
      "1" "2" "3" "4"  "1" "2" "3"  "1" "2" "3" "4" "5" "6"  "1" "4"  "1" "2" }
  >>
  \layout { indent = 0 ragged-right = ##f \context { \Score \override TimeSignature.style = #'numbered
    \override SpacingSpanner.spacing-increment = #3 } }
}
"""


def section(head, items, numbered=False):
    out = [f"\\markup \\column {{ \\vspace #0.8 \\fontsize #3 \\bold {s(head)} \\vspace #0.2 }}"]
    out.append("\\noPageBreak")  # keep each heading with its first point
    for t in items:
        out.append(f"\\markup \\line {{ \\hspace #1 \\column {{ \\vspace #0.35 \\line {{ \\fontsize #1 \"•\" \\hspace #1 "
                   f"{para(t, 1).replace('line-width . ' + str(build.TEXT_WIDTH), 'line-width . ' + str(build.TEXT_WIDTH - 4))} }} }} }}")
    return out


def document():
    build._layout_for(1)
    parts = [build.PREAMBLE.replace("@@HEADER@@", "Read at Sight  -  Before You Begin").replace("@@STAFF_SIZE@@", "22"),
             "\\book {"]
    kb = keyboard_markup(21, 35, [(21, None, "C", "RH"), (24, None, "F", "LH"), (28, None, "C", "RH"),
                                  (31, None, "F", "LH"), (35, None, "C", "RH")], {28: "Middle C"})
    parts.append(rf"""\markup \column {{
  \vspace #3
  \fill-line {{ \fontsize #10 \bold "Before You Begin" }}
  \vspace #0.6
  \fill-line {{ \fontsize #3 \italic "Read at Sight: habits that make sight-reading work" }}
  \vspace #2
  {para("Read this once before Volume 1, and again whenever something feels stuck. Seven short sections: "
        "where to look, what to check before playing, how to read key and time signatures, the metronome, "
        "fingering, reading habits, and how to practise.", 1)}
}}""")
    parts += section(*SECTIONS[0])
    parts.append(rf"""\markup \column {{ \vspace #1 \fill-line {{ {kb} }} \vspace #1.6
  \fill-line {{ \fontsize #-1 \italic "C is left of every two black keys; F is left of every three. Find them by touch." }} }}""")
    parts += section(*SECTIONS[1])
    parts += section("Reading the key signature", KEYS)
    parts.append("\\markup \\vspace #0.6")
    parts.append(KEY_EXAMPLE)
    parts += section("Reading the time signature", TIMES)
    parts.append("\\markup \\vspace #0.6")
    parts.append(TIME_EXAMPLE)
    for head, items in LATER:
        parts += section(head, items)
    rows = " ".join(f"\\vspace #0.4 \\line {{ \\bold \"{i + 1}.\" {s(t)} }}" for i, t in enumerate(QUICK))
    parts.append(f"\\markup \\column {{ \\vspace #1 \\fill-line {{ \\override #'(box-padding . 1.6) \\box \\column {{ "
                 f"\\fontsize #2 \\bold \"On one card: the seven habits\" \\fontsize #1 \\column {{ {rows} }} }} }} }}")
    parts.append("}")
    return "\n".join(parts)


def main():
    ly = OUT + ".ly"
    open(ly, "w").write(document())
    r = subprocess.run([build.lilypond_bin(), "-l", "WARNING", "-o", OUT, ly], capture_output=True, text=True)
    warns = [l for l in r.stderr.splitlines() if re.search(r"(warning|error):", l)]
    for w in warns:
        print("WARN:", w)
    if r.returncode != 0:
        raise SystemExit("LilyPond failed")
    os.remove(ly)
    print("built", OUT + ".pdf")


if __name__ == "__main__":
    main()
