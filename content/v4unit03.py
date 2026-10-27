"""Volume 4, Unit 3: High notes (ledger lines above the treble staff)."""

KEYBOARDS = [["RH_C5"], ["RH_G5"]]

INTRO = [
    "The treble staff ends at F, on its top line. Notes above it are written on short extra lines called ledger "
    "lines. Counting ledger lines note by note is slow; instead, learn a few landmarks and read from them. In "
    "this unit the right hand works in two high positions, and also jumps up and down an octave.",
]

NEW_IDEAS = [
    ("Ledger lines above", "G5 sits just above the staff. A5 is on the first ledger line, B5 just above it, and "
                           "high C (C6) on the second ledger line. D6 sits above two ledger lines."),
    ("Landmarks", "Know three Cs at a glance: middle C on its own ledger line below the staff, C5 in the third "
                  "space, and C6 on two ledger lines above. Read nearby notes as steps from the nearest C."),
    ("The octave move", "Moving a hand up an octave changes a note on a line to the same letter in a space, and "
                        "the other way round: G4 is on a line, G5 is in a space. A finger number marks the move."),
]

TIPS = [
    "In your scan, find the highest note and name it from a landmark before you start.",
    "For an octave move, keep the same finger on the same letter and let the arm carry the hand.",
    "Play high notes lightly: they sound bright and carry easily.",
]

PART_NOTES = {
    "A": "Right hand in high C position: C5 (thumb) to G5 (finger 5).",
    "B": "The right hand moves between C position and high C position, an octave apart. Watch the finger numbers.",
    "C": "G major: the right hand in high G position (G5 to D6) over broken chords.",
    "D": "D major in 2/4: the right hand moves between D position and high D position over an Alberti bass.",
}

PIECES = [
    {
        "title": "Humming Song", "credit": "Robert Schumann, Op. 68 No. 3 (first section) - left hand an octave lower",
        "meter": "4/4", "tempo": 72,
        "note": "From Schumann's Album for the Young. The tune sits in high C position all the way through. Schumann "
                "wrote the left hand in the treble clef; here it is an octave lower, in the bass clef. Notes from "
                "Mutopia Project no. 651.",
        "rh": "e''4^3\\p( d'' c'' d'' | e'' f'' g''2) | f''4^4( g'' e'' f'' | d'' f'' c'' d'') | \\break "
              "e''4^3( d'' c'' d'' | e'' f'' g''2) | f''4^4( g'' e'' f'' | d''2 c''4) r",
        "lh": "c8_3( g b, g a, g b, g | c g d g e g e g) | d_3( g b, g c g a, g | b, g d g a, g b, g) | "
              "c_3( g b, g a, g b, g | c g d g e g e g) | d( g b, g c g a, g | b, g b, f <c e>4) r",
    },
    {
        "title": "Sonata in C (opening)", "credit": "Wolfgang Amadeus Mozart, Sonata K. 545, first movement - simplified",
        "meter": "4/4", "tempo": 92,
        "note": "The famous opening of Mozart's 'easy' sonata. The tune climbs to high C in bar 3; the left hand plays "
                "an Alberti bass, here an octave lower than Mozart wrote it. The quick notes of bars 2 and 4 are "
                "simplified. Notes from Mutopia Project no. 998.",
        "rh": "c''2^1\\mp( e''4^3 g''^5 | b'2^1 c''4) r | a''2^3( g''4 c'''^5 | g''4 f'' e''2)",
        "lh": "c8_5( g_1 e_3 g c g e g) | d_4( g_1 f_2 g c_5 g_1 e_3 g) | c_5( a_1 f_2 a c g_1 e_3 g) | "
              "b,_5( g_1 d_3 g c_4 g_1 e_2 g)",
    },
    {
        "title": "Starlight", "credit": "Original", "meter": "4/4", "tempo": 66, "key": "g \\major",
        "note": "A quiet piece in high G position: G5 above the staff up to D6. The left hand holds block chords. In "
                "bar 3 the thumb stretches down to F-sharp.",
        "rh": "b''4^3\\p a'' g'' b'' | c'''2 a''4 c''' | a''4 c''' a'' fis''^1 | g''1 | \\break "
              "d'''4^5\\mp b'' g'' b'' | c'''4 b'' c''' a'' | a''4\\> b'' c''' a'' | g''1\\pp",
        "lh": "<g,-5 b,-3 d-1>1 | <g,-5 c-2 e-1>1 | <fis,-5 c-2 d-1>1 | <g, b, d>1 | <g, b, d>1 | <g,-5 c-2 e-1>1 | "
              "<fis,-5 c-2 d-1>1 | <g, b, d>1",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Name any note up to D6 at a glance, and make octave moves without looking down.",
    "When you pass, move on to Unit 4.",
]
