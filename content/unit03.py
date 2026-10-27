"""Unit 3: Hands take turns; 3/4 time and the dotted half note."""

INTRO = [
    "From now on both hands sit in C position at the same time: the left hand on C to G below middle C, "
    "the right hand on C to G from middle C. In this unit they take turns. One hand plays while the other waits, "
    "resting on its keys and ready. You will also meet a new time signature, 3/4.",
]

NEW_IDEAS = [
    ("Taking turns", "The melody moves from one staff to the other. When it moves to the bass staff, the left hand plays; when it moves back up, the right hand plays."),
    ("Full-bar rests", "A bar with only a rest in it means that hand is silent for the whole bar. In every time signature this is the whole-rest sign, a small block hanging under the fourth line."),
    ("3/4 time", "Three beats in every bar. Count 1 - 2 - 3, and lean a little on beat 1, like a waltz."),
    ("The dotted half note", "A dot adds half of the note's value: a half note (2 beats) plus its dot (1 beat) makes 3 beats, a full bar in 3/4."),
]

TIPS = [
    "Look ahead to the bar where the melody changes staff. Know which hand plays next before you get there.",
    "The resting hand stays on its five keys, so it can start without looking down.",
    "In 3/4, keep counting 1 - 2 - 3 right through a dotted half note. It is easy to cut it short to two beats.",
    "As always: keep the beat going, even after a mistake.",
]

PART_NOTES = {
    "A": "The melody passes between the hands every two bars. 4/4 time, metronome 60.",
    "B": "3/4 time, right hand only. New rhythm: the dotted half note, worth three beats.",
    "C": "Eight-bar phrases in 3/4, with the hands taking turns.",
}

PIECES = [
    {
        "title": "Echo", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The left hand echoes the right hand an octave lower. Play the echo a little softer.",
        "rh": "c'4^1 d' e' d' | c'2 d' | R1 | R1 | \\break e'4^3 f' e' d' | c'1 | R1 | R1",
        "lh": "R1 | R1 | c4_5 d e d | c2 d | R1 | R1 | e4_3 f e d | c1",
    },
    {
        "title": "Waltz for Two Hands", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "One, two, three. The tune passes from hand to hand every two bars. Hold each dotted half note for all three beats.",
        "rh": "e'4^3 f' g' | f'2. | R2. | R2. | \\break e'2 f'4 | g'2. | R2. | R2.",
        "lh": "R2. | R2. | e4_3 d c | d2. | R2. | R2. | f4_2 e d | c2.",
    },
    {
        "title": "The Swing", "credit": "Original", "meter": "3/4", "tempo": 80,
        "note": "The right hand swings down from G, then the left hand answers from its own G.",
        "rh": "g'2.^5 | f'4 e' d' | e'2 f'4 | g'2. | \\break R2. | R2. | R2. | R2.",
        "lh": "R2. | R2. | R2. | R2. | g2._1 | f4 e d | e2 d4 | c2.",
    },
    {
        "title": "Ode to Joy (shared)", "credit": "Ludwig van Beethoven (1824), simplified", "meter": "4/4", "tempo": 80,
        "note": "The right hand plays the first half and the left hand finishes the tune. Be ready to start the left hand in bar 5.",
        "rh": "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | e' d' d'2 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | e4_3 e f g | g f e d | c c d e | d c c2",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 72 beats per minute.",
    "Pass if the beat never stops when the melody changes hands.",
    "Pass if every dotted half note gets its full three beats, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 4. If not, read more Part A and C exercises in a week.",
]
