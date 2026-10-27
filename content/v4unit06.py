"""Volume 4, Unit 6: Sixteenth notes."""

KEYBOARDS = []

INTRO = [
    "A sixteenth note has two beams (or two flags) and lasts half an eighth: four of them fill one beat. "
    "Sixteenths come in a few common groups, and each group has its own look on the page. Learn to recognise the "
    "group as one picture and count it as one beat.",
]

NEW_IDEAS = [
    ("Four sixteenths", "Four notes beamed together with two beams: one beat. Count 1-e-and-a, 2-e-and-a. In this "
                        "unit four sixteenths always move by step, like a tiny scale."),
    ("Eighth and two sixteenths", "One beam over the group and a second beam under the last two notes: long, "
                                  "short-short. Count 1, and-a."),
    ("Dotted eighth and sixteenth", "A dotted eighth lasts three sixteenths, so the pair goes long-short, "
                                    "snappier than a dotted quarter and eighth. Count 1, a. It is the rhythm of "
                                    "marches."),
]

TIPS = [
    "Count sixteenths slowly at first: say '1-e-and-a' for every beat, then just feel the beats.",
    "Read four sixteenths as one shape: which way does the little scale go, up or down?",
    "Keep dotted rhythms crisp: the sixteenth belongs to the next beat, almost like a grace note.",
]

PART_NOTES = {
    "A": "Right hand in C position, 2/4: sixteenths in groups of four and two.",
    "B": "Left hand in C position, 2/4.",
    "C": "G major in 4/4: sixteenths in the right hand over block chords.",
    "D": "F major in 2/4: dotted eighths and sixteenths over an oom-pah bass.",
}

PIECES = [
    {
        "title": "Musette in D", "credit": "From the Notebook for Anna Magdalena Bach (1725), BWV Anh. 126 - first part",
        "meter": "2/4", "tempo": 72, "key": "d \\major", "positions": ["RH_D", "RH_D5", "LH_C2", "LH_D"],
        "allow_leap": 11,
        "note": "A musette imitates bagpipes: the left hand drones on low D in octaves, two ledger lines below the "
                "bass staff. The right hand starts high, on A above the staff, drops an octave in bar 3, and leaps "
                "back up for bar 5. Source: Mutopia Project no. 79.",
        "rh": "a''4^5\\f g''16 fis'' e'' d'' | a''4 g''16 fis'' e'' d'' | fis'16^3 g' a'8 g' fis' | e'8 a' fis' d' | \\break "
              "a''4^5\\p g''16 fis'' e'' d'' | a''4 g''16 fis'' e'' d'' | fis'16^3 g' a'8 g' fis' | e'8 a' d'4\\fermata",
        "lh": "d,8_5 d_1 d, d | d, d d, d | fis16_3 g a8 g fis | e a fis d | "
              "d,8 d d, d | d, d d, d | fis16_3 g a8 g fis | e a d4\\fermata",
    },
    {
        "title": "Soldiers' March", "credit": "Robert Schumann, Op. 68 No. 2 (first part) - shortened",
        "meter": "2/4", "tempo": 108, "key": "g \\major",
        "note": "From Schumann's Album for the Young: crisp dotted rhythms and chords in both hands, with rests "
                "between the chords. Bars 1-6 are as Schumann wrote them; bars 7-8 come from the end of his second "
                "phrase, so the march stops at home. Notes from Mutopia Project no. 650.",
        "rh": "<g' b'>8.\\f <g' c''>16 <g' d''>8 r | <g' e''> r <g' d''> r | <fis' c''> r <g' b'> r | <fis' a'> r g' r | \\break "
              "<g' b'>8. <g' c''>16 <g' d''>8 r | <g' e''> r <g' d''> r | <fis' c''> r <g' b'> r | <fis' a'> r g' r",
        "lh": "g8. a16 b8 r | c' r b r | a r g r | <d c'> r <g b> r | "
              "g8. a16 b8 r | c' r b r | a r g r | <d c'> r <g b> r",
    },
    {
        "title": "Busy Bee", "credit": "Original", "meter": "2/4", "tempo": 72,
        "note": "Groups of four sixteenths buzz up and down the C position; each group is a little scale. The left "
                "hand plays oom-pah.",
        "rh": "c'16^1\\mf d' e' f' g'8 e' | f'16 e' d' c' d'4 | e'16 f' g' f' e'8 c' | d'2 | \\break "
              "g'16^5 f' e' d' e'8 c' | f'16 e' d' c' c'4 | d'16\\< e' f' e' d'8 b^1 | c'2\\f",
        "lh": "c4_5 <e-3 g-1> | b,_5 <f-2 g-1> | c_5 <e g> | b,_5 <f g> | c_5 <e g> | c_5 <f-2 a-1> | b,_5 <f g> | <c e g>2",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every group of sixteenths fits evenly into its beat, and dotted rhythms stay crisp.",
    "When you pass, move on to Unit 7.",
]
