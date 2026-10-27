"""Volume 2, Unit 3: Dotted quarter notes."""

KEYBOARDS = [["LH_C", "RH_C"]]

INTRO = [
    "A dot after a note adds half of its value. You already know the dotted half note (3 beats). Now meet the "
    "dotted quarter note: one and a half beats, almost always followed by a single eighth note that completes the second beat.",
]

NEW_IDEAS = [
    ("The dotted quarter", "A quarter note (1 beat) plus its dot (half a beat) makes one and a half beats."),
    ("Long-short", "A dotted quarter and an eighth together fill two beats. Count '1 and 2 and': the dotted quarter lasts through '1 and 2', and the eighth comes on the second 'and'."),
    ("How it sounds", "A lilting long-short, like the end of the first line of 'Ode to Joy'."),
]

TIPS = [
    "When you scan, count in eighths ('1 and 2 and') and notice that the dotted quarter covers '1 and 2'.",
    "Don't shorten the dotted quarter. The eighth comes late, just before the next beat.",
    "A dotted quarter in the middle of a bar crosses a beat. Keep counting through it.",
    "Use the metronome, and keep it slow.",
]

PART_NOTES = {
    "A": "Dotted quarter and eighth patterns in the right hand. Metronome 60.",
    "B": "The same rhythms in the left hand.",
    "C": "Dotted rhythms in 3/4.",
    "D": "Hands together, with the right hand moving between C and G positions.",
}

PIECES = [
    {
        "title": "Ode to Joy (real rhythm)", "credit": "Ludwig van Beethoven (1824)", "meter": "4/4", "tempo": 80,
        "note": "Now in its real rhythm, with the middle section. Bars 4, 8 and 16 have the dotted quarter. In bar 12 the left hand plays the low G with its thumb.",
        "rh": "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | e'4. d'8 d'2 | \\break "
              "e'4 e' f' g' | g' f' e' d' | c' c' d' e' | d'4. c'8 c'2 | \\break "
              "d'4^2 d' e' c' | d' e'8 f' e'4 c' | d' e'8 f' e'4 d' | c'4 d' r2 | \\break "
              "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | d'4. c'8 c'2",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | r2 g2_1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Dotted March", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "Every bar starts with long-short. March steadily, and give each dotted quarter its full length.",
        "rh": "c'4.^1 d'8 e'4 c' | e'4. f'8 g'2 | f'4. e'8 d'4 f' | e'4. d'8 c'2 | \\break "
              "g'4. f'8 e'4 g' | f'4. e'8 d'2 | e'4. d'8 c'4 d' | c'1",
        "lh": "c1_5 | c1 | g1 | c1 | c1 | g1 | c2 g2 | c1",
    },
    {
        "title": "Waltz with a Dot", "credit": "Original", "meter": "3/4", "tempo": 80,
        "note": "In 3/4 the long-short falls on beats 1 and 2. Count '1 and 2 and 3 and'.",
        "rh": "e'4.^3 f'8 g'4 | e'2 c'4 | d'4. e'8 f'4 | d'2. | \\break e'4. f'8 g'4 | g'4. f'8 e'4 | f'4. e'8 d'4 | c'2.",
        "lh": "c2._5 | c2. | g2. | g2. | c2. | c2. | g2. | c2.",
    },
]

CHECKPOINT = [
    "Play five Part D exercises you have not played before, at 60 beats per minute.",
    "Pass if every dotted quarter is held for its full length and the eighth after it is not rushed.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 4.",
]
