"""Unit 9: Eighth notes."""

KEYBOARDS = [["LH_C", "RH_C"]]

INTRO = [
    "Eighth notes are twice as fast as quarter notes: two of them share one beat. "
    "They look like quarter notes with a flag, or joined in pairs by a beam. "
    "Back in C position for this unit, so all your attention can go to the new rhythm.",
]

NEW_IDEAS = [
    ("The eighth note", "Half a beat. A single eighth note has a flag; two or more are usually joined by a beam."),
    ("Counting eighths", "Say '1 and 2 and 3 and 4 and'. The number falls on the beat and 'and' falls halfway between beats. A pair of eighths is '1-and'."),
    ("Even eighths", "Both eighths in a pair are the same length. Don't rush the second one."),
    ("Beams show the beat", "Each beamed pair fills one beat, so beams help you see where the beats fall in the bar."),
]

TIPS = [
    "In your 10-second scan, find the eighth-note pairs and count them '1-and' in your head.",
    "Keep the metronome slow. Eighths double the number of notes in a beat, not the speed of the beat.",
    "Beamed pairs usually step up or down: read the pair as one shape.",
    "If you stumble, keep the beat and pick up again on the next click.",
]

PART_NOTES = {
    "A": "Eighth notes in the right hand. Metronome 60: two eighths for each click.",
    "B": "Hands together: eighths on top, half notes in the bass.",
    "C": "Eighth notes in the left hand.",
}

PIECES = [
    {
        "title": "Hot Cross Buns (real rhythm)", "credit": "Traditional", "meter": "4/4", "tempo": 72,
        "note": "Now bar 3 has its real rhythm: 'one a pen-ny, two a pen-ny', four eighths on C, then four on D.",
        "rh": "e'4^3 d' c'2 | e'4 d' c'2 | c'8 c' c' c' d' d' d' d' | e'4 d' c'2",
        "lh": "c1_5 | c1 | c2 g2 | c1",
    },
    {
        "title": "Running Water", "credit": "Original", "meter": "4/4", "tempo": 66,
        "note": "Four eighths run up or down, then two quarters rest the stream. Keep the eighths even.",
        "rh": "c'8^1 d' e' f' g'4 g' | f'8 e' d' e' f'4 f' | e'8 d' c' d' e'4 e' | d'8 e' d' c' d'2 | \\break "
              "c'8 d' e' f' g'4 g' | f'8 e' d' e' f'4 e' | d'8 e' f' e' d'4 d' | c'1",
        "lh": "c1_5 | g1 | c1 | g1 | c1 | g1 | g1 | c1",
    },
    {
        "title": "Little Dance", "credit": "Original", "meter": "3/4", "tempo": 80,
        "note": "A waltz with an eighth-note pair on beat 2. Count '1, 2-and, 3'.",
        "rh": "e'4^3 d'8 e' f'4 | g'2 e'4 | f'4 e'8 d' e'4 | d'2. | \\break e'4 d'8 e' f'4 | g'2 e'4 | d'8 e' d' c' d'4 | c'2.",
        "lh": "c2._5 | c2. | g2. | g2. | c2. | c2. | g2. | c2.",
    },
    {
        "title": "Jingle Bells (chorus)", "credit": "James Lord Pierpont (1857), simplified", "meter": "4/4", "tempo": 92,
        "note": "Sixteen bars on four lines. Bar 3 has a 5th, from G down to C, and bars 6 and 14 end with an eighth-note pair.",
        "rh": "e'4^3 e' e'2 | e'4 e' e'2 | e'4 g' c' d' | e'1 | \\break "
              "f'4 f' f' f' | f' e' e' e'8 e' | e'4 d' d' e' | d'2 g' | \\break "
              "e'4 e' e'2 | e'4 e' e'2 | e'4 g' c' d' | e'1 | \\break "
              "f'4 f' f' f' | f' e' e' e'8 e' | g'4 g' f' d' | c'1",
        "lh": "c1_5 | c1 | c1 | c1 | g1 | c1 | g1 | g1 | c1 | c1 | c1 | c1 | g1 | c1 | g1 | c1",
    },
]

CHECKPOINT = [
    "Play five Part B exercises you have not played before, at 60 beats per minute.",
    "Pass if the eighth notes stay even and the beat never speeds up.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 10, the last unit of Volume 1.",
]
