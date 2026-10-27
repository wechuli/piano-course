"""Volume 5, Unit 1: Two voices in one hand."""

KEYBOARDS = []

INTRO = [
    "Real piano music often asks one hand to play two things at once: a tune on top and a second, quieter "
    "voice underneath, or a bass note held while the hand moves above it. To show this, the music is written "
    "in two voices on the same staff. The upper voice has its stems up, the lower voice its stems down.",
    "From this volume on there are no hand-position pictures. Read by key and by chord: before you play, "
    "name the key and look at the shapes the hands make.",
]

NEW_IDEAS = [
    ("Stems up, stems down", "When a staff holds two voices, the upper voice's stems point up and the lower "
                             "voice's stems point down, even where the notes are close together. Each voice "
                             "has its own complete rhythm, so both must add up to a full bar."),
    ("A held note under a moving tune", "A half or whole note with its stem down keeps sounding while the upper "
                                        "voice moves on. Hold it down with one finger (often the thumb in the right "
                                        "hand, or the little finger in the left) and play the tune with the others."),
    ("Shared notes", "Where both voices sing the same note, it is printed once with two stems. Play it once."),
    ("Two voices in the left hand", "The bass (stems down) holds while a tenor line (stems up) moves above it. "
                                    "The little finger holds the bass; the thumb and middle fingers play the tenor."),
]

EXAMPLES = [
    {"title": "Two voices on one staff",
     "text": "Upper voice (stems up): E D C, then C. Lower voice (stems down): G held for two beats, then E. "
             "Count the voices separately: each adds up to a full bar.",
     "staff": "treble", "time": "4/4",
     "rh": "<< { e''4 d'' c''2 | c''1 } \\\\ { g'2 e'2 | e'1 } >> \\bar \"||\""},
    {"title": "A bass and a tenor in the left hand",
     "text": "The left hand holds C (stems down) while the tenor walks E F G E above it.",
     "staff": "bass", "time": "4/4",
     "rh": "<< { e4 f g e | e1 } \\\\ { c1 | c1 } >> \\bar \"||\""},
]

TIPS = [
    "Before you play, find each voice's longest notes: those are the ones to hold.",
    "Play the upper voice alone once in your head, then imagine the held notes underneath it.",
    "Let the tune sing and keep the held voice quiet.",
    "If a held note is hard to keep down, it is better to let it go a little early than to stop the beat.",
]

PART_NOTES = {
    "A": "C major and G major. The right hand holds the stems-down note for the whole bar while the tune "
         "moves above it. The left hand plays held chords.",
    "B": "F major and D major in 3/4. The same two voices in the right hand, over a waltz bass.",
    "C": "G, F and B-flat major. The left hand holds the bass and plays a tenor line above it; the tune is in "
         "the right hand.",
}

PIECES = [
    {
        "title": "Evening Bells", "credit": "Original", "meter": "3/4", "tempo": 80, "key": "f \\major",
        "note": "The right hand plays two voices: a tune with stems up, and a held note with stems down in every "
                "bar. Hold the lower note with the thumb (or finger 2 for the B-flats).",
        "rh": "<< { a'4\\p c'' f'' | e''2 d''4 | a'2 c''4 | bes'2. | \\break a'4 c''\\< f'' | f''2\\mf d''4 | "
              "c''4\\> bes' g' | a'2.\\p } \\\\ { f'2. | bes'2. | f'2. | e'2. | f'2. | bes'2. | e'2. | f'2. } >>",
        "lh": "f2. | c2. | f2. | c2. | f2. | bes,2. | c2. | f,2.",
    },
    {
        "title": "Melody", "credit": "Robert Schumann (1848), Album for the Young, Op. 68 No. 1 - complete",
        "meter": "4/4", "tempo": 72, "allow": ["clef changes"], "allow_leap": 14,
        "note": "The first piece of Schumann's Album for the Young. The left hand plays above middle C, so it is "
                "written in the treble clef: read it like right-hand music. Its eighth notes are really two "
                "voices, a moving line and a repeated G above it. In bars 7 and 15 the right hand splits into two "
                "voices, and in bars 10 and 18 it jumps up from G to the high A. Play the repeat sign at bar 4: go back to the start once. Notes retyped from the Mutopia "
                "Project engraving no. 647 by Philippe Hezaine (CC BY-SA 2.5).",
        "rh": "\\repeat volta 2 { e''4-5\\p( d'' c'' b' | a'8 c'' b' d'' c''4 g') | g''4-5( f'' e'' c'' | "
              "b'4 <fis' a'> g') r | } \\break "
              "d''4( c'' b') r | f''4( e'' d'') r | a''4-5( g'' f'' e'' | "
              "d''8 f'' e'' g'') << { f''4.\\> d''8\\! } \\\\ { a'8 c'' b' d'' } >> | \\break "
              "<c'' e''>4( d'' c'' b' | a'8 c'' b' d'' c''4 g') | a''4-5( g'' <b' f''> <c'' e''> | "
              "d''8 f'' b' d'' c''4) r | \\break "
              "d''4( c'' b') r | f''4( e'' d'') r | a''4( g'' f'' e'' | "
              "d''8 f'' e'' g'') << { f''4.\\> d''8\\! } \\\\ { a'8 c'' b' d'' } >> | \\break "
              "<c'' e''>4( d'' c'' b' | a'8 c'' b' d'' c''4 g') | a''4( g'' <b' f''> <c'' e''> | "
              "d''8 f'' b' d'' c''4) r \\bar \"|.\"",
        "lh": "\\clef treble \\repeat volta 2 { c'8( g' f' g' e' g' c' e' | f' d' g' f' e' f' e' d') | "
              "e'( g' d' g' c' g' e' g' | d' g' c' d' b d' g4) | } "
              "f'8( g' e' g' d' g' fis' g') | d'( g' c' g' b g' fis' g') | f'( g' e' g' d' g' c' g' | "
              "b g' c' cis' d'4 g') | "
              "c'8( g' f' g' e' g' c' e' | f' d' g' f' e' f' e' c') | f'( c'' e' c'' d' g' c' g' | "
              "f' a' g' f' e' g' c' e') | "
              "f'( g' e' g' d' g' fis' g') | d'( g' c' g' b g' fis' g') | f'( g' e' g' d' g' c' g' | "
              "b g' c' cis' d'4 g') | "
              "c'8( g' f' g' e' g' c' e' | f' d' g' f' e' f' e' c') | f'( c'' e' c'' d' g' c' g' | "
              "f' a' g' f' e' g' c'4)",
    },
    {
        "title": "Consolation", "credit": "Friedrich Burgmuller (1851), 25 Easy Studies, Op. 100 No. 13 - "
                                        "the introduction, with a closing chord added",
        "meter": "4/4", "tempo": 72,
        "note": "The right hand holds a long note (stems down) while its upper fingers rock between two notes. In bar "
                "6 the two voices join into one line, and in bar 7 the tune (stems up) shares its notes with the "
                "eighth notes below it. The left hand reads above middle C with ledger lines. Source: Mutopia "
                "Project no. 224 (public domain).",
        "rh": "<< { r8 d''( e'' d'' e'' d'' e'' d'') | r8 c''( d'' c'' d'' c'' d'' c'') | r8 f''( g'' f'' g'' f'' g'' f'') | "
              "r8 e''( f'' e'' f'' e'' f'' e'') | \\break r8 e''( f'' e'' dis'' e'' f'' e'') | "
              "e''8->( d'' cis'' d'' b'' a'' f'' d'' | c''8 g' b' c'' e''4 d'') | c''1 } \\\\ "
              "{ g'1\\p | g'1 | b'1\\< | c''1\\! | a'1 | s1 | s2 e''8 g' d'' g' | <e' g'>1 } >>",
        "lh": "<g f'>1 | <g e'>1 | <g d'>1 | <g c'>1 | <g a cis'>1 | <f a d'>1 | <g c' e'>2 <g b f'>2 | <c g>1",
    },
    {
        "title": "Hymn with a Moving Tenor", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "g \\major",
        "note": "Now the left hand has the two voices: the bass holds a whole note (stems down) while the tenor "
                "walks in quarter notes above it (stems up). Hold the bass with finger 5.",
        "rh": "b'4\\mp a' g' b' | c''2 e'' | d''4 b' g' b' | a'1 | \\break b'4 c'' d'' b' | e''4\\< d'' c'' e'' | "
              "c''4\\> b' a' fis' | g'1\\p",
        "lh": "<< { d4 c b, d | e f g e | d e d g | fis e fis2 | d4 e fis g | g f e g | a c' c' a | g1 } \\\\ "
              "{ g,1 | c1 | b,1 | d1 | g,1 | c1 | d1 | g,1 } >>",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 2?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if every held note lasts its full length while the other voice keeps moving.",
    "Pass if you can play Evening Bells and the Hymn at sight, steadily, and Schumann's Melody after a week's practice.",
    "When you pass, move on to Unit 2.",
]
