"""Unit 10: Sharps, flats, key signatures; review of Volume 1."""

KEYBOARDS = [["LH_D", "RH_D"], ["LH_F", "RH_F"]]

INTRO = [
    "Until now you have played only white keys. Sharps and flats take you to the black keys. "
    "This unit adds two new positions that each use one black key, and shows how a key signature "
    "tells you about it once, for the whole piece. The unit ends with a review of everything in Volume 1.",
]

NEW_IDEAS = [
    ("Sharp", "A sharp sign before a note means: play the very next key to the right (higher), usually a black key. F-sharp is the black key between F and G."),
    ("Flat", "A flat sign means: play the very next key to the left (lower). B-flat is the black key between A and B."),
    ("Natural", "A natural sign cancels a sharp or flat: play the white key."),
    ("How long an accidental lasts", "A sharp, flat or natural written in front of a note lasts until the end of that bar."),
    ("Key signature", "Sharps or flats at the start of every line apply to every note with that letter name, all the way through the piece. D major has F-sharp and C-sharp; F major has B-flat."),
    ("The two new positions", "D position is D E F-sharp G A, with finger 3 on the black key. F position is F G A B-flat C, with finger 4 on the black key."),
]

TIPS = [
    "Check the key signature first; it is now part of your 10-second scan.",
    "In D position, finger 3 sits on the black key F-sharp and stays there, so every F is automatically F-sharp.",
    "In F position, finger 4 sits on B-flat. Put it there before you start.",
    "The review part mixes everything: rests, ties, eighths, skips and 5ths. Scan for each before you play.",
]

PART_NOTES = {
    "A": "Right hand in D position, with the D major key signature. Metronome 60.",
    "B": "Left hand in D position. Bass D is the middle line, and F-sharp is the fourth line.",
    "C": "Right hand in F position, with the F major key signature (B-flat).",
    "D": "Review: hands together in C position, using everything from Volume 1.",
}

PIECES = [
    {
        "title": "Au clair de la lune in D", "credit": "Traditional French song (opening)", "meter": "4/4", "tempo": 76,
        "key": "d \\major",
        "note": "The tune from Unit 4, now in D position: every F is F-sharp because of the key signature.",
        "rh": "d'4^1 d' d' e' | fis'2 e' | d'4 fis' e' e' | d'1 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | d4_5 d d e | fis2 e | d4 fis e e | d1",
    },
    {
        "title": "Ode to Joy in D", "credit": "Ludwig van Beethoven (1824), simplified", "meter": "4/4", "tempo": 76,
        "key": "d \\major",
        "note": "Finger 3 starts on the black key F-sharp. The bass alternates D (finger 5) and A (finger 1).",
        "rh": "fis'4^3 fis' g' a' | a' g' fis' e' | d' d' e' fis' | fis' e' e'2 | \\break fis'4 fis' g' a' | a' g' fis' e' | d' d' e' fis' | e' d' d'2",
        "lh": "d1_5 | a1 | d1 | a1 | d1 | a1 | d1 | d1",
    },
    {
        "title": "Song in F", "credit": "Original", "meter": "4/4", "tempo": 72,
        "key": "f \\major",
        "note": "Finger 4 plays B-flat every time. The bass alternates F (finger 5) and middle C (finger 1).",
        "rh": "f'4^1 g' a' bes' | c''2 bes' | a'4 bes' a' g' | f'1 | \\break c''4 bes' a' bes' | c''2 a' | g'4 a' bes' g' | f'1",
        "lh": "f1_5 | c'1 | f1 | f1 | c'1 | f1 | c'1 | f1",
    },
    {
        "title": "Farewell Waltz", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "A goodbye to Volume 1, using skips, a 4th, eighths, a tie and a rest. Scan for each one before you play.",
        "rh": "e'2^3 g'4 | f'2 d'4 | e'4 d'8 c' d'4 | g'2.~ | \\break g'4 e' g' | f'2 d'4 | c'4 r e'8 d' | c'2.",
        "lh": "c2._5 | g2. | c2. | g2. | c2. | g2. | c2. | c2.",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Volume 2?"
CHECKPOINT = [
    "Play five Part D review exercises you have not played before, at 60 beats per minute.",
    "Pass if you keep the beat going with no more than one stop per exercise, and never miss the key signature in Parts A-C.",
    "Pass if at least 9 notes out of 10 are right.",
    "When you pass, you have finished Volume 1. If one skill keeps tripping you up, go back to its unit and read some Part C exercises again.",
]
