"""Volume 3, Unit 6: Accidentals (the raised 7th in minor keys)."""

KEYBOARDS = []
CHORD_SHAPES = [
    ("A minor", "LH_A", "a \\minor", {}, True),
    ("E minor", "LH_E", "e \\minor", {"f": "is"}, True),
    ("B minor", "LH_Bm", "b \\minor", {"f": "is", "c": "is"}, True),
    ("G minor", "LH_Gm", "g \\minor", {"b": "es", "e": "es"}, True),
]

INTRO = [
    "A sharp, flat or natural written in the music, not in the key signature, is called an accidental. In minor "
    "keys you meet one all the time: the 7th note of the scale is raised by a half step so that it leads strongly "
    "home to the tonic. In A minor that note is G-sharp, although the key signature has no sharps at all.",
    "This unit uses four minor keys: A minor and E minor from Volume 2, and two new ones, B minor (the relative "
    "minor of D major, two sharps) and G minor (the relative minor of B-flat major, two flats).",
]

NEW_IDEAS = [
    ("How long an accidental lasts", "An accidental lasts until the next bar line, for that note only. In the "
                                     "next bar the key signature is back in charge. Here a reminder natural (or "
                                     "sharp) is printed in the next bar to help you."),
    ("The raised 7th", "A minor: G-sharp. E minor: D-sharp. B minor: A-sharp. G minor: F-sharp. It appears in "
                       "the V7 chord and, in the right hand, just below the tonic, where the thumb stretches down "
                       "to it."),
    ("Minor chord shapes", "i and iv are minor chords (lower-case numbers); V7 is the same shape as in a major key "
                           "but its bottom note is the raised 7th, so it carries the accidental."),
]

TIPS = [
    "In your scan, look for the accidentals: in these keys they come in the V7 bars, usually near the end.",
    "When you see the raised 7th, expect the tonic next.",
    "After a bar with an accidental, read the next bar carefully: the note goes back to the key signature.",
]

PART_NOTES = {
    "A": "A minor. G-sharp appears in the V7 shape (finger 5) and, in the right hand, under the thumb.",
    "B": "E minor in 3/4. The raised 7th is D-sharp.",
    "C": "B minor with an Alberti bass. Two sharps in the key signature, and A-sharp as an accidental.",
    "D": "G minor in 6/8. Two flats in the key signature, and F-sharp as an accidental.",
}

PIECES = [
    {
        "title": "Greensleeves", "credit": "Traditional English tune (16th century) - simplified",
        "meter": "3/4", "tempo": 76, "key": "a \\minor", "allow_range": True,
        "note": "The tune uses G and G-sharp: G in bars 4 and 12, G-sharp (with F-sharp) in bars 6, 7 and 14. Each "
                "sharp lasts only to the end of its bar. The right hand stays near A position; the thumb moves "
                "down for the low E in bar 8 and the F-sharp in bar 14.",
        "rh": "r2 a'4^1\\p | c''2^3 d''4 | e''4. f''8 e''4 | d''2 b'4 | \\break "
              "g'4.^1 a'8 b'4 | c''2 a'4 | a'4.^2 gis'8^1 a'4 | b'2 gis'4 | \\break "
              "e'2^1 a'4^1\\mf | c''2^3 d''4 | e''4. f''8 e''4 | d''2 b'4 | \\break "
              "g'4.^1 a'8 b'4 | c''4.\\> b'8 a'4 | gis'4.^2 fis'8^1 gis'4 | a'2.\\p",
        "lh": "R2. | a,2._5 | c2. | g,2. | e2. | a,2. | a,2. | e2. | a,2. | a,2. | c2. | g,2. | e2. | a,2. | e2. | a,2.",
    },
    {
        "title": "Song in G minor", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "g \\minor",
        "note": "Two flats in the key signature and an F-sharp in every V7 bar, in both hands. In bar 6 the right "
                "hand stretches finger 5 up to E-flat.",
        "rh": "bes'4^3\\mp a' g' bes' | c''2 bes'4 a' | a'4 fis'^1 a' c'' | bes'2 g' | \\break "
              "d''4^5\\mf c'' bes' d'' | ees''2^5 c'' | a'4\\> c'' fis'^1 a' | g'1\\p",
        "lh": "g,4_5 bes,_3 d_1 bes, | g,_5 c_2 ees_1 c | fis,_5 c_2 d_1 c | g,_5 bes,_3 d bes, | "
              "g, bes, d bes, | g,_5 c_2 ees c | fis,_5 c_2 d c | g,1_5",
    },
    {
        "title": "Dance in B minor", "credit": "Original", "meter": "6/8", "tempo": 56, "tempo_unit": "4.",
        "key": "b \\minor",
        "note": "A-sharp is the raised 7th of B minor. The right-hand thumb stretches down to it in bars 2 and 7, "
                "and it is the bottom note of the left hand's V7 shape.",
        "rh": "d''4^3\\mf cis''8 b'4 d''8 | cis''4 e''8 cis''4 ais'8^1 | cis''4. fis''^5 | d''4 b'8 b'4. | \\break "
              "fis''4^5 e''8 d''4 b'8 | e''4 d''8 cis''4 b'8 | ais'4^1 cis''8 e''4 cis''8 | b'2.",
        "lh": "b,4_5 fis8_1 d4_3 fis8 | ais,4_5 fis8_1 e4_2 fis8 | ais,4 fis8 e4 fis8 | b,4_5 fis8_1 d4_3 fis8 | "
              "b,4 fis8 d4 fis8 | b,4_5 g8_1 e4_2 g8 | ais,4_5 fis8_1 e4_2 fis8 | b,2._5",
    },
]

CHECKPOINT = [
    "Play five new exercises from Parts B to D at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every raised 7th is played sharp, and the same note in the next bar goes back to the key signature.",
    "When you pass, move on to Unit 7.",
]
