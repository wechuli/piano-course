"""Volume 4, Unit 7: Three sharps and three flats."""

KEYBOARDS = [["LH_AM", "RH_AM"], ["LH_Eb", "RH_Eb"]]
CHORD_SHAPES = [
    ("A major", "LH_AM", "a \\major", {"f": "is", "c": "is", "g": "is"}),
    ("E-flat major", "LH_Eb", "ees \\major", {"b": "es", "e": "es", "a": "es"}),
    ("F-sharp minor", "LH_Fsm", "fis \\minor", {"f": "is", "c": "is", "g": "is"}, True),
    ("C minor", "LH_Cm", "c \\minor", {"b": "es", "e": "es", "a": "es"}, True),
]

INTRO = [
    "Two new major keys and their relative minors. A major has three sharps (F, C and G); its relative minor is "
    "F-sharp minor. E-flat major has three flats (B, E and A); its relative minor is C minor. Each new sharp or "
    "flat adds one black key to the hand positions you already know.",
]

NEW_IDEAS = [
    ("Three sharps, three flats", "Sharps come in the order F C G (D A E B); flats in the order B E A (D G C F). "
                                  "The last sharp is the 7th note of the major key: G-sharp in A major. The second "
                                  "last flat names the key: E-flat."),
    ("F-sharp minor: E-sharp", "The raised 7th of F-sharp minor is E-sharp, which is the white key F. It looks "
                               "strange but is just the key below F-sharp."),
    ("C minor: B-natural", "The raised 7th of C minor is B-natural: the key signature has B-flat, so the "
                           "accidental is a natural sign."),
]

TIPS = [
    "Before you play, name the three sharps or flats and touch those keys with the right fingers.",
    "In the minor keys, expect the accidental (E-sharp or B-natural) in V7 bars.",
    "E-sharp and B-sharp, C-flat and F-flat are white keys: read the note name, then trust your hand.",
]

PART_NOTES = {
    "A": "A major with an Alberti bass. G-sharp is the bottom note of the V7 shape.",
    "B": "E-flat major waltzes. The thumb of the right hand sits on E-flat.",
    "C": "F-sharp minor: E-sharp (a white key) in the V7 bars.",
    "D": "C minor with an oom-pah bass: B-natural in the V7 bars.",
}

PIECES = [
    {
        "title": "Minuet in C minor", "credit": "From the Notebook for Anna Magdalena Bach, BWV Anh. 121 - first part",
        "meter": "3/4", "tempo": 92, "key": "c \\minor", "positions": ["RH_C5", "LH_F2"],
        "note": "High in the right hand, low in the left. Three accidentals: B-natural (the raised 7th) in bar 7, "
                "and E-natural (right hand) and A-natural (left hand) in bar 5, which lean briefly towards F minor. The trill in bar 4 is "
                "left out. Source: Mutopia Project no. 1613.",
        "rh": "c''4^1\\mf c'' d'' | ees'' ees'' f'' | g''^4 g'' aes''^5 | fis''2 g''4~ | \\break "
              "g''8 aes'' f'' e'' f''4~ | f''8 g'' ees'' d'' ees''4 | c''8 b' c''4 d'' | g'2.",
        "lh": "c2_5 r4 | c4 c d | ees ees c | d c b, | bes,2 a,4 | aes,2 g,4 | aes,2 f,4 | g,4 g8 f ees d",
    },
    {
        "title": "Spring in A", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "a \\major",
        "note": "A major over an Alberti bass. C-sharp and F-sharp are in the right hand's position; G-sharp comes in "
                "bars 3 and 7, where the thumb stretches down to it.",
        "rh": "cis''4^3\\mp b' a' cis'' | d''4 cis'' b' a' | b'4 d'' e'' gis'^1 | a'1 | \\break "
              "e''4^5\\mf cis'' a' cis'' | d''4 b' a' d'' | b'4\\> d'' b' gis' | a'1\\p",
        "lh": "a,8_5 e_1 cis_3 e a, e cis e | a,_5 fis_1 d_2 fis a, fis d fis | gis,_5 e_1 d_2 e gis, e d e | "
              "a,_5 e_1 cis_3 e a, e cis e | a, e cis e a, e cis e | a,_5 fis_1 d_2 fis a, fis d fis | "
              "gis,_5 e_1 d_2 e gis, e d e | a,1_5",
    },
    {
        "title": "E-flat Waltz", "credit": "Original", "meter": "3/4", "tempo": 120, "key": "ees \\major",
        "note": "Three flats: B-flat, E-flat and A-flat. Both hands start with a finger on E-flat; in bar 7 the "
                "right-hand thumb stretches down to D.",
        "rh": "g'2^3\\p bes'4 | aes'2 c''4 | f'2 aes'4 | g'2. | \\break bes'4^5\\mf g' ees' | aes'4 c'' aes' | "
              "f'4 d'^1 f' | ees'2.",
        "lh": "ees4_5 <g-3 bes-1> <g bes> | ees_5 <aes-2 c'-1> <aes c'> | d_5 <aes-2 bes-1> <aes bes> | "
              "ees_5 <g bes> <g bes> | ees <g bes> <g bes> | ees_5 <aes c'> <aes c'> | d_5 <aes bes> <aes bes> | <ees g bes>2.",
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Name the key of each exercise before you start, and play every sharp, flat and accidental.",
    "When you pass, move on to Unit 8.",
]
