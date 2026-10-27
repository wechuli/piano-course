"""Volume 3, Unit 5: B-flat major (two flats)."""

KEYBOARDS = [["LH_Bb", "RH_Bb"]]
CHORD_SHAPES = [
    ("B-flat major", "LH_Bb", "bes \\major", {"b": "es", "e": "es"}),
]

INTRO = [
    "B-flat major has two flats: B-flat and E-flat. Its home note is a black key, so both hands start with the "
    "thumb or finger 5 on B-flat. It feels strange for a day or two, and then very comfortable, because the hand "
    "sits a little further into the keys.",
]

NEW_IDEAS = [
    ("Two flats", "The key signature has a flat on the B line and in the E space. The scale is B-flat C D E-flat "
                  "F G A B-flat."),
    ("B-flat position", "Right hand: B-flat (1) C (2) D (3) E-flat (4) F (5). Left hand: B-flat (5) C (4) D (3) "
                        "E-flat (2) F (1). Two of the five keys are black."),
    ("Chord shapes in B-flat", "I is B-flat D F (5 3 1), IV is B-flat E-flat G (5 2 1) and V7 is A E-flat F "
                               "(5 2 1)."),
]

TIPS = [
    "Put the thumb (right hand) or finger 5 (left hand) on B-flat before you start, and check where E-flat is.",
    "F position (F G A B-flat C) also fits B-flat major: the right hand often moves between the two.",
    "Say 'B-flat, E-flat' aloud while you scan the key signature.",
]

PART_NOTES = {
    "A": "Right hand in B-flat major, moving between B-flat position and F position. Metronome 60.",
    "B": "Left hand in B-flat position. B-flat is the second line; E-flat is the third space.",
    "C": "An Alberti bass in B-flat major.",
    "D": "A waltz. The right hand moves between F position and B-flat position.",
}

PIECES = [
    {
        "title": "Au clair de la lune", "credit": "Traditional French song",
        "meter": "4/4", "tempo": 84, "key": "bes \\major",
        "note": "The song from Volume 1, now in B-flat major. In bar 9 the right hand moves down to F position "
                "(finger 5 on C) and in bar 13 back to B-flat position. The left hand plays broken chords.",
        "rh": "bes'4^1 bes' bes' c'' | d''2 c'' | bes'4 d'' c'' c'' | bes'1 | \\break "
              "bes'4 bes' bes' c'' | d''2 c'' | bes'4 d'' c'' c'' | bes'1 | \\break "
              "c''4^5 c'' c'' c'' | g'2^2 g' | c''4^5 bes' a' g' | f'1 | \\break "
              "bes'4^1 bes' bes' c'' | d''2 c'' | bes'4 d'' c'' c'' | bes'1",
        "lh": "bes,4_5 d_3 f_1 d | bes, d a,_5 ees_2 | bes,_5 d a,_5 ees | bes,_5 d f d | "
              "bes, d f d | bes, d a,_5 ees | bes,_5 d a,_5 ees | bes,_5 d f d | "
              "a,_5 ees_2 f ees | bes,_5 ees g ees | a,_5 ees f ees | bes,_5 d_3 f d | "
              "bes, d f d | bes, d a,_5 ees | bes,_5 d a,_5 ees | bes,1_5",
    },
    {
        "title": "Song in B-flat", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "bes \\major",
        "note": "A singing tune over an Alberti bass. In bar 7 the right-hand thumb stretches down to A, the note "
                "below B-flat, and resolves up to B-flat.",
        "rh": "d''4^3\\mp( c'' bes' d'') | ees''2( d''4 c'') | c''4( ees'' d'' c'') | d''1 | \\break "
              "f''4^5\\mf( ees'' d'' bes') | ees''4( d'' c'' ees'') | ees''4\\>( c'' a'^1 c'') | bes'1\\p",
        "lh": "bes,8_5 f_1 d_3 f bes, f d f | bes,_5 g_1 ees_2 g bes, g ees g | a,_5 f_1 ees_2 f a, f ees f | "
              "bes,_5 f_1 d_3 f bes, f d f | bes, f d f bes, f d f | bes,_5 g_1 ees_2 g bes, g ees g | "
              "a,_5 f_1 ees_2 f a, f ees f | bes,1_5",
    },
    {
        "title": "Waltz in B-flat", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "bes \\major",
        "note": "Watch the left hand in bars 4 and 7: from the top of IV (G) it reaches down to A for V7.",
        "rh": "d''2^3\\p bes'4 | f''2^5 d''4 | ees''4 d'' c'' | c''2. | \\break "
              "d''4\\mf c'' bes' | ees''2 bes'4 | c''4 a'^1 c'' | bes'2.",
        "lh": "bes,4_5 d_3 f_1 | bes, d f | bes,_5 ees_2 g_1 | a,_5 ees_2 f_1 | bes,_5 d_3 f | "
              "bes,_5 ees_2 g | a,_5 ees_2 f | bes,2._5",
    },
]

CHECKPOINT = [
    "Play five new Part C or D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every B and E is flat, in both hands.",
    "When you pass, move on to Unit 6.",
]
