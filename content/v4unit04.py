"""Volume 4, Unit 4: Low notes and the middle (ledger lines below the bass staff and between the staves)."""

KEYBOARDS = [["LH_C2"], ["RH_A3"], ["LH_C4"]]

INTRO = [
    "The bass staff ends at G on its bottom line; lower notes need ledger lines too. And between the two "
    "staves, around middle C, either hand can borrow ledger lines: the right hand reads notes below the treble "
    "staff, and the left hand reads notes above the bass staff. The same key can be written in either staff.",
]

NEW_IDEAS = [
    ("Ledger lines below", "F2 sits just below the bass staff, E2 on its first ledger line, D2 below it and C2 on "
                           "the second ledger line. Landmark: low C (C2) on two ledger lines."),
    ("Between the staves", "Middle C has one ledger line in both clefs. In the treble staff, B3 hangs just below "
                           "it and A3 sits on the second ledger line down. In the bass staff, D4 sits above middle C "
                           "and E4 on the second ledger line up."),
    ("The tune in the bass", "When the left hand has the tune, the right hand accompanies with short chords on "
                             "the off-beats. Let the left hand sing and keep the right hand light."),
]

TIPS = [
    "Find the lowest note first and name it from low C or middle C.",
    "Near middle C, check which staff a note is in before you decide which hand plays it.",
    "When the right hand plays after the beat, count out loud and let the left hand land on the beat.",
]

PART_NOTES = {
    "A": "The left hand down low: low C position (C2 to G2) and low F position (F2 to C3).",
    "B": "F major: the tune in the left hand, low F position; the right hand plays chords on beats 2 and 4.",
    "C": "The right hand below middle C, from A3 up to E4.",
    "D": "Both hands near middle C, taking turns: the right hand below it in the treble staff, the left hand above "
         "it in the bass staff.",
}

PIECES = [
    {
        "title": "The Happy Farmer", "credit": "Robert Schumann, Op. 68 No. 10 (first part) - simplified",
        "meter": "4/4", "tempo": 108, "key": "f \\major", "positions": ["LH_F", "LH_C", "RH_F"],
        "note": "Schumann's farmer sings in the left hand, coming home from work; the right hand answers with short "
                "chords on the off-beats. The tune rises above the bass staff to F, on a ledger line. The opening "
                "upbeat is left out, and bars 3 and 7 use the same chord. Notes from Mutopia Project no. 659.",
        "rh": "r8 <c' f' a'>\\mf <c' f' a'> r r <f' a' c''> <f' a' c''> r | r <f' bes' d''> <bes' d''> r r <f' a' c''> <f' a' c''> r | "
              "r <e' bes' c''> <e' bes' c''>4 r8 <c' f' a'> <c' f' a'>4 | r8 <c' g'> r <f' g' b'> r <e' g' c''> <e' g' c''>4 | \\break "
              "r8 <c' f' a'> <c' f' a'> r r <f' a' c''> <f' a' c''> r | r <f' bes' d''> <bes' d''> r r <f' a' c''> <f' a' c''> r | "
              "r <e' bes' c''> <e' bes' c''>4 r8 <c' f' a'> <c' f' a'>4 | r8 <d' g'> r <bes c'> r <a c' f'> <a c' f'> r",
        "lh": "f4._3( a8 c'4. f8 | bes d' f' d' c'4.) a8( | bes g c bes a f c a | e4 d c) r | "
              "f4.( a8 c'4. f8 | bes d' f' d' c'4.) a8( | bes g c bes a f c a | <bes, g>4 <c e> f) r",
    },
    {
        "title": "The Bear", "credit": "Original", "meter": "4/4", "tempo": 80,
        "note": "A heavy dance in low C position, C2 to G2, two ledger lines below the bass staff. The right hand "
                "plays chords on beats 2 and 4.",
        "rh": "r4 <c'-1 e'-3 g'-5> r <c' e' g'> | r <c' e' g'> r <c' e' g'> | r <d'-2 f'-4 g'-5> r <d' f' g'> | "
              "r <c'-1 e'-3 g'-5> r <c' e' g'> | \\break r <c' e' g'> r <c' e' g'> | r <c'-1 f'-4 a'-5> r <c' f' a'> | "
              "r <d'-2 f'-4 g'-5> r <d' f' g'> | <c' e' g'>1",
        "lh": "c,4_5\\f e, g, e, | c, d, e, c, | d, f, g, f, | e,2 c, | g,4_1 f, e, g, | f,2 c, | d,4 g, f, d, | c,1",
    },
    {
        "title": "Meeting in the Middle", "credit": "Original", "meter": "3/4", "tempo": 88,
        "note": "The hands take turns around middle C. The right hand plays below it, in the treble staff; the left "
                "hand plays above it, in the bass staff, with up to three ledger lines.",
        "rh": "c'4^3\\mp b a | b2 c'4 | R2. | R2. | \\break d'4^4 c' b | a2 b4 | R2. | R2.",
        "lh": "R2. | R2. | e'4_3 f' g' | e'2 c'4 | R2. | R2. | d'4_4 e' d' | c'2._5",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Name any note from C2 up to G4 in the bass staff, and from A3 up in the treble staff, at a glance.",
    "When you pass, move on to Unit 5.",
]
