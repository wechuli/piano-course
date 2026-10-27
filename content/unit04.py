"""Unit 4: Skips (thirds)."""

KEYBOARDS = [["LH_C", "RH_C"]]

INTRO = [
    "Until now every melody moved by step or stayed on the same note. Now notes can skip: jump over one key, "
    "and over one finger. Both hands are still in C position, so a skip never needs a hand move.",
]

NEW_IDEAS = [
    ("The skip (a third)", "A skip jumps over one white key and one finger: C to E, D to F, E to G, and back down."),
    ("Skips on the staff", "A step always goes from a line to a space or from a space to a line. A skip goes from a line to the next line, or from a space to the next space."),
    ("Fingers for skips", "Skips use every other finger: 1 to 3, 2 to 4, or 3 to 5."),
    ("Chains of skips", "C, E and G can follow each other. In the treble clef they sit on the ledger line, line 1 and line 2; in the bass clef they sit in three spaces in a row."),
]

TIPS = [
    "In your 10-second scan, look for pairs of notes that are both on lines or both in spaces. Those are skips.",
    "Think of a skip as a finger jump (1-3, 2-4, 3-5) rather than naming the new note.",
    "Spot chains: line-line-line, or space-space-space, is C-E-G. Read it as one shape.",
    "If a skip catches you out, keep the beat and carry on. Accuracy improves with more reading, not with stopping.",
]

PART_NOTES = {
    "A": "Skips in the right hand, mixed with steps. Metronome 60.",
    "B": "Skips in the left hand. In the bass clef, C, E and G sit in the second, third and top spaces.",
    "C": "Skips with the hands taking turns, in eight-bar phrases.",
}

PIECES = [
    {
        "title": "Mary Had a Little Lamb", "credit": "Traditional", "meter": "4/4", "tempo": 84,
        "note": "One skip only: E up to G in bar 4. Everything else moves by step or repeats.",
        "rh": "e'4^3 d' c' d' | e' e' e'2 | d'4 d' d'2 | e'4 g' g'2 | \\break e'4 d' c' d' | e' e' e' e' | d' d' e' d' | c'1",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Au clair de la lune", "credit": "Traditional French song (opening)", "meter": "4/4", "tempo": 76,
        "note": "The right hand sings the phrase, then the left hand repeats it. Find the skip in bar 3 before you start.",
        "rh": "c'4^1 c' c' d' | e'2 d' | c'4 e' d' d' | c'1 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | c4_5 c c d | e2 d | c4 e d d | c1",
    },
    {
        "title": "Leapfrog", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "Skip, step, skip, step: the right hand hops up, then the left hand hops down from G.",
        "rh": "c'4^1 e' d' f' | e' g' f'2 | e'4 c' d' e' | c'1 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | g4_1 e f d | e c d2 | e4 d c d | c1",
    },
    {
        "title": "Stepping Stones", "credit": "Original", "meter": "3/4", "tempo": 88,
        "note": "Each bar steps down and then skips up, like crossing a stream on stones. Lean on beat 1.",
        "rh": "e'2^3 c'4 | d'2 f'4 | e'2 g'4 | f'2. | \\break e'2 c'4 | d'2 f'4 | e'4 d' d' | c'2.",
        "lh": "R2. | R2. | R2. | R2. | R2. | R2. | R2. | R2.",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if you keep the beat going, with no more than one stop per exercise.",
    "Pass if you play the skips without looking down, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 5, where both hands play at the same time.",
]
