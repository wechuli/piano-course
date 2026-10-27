"""Volume 5, Unit 2: Chorales."""

KEYBOARDS = []

INTRO = [
    "A chorale is a hymn tune harmonised in four voices: soprano, alto, tenor and bass. On the piano the right "
    "hand plays the soprano (stems up) and the alto (stems down) on the treble staff, and the left hand plays the "
    "tenor (stems up) and the bass (stems down) on the bass staff. Every beat is a new chord, so you read "
    "vertically: one chord at a time, top to bottom, then the next.",
    "Bach harmonised hundreds of chorales, and organists and church pianists have read them at sight for three "
    "hundred years. They are the best training there is for reading chords.",
]

NEW_IDEAS = [
    ("Four voices on two staves", "Soprano and alto share the treble staff, tenor and bass the bass staff. "
                                  "Stems up for the higher voice of each pair, stems down for the lower."),
    ("Chords on every degree", "Besides I, IV and V you will meet ii (D F A in C major) and vi (A C E), and V7. "
                               "In a minor key the chords are i, iv, V (with the raised 7th) and VI."),
    ("First inversion", "A chord with its third in the bass, such as C major with E in the bass, is in first "
                        "inversion. It sounds lighter than a root-position chord and helps the bass move by step."),
    ("Fermatas", "A fermata (a dot under an arch) marks the end of a line of the hymn. Hold the chord a little "
                 "longer, breathe, and start the next line in time."),
    ("When the left hand can't reach", "Sometimes the tenor sits more than an octave above the bass. Then the "
                                       "right hand takes the tenor note: an old organist's trick that every "
                                       "chorale player uses."),
]

EXAMPLES = [
    {"title": "One chord, four voices",
     "text": "Soprano E, alto C (right hand); tenor G, bass C (left hand). Then the same chord in first "
             "inversion (E in the bass), then ii (D F A), V7 and I. The 7th of V7 (F, in the tenor) falls to E.",
     "time": "4/4",
     "rh": "<< { e''4 e'' f'' d'' | e''1 } \\\\ { c''4 c'' a' b' | c''1 } >> \\bar \"||\"",
     "lh": "<< { g4 g d' f | e1 } \\\\ { c4 e d g, | c1 } >>"},
]

TIPS = [
    "Read each chord from the bass up: it tells you which chord it is and whether it is inverted.",
    "Most voices move by step or stay on the same note. Look for the notes that don't move: hold them.",
    "Breathe at every fermata, as a choir would, but keep the beat underneath.",
    "If four voices are too many at first, play soprano and bass only, then add the inner voices.",
]

PART_NOTES = {
    "A": "Three voices in half notes: soprano and alto in the right hand, the bass in the left. C, G and F major.",
    "B": "Four voices in quarter notes, with fermatas at the end of each line. Look out for first inversions "
         "and for ii and vi. Keys with up to two sharps or flats.",
    "C": "Four-voice chorales in A, D and E minor. The raised 7th (G-sharp, C-sharp, D-sharp) appears in every "
         "V chord.",
}

PIECES = [
    {
        "title": "Aus meines Herzens Grunde", "credit": "J. S. Bach, chorale, BWV 269 - first two lines",
        "meter": "3/4", "tempo": 72, "key": "g \\major", "allow_span": 19, "upbeat": "1/4",
        "note": "A chorale in 3/4 that begins with an upbeat (one beat before the first bar line). Play the whole "
                "passage twice, as the repeat sign asks. The tenor and bass are often more than an octave apart: take the "
                "tenor with the right hand wherever the left hand cannot reach. Source: Mutopia Project no. 378 (public domain).",
        "rh": "\\repeat volta 2 { \\partial 4 << { g'4 | g'2 d''4 | b'4. a'8 g'4 | g'4. a'8 b'4 | a'2\\fermata b'4 | "
              "\\break d''2 c''4 | b'4 a'2 | g'2\\fermata } \\\\ { d'4 | d'4 e' d' | d'2 b4 | e'8 d' e' fis' g'4 | "
              "fis'2 g'4 | d'4 e' fis' | g'2 fis'4 | d'2 } >> }",
        "lh": "\\repeat volta 2 { \\partial 4 << { b4 | b4 c'8 b a4 | g4 fis g | c'8 b c'4 d' | d'2 d'4 | "
              "a4 b c' | d'4 e' d'8 c' | b2 } \\\\ { g,4 | g4 e fis | g4 d e | c4 b,8 a, g,4 | d2\\fermata g,4 | "
              "fis,4 g, a, | b,4 c d | g,2\\fermata } >> }",
    },
    {
        "title": "Chorale", "credit": "Robert Schumann (1848), Album for the Young, Op. 68 No. 4 - complete",
        "meter": "4/4", "tempo": 92, "key": "g \\major",
        "note": "Schumann's setting of the chorale 'Freue dich, o meine Seele', in half notes: each half note is a "
                "new chord. Play bars 1-8 twice. Notes retyped from the Mutopia Project engraving no. 782 by "
                "Philippe Hezaine (CC BY-SA 2.5).",
        "rh": "\\repeat volta 2 { << { g'2\\p a' | b' a' | g' fis' | e' d'\\fermata | \\break g' a' | b' c'' | b' a' | "
              "g'1\\fermata } \\\\ { d'2 d' | d' d' | cis' d' | cis' d' | b d' | d' g' | d'2~ d'4 c' | b1 } >> } "
              "\\break << { b'2 c'' | d'' c'' | b' a' | b'1\\fermata | \\break d''2 d'' | e'' d'' | c'' b' | "
              "a'1\\fermata | \\break b'4( c'' d''2) | c''2 b' | g' a' | b'2\\fermata g'\\fermata | \\break "
              "b'4( c'' d''2) | c''2 b' | a' a' | g'1\\fermata } \\\\ { g'2 fis' | g' fis' | g' g'4( fis') | g'1 | "
              "g'2 g' | g' g' | fis' g' | fis'1 | g'2 g' | g' g' | e' fis' | g' e' | g' g' | fis' g' | e' fis' | g'1 } >>",
        "lh": "\\repeat volta 2 { << { b2 a | g a | a a | a fis | e fis | g g | g fis | g1 } \\\\ "
              "{ g2 fis | g fis | e d | a, d | e d | g e | d d | g,1 } >> } "
              "<< { d'2 c' | b c' | d' e'4( d') | d'1 | b2 d' | c' d' | d' d' | d'1 | d'2 d' | e' d' | c' c' | "
              "d' c' | d' d' | d' d' | c' c' | b1 } \\\\ { g2 a | b a | g c'4( d') | g1 | g2 b | c' b | a g | d1 | "
              "g4( a b2) | c'2 g | c' a | g c | g4( a b2) | a2 g | c d | g1 } >>",
    },
    {
        "title": "O Haupt voll Blut und Wunden", "credit": "J. S. Bach, chorale from the St Matthew Passion - complete",
        "meter": "4/4", "tempo": 60, "key": "d \\minor", "allow_span": 19, "upbeat": "1/4",
        "note": "The Passion Chorale. It begins in D minor and ends on an F major chord. C-sharp is the raised 7th of "
                "D minor; F-sharp in bar 11 leads to G minor. Bach often puts the tenor more than an octave above the "
                "bass: wherever your left hand cannot reach both, take the tenor note with the right hand. Source: Mutopia Project no. 107 "
                "(public domain).",
        "rh": "\\partial 4 << { a'4 | d''4 c'' bes' a' | g'2 a'4\\fermata e'' | f''4 f'' e''8 d'' e''4 | "
              "d''2.\\fermata a'4 | \\break d''4 c'' bes' a' | g'2 a'4\\fermata e'' | f''4 f'' e''8 d'' e''4 | "
              "d''2.\\fermata f''4 | \\break e''8 d'' c''4 d'' e'' | f''2 f''4\\fermata c'' | d''4 c'' bes'8 a' bes'4 | "
              "a'2.\\fermata f''4 | \\break e''8 f'' g''4 f'' e'' | d''2 e''4\\fermata a' | bes'4 a' g' c'' | "
              "a'2.\\fermata } \\\\ { f'4 | f'8 g' a'4 d'8 e' f'4 | f'4( e') f' a' | a'4 a' a' a'8 g' | f'2. f'4 | "
              "f'8 g' a'4 d'8 e' f'4 | f'4( e') f' a' | a'4 a' a' a'8 g' | f'2. a'4 | g'4 g'8 f' f'4 bes' | "
              "bes'4( a'8 g') a'4 a' | a'8 g' a'4 g'8 fis' g'4 | fis'2. g'4 | g'4 c'' c'' c'' | c''4( b') c'' f'8 e' | "
              "d'8 e' f'4 f' e' | f'2. } >>",
        "lh": "\\partial 4 << { d'4 | d'8 e' f'4 g' c' | d'4( c') c' e' | e'4 d' d' cis' | a2. d'4 | "
              "d'8 e' f'4 g' c' | d'4( c') c' e' | e'4 d' d' cis' | a2. d'8 c' | bes4 c' c' bes8 c' | "
              "d'4( c'8 bes) c'4 f'8 ees' | d'4 d' d' d' | d'2. d'4 | c'8 d' e'4 f' g' | a'4( g') g' c' | "
              "bes4 c' c'8( bes16 a) g8 c' | c'2. } \\\\ { d'8 c' | bes4 a g f | bes,4( c) f\\fermata cis | "
              "d8 e f g a4 a, | d2.\\fermata d'8 c' | bes4 a g f | bes,4( c) f\\fermata cis | d8 e f g a4 a, | "
              "d2.\\fermata d4 | g4 a bes8 a g4 | f2 f4\\fermata f | bes4 fis g g, | d2.\\fermata b,4 | "
              "c4 c'8 b a4 g | f4( g) c\\fermata f | g4 a8 bes c'4 c | f2.\\fermata } >>",
    },
    {
        "title": "Ich dank dir, lieber Herre", "credit": "J. S. Bach, chorale, BWV 347 - complete, without the repeat",
        "meter": "4/4", "tempo": 66, "key": "a \\major", "allow_span": 19, "upbeat": "1/4",
        "note": "Three sharps: F, C and G. In bar 2 Bach writes G-natural for a moment; in bar 7 A-sharp leads to "
                "B minor. The tenor has a few eighth notes and two sixteenths of its own: keep them light. Where the "
                "left hand cannot reach, take the tenor with the right hand. Source: Mutopia Project no. 379 "
                "(public domain).",
        "rh": "\\partial 4 << { a'4 | a'4 a' a' b' | g'4 fis' e'\\fermata b' | cis''4 b' a' gis'8 fis' | "
              "gis'4 fis' e'\\fermata e'' | \\break d''4 cis'' b' a' | a'8 b' cis''4 b'\\fermata cis'' | d''4 cis'' b' ais' | "
              "b'2.\\fermata e'4 | \\break a'4 b' cis'' d'' | e''4 d''8 cis'' b'4\\fermata d'' | cis''4 b' e''4. d''8 | "
              "cis''8 b' a' b' cis''4 b' | a'2.\\fermata } \\\\ { e'4 | fis'4 e' fis' fis' | e'4 dis' b gis' | "
              "a'4 gis'8 fis' e'2~ | e'4 dis' b cis''8 b' | a'4 a' gis' a'8 g' | fis'8 gis' a'4 gis' ais' | "
              "b'8 a' g'4 fis'8 e' fis'4 | fis'2. e'8 d' | cis'4 d' e' fis'8 gis' | a'2 e'4 b' | "
              "a'8 gis' fis'4 e' fis'8 gis' | a'2 a'4 gis' | e'2. } >>",
        "lh": "\\partial 4 << { cis'4 | cis'4 cis'8 b a gis fis4 | b4. a8 gis4 e' | e'4 dis' cis'2 | "
              "b4. a8 gis4 gis | a8 b cis' d' e'4 e' | d'4 e' e' e' | fis'8 b4 ais8 b4 cis' | d'2. gis4 | "
              "a4 gis8 fis e e' d'4 | cis'8 d' e' fis' gis'4 fis' | fis'8 e' d' cis' b4 cis'8 d' | "
              "e'4. d'8 cis' fis' b e'16 d' | cis'2. } \\\\ { a8 gis | fis4 cis d dis | e4 b, e,\\fermata e | "
              "a4 b cis' b8 a | b4 b, e\\fermata cis | fis8 gis a4 e cis8 a, | d4 cis8 d e4\\fermata cis | "
              "b,4 cis d8 g fis4 | b,2.\\fermata cis4 | fis4 e8 d cis4 b, | a,8 b, cis d e4\\fermata b, | "
              "fis8 gis a4 gis8 e a4~ | a8 gis fis4 e8 d e4 | a,2.\\fermata } >>",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 3?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if you can say, before you play, which bars end with a fermata and whether each of those lines ends "
    "on I or on V.",
    "Pass if you can read the Bach chorale 'Aus meines Herzens Grunde' at sight with soprano and bass, then "
    "with all four voices after a few days.",
    "When you pass, move on to Unit 3.",
]
