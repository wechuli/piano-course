"""Volume 2, Unit 9: E minor and D minor."""

KEYBOARDS = [["LH_E", "RH_E"], ["LH_Dm", "RH_Dm"]]

INTRO = [
    "Two more minor keys. E minor is the relative minor of G major: the same key signature (one sharp, F-sharp), "
    "with home note E. D minor is the relative minor of F major: the same key signature (one flat, B-flat), with home note D.",
]

NEW_IDEAS = [
    ("E minor", "One sharp in the key signature, ending on E. In E position (E F-sharp G A B), the black key F-sharp is finger 2 in the right hand and finger 4 in the left."),
    ("D minor", "One flat in the key signature, ending on D. D position (D E F G A) contains no B, so every note is a white key."),
    ("Which key?", "One sharp: G major or E minor. One flat: F major or D minor. The last note and the lowest bass note tell you which."),
]

TIPS = [
    "Scan the key signature, then the last bass note, and name the key before you start.",
    "In E position, put finger 2 (right hand) or finger 4 (left hand) on F-sharp first.",
    "D minor's position uses only white keys, even though there is a flat in the key signature.",
    "Keep going even if a note goes wrong.",
]

PART_NOTES = {
    "A": "E minor in the right hand. Metronome 60.",
    "B": "E minor, hands together.",
    "C": "D minor in the right hand.",
    "D": "D minor, hands together in 3/4.",
}

PIECES = [
    {
        "title": "Song in E Minor", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "e \\minor",
        "note": "The tune starts with the little finger on B. Finger 2 plays F-sharp; the bass alternates E (finger 5) and B (finger 1).",
        "rh": "b'2^5 a'4 g' | fis'2 e' | g'4 a' b' a' | b'1 | \\break b'2 a'4 g' | fis'2 g' | fis'4 e' e' fis' | e'1",
        "lh": "e1_5 | b1 | e1 | b1 | e1 | b1 | b1 | e1",
    },
    {
        "title": "D Minor Waltz", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "d \\minor",
        "note": "D position, all white keys. The bass alternates D (finger 5) and A (finger 1).",
        "rh": "d'4^1 f' a' | g'2 f'4 | e'4 f' g' | a'2. | \\break a'4 g' f' | e'2 f'4 | e'4 d' e' | d'2.",
        "lh": "d2._5 | a2. | a2. | a2. | d2. | a2. | a2. | d2.",
    },
    {
        "title": "E Minor Walk", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "e \\minor",
        "note": "For the left hand alone, in E position; finger 4 plays F-sharp.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "e4_5 fis g a | b2 g | a4 g fis g | e1 | g4 a b a | g2 fis | e4 fis g fis | e1",
    },
]

CHECKPOINT = [
    "Play three Part B and three Part D exercises you have not played before, at the speeds shown.",
    "Pass if you name each key correctly before you start.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 10, the review.",
]
