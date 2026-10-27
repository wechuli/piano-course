"""Volume 4, Unit 2: Chords in both hands; 2/4 time."""

KEYBOARDS = []

INTRO = [
    "Now the right hand plays chords too. A right-hand chord sits under the tune: the top note is the melody, "
    "and the two notes below it fill in the harmony. This unit also brings a new time signature, 2/4: two "
    "quarter-note beats in a bar, the time of marches and polkas.",
]

NEW_IDEAS = [
    ("Right-hand chords", "Read the top note first: it is the tune. Then recognise the shape below it, two notes "
                          "a third or fourth apart, all from the same chord as the left hand."),
    ("Chorale", "A chorale is a hymn texture: every beat is a chord, in both hands, and the music moves slowly in "
                "half notes. Listen for the top line."),
    ("2/4 time", "Two quarter-note beats in each bar: ONE two, ONE two. A half note fills the whole bar. The "
                 "oom-pah bass in 2/4 is one 'oom' and one 'pah' per bar."),
]

TIPS = [
    "Look at the top note of each right-hand chord and follow the tune from top note to top note.",
    "Drop the whole hand onto a chord, so all three notes sound exactly together.",
    "In 2/4, feel a strong beat at every bar line, like marching feet: LEFT right, LEFT right.",
]

PART_NOTES = {
    "A": "C major: right-hand chords on the long notes, block chords in the left hand.",
    "B": "A march in 2/4, G major: right-hand chords on the beat, oom-pah in the left hand.",
    "C": "F major in half notes, chords in both hands.",
    "D": "A B-flat major waltz with right-hand chords on the beat.",
}

PIECES = [
    {
        "title": "Morning Prayer", "credit": "Pyotr Ilyich Tchaikovsky, Op. 39 No. 1 (opening and close) - simplified",
        "meter": "3/4", "tempo": 56, "key": "g \\major",
        "note": "The first piece of Tchaikovsky's Album for the Young, a quiet chorale in both hands. Bars 1-4 are as "
                "Tchaikovsky wrote them (the left hand an octave higher); bars 5-8 shorten the rest of the piece. Bar 4 "
                "ends on a B major chord: D-sharp is its middle note. Source: Mutopia Project no. 2032.",
        "rh": "<g'-1 b'-3>4\\p <g' b'>4. <fis'-1 a'-2>8 | <g'-1 c''-4>4 <g' b'>2 | <fis' a'>4\\<( <e' g'>) <e' a'> | "
              "<dis' b'>2.\\! | \\break "
              "<g' b'>4\\p <g' b'>4. <fis' a'>8 | <g' c''>4\\< <g' b'>4. <g' b'>8 | <g' c''>4 <g' b' d''> <g' c'' e''>\\! | "
              "<g' b' d''>2.\\pp",
        "lh": "<g-5 d'-1>4 <g d'>4. <d d'>8 | <e c'>4 <g d'>2 | <d d'>4( <e b>) <c e> | <b, fis>2. | "
              "<g d'>4 <g d'>4. <d d'>8 | <e c'>4 <g d'>2 | c'4 b c' | <g d'>2.",
    },
    {
        "title": "Toy Soldiers' March", "credit": "Original", "meter": "2/4", "tempo": 96, "key": "g \\major",
        "note": "A march in 2/4. The right hand plays a chord on every first beat; the left hand plays oom-pah, one "
                "'oom' and one 'pah' in each bar.",
        "rh": "<g'-1 b'-3 d''-5>4\\f b'8 g' | <g' b' d''>4 d'' | <fis' a' c''>4 a'8 fis' | <g' b' d''>2 | \\break "
              "<g' c'' e''>4\\p c''8 e'' | <g' b' d''>4 b' | <fis' a' c''>4\\< a'8 c'' | g'2\\f",
        "lh": "g,4_5 <b,-3 d-1> | g, <b, d> | fis,_5 <c-2 d-1> | g,_5 <b, d> | g,_5 <c-2 e-1> | g,_5 <b,-3 d-1> | "
              "fis,_5 <c-2 d-1> | <g, b, d>2",
    },
    {
        "title": "Grand Waltz in B-flat", "credit": "Original", "meter": "3/4", "tempo": 132, "key": "bes \\major",
        "note": "Chords in both hands. The right hand's chords are B-flat D F (I), B-flat E-flat G (IV) and A C "
                "E-flat or C E-flat F (V7); finger 5 stretches up to G in bars 2 and 6.",
        "rh": "<bes'-1 d''-3 f''-5>2\\mf d''4 | <bes' ees'' g''>2 ees''4 | <a' c'' ees''>2 c''4 | <bes' d'' f''>2. | \\break "
              "<bes' d'' f''>4\\p f'' d'' | <bes' ees'' g''>4 g'' ees'' | <c'' ees'' f''>4\\< ees'' c'' | bes'2.\\f",
        "lh": "bes,4_5 <d-3 f-1> <d f> | bes,_5 <ees-2 g-1> <ees g> | a,_5 <ees-2 f-1> <ees f> | bes,_5 <d f> <d f> | "
              "bes, <d f> <d f> | bes,_5 <ees g> <ees g> | a,_5 <ees f> <ees f> | <bes, d f>2.",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Every chord sounds together, and the top line of the right hand sings.",
    "When you pass, move on to Unit 3.",
]
