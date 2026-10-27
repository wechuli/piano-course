"""Volume 3, Unit 9: Imitation."""

KEYBOARDS = []

INTRO = [
    "In imitation, one voice plays a tune and another voice repeats it a little later, while the first voice "
    "goes on with something new. It is the oldest trick in counterpoint, and the simplest kind of music in which "
    "two voices are truly equal. In this unit the right hand plays a short tune and the left hand answers with "
    "the same tune, an octave or two lower, two bars later.",
]

NEW_IDEAS = [
    ("Spot the tune once, play it twice", "The left hand's entry looks exactly like the right hand's first two "
                                          "bars, moved down. You have already read it, so you can watch the right "
                                          "hand while the left hand repeats it."),
    ("The other voice keeps going", "While the left hand imitates, the right hand plays a new, slower line "
                                    "above it. Hold its long notes for their full length."),
    ("Rounds and canons", "When the second voice copies the whole tune, the piece is a round or canon, like "
                          "Frère Jacques."),
]

TIPS = [
    "In your scan, compare bars 1-2 (right hand) with bars 3-4 (left hand): the shape is the same.",
    "Bring out whichever hand has the tune at the moment.",
    "Count the rests at the start carefully, so the left hand comes in exactly on time.",
]

PART_NOTES = {
    "A": "C major, four bars: the left hand repeats the right hand's tune an octave lower.",
    "B": "G major, eight bars: two tunes, each answered two octaves lower. In bars 5-6 the left hand has a "
         "counter-melody under the second tune.",
    "C": "F major in 3/4.",
    "D": "D major in 6/8.",
}

PIECES = [
    {
        "title": "Frère Jacques", "credit": "Traditional French round - simplified",
        "meter": "4/4", "tempo": 84,
        "note": "A round: the left hand starts the same song two bars after the right hand. In the last line of the "
                "tune each hand jumps up to G instead of down.",
        "rh": "c'4^1\\mf d' e' c' | c' d' e' c' | e' f' g'2 | e'4 f' g'2 | g'8 a' g' f' e'4 c' | \\break "
              "g'8 a' g' f' e'4 c' | c'4 g' c'2 | c'4 g' c'2 | e'1\\p | c'1",
        "lh": "R1 | R1 | c4_5 d e c | c d e c | e f g2 | e4 f g2 | g8 a g f e4 c | g8 a g f e4 c | "
              "c4 g c2 | c4 g c2",
    },
    {
        "title": "Echo Waltz", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "g \\major",
        "note": "Two little tunes, each echoed two octaves lower by the left hand, under long right-hand notes.",
        "rh": "d''4^5\\mf c'' b' | a'2 g'4 | b'2.^3\\p | c''2 b'4 | \\break "
              "b'4\\mf a' b' | a'2 g'4 | d''2.^5\\p | c''2 g'4^1",
        "lh": "R2. | R2. | d4_1 c b, | a,2 g,4 | g,2._5 | c2_2 b,4 | b,4_3 a, b, | a,2 g,4",
    },
    {
        "title": "Follow the Leader", "credit": "Original", "meter": "4/4", "tempo": 80, "key": "d \\major",
        "note": "Each two-bar tune is copied an octave lower by the left hand, in D position. In bar 6 the left "
                "hand stretches finger 5 down to C-sharp.",
        "rh": "fis'4^3\\mf e' d' fis' | a'2^5 g' | a'2\\p fis' | fis'2 e' | \\break "
              "a'4^5\\mf g' fis' a' | e'2 d' | e'2^2\\p fis' | g'2 d'^1",
        "lh": "R1 | R1 | fis4_3 e d fis | a2_1 g | d2_5 a | cis_5 d | a4_1 g fis a | e2 d_5",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "The left hand comes in on time, and the tune passes clearly from hand to hand. Then move on to Unit 10.",
]
