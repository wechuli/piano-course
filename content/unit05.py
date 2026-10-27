"""Unit 5: Hands together."""

INTRO = [
    "Both hands now play at the same time. To make this manageable, the left hand keeps it simple: "
    "it holds long notes, only C (finger 5) or G (finger 1), while the right hand plays the tune. "
    "These two bass notes are the roots of the two most important chords in C major.",
]

NEW_IDEAS = [
    ("Reading two staves at once", "Notes that line up vertically are played together. Read the beat as a column: the right-hand note on top, the left-hand note below."),
    ("C and G in the bass", "C sits in the second space (finger 5) and G in the top space (finger 1). In this unit those are the only two left-hand notes."),
    ("Where the bass changes", "The left hand changes only on beat 1 (whole notes) or on beats 1 and 3 (half notes). Between those moments, spend all your attention on the right hand."),
]

TIPS = [
    "Before you start, find the first note in each hand and put both hands in place.",
    "Read the top line. Glance down only when a new bass note is due, on beat 1 or beat 3.",
    "If playing hands together falls apart, keep the right hand going and let the left hand drop out for a bar. Never stop the beat.",
    "Count aloud. Hands together is mostly a counting skill.",
]

PART_NOTES = {
    "A": "The left hand holds one whole note per bar: C or G. The right hand moves by step. Metronome 56.",
    "B": "The left hand may change on beat 3 (half notes), and the right hand uses skips too.",
    "C": "Eight-bar duets for your two hands.",
}

PIECES = [
    {
        "title": "Hot Cross Buns (hands together)", "credit": "Traditional (bar 3 simplified to quarter notes)",
        "meter": "4/4", "tempo": 72,
        "note": "The left hand holds C, and changes to G only once, in bar 3.",
        "rh": "e'4^3 d' c'2 | e'4 d' c'2 | c'4 c' d' d' | e'4 d' c'2",
        "lh": "c1_5 | c1 | c2 g2 | c1",
    },
    {
        "title": "Ode to Joy (hands together)", "credit": "Ludwig van Beethoven (1824), simplified",
        "meter": "4/4", "tempo": 76,
        "note": "The bass alternates C and G every bar, then stays on C at the end. Bars 1-3 and 5-7 are the same.",
        "rh": "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | e' d' d'2 | \\break e'4 e' f' g' | g' f' e' d' | c' c' d' e' | d' c' c'2",
        "lh": "c1_5 | g1 | c1 | g1 | c1 | g1 | c1 | c1",
    },
    {
        "title": "Morning Song", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The tune climbs the chain C-E-G in the first bar. The bass changes on beat 3 only in bar 7.",
        "rh": "c'4^1 e' g' e' | f'2 d' | e'4 c' d' e' | d'1 | \\break c'4 e' g' e' | f'2 d' | e'4 d' c' d' | c'1",
        "lh": "c1_5 | g1 | c1 | g1 | c1 | g1 | c2 g2 | c1",
    },
    {
        "title": "Bells in C", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "A waltz: the left hand rings one long bass note in every bar while the right hand sways.",
        "rh": "g'2^5 e'4 | f'2 d'4 | f'4 e' d' | e'2. | \\break g'2 e'4 | f'2 d'4 | e'4 d' d' | c'2.",
        "lh": "c2._5 | g2. | g2. | c2. | c2. | g2. | g2. | c2.",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 60 beats per minute.",
    "Pass if both hands keep going together, with no more than one stop per exercise.",
    "Pass if every left-hand change lands exactly on its beat.",
    "When you pass, move on to Unit 6. If not, play Part A again, then try Part C a week later.",
]
