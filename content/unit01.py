"""Hand-written content for Unit 1. Pieces are LilyPond music (relative to nothing: absolute pitches)."""

INTRO = [
    "In this unit your right hand learns its first home on the keyboard: the C position. "
    "Put your right thumb (finger 1) on middle C and let fingers 2, 3, 4 and 5 rest on the next four white keys: D, E, F and G. "
    "Your hand does not move for the whole unit, so every note you read is already under a finger.",
]

NEW_IDEAS = [
    ("The treble clef", "The curl of the treble clef wraps around the second line from the bottom. That line is G, the note under your little finger."),
    ("Middle C", "Middle C sits on its own short line (a ledger line) just below the treble staff. It is your thumb."),
    ("Lines and spaces", "Notes alternate line, space, line, space as they go up: C (ledger line), D (space under the staff), E (bottom line), F (first space), G (second line)."),
    ("Note values", "Whole note = 4 beats (open, no stem). Half note = 2 beats (open, with stem). Quarter note = 1 beat (filled in, with stem)."),
    ("4/4 time", "The top 4 means four beats in every bar. Count 1 - 2 - 3 - 4 out loud, steadily, in every bar."),
]

TIPS = [
    "Read the direction, not the names. Ask: does the next note go up, down, or stay the same? A step goes from a line to the very next space (or space to line), and is always the next finger.",
    "Keep your eyes on the page. Your fingers already sit on the right keys, so there is no need to look down.",
    "Count out loud and never stop. If you play a wrong note, keep going: the beat matters more than the note.",
    "Before each exercise, take 10 seconds: find the starting note and finger, then scan for where the line goes up and where it goes down.",
]

PART_NOTES = {
    "A": "Long notes only: whole notes (4 beats) and half notes (2 beats). Set the metronome to 60 and count every beat aloud.",
    "B": "Now quarter notes (1 beat) join in. Keep the same steady 60. Notice how many exercises move in steps of a single finger.",
    "C": "Eight-bar phrases, written on two lines. Look for bars that repeat: many phrases restart in bar 5 the same way they began in bar 1. Spotting a repeat means less to read.",
}

PIECES = [
    {
        "allow_leap": 2,  # the tune skips C-E; the note points it out
        "title": "Hot Cross Buns", "credit": "Traditional (bar 3 simplified to quarter notes)", "meter": "4/4", "tempo": 72,
        "note": "Three notes, one pattern. Bars 1, 2 and 4 are almost the same. One new move: after each C, skip back up to E (finger 1 to finger 3).",
        "rh": "e'4^3 d' c'2 | e'4 d' c'2 | c'4 c' d' d' | e'4 d' c'2 \\bar \"|.\"",
        "lh": "R1 | R1 | R1 | R1",
    },
    {
        "title": "First Steps", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "A question (bars 1-4) and an answer (bars 5-8). The answer starts exactly like the question.",
        "rh": "c'4^1 d' e' d' | e' f' g'2 | g'4 f' e' f' | e'2 d' | \\break "
              "c'4 d' e' d' | e' f' g'2 | f'4 e' e' d' | c'1 \\bar \"|.\"",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Seesaw", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "Repeated notes stay on the same line or space. Keep the half notes full: count 1 - 2, 3 - 4.",
        "rh": "e'2^3 e' | d' d' | e'4 f' g' g' | g'1 | \\break "
              "g'4 f' e' e' | d' e' f'2 | e'4 d' c' d' | c'1 \\bar \"|.\"",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Ode to Joy", "credit": "Ludwig van Beethoven (1824), simplified", "meter": "4/4", "tempo": 80,
        "note": "The famous theme from the Ninth Symphony uses only your five C-position notes. Bars 1-3 and 5-7 are identical; only the endings differ.",
        "rh": "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | e' d' d'2 | \\break "
              "e'4 e' f' g' | g' f' e' d' | c' c' d' e' | d' c' c'2 \\bar \"|.\"",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if you keep the beat going to the end of each one, with no more than one stop per exercise.",
    "Pass if at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 2. If not, play Part B and C exercises again in a week; by then you will have forgotten them.",
]
