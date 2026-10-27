"""Volume 6, Unit 7: Open score, C clefs and transposing."""

KEYBOARDS = []

INTRO = [
    "Choir directors, organists and rehearsal pianists play from scores that were not written for the piano: "
    "four voices on four staves (open score), or a string quartet with its viola part in the alto clef. The "
    "pianist reads the staves together and plays them with two hands: soprano and alto in the right hand, "
    "tenor and bass in the left.",
    "Two skills make this possible. First, new clefs: the treble clef with an 8 below (the tenor voice), and "
    "the C clefs, whose middle points to middle C. Second, transposing at sight: playing a tune in a different "
    "key from the one it is printed in, by reading intervals and shapes instead of note names.",
]

NEW_IDEAS = [
    ("Open score", "Each voice has its own staff, top to bottom: soprano, alto, tenor, bass. Take the top two with "
                   "the right hand and the bottom two with the left. Read down each beat (the chord), then along "
                   "each line (the voices)."),
    ("The tenor's clef", "A treble clef with a small 8 below it means: an octave lower than written. The tenor's "
                         "notes look like the alto's but sound an octave lower, in the left hand's range."),
    ("The alto clef", "A C clef on the middle line: that line is middle C. The viola reads it. Its lines, from "
                      "bottom to top, are F, A, C, E, G: each note sits one step below where it would be in the "
                      "treble clef."),
    ("The tenor clef", "A C clef on the fourth line from the bottom: that line is middle C. Cellos, bassoons and "
                       "trombones read it for high notes. Its lines are D, F, A, C, E."),
    ("Transposing at sight", "To play a tune a tone higher, change the key signature in your head (F major becomes G "
                             "major), then read the notes as a pattern of steps and leaps, starting a tone higher. "
                             "Do not rename every note: follow the shape."),
]

EXAMPLES = [
    {"title": "Middle C in five clefs",
     "text": "The same note, middle C, in the treble, alto, tenor and bass clefs, and the tenor voice's treble-8 "
             "clef (where a C on the third space sounds as middle C).",
     "staff": "treble", "wide": True,
     "rh": "c'1 \\clef alto c'1 \\clef tenor c'1 \\clef bass c'1 \\clef \"treble_8\" c'1"},
    {"title": "A scale in the alto clef",
     "text": "C major from the C below middle C up to middle C, as the viola reads it.",
     "staff": "alto", "wide": True,
     "rh": "c4 d e f g a b c'"},
    {"title": "Transposing a tone up",
     "text": "Printed in F major; played in G major: every note a tone higher. The shape (step, step, leap of a "
             "third ...) stays the same.",
     "staff": "treble", "key": "f \\major", "time": "4/4", "wide": True,
     "rh": "f'4 g' a' f' | c''2 a' \\bar \"||\" \\key g \\major g'4^\\markup \\small \\italic \"played\" a' b' g' | d''2 b'"},
]

TIPS = [
    "Name the clef of every staff before you start, and find middle C in each.",
    "In open score, play soprano and alto with the right hand, tenor and bass with the left; read down the beat.",
    "If four staves are too many, play the outer voices first (soprano and bass), then add the others.",
    "When transposing, say the new key and its sharps or flats aloud, then read by intervals.",
    "The answers to Part C are at the back of the book (in the full volume): play first, check afterwards.",
]

PART_NOTES = {
    "A": "Four-part chorales on four staves: soprano and alto in the treble clef, the tenor in the treble clef with "
         "an 8 below (an octave lower than written), the bass in the bass clef. Play them on the piano.",
    "B": "String quartet scores (violins, viola in the alto clef, cello) alternating with chorales printed in the "
         "old way: the alto in the alto clef and the tenor in the tenor clef.",
    "C": "Play each tune in the key named above it: a tone (or a minor third) higher or lower than printed. The "
         "answers, written out, are at the back of the book.",
}

PIECES = [
    {
        "title": "If ye love me", "credit": "Thomas Tallis (1565), If ye love me - the first section",
        "meter": "4/4", "tempo": 72, "key": "f \\major", "group": "choir",
        "note": "An anthem for four voices: \"If ye love me, keep my commandments\". The four lines move mostly "
                "together, but in bars 5-9 they enter one after another (soprano, then alto, tenor and bass). The "
                "tenor's staff is an octave lower than written. Play soprano and alto with the right hand, tenor "
                "and bass with the left. Source: Mutopia Project no. 412 (public domain).",
        "staves": [
            {"name": "soprano", "clef": "treble", "instrument": "Soprano",
             "music": "f'2. f'4 | g'2 a'~ | a'4 a' g' f' | bes'2 a' | \\break r4 a' a' a' | c''2 bes'4 a'~ | "
                      "a'8 bes' g'4 a'2 | R1 | \\break r4 g' f' f' | bes'2. a'4~ | a'4 f' a' g'~ | g'4 f'2 e'4 | f'1\\fermata"},
            {"name": "alto", "clef": "treble", "instrument": "Alto",
             "music": "c'2. d'4 | e'2 f'~ | f'4 f' e' d' | f'2 f'~ | f'2 r | R1 | r4 d' d' d' | f'2 e'4 d'~ | "
                      "d'4 c' d' d' | bes4 bes f'2 | f'4 c' f' e' | d'4( bes c'4.) c'8 | c'1\\fermata"},
            {"name": "tenor", "clef": "treble_8", "instrument": "Tenor",
             "music": "a2. f4 | c'2 c'~ | c'4 c' c' a | d'2 c'~ | c'2 r4 a | a4 a d'4. c'8 | bes2 a~ | a2 r | "
                      "r2 r4 bes | g4 g d2 | c'4 a c'2( | bes8 a) f4 g4. g8 | f1\\fermata"},
            {"name": "bass", "clef": "bass", "instrument": "Bass",
             "music": "f2. d4 | c2 f~ | f4 f c d | bes,2 f~ | f1 | R1 | r2 d | d4 d g4. f8 | e2 d | r4 g d d | "
                      "f2 f4 c | d4 d c c | f1\\fermata"},
        ],
    },
    {
        "title": "O nata lux", "credit": "Thomas Tallis (1575), O nata lux de lumine - the first and last phrases",
        "meter": "3/2", "tempo": 66, "tempo_unit": "2", "key": "g \\minor", "group": "choir", "upbeat": "3/4",
        "note": "Five voices (Superius, Discantus, Contratenor, Tenor, Bassus), the top two in the treble clef, the middle two in the tenor's "
                "treble-8 clef, and the bass. Count three half notes in a bar; the music starts on an upbeat of "
                "three quarters. The first phrase ends in bar 4; the excerpt then jumps to Tallis's last phrase, "
                "which ends on a G major chord (the B natural in the Discantus and Tenor). The small accidentals of "
                "the source (added by the editor) are printed as normal ones here. Source: Mutopia Project no. 949 "
                "(public domain).",
        "staves": [
            {"name": "s1", "clef": "treble", "instrument": "Sup.",
             "music": "\\partial 2. d''4 ees'' c'' | d''2. a'4 bes' g' | a'2 e''4 f'' d'' e''~ | e''4 c'' d'' bes'( a'2) | "
                      "\\break g'2 r4 a'4 a' g' | a'2. a'4 a' g' | a'2. d''4 a' bes' | a'2 g'4 g'2 fis'4 | g'2.\\fermata"},
            {"name": "s2", "clef": "treble", "instrument": "Disc.",
             "music": "\\partial 2. g'4 g' g' | f'4.( e'8 d'4) d' d' d' | e'4.( d'8 cis'4) c'' bes' bes' | a'2 a'4 g'2 fis'4 | "
                      "g'2 r4 f'4 f' d' | f'2. f'4 f' d' | f'2. f'4 f' d' | f'2 ees' d'4 d' | b2.\\fermata"},
            {"name": "ct", "clef": "treble_8", "instrument": "Ctr.",
             "music": "\\partial 2. bes4 c' g | a4.( g8 f4) f d d' | cis'4.( b8 a2) f'4 g' | e'4 f'2 bes4 d' d' | "
                      "d'2 r4 d'4 d' d' | d'2. d'4 d' d' | d'2. d'4 d' bes | d'4. c'8( bes4) c'( a) a | g2.\\fermata"},
            {"name": "t", "clef": "treble_8", "instrument": "Tenor",
             "music": "\\partial 2. g4 g c | f4.( g8 a4) a g g | e2 r4 c' d' bes | c'2 a4 d'4. c'8( a4) | "
                      "b2 r4 a4 a bes | a2. a4 a bes | a2. a4 a g | f2 g4 ees( f4.) ees8 | d2.\\fermata"},
            {"name": "b", "clef": "bass", "instrument": "Bass",
             "music": "\\partial 2. g4 c ees | d2. d4 g, bes, | a,2. a4 bes g | a2 f4 g d2 | "
                      "g,2 r4 d4 f g | d2. d4 f g | d2. d4 d g | d2 ees4 c( d) d | g,2.\\fermata"},
        ],
    },
    {
        "title": "Emperor Quartet: the theme", "credit": "Joseph Haydn (1797), String Quartet Op. 76 No. 3, second "
                                                       "movement - the theme",
        "meter": "2/2", "cut": True, "tempo": 40, "tempo_unit": "2", "key": "g \\major", "group": "quartet",
        "upbeat": "1/2",
        "note": "Haydn's hymn (now the German national anthem) in a string quartet. The first violin has the tune, the "
                "second violin a lower voice, the viola (alto clef: the middle line is middle C) and the cello the "
                "harmony. The phrase in bars 12-15 is repeated in bars 16-19 (fz: a sudden accent). Play violins "
                "with the right hand, viola and cello with the left. Source: Mutopia Project no. 385 (public "
                "domain).",
        "staves": [
            {"name": "v1", "clef": "treble", "instrument": "Violin 1",
             "music": "\\partial 2 g'4.(\\p a'8 | b'4 a' c'' b') | a'8( fis' g'4) e''( d'' | c''4 b') a'( b'8 g') | "
                      "d''2 g'4.( a'8 | b'4 a' c'' b') | \\break a'8( fis' g'4) e''( d'' | c''4 b') a'( b'8 g') | "
                      "d''2 a'4( b' | a'8 fis' d'4) c''( b' | a'8 fis' d'4) d''( c'' | b'4.) b'8 cis''4 cis''8( d'') | \\break "
                      "d''2\\fermata g''4.\\(\\fz fis''8 | \\appoggiatura fis''8 e''4 d''\\) e''4.\\(\\fz d''8 | "
                      "\\appoggiatura d''8 c''4 b'\\) a'4.(\\p b'16 c'') | d''8( e'' c'' a') g'4\\( \\acciaccatura b'16 a'8 g'\\) | \\break "
                      "g'2 g''4.\\(\\fz fis''8 | \\appoggiatura fis''8 e''4 d''\\) e''4.\\(\\fz d''8 | "
                      "\\appoggiatura d''8 c''4 b'\\) a'4.(\\p b'16 c'') | d''8( e'' c'' a') g'4\\( \\acciaccatura b'16 a'8 g'\\) | g'2"},
            {"name": "v2", "clef": "treble", "instrument": "Violin 2",
             "music": "\\partial 2 b4.(\\p d'8 | g'4 fis' a' g') | c'4( b) c''( b' | fis'4 g') e'2( | d'2) b4.( d'8 | "
                      "g'4 fis' a' g') | c'4( b) c''( b' | fis'4 g') e'2( | d'2) fis'4( g' | fis'4) r fis'( g' | "
                      "fis'4) r b'( a' | g'2.) g'8( fis') | fis'2\\fermata <g g'>4.\\fz g'8 | g'8.( a'16) b'4 c''4.(\\fz b'8) | "
                      "fis'4( g') fis'4.(\\p g'16 a') | g'4( e'8 a') g'4( fis') | g'2 <g g'>4.\\fz g'8 | "
                      "g'8.( a'16) b'4 c''4.(\\fz b'8) | fis'4( g') fis'4.(\\p g'16 a') | g'4( e'8 a') g'4( fis') | g'2"},
            {"name": "va", "clef": "alto", "instrument": "Viola",
             "music": "\\partial 2 g4\\p r | r2 d'4-.( d'-.) | fis8( a g4) r2 | a4( b e' g) | fis2 g4 r | r2 d'4-.( d'-.) | "
                      "fis8( a g4) r2 | a4( b e' g) | fis2 d'4 d' | d'4 r a( g8 b | d'4) r d'( e'8 fis' | g'4) g e' e'8( d') | "
                      "d'2\\fermata <g d'>2\\fz | e'8.( fis'16) g'4 g'4.\\fz g'8 | <d' a'>4-. <d' b'>-. d'2\\p | "
                      "g4( e'8 c') b4\\( \\acciaccatura d'8 c'4\\) | b2 <g d'>2\\fz | e'8.( fis'16) g'4 g'4.\\fz g'8 | "
                      "<d' a'>4-. <d' b'>-. d'2\\p | g4( e'8 c') b4\\( \\acciaccatura d'8 c'4\\) | b2"},
            {"name": "vc", "clef": "bass", "instrument": "Cello",
             "music": "\\partial 2 g4\\p r | r2 fis4( g) | d4 g, r2 | d4( g c cis) | d2 g4 r | r2 fis4( g) | d4 g, r2 | "
                      "d4( g c cis) | d2 d4 d | d4 r d d | d4 r b,( c8 d) | e2 a,4 a, | d2\\fermata b4.\\fz b8 | "
                      "c'4 g c4.\\fz g8 | d4 g c2\\p | b,4( c d) d | g,2 b4.\\fz b8 | c'4 g c4.\\fz g8 | d4 g c2\\p | "
                      "b,4( c d) d | g,2"},
        ],
    },
    {
        "title": "Chorale in the C Clefs", "credit": "Original, written for this book",
        "meter": "4/4", "tempo": 60, "key": "bes \\major", "group": "choir",
        "note": "A chorale printed as choirs and organists once read it: the alto in the alto clef (the middle line is "
                "middle C) and the tenor in the tenor clef (the fourth line is middle C). Name the first note of "
                "each voice before you play. Then play it again a tone higher, in C major.",
        "staves": [
            {"name": "soprano", "clef": "treble", "instrument": "Soprano",
             "music": "d''4 c'' a' bes' | ees''4 d'' c''2\\fermata | d''4 c'' bes' d'' | bes'4 c'' bes'2\\fermata | \\break "
                      "c''4 ees'' d'' c'' | ees''4 d'' c''2\\fermata | d''4 ees'' c'' d'' | bes'4 c'' bes'2\\fermata"},
            {"name": "alto", "clef": "alto", "instrument": "Alto",
             "music": "bes'4 g' f' d' | ees'4 f' f'2 | f'4 f' f' g' | g'4 a' f'2 | g'4 f' f' g' | f'4 f' f'2 | "
                      "f'4 g' f' f' | ees'4 ees' d'2"},
            {"name": "tenor", "clef": "tenor", "instrument": "Tenor",
             "music": "f'4 c' c' bes | bes4 bes a2 | bes4 a bes bes | ees'4 c' d'2 | c'4 a bes g | a4 bes a2 | "
                      "bes4 bes a bes | bes4 a f2"},
            {"name": "bass", "clef": "bass", "instrument": "Bass",
             "music": "bes4 ees f g | g4 bes, f2\\fermata | bes,4 f d bes, | g4 f bes2\\fermata | ees4 f bes, ees | "
                      "f4 bes, f2\\fermata | bes,4 ees f bes, | g4 f bes,2\\fermata"},
        ],
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speed shown, with no more than one stop each.",
    "Pass if you read every clef without stopping to work out the notes, and your transpositions match the "
    "answers at the back of the book.",
    "Pass if you can play the Emperor theme at sight and If ye love me after a few days.",
    "When you pass, move on to Unit 8.",
]
