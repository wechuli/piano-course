"""Volume 6, Unit 4: Chromatic harmony."""

KEYBOARDS = []

INTRO = [
    "Romantic music is full of notes outside the key: sharps and flats that appear for one chord and vanish. "
    "Read one by one, they are a forest of accidentals. Read as chords, they are a handful of familiar shapes: "
    "the dominant seventh of a chord other than the tonic, the diminished seventh, the Neapolitan sixth and the "
    "augmented sixths. Each one has a strong pull towards the chord that follows.",
    "This unit's exercises are written as four-part harmony at the keyboard: the right hand plays three voices, "
    "the left hand the bass. Name each chord as you meet it and let your hands find the shape; then listen for "
    "where each chromatic note goes.",
]

NEW_IDEAS = [
    ("Secondary dominants", "Any major or minor chord of the key can have its own dominant seventh: V7 of V "
                            "(in C: D F-sharp A C) leads to G, V7 of ii (A C-sharp E G) leads to D minor. The "
                            "sharp is the leading note of the chord that follows: it rises a half step; the 7th "
                            "falls."),
    ("Diminished sevenths", "Four notes a minor third apart (B D F A-flat in C). The bottom note is a leading note "
                            "and rises; the top note falls. Every chord of the key can have one: vii°7 of V is "
                            "F-sharp A C E-flat."),
    ("The Neapolitan sixth", "In a minor key, the major chord on the lowered 2nd (in A minor: B-flat D F), usually "
                             "with its third (D) in the bass. It goes to V: the B-flat falls to G-sharp."),
    ("The augmented sixths", "Built on the lowered 6th in the bass (in A minor: F) with the raised 4th above it "
                             "(D-sharp): an augmented sixth that opens out to the octave E-E. The Italian sixth adds "
                             "the tonic (F A D-sharp), the French sixth also the 2nd (F A B D-sharp), the German "
                             "sixth the 3rd (F A C D-sharp, which goes to the tonic 6/4 chord first)."),
    ("Double sharps and flats", "In sharp keys a raised note may already be sharp: in E major, V7 of vi is G-sharp "
                                "B-sharp D-sharp F-sharp, and its diminished seventh B-sharp D-sharp F-sharp A. A "
                                "double sharp raises a natural note by two half steps."),
    ("Modulation", "A pivot chord belongs to both keys (in C major, A minor is vi; in G major it is ii) and leads to "
                   "the new key's V7. A diminished seventh can be respelled: B D F A-flat in C is the same sound as "
                   "G-sharp B D F, the diminished seventh of A, so it can lead to a key a minor third away."),
]

EXAMPLES = [
    {"title": "V7 of V and the diminished seventh of V",
     "text": "In C major: D7 (F-sharp rises to G, C falls to B), then F-sharp A C E-flat (F-sharp rises, E-flat falls).",
     "time": "4/4", "wide": True,
     "rh": "<c' fis' a'>2 <b d' g'>2 | <ees' a' c''>2 <d' g' b'>2",
     "lh": "d2 g,2 | fis,2 g,2"},
    {"title": "The Neapolitan sixth and the augmented sixths in A minor",
     "text": "N6 (B-flat falls to G-sharp), the Italian sixth, the French sixth, and the German sixth through the "
             "tonic 6/4: in each, F in the bass falls to E and D-sharp rises to E.",
     "time": "4/4", "key": "a \\minor", "wide": True,
     "rh": "<f' bes' d''>2 <e' gis' b'>2 | <a' dis''>2 <a' e''>2 | <a' b' dis''>2 <gis' b' e''>2 | "
           "<c'' dis''>2 <c'' e''>4 <b' d''>4",
     "lh": "d2 e2 | f2 e2 | f2 e2 | f2 e2"},
    {"title": "One sound, two spellings",
     "text": "The diminished seventh of C (B D F A-flat) is respelled as the diminished seventh of A (G-sharp B D F) "
             "and resolves to A major.",
     "time": "4/4", "wide": True,
     "rh": "<f' aes' d''>2 <d' f' b'>2 | <cis' e' a'>1",
     "lh": "b,2 gis,2 | a,1"},
]

TIPS = [
    "Name each chromatic chord before you play it: \"V7 of V\", \"diminished seventh\", \"Neapolitan\".",
    "A sharp (or natural that raises a note) is usually a leading note: expect it to rise. A flat usually falls.",
    "Hold the common notes between chords and move the others the shortest way.",
    "In the first two exercises of each part the chords are named under the bass: read the names, then the notes.",
    "After a modulation, check the new key signature before you read on.",
]

PART_NOTES = {
    "A": "Secondary dominants (V7 of ii, iii, IV, V or vi) and diminished sevenths (vii°7 of the same chords), "
         "each followed by its chord; the cadence V7-I at the end. Right hand: three upper voices; left hand: "
         "the bass. The first two exercises name the chords.",
    "B": "Minor keys: three cadences in each exercise, each prepared by a Neapolitan sixth or an augmented sixth "
         "(Italian, French, or German through the 6/4 chord). The first two exercises name the chords.",
    "C": "Modulation: three bars in the first key, a pivot bar, and four bars in the new key, whose key signature "
         "appears in bar 5. Odd-numbered exercises use a pivot chord (marked \"pivot\" in the first one); the "
         "even-numbered use a diminished seventh, respelled (marked in the second).",
}

PIECES = [
    {
        "title": "Prelude in C minor", "credit": "Frederic Chopin (1839), Prelude Op. 28 No. 20 - bars 1-8, with the "
                                               "closing chord",
        "meter": "4/4", "tempo": 42, "key": "c \\minor", "allow_span": 14,
        "note": "A slow procession of chords, one on each beat. Bar 2 goes from A-flat to D-flat major: the "
                "Neapolitan chord (here with its root in the bass); bar 3 has C7, the dominant seventh of iv; bar 4 "
                "has D7 over C, the dominant seventh of V. From bar 5 the bass falls by half steps under the "
                "chords. The right hand starts in the bass clef. Use the pedal on every beat (marked in bar 1). On the third beat of bar 2 the right hand "
                "stretches a ninth (D-flat to E-flat): roll the chord quickly from the bottom if it is too wide. "
                "Source: Mutopia Project no. 472 (public domain).",
        "rh": "\\clef bass <g c' ees' g'>4\\ff( <aes c' ees' aes'> << { <ees' g'>8. <d' f'>16 } \\\\ { <g b>4 } >> <ees g c' ees'>) | "
              "<ees aes c' ees'>4( <f aes des' f'> << { <c' ees'>8. <bes des'>16 } \\\\ { <des ees g>4 } >> <c ees aes c'>) | "
              "<d f b d'>4(\\< <e g bes c' e'> << { g'8. f'16 } \\\\ { <aes c'>4 } >> <g c' ees'> | "
              "<fis c' d'>4 <g b d' g'> \\clef treble << { b'8. a'16 } \\\\ { <c' d' fis'>4 } >> <b d' g'>4)\\! | \\break "
              "<ees' g' ees''>4\\p( <ees' aes' ees''> << { <d' d''>4 } \\\\ { aes'8. fis'16 } >> <d' g' d''>4 | "
              "<c' g' c''>4 <c' d' fis' d''> <d' g' b'>8. <c' a'>16 <b d' g'>4 | "
              "<c' g' c''>4 <aes c' aes'> << { <g d'>4 } \\\\ { g'8. f'16 } >> <g c' ees'>4 | "
              "\\clef bass <ees aes c' ees'>4 <f aes des' f'> << { ees'8. d'16 } \\\\ { <f g b>4 } >> <ees g c'>4) | "
              "\\clef treble <c' ees' g' c''>1->\\fermata",
        "lh": "<c, c>4\\sustainOn <f,, f,>\\sustainOff\\sustainOn <g,, g,>\\sustainOff\\sustainOn <c, g, c>\\sustainOff\\sustainOn | "
              "<aes,, aes,>4\\sustainOff_\\markup \\italic \"(pedal on every beat)\" <des,, des,> <ees,, ees,> <aes,, aes,> | "
              "<g,, g,>4 <c,, c,> <f,, f,> <c, c> | <d, a, d>4 <g,, g,> <d,, d,> <g,, g,> | "
              "<c, c>4( <c c'> <b, b> <bes, bes> | <a, a>4 <aes, aes> <g, g> <f, f> | <ees, ees>4 <f, f> <b,, b,> <c, c> | "
              "<aes,, aes,>4 <des,, des,> <g,, g,> <c,, c,>) | <c, g,>1->\\fermata",
    },
    {
        "title": "Pathetique: Grave", "credit": "Ludwig van Beethoven (1798), Sonata Op. 13, first movement - "
                                              "bars 1-4, the run simplified",
        "meter": "4/4", "tempo": 60, "tempo_unit": "8", "key": "c \\minor", "allow_32": True,
        "note": "Count eighth notes: eight slow beats in a bar. Each phrase starts with a loud chord that suddenly "
                "becomes soft (fp) and rises through dotted rhythms to a chord full of tension: in bar 1 the "
                "diminished seventh A C E-flat (over F-sharp in the left hand) and in bar 3 the diminished seventh "
                "F-sharp A C E-flat. Bar 4 climbs to A-flat (sf) and runs down to E-flat; Beethoven's run is faster "
                "and longer (a written-out cadenza). The excerpt ends on the E-flat major chord of bar 5. Source: "
                "Mutopia Project no. 299 (public domain).",
        "rh": "<ees g c'>4\\fp~ <ees g c'>16. <g c'>32 <g b d'>16. <g c' ees'>32 <a c' ees'>4( <b d'>8) r | "
              "<b d' f'>4\\fp~ <b d' f'>16. <b d' f'>32 <b d' g'>16. <b d' aes'>32 <b d' aes'>4( <c' ees' g'>8) r | \\break "
              "<fis' a' c''>4\\fp~ <fis' a' c''>16. <fis' a' c''>32 <fis' a' d''>16. <fis' a' ees''>32 "
              "<fis' a' ees''>4(\\sf <d' g' d''>16) r32 <fis' a' c''>32 <fis' a' d''>16. <fis' a' ees''>32 | "
              "<fis' a' ees''>4(\\sf <d' g' d''>8\\p <g' c'' e''> <aes' c'' f''>) aes''8\\sf~ aes''32( g'' f'' ees'' d'' c'' bes' aes') | "
              "<ees' g' bes'>1\\p\\fermata",
        "lh": "<c, ees, g, c>4~ <c, ees, g, c>16. ees32 d16. c32 fis4( g8) r16. aes,32 | "
              "aes4~ aes16. aes32 g16. f32 ees4~ ees8 r16. ees32 | "
              "ees'4~ ees'16. ees'32 d'16. c'32 c'4( b16) r32 ees'32 d'16. c'32 | "
              "c'4( b8 <bes c' e'> <aes c' f'>) r <bes,, bes,>4 | <ees, ees>1\\fermata",
    },
    {
        "title": "Album Leaf", "credit": "Edvard Grieg (1867), Lyric Pieces Op. 12 No. 7 - the first section",
        "meter": "2/4", "tempo": 112, "key": "e \\minor", "upbeat": "1/8",
        "note": "E minor over a pedal: the left hand plays E in the bass of every bar. In bars 1, 3, 5 and 7 the chord "
                "above it is chromatic: C, D-sharp and A (and B, D-sharp, A), a diminished seventh whose D-sharp "
                "leads to E. Bar 5 has a chromatic line in the tune: A, G-sharp, G, F-sharp. The small notes "
                "(acciaccaturas) are crushed in quickly before the beat. Notes retyped from the Mutopia Project "
                "engraving no. 2194 (Creative Commons Attribution-ShareAlike 4.0).",
        "rh": "\\partial 8 b'8\\p( | e''8. fis''16 g''8 fis'' | \\acciaccatura fis''8 b''8-.) b''( e''4->) | "
              "\\acciaccatura e''8 fis''8-. fis''( b'4->) | \\acciaccatura b'8 e''8-. e''( e'8->) b' | \\break "
              "\\acciaccatura b'8 e''8.( fis''16 \\acciaccatura fis''8 a''16 gis'' g'' fis'' | "
              "\\acciaccatura fis''8 b''8-.) b''( e''4->) | \\acciaccatura e''8 fis''8-. fis''( b' b'') | e''4( e'''8) r",
        "lh": "\\partial 8 r8 | e8( <b g'>) e( <c' dis' a'>) | e8( <b g'>) e( <b g'>) | e8( <b dis' a'>) e( <b dis' a'>) | "
              "e8( <b g'>) e( <b g'>) | e8( <b g'>) e( <c' dis' a'>) | e8( <b g'>) e( <b g'>) | "
              "e8( <b dis' a'>) e( <b dis' a'>) | e8( <b g'>) e,8 r",
    },
    {
        "title": "Modulation Study", "credit": "Original, written for this book",
        "meter": "4/4", "tempo": 56, "key": "c \\major",
        "note": "A journey from C major to E-flat major and back, in four-part harmony. Bar 3: the diminished seventh "
                "of C (B D F A-flat). Bar 4: the same sound, spelled as the diminished seventh of E-flat (C-flat D F "
                "A-flat; the bass B becomes C-flat), with E-flat's key signature; it goes to E-flat's tonic 6/4. "
                "Bar 6: the A-flat major chord is IV in E-flat and VI in C minor (a pivot), followed by the "
                "dominant seventh of C; bar 7 is in C major again.",
        "rh": "<e' g' c''>2\\mp <f' a' c''> | <f' g' b'>2 <e' g' c''> | <f' a' c''>2 <f' aes' d''> | \\break "
              "\\key ees \\major <f' aes' d''>2 <ees' g' ees''> | <f' aes' d''>2 <ees' g' ees''> | "
              "<ees' aes' c''>2 <d' f' b'> | \\break \\key c \\major <c' e' c''>2 <c' f' a'> | <c' e' g'>2 <b d' f'> | <c' e' c''>1",
        "lh": "c2 f, | g,2 c | a,2 b, | \\key ees \\major ces2 bes, | bes,2 ees | aes,2 g, | "
              "\\key c \\major c2 f, | g,2 g, | c1",
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speed shown, with no more than one stop each.",
    "Pass if you can name the chromatic chords of Part A and Part B as you play them, and every leading note "
    "rises and every 7th falls.",
    "Pass if you can play the Modulation Study at sight and the Chopin Prelude after a few days.",
    "When you pass, move on to Unit 5.",
]
