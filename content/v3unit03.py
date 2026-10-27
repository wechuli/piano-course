"""Volume 3, Unit 3: Six-eight time."""

KEYBOARDS = []  # C position needs no picture by now; this unit is about rhythm

INTRO = [
    "In 6/8 time a bar holds six eighth notes, grouped in two sets of three: ONE two three FOUR five six. "
    "At a slow speed you can count all six. At a normal speed you feel only two beats in a bar, and each beat "
    "splits into three. That gives 6/8 its rocking, swinging feel, like a boat song or a lullaby.",
]

NEW_IDEAS = [
    ("6/8", "The bottom 8 means the eighth note is the counting unit, and the top 6 means six of them in a bar. "
            "Eighths are beamed in threes, so you can see the two beats."),
    ("The beat is a dotted quarter", "One beat in 6/8 lasts three eighths: a dotted quarter note. A dotted half "
                                     "note fills the whole bar. The metronome marks in this unit count dotted "
                                     "quarters."),
    ("Long-short", "A quarter note followed by an eighth (counted 1-2 3) is the typical 6/8 rhythm: long, short, "
                   "long, short. Do not let it turn into an even pair."),
    ("Two new bass patterns", "Lilting: bottom (quarter), top (eighth), middle (quarter), top (eighth). Rolling: "
                              "six eighths, bottom, middle, top, middle, top, middle."),
]

TIPS = [
    "Count six slowly first, then switch to two beats: ONE-and-a TWO-and-a.",
    "Find the dotted quarters and dotted halves before you start: they show where the beats are.",
    "Feel the long-short swing in the left hand, and let the right hand ride on it.",
]

PART_NOTES = {
    "A": "Right hand in C position. Count six eighths at first; the metronome gives one click per dotted quarter.",
    "B": "Left hand in C position, in 6/8.",
    "C": "G major, hands together. The left hand plays the lilting pattern: long, short, long, short.",
    "D": "F major with the rolling pattern: six even eighths in the left hand.",
}

PIECES = [
    {
        "title": "Row, Row, Row Your Boat", "credit": "Traditional song (published 1852)",
        "meter": "6/8", "tempo": 56, "tempo_unit": "4.",
        "note": "The best-known 6/8 song. In bar 5 the right hand moves up so finger 5 takes high C; in bar 6 it "
                "moves back to C position. The left hand lilts on I until the V7 in bar 7. It is also a round: two "
                "players can start two bars apart.",
        "rh": "c'4.^1 c' | c'4 d'8 e'4. | e'4 d'8 e'4 f'8 | g'2. | \\break "
              "c''8^5 c'' c'' g'^1 g' g' | e'^3 e' e' c'^1 c' c' | g'4^5 f'8 e'4 d'8 | c'2.",
        "lh": "c4_5 g8_1 e4_3 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | "
              "b,4_5 g8_1 f4_2 g8 | c2._5",
    },
    {
        "title": "Silent Night", "credit": "Franz Xaver Gruber (1818) - shortened and simplified",
        "meter": "6/8", "tempo": 44, "tempo_unit": "4.", "allow_range": True,
        "note": "The first eight bars and the last eight bars of the carol. The tune climbs through three hand "
                "positions; the finger numbers show each move. The left hand lilts on I and V7.",
        "rh": "g'4.^4 a'8 g'4 | e'2. | g'4. a'8 g'4 | e'2. | \\break "
              "d''2^5 d''4 | b'2. | c''2^4 c''4 | g'2.^1 | \\break "
              "d''2^5 d''4 | f''4.^5 d''8^3 b'4^1 | c''2.^2 | e''2.^4 | \\break "
              "c''4^5 g'^3 e'^1 | g'4.^5 f'8 d'4 | c'2. | c'2.",
        "lh": "c4_5 g8_1 e4_3 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | c4 g8 e4 g8 | b,4_5 g8_1 f4_2 g8 | b,4 g8 f4 g8 | "
              "c4_5 g8_1 e4_3 g8 | c4 g8 e4 g8 | b,4_5 g8_1 f4_2 g8 | b,4 g8 f4 g8 | c4_5 g8_1 e4_3 g8 | "
              "c4 g8 e4 g8 | c4 g8 e4 g8 | b,4_5 g8_1 f4_2 g8 | c4_5 g8 e4 g8 | c2.",
    },
    {
        "title": "Hunting Horns", "credit": "Original", "meter": "6/8", "tempo": 52, "tempo_unit": "4.",
        "key": "f \\major",
        "note": "Loud horn calls, then a soft echo. The left hand plays rolling eighths; in bars 3 and 4 the V7 "
                "shape has B-flat in the middle. In bar 3 the right hand stretches finger 1 down to E.",
        "rh": "c''4^5\\f a'8 f'4 a'8 | c''4. a' | g'4 bes'8 g'4 e'8^1 | g'4. c'' | \\break "
              "a'4^3\\p c''8 a'4 f'8 | bes'4 a'8 g'4 f'8 | g'4 a'8 bes'4 g'8 | f'2.",
        "lh": "f8_5 a_3 c'_1 a c' a | f a c' a c' a | e_5 bes_2 c'_1 bes c' bes | e bes c' bes c' bes | "
              "f_5 a_3 c'_1 a c' a | f_5 bes_2 d'_1 bes d' bes | e_5 bes_2 c'_1 bes c' bes | f2._5",
    },
]

CHECKPOINT = [
    "Play five new Part C or D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "You can feel two beats in each bar, and the long-short rhythm swings rather than sounding even.",
    "When you pass, move on to Unit 4.",
]
