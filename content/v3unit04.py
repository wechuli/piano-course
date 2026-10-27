"""Volume 3, Unit 4: D major (two sharps)."""

KEYBOARDS = []
CHORD_SHAPES = [
    ("D major", "LH_D", "d \\major", {"f": "is", "c": "is"}),
]

INTRO = [
    "D major has two sharps: F-sharp and C-sharp. You met D position in Volume 1, when only F was sharp. Now "
    "the key signature shows both sharps, so every F and every C in the piece is played on a black key.",
]

NEW_IDEAS = [
    ("Two sharps", "The key signature of D major has a sharp on the F line and in the C space. The scale is D E "
                   "F-sharp G A B C-sharp D."),
    ("Where C-sharp comes from", "In the right hand, C-sharp is the note just below D: stretch the thumb down to "
                                 "it from D position, or play it with finger 3 in A position (A B C-sharp D E)."),
    ("Chord shapes in D", "I is D F-sharp A (5 3 1), IV is D G B (5 2 1) and V7 is C-sharp G A (5 2 1). The "
                          "V7 shape puts finger 5 on a black key."),
]

TIPS = [
    "Before you play, name the two sharps aloud, and put the fingers that will play them over the black keys.",
    "Read C-sharp in the left hand as 'the key below D': it is the bottom note of every V7 shape.",
    "If you play a white key by mistake, keep going, and check the key signature at the next line.",
]

PART_NOTES = {
    "A": "Right hand in D major. The thumb stretches down to C-sharp and finger 5 up to B. Metronome 60.",
    "B": "Alberti bass in D major. The right hand moves between D position and A position.",
    "C": "A waltz in D major, with the broken-chord bass from Unit 1.",
    "D": "D major in 6/8, with the lilting bass from Unit 3.",
}

PIECES = [
    {
        "title": "Lightly Row", "credit": "Traditional German folk song ('Hänschen klein')",
        "meter": "4/4", "tempo": 88, "key": "d \\major",
        "note": "A folk song in D major. The right hand stays in D position all the way through. In bar 15 the "
                "left hand changes from I to V7 halfway through the bar.",
        "rh": "a'4^5 fis' fis'2 | g'4 e' e'2 | d'4 e' fis' g' | a' a' a'2 | \\break "
              "a'4 fis' fis'2 | g'4 e' e'2 | d'4 fis' a' a' | d'1 | \\break "
              "e'4 e' e' e' | e' fis' g'2 | fis'4 fis' fis' fis' | fis' g' a'2 | \\break "
              "a'4 fis' fis'2 | g'4 e' e'2 | d'4 fis' a' a' | d'1",
        "lh": "d4_5 fis_3 a_1 fis | cis_5 g_2 a_1 g | d_5 fis_3 a fis | d fis a fis | d fis a fis | cis_5 g_2 a g | "
              "d_5 fis_3 a fis | d fis a fis | cis_5 g_2 a g | cis g a g | d_5 fis_3 a fis | d fis a fis | "
              "d fis a fis | cis_5 g_2 a g | d_5 fis cis_5 g | d1_5",
    },
    {
        "title": "Country Dance in D", "credit": "Original", "meter": "6/8", "tempo": 60, "tempo_unit": "4.",
        "key": "d \\major",
        "note": "A 6/8 dance with the lilting bass. In bars 3 and 7 the right-hand thumb stretches down to "
                "C-sharp, which leads up to D.",
        "rh": "fis'4^3\\mf a'8 fis'4 d'8 | g'4 b'8^5 g'4 e'8 | e'4 g'8 e'4 cis'8^1 | d'2. | \\break "
              "a'4^5 fis'8 a'4 fis'8 | g'4. b' | a'4\\> g'8 e'4 cis'8 | d'2.\\p",
        "lh": "d4_5 a8_1 fis4_3 a8 | d4_5 b8_1 g4_2 b8 | cis4_5 a8_1 g4_2 a8 | d4_5 a8_1 fis4_3 a8 | "
              "d4 a8 fis4 a8 | d4_5 b8_1 g4_2 b8 | cis4_5 a8_1 g4_2 a8 | d2._5",
    },
    {
        "title": "Bells in D", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "d \\major",
        "note": "The right hand starts in A position, where finger 3 plays C-sharp, and moves down to D position "
                "in bar 6. The left hand plays an Alberti bass.",
        "rh": "a'2^1\\mf d''4^4 a' | cis''2^3 e''4^5 cis'' | d''4 cis'' b' a' | a'2 cis'' | \\break "
              "b'2\\p d''4 b' | a'4 fis'^3 d' fis' | e'2\\< g'4 e' | d'1\\mf",
        "lh": "d8_5 a_1 fis_3 a d a fis a | cis_5 a_1 g_2 a cis a g a | d_5 a_1 fis_3 a d a fis a | "
              "cis_5 a_1 g_2 a cis a g a | d_5 b_1 g_2 b d b g b | d_5 a_1 fis_3 a d a fis a | "
              "cis_5 a_1 g_2 a cis a g a | d1_5",
    },
]

CHECKPOINT = [
    "Play five new Part B or D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every F and C is sharp, in both hands, without stopping to think.",
    "When you pass, move on to Unit 5.",
]
