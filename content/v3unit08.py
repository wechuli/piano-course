"""Volume 3, Unit 8: Two independent voices."""

KEYBOARDS = []

INTRO = [
    "Until now the left hand has accompanied: it held notes or played chord patterns. Now it plays a real "
    "melody of its own, a second voice. Each hand has its own rhythm and its own direction, and the two voices "
    "fit together beat by beat. Music written like this, with independent lines, is called counterpoint.",
]

NEW_IDEAS = [
    ("Contrary motion", "One hand goes up while the other goes down. It is the easiest motion to read: the hands "
                        "move like a mirror."),
    ("Parallel and oblique motion", "Parallel: both hands move the same way, often a third or sixth apart. "
                                    "Oblique: one hand holds a note while the other moves."),
    ("How the voices fit", "On the main beats the two hands sound a third, sixth, fifth or octave apart. A note "
                           "that clashes falls between the beats, on the way from one note to the next."),
    ("Read down, then across", "Look at both staves on beat 1 of each bar, then follow each line. In Part B the "
                               "tune is in the left hand; let it sing louder than the right."),
]

TIPS = [
    "Before you start, follow the direction of each hand through the first two bars.",
    "Count out loud: two independent rhythms only fit together if the beat is steady.",
    "If one hand has long notes, keep them held for their full length while the other hand moves.",
]

PART_NOTES = {
    "A": "The right hand has the tune; the left hand answers in half notes, often moving the other way.",
    "B": "The tune is in the left hand. The right hand plays long notes above it.",
    "C": "Two voices in G major, in 3/4. The left hand moves in quarter and half notes.",
    "D": "Both hands in quarter notes: real two-part writing in F major.",
}

PIECES = [
    {
        "title": "Ode to Joy in Two Voices",
        "credit": "Ludwig van Beethoven, theme from Symphony No. 9 - with an added second voice",
        "meter": "4/4", "tempo": 72,
        "note": "The tune from Unit 1, now with a left-hand melody in half notes instead of broken chords. In bar 1 "
                "the hands move apart: the right hand climbs while the left hand falls.",
        "rh": "e'4^3\\mf e' f' g' | g' f' e' d' | c' c' d' e' | e'4. d'8 d'2 | \\break "
              "e'4 e' f' g' | g' f' e' d' | c' c' d' e' | d'4. c'8 c'2",
        "lh": "e2_3 c_5 | b,_5 c | e_3 g_1 | c_5 b, | e_3 c_5 | b,_5 c | e_3 g_1 | g c_5",
    },
    {
        "title": "Mirror Talk", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "Quarter notes in both hands, mostly in contrary motion: when the right hand steps up, the left hand "
                "steps down. Both hands are in C position; the left hand stretches finger 5 down to B in bar 4.",
        "rh": "e'4^3\\p f' g' e' | d'2 g' | f'4 e' d' f' | e'2 d' | \\break "
              "c'4^1\\mf d' e' c' | f'2 e' | d'4 e' f' d' | c'1",
        "lh": "g4_1 f e g | f2 e | d4 e f d | c2 b,_5 | e4_3 d c e | d2 g | g4_1 e d g | c1_5",
    },
    {
        "title": "The Cellist", "credit": "Original", "meter": "3/4", "tempo": 80, "key": "g \\major",
        "note": "The tune is in the left hand, low like a cello. Let it sing; the right hand holds quiet notes above.",
        "rh": "b'2.^3\\pp | a'2. | c''2. | b'2. | \\break c''2. | d''2. | a'2. | g'2.",
        "lh": "g,4_5\\mf a, b, | c2 b,4 | a, b, c | d2. | e4_1 d c | b,2 a,4 | d c b, | g,2._5",
    },
]

CHECKPOINT = [
    "Play five new exercises from Parts B to D at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Both lines are clear: long notes are held, and the tune sings in whichever hand has it.",
    "When you pass, move on to Unit 9.",
]
