"""Volume 6, Unit 5: Big textures."""

KEYBOARDS = []

INTRO = [
    "Late Romantic piano music fills the keyboard: tunes doubled in octaves, chords of five and six notes, "
    "arpeggios that sweep over three octaves, a left hand that crosses over the right, and sometimes a third "
    "staff when two are not enough. The notes are printed in signs that save ledger lines: 8va (an octave "
    "higher than written) and 8vb (an octave lower).",
    "No one reads every note of such a texture at sight. A professional reads the outline (the tune on top and "
    "the bass at the bottom) and fills in what the hands can grasp. This unit teaches both: reading big "
    "shapes quickly, and simplifying when the page is too full.",
]

NEW_IDEAS = [
    ("Octaves", "Read the top note of an octave and let the hand keep its shape (thumb and fifth finger): the "
                "lower note is always the same letter. Move the whole hand from the wrist."),
    ("8va and 8vb", "8va (or 8) over the staff, with a dashed line, means play an octave higher than written, "
                    "until the line ends. 8vb (or 8 under the staff) means an octave lower. Read the notes as "
                    "printed, then move the hand."),
    ("Full chords", "In a chord of four to six notes the tune is the top note. Read it first, then the bass, then "
                    "the shape between them (a triad in an octave, a seventh chord)."),
    ("Wide arpeggios and the pedal", "A left hand that rises over two octaves cannot hold its notes: the pedal "
                                     "holds them. Change the pedal with each new chord."),
    ("Crossed hands", "When a note on the upper staff is marked l.h. (left hand), the left hand crosses over the "
                      "right to play it, then comes back. Lift it in plenty of time."),
    ("Three staves", "When a passage needs three staves, the right hand usually reads the top one and the left "
                     "hand the two lower ones (or the other way round). Look for the bracket and the hand marks."),
    ("Simplifying at sight", "If a texture is too full, keep the tune and the bass and drop the inner notes; keep "
                             "the rhythm going at all costs. Part C prints a suggested reduction under each "
                             "exercise."),
]

EXAMPLES = [
    {"title": "Octaves under an 8va sign",
     "text": "The right hand plays octaves an octave higher than written; the left hand's octaves are under 8vb, "
             "an octave lower than written.",
     "time": "4/4", "key": "f \\major", "wide": True,
     "rh": "\\ottava #1 <f'' f'''>4 <g'' g'''> <a'' a'''> <c''' c''''> | <a'' a'''>2 <f'' f'''> \\ottava #0",
     "lh": "\\ottava #-1 <f,, f,>2 <c,, c,> | <f,, f,>1 \\ottava #0"},
    {"title": "The left hand crosses over",
     "text": "The left hand plays the bass and the chord, then crosses over the right hand for the high note "
             "marked l.h.",
     "time": "3/4", "wide": True,
     "rh": "<< { e''2. | d''2. } \\\\ { s2 g''4^\\markup \\small \\italic \"l.h.\" | s2 b''4^\\markup \\small \\italic \"l.h.\" } >>",
     "lh": "c4 <g c'> s4 | g,4 <d g> s4"},
]

TIPS = [
    "Read the outline first: the tune (top notes) and the bass (bottom notes).",
    "Look for 8va and 8vb signs before you play, and where their dashed lines end.",
    "Keep the hand's shape for octaves and chords; move it from the wrist and arm.",
    "Change the pedal with the harmony, not with the beat.",
    "If you cannot play everything, drop inner notes, never the beat.",
]

PART_NOTES = {
    "A": "The tune in right-hand octaves over left-hand octaves. Some exercises lie high (under 8va), some low "
         "(under 8vb).",
    "B": "Full right-hand chords over a left hand that sweeps up an octave and a half with the pedal, alternating "
         "with 3/4 exercises in which the left hand crosses over the right on the third beat.",
    "C": "Full chords in both hands. Under each exercise a smaller staff prints the outline: the tune and the "
         "bass. Play the full version if you can; if not, play the outline and keep going.",
}

PIECES = [
    {
        "title": "Wedding Day at Troldhaugen", "credit": "Edvard Grieg (1896), Lyric Pieces Op. 65 No. 6 - bars 1-10",
        "meter": "4/4", "tempo": 112, "key": "d \\major", "allow_32": True,
        "note": "A festive march. The left hand jumps between low and middle open fifths; the right hand starts in "
                "the bass clef with the same fifths, then plays the tune with chords and a held lower voice. "
                "Accented chords (marked > and staccato) are the march's steps. In bar 10 the left hand jumps "
                "two octaves for the last chord. Source: Mutopia Project no. 781 (public domain).",
        "rh": "\\clef bass r4 <d a>8\\f <d a> <d a>4-.-> r4 | r4 <d a>8 <d a> <d a>4-.-> r8 \\clef treble \\tuplet 3/2 { a'16 b' a' } | "
              "<< { fis'8( a') d'' fis'' e''( d'') fis' a' } \\\\ { fis'4 fis'8 fis' fis'4 fis'8 fis' } >> | "
              "<fis' a' b'>4-.-> <fis' a' b'>8 r16 <fis' a' b'>16 <fis' a' b'>4-. <d' fis'>8-. <d' fis' gis'>-. | \\break "
              "<< { a'8( b') fis'-. gis'-. a'( b') fis'-. gis'-. } \\\\ { <d' fis'>4 <d' fis'>8 <d' fis'> <d' fis'>4 <d' fis'>8 <d' fis'> } >> | "
              "<d' e' a'>4-.-> <cis' a'>8 r16 <cis' a'>16 <cis' a'>4 r8 \\tuplet 3/2 { cis''16 d'' cis'' } | "
              "<< { b'8( d'') g''-. b''-. a''( g'') b'-. d''-. } \\\\ { b'4 b'8 b' b'4 <g' b'>8 <g' b'> } >> | \\break "
              "<g' b' d'' fis''>4-.-> <g' b' d'' fis''>8 r16 <g' b' d'' fis''>16 <g' b' d'' fis''>4-. <g' b'>8-. <g' b' cis''>-. | "
              "<< { d''8( e'') b'-. cis''-. d''( e'') b'-. cis''-. } \\\\ { <g' b'>4 <g' b'>8 <g' b'> <g' b'>4 <g' b'>8 <g' b'> } >> | "
              "<g' a' d''>4-.-> <fis' d''>8 r16 <fis' d''>16 <fis' d''>4-. r4",
        "lh": "<d, a,>4-.-> r4 r4 <d, a,>8 <d, a,> | <d, a,>4-.-> r4 r4 <d, a,>8 <d, a,> | "
              "<d, a,>4-.-> <d a>8 <d a> <d a>4-.-> <d, a,>8 <d, a,> | <d, a,>4-. <d a>8 r16 <d a>16 <d a>4-. r4 | "
              "<b,, fis,>4 <b, fis>8 <b, fis> <e, b,>4 <e b>8 <e b> | <a,, e,>4 <a e'>8 r16 <a e'>16 <a e'>4-. r4 | "
              "<g, d>4 <g d'>8 <g d'> <g d'>4 r4 | <e, b,>4 <e b>8 r16 <e b>16 <e b>4-. r4 | "
              "<a, e>4 <a e'>8 <a e'> <a e'>4-. r4 | <d, a,>4-. <d' a'>8 r16 <d' a'>16 <d' a'>4-. r4",
    },
    {
        "title": "March of the Trolls", "credit": "Edvard Grieg (1891), Lyric Pieces Op. 54 No. 3 - bars 1-10, with "
                                                "a closing chord",
        "meter": "2/4", "tempo": 112, "key": "d \\minor",
        "note": "Very soft and very short (pp, staccato): the trolls creep. The left hand repeats D and A in the "
                "bass all through; the right hand's three-note chords slide down by half steps while their two "
                "lower notes stay. Each phrase starts with a quick run of four 32nd notes up to the first chord. "
                "Grieg's march goes on; the excerpt closes on D minor. Source: Mutopia Project no. 2014 (public "
                "domain).",
        "allow_32": True,
        "rh": "R2 | r4 r8 d'32(\\pp e' f' g' | a'8-.) <d' f' d''>-. <d' f' d''>-. <d' f' cis''>-. | "
              "<d' f' cis''>8-. <d' f' c''>-. <d' f' c''>-. <d' f' b'>-. | <d' f' b'>8-. <d' f' bes'>-. <d' f' bes'>-. <d' f' a'>-. | "
              "<b e' gis'>8-. <b e' gis'>4-- g'32( a' bes' c'' | \\break d''8-.) <g' bes' g''>-. <g' bes' g''>-. <g' bes' fis''>-. | "
              "<g' bes' fis''>8-. <g' bes' f''>-. <g' bes' f''>-. <g' bes' e''>-. | "
              "<g' bes' e''>8-. <g' bes' ees''>-. <g' bes' ees''>-. <g' bes' d''>-. | <e' a' cis''>8-. <e' a' cis''>4-- r8 | "
              "<d' f' a' d''>4-. r4",
        "lh": "d,8->-.\\pp a,-. d,->-. a,-. | d,8-. a,-. d,-. a,-. | d,8 a, d, a, | d,8 a, d, a, | d,8 a, d, a, | "
              "d,8 a, d, a, | d,8 a, d, a, | d,8 a, d, a, | d,8 a, d, a, | d,8 a, d, a, | <d, a,>4-. r4",
    },
    {
        "title": "March of the Wooden Soldiers", "credit": "Peter Ilyich Tchaikovsky (1878), Children's Album Op. 39 "
                                                         "No. 5 - the first strain",
        "meter": "2/4", "tempo": 132, "key": "d \\major",
        "note": "Both hands in the treble clef, playing short chords and dotted rhythms like toy drums and fifes. "
                "The dotted rhythm (dotted eighth, sixteenth) must be sharp; the rests are as important as the "
                "notes. The strain moves from D major to A major in bar 16. Source: Mutopia Project no. 1806 "
                "(public domain).",
        "rh": "<a' d''>8 r d'' r | b'8.( ais'16 b'8) r16 cis''( | <a' d''>8) r d'' r | b'8.( ais'16 b'8) r16 cis''( | "
              "<a' d''>8) r <cis'' e''> r | fis''8 r <d'' fis''> r | <e'' g''>8 r16 <d'' fis''>( <cis'' e''>8) r16 <b' d''>( | "
              "<cis'' e''>8) r4. | \\break <a' d''>8 r d'' r | b'8.( ais'16 b'8) r16 cis''( | <a' d''>8) r d'' r | "
              "b'8.( ais'16 b'8) r16 cis''( | <a' d''>8) r <cis'' e''> r | fis''8 r <d'' fis''> r | "
              "<cis'' e''>8 r16 <b' d''>( <a' cis''>8) r16 <gis' b'>( | a'8) r4.",
        "lh": "\\clef treble <d' fis'>8 r4. | <d' g'>8.( fis'16 g'8) r16 e'( | <d' fis'>8) r4. | <d' g'>8.( fis'16 g'8) r16 e'( | "
              "<d' fis'>8) r a' r | d''8 r4. | <d' a'>8 r4. | a'8-. a'16-. a'-. a'8-. a'-. | "
              "<d' fis'>8 r4. | <d' g'>8.( fis'16 g'8) r16 e'( | <d' fis'>8) r4. | <d' g'>8.( fis'16 g'8) r16 e'( | "
              "<d' fis'>8) r a' r | d''8 r d' r | e'2 | a8-. a16-. a-. a8-. a-.",
    },
    {
        "title": "Bells", "credit": "Original, written for this book",
        "tempo": 52, "meter": "4/4", "key": "cis \\minor",
        "note": "Three staves. The right hand reads the top staff: bells in octaves, printed under 8va (an octave "
                "higher than written). The left hand reads both lower staves: the deep octave on the first beat "
                "(the bottom staff, under 8vb: an octave lower than written), then the chords on the second, third "
                "and fourth beats (the middle staff). Use the pedal in every bar: it holds the deep bass under the "
                "chords. The texture is modelled on the opening of Rachmaninoff's Prelude in C-sharp minor.",
        "staves": [
            {"name": "bells", "clef": "treble", "hand": "rh",
             "music": "\\ottava #1 <e'' e'''>2->\\ff <dis'' dis'''>4 <cis'' cis'''> | <cis'' cis'''>1 | "
                      "<fis'' fis'''>2-> <e'' e'''>4 <dis'' dis'''> | <bis' bis''>1 | \\break "
                      "<e'' e'''>2-> <dis'' dis'''>4 <cis'' cis'''> | <a' a''>2 <fis' fis''> | "
                      "<gis' gis''>2 <bis' bis''> | <cis'' cis'''>1\\fermata \\ottava #0"},
            {"name": "chords", "clef": "bass", "hand": "lh",
             "music": "r4 <gis cis' e'>\\p <gis cis' e'> <gis cis' e'> | r4 <gis cis' e'> <gis cis' e'> <gis cis' e'> | "
                      "r4 <a cis' fis'> <a cis' fis'> <a cis' fis'> | r4 <gis bis dis'> <gis bis dis'> <gis bis dis'> | "
                      "r4 <gis cis' e'> <gis cis' e'> <gis cis' e'> | r4 <a cis' fis'> <a cis' fis'> <a cis' fis'> | "
                      "r4 <gis bis dis'> <gis bis fis'> <gis bis dis'> | r4 <gis cis' e'>2.\\fermata"},
            {"name": "bass", "clef": "bass", "hand": "lh",
             "music": "\\ottava #-1 <cis,, cis,>4\\sustainOn r2. | <cis,, cis,>4\\sustainOff\\sustainOn r2. | "
                      "<fis,, fis,>4\\sustainOff\\sustainOn r2. | <gis,, gis,>4\\sustainOff\\sustainOn r2. | "
                      "<cis,, cis,>4\\sustainOff\\sustainOn r2. | <a,, a,>4\\sustainOff\\sustainOn r2. | "
                      "<gis,, gis,>4\\sustainOff\\sustainOn r2. | <cis,, cis,>1\\sustainOff\\sustainOn\\fermata \\ottava #0"},
        ],
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if every 8va and 8vb passage is played in the right octave and the crossed-hand notes come on time.",
    "Pass if you can play Part C's exercises in full or in outline without stopping, and the Wedding Day at "
    "Troldhaugen excerpt after a few days.",
    "When you pass, move on to Unit 6.",
]
