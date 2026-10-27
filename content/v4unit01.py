"""Volume 4, Unit 1: Block chords."""

KEYBOARDS = []
CHORD_SHAPES = [
    ("C major", "LH_C", "c \\major", {}),
    ("G major", "LH_G", "g \\major", {"f": "is"}),
]

INTRO = [
    "In Volume 3 the left hand played its chords one note at a time. Now it plays them as block chords, all "
    "three notes together. A block chord is read as one shape, not three notes: you already know the shapes, so "
    "the left hand becomes a quick glance while your eyes stay on the tune.",
]

NEW_IDEAS = [
    ("Block chords", "Three notes stacked on the staff and played together: I is C-E-G (fingers 5 3 1), IV is "
                     "C-F-A and V7 is B-F-G (both 5 2 1). Drop the hand onto all three keys at once."),
    ("Oom-pah", "In 4/4 the left hand plays the bottom note of the shape on beats 1 and 3 (the 'oom') and the "
                "upper two notes together on beats 2 and 4 (the 'pah')."),
    ("Waltz bass", "In 3/4: the bottom note on beat 1, then the upper two notes on beats 2 and 3. Oom-pah-pah."),
    ("Finger numbers in chords", "When a new shape starts, its finger numbers are printed next to the notes: "
                                 "5 on the bottom note, 1 on the top."),
]

TIPS = [
    "Before you play, find each new chord shape in the left hand and name it: I, IV or V7.",
    "Keep the 'pah' chords light and short. The 'oom' notes carry the bass line.",
    "The first note of each bar in the right hand belongs to the left hand's chord: check that they fit.",
]

PART_NOTES = {
    "A": "C major. The left hand holds one chord for each bar.",
    "B": "G major with an oom-pah bass: bottom note, then the upper two notes together.",
    "C": "F major waltzes: oom-pah-pah.",
    "D": "D major oom-pah. The right hand moves between D position and A position.",
}

PIECES = [
    {
        "title": "La Candeur", "credit": "Friedrich Burgmüller, Op. 100 No. 1 (opening) - simplified",
        "meter": "4/4", "tempo": 88,
        "note": "'Candour' (honesty) from Burgmüller's 25 Easy Studies. The left hand holds the chords exactly as "
                "Burgmüller wrote them; the right hand is an octave lower than written, and the last two bars are "
                "simplified so the piece ends at home. Source: Mutopia Project no. 202.",
        "rh": "g'8^5\\p( e' d' c') g'( e' d' c') | c''^5( a' g' f') c''( a' g' f') | "
              "g'^5( e' d' c' b^2 c'^1 e'^3 f') | g'( e' d' c' b c' d' e') | \\break "
              "g'\\<( f' e' d') g'( f' e' d') | f'\\mf( e' d' c') f'( e' d' c') | "
              "d'\\>( e' f' e' d' c' b c') | c'1\\p",
        "lh": "<c-5 e-3 g-1>1 | <c-5 f-2 a-1>1 | <c-5 e-3 g-1>1~ | <c e g>1 | <b,-5 f-2 g-1>1 | <c-5 e-3 g-1>1 | "
              "<b,-5 f-2 g-1>1 | <c e g>1",
    },
    {
        "title": "Oom-pah March", "credit": "Original", "meter": "4/4", "tempo": 96, "key": "g \\major",
        "note": "A march over an oom-pah bass in G major. In bars 3 and 7 the left hand's V7 shape has F-sharp at "
                "the bottom; in bar 3 the right-hand thumb stretches down to F-sharp too.",
        "rh": "b'4^3\\f a' b' d'' | c''4 b' c'' a' | a'4 c'' a' fis'^1 | g'2 b' | \\break "
              "d''4^5\\p c'' b' d'' | c''4 b' c'' e'' | a'4\\< b' c'' a' | g'1\\f",
        "lh": "g,4_5 <b,-3 d-1> g, <b, d> | g,_5 <c-2 e-1> g, <c e> | fis,_5 <c-2 d-1> fis, <c d> | g,_5 <b, d> g, <b, d> | "
              "g, <b, d> g, <b, d> | g,_5 <c-2 e-1> g, <c e> | fis,_5 <c-2 d-1> fis, <c d> | <g, b, d>1",
    },
    {
        "title": "Ballroom Waltz", "credit": "Original", "meter": "3/4", "tempo": 120, "key": "f \\major",
        "note": "Oom-pah-pah in F major. The IV shape (F, B-flat, D) and the V7 shape (E, B-flat, C) both have "
                "B-flat in the middle.",
        "rh": "a'2^3\\mp c''4 | bes'2 d''4 | g'2 bes'4 | a'2. | \\break "
              "c''2^5\\mf a'4 | bes'4 a' g' | g'4\\> e'^1 g' | f'2.\\p",
        "lh": "f4_5 <a-3 c'-1> <a c'> | f_5 <bes-2 d'-1> <bes d'> | e_5 <bes-2 c'-1> <bes c'> | f_5 <a-3 c'-1> <a c'> | "
              "f <a c'> <a c'> | f_5 <bes-2 d'-1> <bes d'> | e_5 <bes-2 c'-1> <bes c'> | <f a c'>2.",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every left-hand chord sounds together, and you can name it (I, IV or V7) from its shape.",
    "When you pass, move on to Unit 2.",
]
