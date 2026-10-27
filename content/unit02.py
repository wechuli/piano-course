"""Hand-written content for Unit 2: the left hand and the bass clef."""

INTRO = [
    "Now the left hand gets its own home. Put your left little finger (finger 5) on the C one octave below middle C, "
    "and let fingers 4, 3, 2 and 1 rest on D, E, F and G. Your thumb ends up on G, a little below middle C. "
    "The left hand reads from the lower staff, which uses the bass clef.",
]

NEW_IDEAS = [
    ("The bass clef", "The bass clef is also called the F clef: its two dots sit on either side of the fourth line from the bottom. That line is F, the note under your finger 2."),
    ("Your five notes", "C sits in the second space, D on the middle line, E in the third space, F on the fourth line (between the clef dots) and G in the top space."),
    ("Left-hand finger numbers", "Thumb is still finger 1, so in the left hand the numbers run the other way: going up the keyboard means 5, 4, 3, 2, 1."),
    ("A new staff, not a copy", "The bass staff is not the treble staff moved down. The bottom line is G in the bass clef but E in the treble clef. Learn the bass notes as a new set, from their own landmarks."),
]

TIPS = [
    "Use two landmarks: F is the line between the clef's dots, and C is the space just below the middle line. Read everything else as a step up or down from one of them.",
    "Higher on the staff still means further to the right on the keyboard. In the left hand that means a smaller finger number.",
    "Never work a bass note out by thinking of the treble clef. That habit makes the bass clef slow for years. Go straight from the line or space to the key.",
    "Keep the beat going and your eyes on the page, exactly as in Unit 1.",
]

PART_NOTES = {
    "A": "Whole and half notes in the bass clef. Metronome at 60; count every beat aloud. Say the finger number as you play if it helps.",
    "B": "Quarter notes join in. Watch for runs of steps: they are always the next finger.",
    "C": "Eight-bar phrases on two lines. Look for bar 5 repeating bar 1.",
}

PIECES = [
    {
        "allow_leap": 2,  # the tune skips C-E; the note points it out
        "title": "Hot Cross Buns (left hand)", "credit": "Traditional (bar 3 simplified to quarter notes)",
        "meter": "4/4", "tempo": 72,
        "note": "The same tune you played in Unit 1, now in the bass clef. Notice that it looks quite different, yet you play the same keys an octave lower. After each C, skip back up to E (finger 5 to finger 3).",
        "rh": "R1 | R1 | R1 | R1",
        "lh": "e4_3 d c2 | e4 d c2 | c4 c d d | e4 d c2",
    },
    {
        "title": "Bear Walk", "credit": "Original", "meter": "4/4", "tempo": 66,
        "note": "Heavy, slow steps. Play firmly, and keep the whole notes held for all four beats.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c2_5 d | e1 | e2 d | c1 | c4 d e f | g2 g | f4 e d d | c1",
    },
    {
        "title": "Evening Bells", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The bells ring from high to low. Bars 5-6 echo bars 1-2. Start with your thumb.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "g2_1 f | e d | c4 d e f | g1 | g2 f | e d | c4 d e d | c1",
    },
    {
        "title": "Ode to Joy (left hand)", "credit": "Ludwig van Beethoven (1824), simplified",
        "meter": "4/4", "tempo": 80,
        "note": "A tune you know, read in a new clef. Trust the staff rather than your memory of the tune.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "e4_3 e f g | g f e d | c c d e | e d d2 | e4 e f g | g f e d | c c d e | d c c2",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if you keep the beat going to the end of each one, with no more than one stop per exercise.",
    "Pass if at least 9 notes out of 10 are right, and you never worked a note out through the treble clef.",
    "When you pass, move on to Unit 3, where the two hands take turns. If not, play Part B and C exercises again in a week.",
]
