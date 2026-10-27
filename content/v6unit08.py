"""Volume 6, Unit 8: Lead sheets, simplifying and review."""

KEYBOARDS = []

INTRO = [
    "Much of the music a pianist is handed is not written out at all: a tune with chord symbols above it, a "
    "\"lead sheet\". Hymnals, folk-song books, musicals and jazz standards all use them. The pianist plays the "
    "tune (or lets a singer have it) and makes the accompaniment from the symbols.",
    "This last unit teaches you to read chord symbols as fast as notes, and ends the course with a review: one "
    "exercise of each kind from this volume, and the opening of one of the best-loved piano pieces ever "
    "written.",
]

NEW_IDEAS = [
    ("Chord symbols", "A letter names the chord's root: C is C major (C E G). A small m makes it minor (Am: A C E). "
                      "7 adds the minor seventh above the root (G7: G B D F); maj7 adds the major seventh (Cmaj7: C "
                      "E G B); m7 is a minor chord with a minor seventh (Dm7: D F A C). 6 adds the sixth (C6: C E G "
                      "A)."),
    ("Slash chords", "A letter after a slash is the bass note: G7/B is G7 with B in the bass; C/E is C major with E "
                     "in the bass. Play the bass note with the left hand and the chord above it."),
    ("Realising a lead sheet", "Start simple: the left hand plays the chord in root position, one per bar, while the "
                               "right hand plays the tune. Then break the chord up: bass note and chord (oom-pah), "
                               "or a broken chord (root, fifth, tenth). Keep the left hand below the tune."),
    ("Simplifying, again", "If a passage is too hard at sight, keep the tune and the bass and drop the inner notes "
                           "(Unit 5). Keep the beat going: a simple version in time is better than a full version "
                           "that stops."),
]

EXAMPLES = [
    {"title": "One lead sheet, three ways",
     "text": "The symbols C, Am, F and G7. Bars 1-2: the left hand plays each chord in root position; bars 3-4: bass "
             "note and chord (oom-pah).",
     "time": "4/4", "wide": True,
     "rh": "e'4 g' c'' g' | a'2 c'' | a'4 f' c'' a' | b'2 g'",
     "lh": "<c e g>1 | <a, c e>1 | f,4 <a c'> f, <a c'> | g,4 <b f'> g, <b f'>"},
    {"title": "Slash chords",
     "text": "C, G7/B (B in the bass), Am, C/E: the bass line falls and rises by step under the chords.",
     "time": "4/4", "wide": True,
     "rh": "<e' g' c''>2 <d' f' g'> | <c' e' a'>2 <c' e' g'>",
     "lh": "c2 b, | a,2 e"},
]

TIPS = [
    "Before you play, read the chord symbols of the whole lead sheet aloud: \"C, A minor, F, G seven\".",
    "Play the bass note of every symbol first (the root, or the note after the slash).",
    "Find the chords near each other: Am after C keeps two notes, G7 after C keeps one.",
    "Keep the left hand's accompaniment simple and steady; the tune is what the listener follows.",
    "In the review, name the skill each exercise practises before you start.",
]

PART_NOTES = {
    "A": "Lead sheets with major and minor chords. Play the tune with the right hand and each chord in root position "
         "with the left; then play them again with a bass note and the chord (oom-pah or oom-pah-pah).",
    "B": "Lead sheets with seventh chords and slash chords. Choose an accompaniment pattern (block chords, oom-pah, "
         "broken chords) and keep it all through.",
    "C": "Review: one exercise of each kind from this volume: the middle voice changing hands, a hemiola, 7/8, "
         "secondary dominants, octaves, a song, a string quartet and a fugue exposition.",
}

PIECES = [
    {
        "title": "Amazing Grace", "credit": "Traditional (the tune \"New Britain\"), a lead sheet",
        "meter": "3/4", "tempo": 84, "key": "g \\major", "upbeat": "1/4", "group": "lead",
        "note": "A lead sheet: the tune and the chord symbols only. Play the tune with the right hand and make the "
                "accompaniment with the left: first each chord in root position, held for the bar, then a bass "
                "note and two chords (oom-pah-pah). D7 in bar 14 leads home to G.",
        "staves": [
            {"name": "symbols", "clef": "chords",
             "music": "\\chordmode { \\partial 4 s4 | g2. | g2. | c2. | g2. | g2. | g2. | d2. | d2. | g2. | g2. | c2. | g2. | "
                      "g2. | d2.:7 | g2. | g2 }"},
            {"name": "tune", "clef": "treble", "hand": "rh",
             "music": "\\partial 4 d'4 | g'2 b'8( g') | b'2 a'4 | g'2 e'4 | d'2 d'4 | g'2 b'8( g') | b'2 a'4 | "
                      "d''2.~ | d''2 b'4 | \\break d''2 b'8( g') | b'2 a'4 | g'2 e'4 | d'2 d'4 | g'2 b'8( g') | "
                      "b'2 a'4 | g'2.~ | g'2"},
        ],
    },
    {
        "title": "Greensleeves", "credit": "Traditional English tune (16th century), a lead sheet",
        "meter": "3/4", "tempo": 92, "key": "a \\minor", "upbeat": "1/4", "group": "lead",
        "note": "A lead sheet with seventh chords and slash chords. Am7 is A C E G; Cmaj7 is C E G B; E7/G-sharp "
                "has G-sharp in the bass. Choose an accompaniment (block chords, or a bass note and two chords) and "
                "keep it steady; the G-sharps in the tune belong to the E7 chords.",
        "staves": [
            {"name": "symbols", "clef": "chords",
             "music": "\\chordmode { \\partial 4 s4 | a2.:m7 | c2.:maj7 | g2. | e2.:m7 | a2.:m | a2.:m/e | e2.:7 | e2.:7 | "
                      "a2.:m7 | c2./e | g2. | e2.:m7 | f2.:maj7 | e2.:7/gis | a2.:m | a2:m }"},
            {"name": "tune", "clef": "treble", "hand": "rh",
             "music": "\\partial 4 a'4 | c''2 d''4 | e''4. f''8 e''4 | d''2 b'4 | g'4. a'8 b'4 | c''2 a'4 | "
                      "a'4. gis'8 a'4 | b'2 gis'4 | e'2 a'4 | \\break c''2 d''4 | e''4. f''8 e''4 | d''2 b'4 | "
                      "g'4. a'8 b'4 | c''4. b'8 a'4 | gis'4. fis'8 gis'4 | a'2.~ | a'2"},
        ],
    },
    {
        "title": "Old Hundredth", "credit": "Genevan Psalter (1551), the hymn tune \"Old Hundredth\"",
        "meter": "4/4", "tempo": 72, "tempo_unit": "2", "key": "g \\major",
        "note": "Transposing at sight: play the tune as printed (G major), then a tone lower in F major (one flat), "
                "then a tone higher in A major (three sharps). Read the shape of each line, not the note names. "
                "When you can, add a bass note under each half note with the left hand.",
        "staves": [
            {"name": "tune", "clef": "treble", "hand": "rh",
             "music": "g'2 g' fis' e' | d'2 g' a' b'\\fermata | b'2 b' b' a' | g'2 c'' b' a'\\fermata | \\break "
                      "g'2 a' b' a' | g'2 e' fis' g'\\fermata | d''2 b' g' a' | c''2 b' a' g'\\fermata"},
        ],
    },
    {
        "title": "Waltz: Bethena", "credit": "Scott Joplin (1905), Bethena: A Concert Waltz - the first strain, with "
                                            "chord symbols",
        "meter": "3/4", "tempo": 96, "key": "g \\major",
        "note": "Joplin's waltz, with chord symbols added above it (they are not in Joplin's score): read the "
                "harmony of each bar as a symbol, then find it in the notes. A7/E is A7 with E in the bass; C6 adds "
                "A to C major. The right hand plays the tune over held lower notes. Joplin holds the bass octaves "
                "of bars 3, 8 and 11 (with the pedal); here they are quarter notes. Source: Mutopia Project no. "
                "463 (public domain).",
        "staves": [
            {"name": "symbols", "clef": "chords",
             "music": "\\chordmode { g2. a2.:7/e d2.:7 e2.:m c2.:6 g2./d a2.:7 d2.:7 g2. a2.:7/e d2.:7 e2.:m c2.:6 g2./d "
                      "a2:7/e d4:7 g2. }"},
            {"name": "up", "clef": "treble", "hand": "rh",
             "music": "<< { a'8 g'4 b'8 a'4 | a'8 g'4 b'8 a'4 | a'8 c''4 b'8 a'4 | g'2. | e''8 a''4 e''8 g''4 | "
                      "b'8 e''4 b'8 d''4 | g'8 b'4 g'8 b'4 | a'2. | \\break a'8 g'4 b'8 a'4 | a'8 g'4 b'8 a'4 | "
                      "a'8 c''4 b'8 a'4 | g'2. | e''8 a''4 e''8 g''4 | b'8 e''4 b'8 d''8( d') | "
                      "cis'8( <g' b'>4) c'8( <fis' a'>4) | g'2( b'4) } \\\\ "
                      "{ <b d'>2. | <cis' g'>2. | <c' fis'>2 <c' fis'>4 | <b e'>2. | c''2 c''4 | g'2 <g' b'>4 | "
                      "cis'2 <cis' g'>4 | <c' fis'>2. | <b d'>2. | <cis' g'>2. | <c' fis'>2 <c' fis'>4 | <b e'>2. | "
                      "c''2 c''4 | g'2 r4 | cis'4. c'8 c'4 | <b d'>2. } >>"},
            {"name": "down", "clef": "bass", "hand": "lh",
             "music": "g,4 <d g> <d g> | <e, e>4 <e g a> <e g a> | << { r4 <fis a> r } \\\\ { <d, d>4 s <dis, dis> } >> | "
                      "<e, e>4 <e g> <e g> | <c, c>4 <e g c'> <e g c'> | <d, d>4 <d g b> <d g b> | "
                      "<a,, a,>4 <e g a> <a,, a,> | << { r4 <d fis a> <d fis a> } \\\\ { <d, d>4 s2 } >> | "
                      "g,4 <d g> <d g> | <e, e>4 <e g a> <e g a> | << { r4 <fis a> r } \\\\ { <d, d>4 s <dis, dis> } >> | "
                      "<e, e>4 <e g> <e g> | <c, c>4 <e g c'> <e g c'> | <d, d>4 <d g b> <d g b> | "
                      "<e, e>4 <a,, a,> <d, d> | <g, g>2."},
        ],
    },
    {
        "title": "Clair de lune", "credit": "Claude Debussy (1890-1905), Suite bergamasque: Clair de lune - bars 1-8, "
                                           "with a closing chord",
        "meter": "9/8", "tempo": 44, "tempo_unit": "4.", "key": "des \\major",
        "note": "The last piece of the course. 9/8: three slow beats of three eighths. The music floats: tied notes "
                "hide the beat, and in bar 3 two duplets (two notes in the time of three) sound against the "
                "eighths. Both hands start in the treble clef; the left hand moves to the bass clef in bar 6. Five "
                "flats, and in bar 2 a B double-flat (the white key A). Debussy asks for \"con sordina\" (the soft "
                "pedal); use the sustain pedal lightly at each change of harmony. Source: Mutopia Project no. 1778 "
                "(public domain).",
        "rh": "\\dynamicUp << { r4\\pp <f'' aes''>8~( <f'' aes''>4. <des'' f''>4.~ | <des'' f''>8) <c'' ees''>( <des'' f''> <c'' ees''>2.~ | "
              "<c'' ees''>8) <bes' des''>( <c'' ees''> \\tuplet 2/3 { des''8 f''~ } \\tuplet 2/3 { f''8 des''~ } | "
              "des''8 <aes' c''> <bes' des''> <aes' c''>2.)~ | \\break "
              "c''8( bes' c'' bes' ees'' bes' aes' bes' aes'~ | aes'8 ges' aes' ges'4. f'4.) | "
              "f'8( f' ges' f' bes' f' ees' f' ees'~ | ees'8 des' ees' des'4. c'4.) } \\\\ "
              "{ s8*9 | s8*9 | s4. bes'2.~ | bes'8 s1 | ges'2. ges'4. | ees'2. ees'4. | des'2.~ des'4. | bes2. aes4. } >> | "
              "<f' aes' des''>2.~ <f' aes' des''>4.\\fermata",
        "lh": "\\clef treble r8 <f' aes'>4~ <f' aes'>2. | <ges' beses'>2.~ <ges' beses'>4. | <f' aes'>2.~ <f' aes'>4. | "
              "<ees' ges'>2.~ <ees' ges'>4. | << { ees'2. ees'4. | \\clef bass des'2. c'4. | bes2.~ bes4. | aes2. ges4. } "
              "\\\\ { des'2. c'4. | bes2. a4. | aes2. ges4. | f2. ees4. } >> | <des, aes,>2.~ <des, aes,>4.\\fermata",
    },
]

CHECKPOINT_TITLE = "The end of the course"
CHECKPOINT = [
    "Play two new exercises from each part at the speed shown, with no more than one stop each.",
    "Pass if you can play Amazing Grace and Greensleeves from their lead sheets with a steady left-hand "
    "accompaniment, and Old Hundredth in three keys.",
    "Pass if you can play the review exercises of Part C at sight, and Clair de lune after a few days.",
    "What next: read something new every day. Hymnals, the Bach chorales, Schubert's songs with a singer, "
    "Haydn quartets with friends, Mozart and Haydn sonatas, Chopin's mazurkas, folk-song books and lead "
    "sheets. You are a sight-reader now: keep the habit.",
]
