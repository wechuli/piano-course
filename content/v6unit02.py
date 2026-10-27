"""Volume 6, Unit 2: Rhythm against rhythm."""

KEYBOARDS = []

INTRO = [
    "Until now both hands have shared one way of dividing the beat: both in eighths, or both in triplets. "
    "In much Romantic and Impressionist music the hands divide the beat differently: the right hand plays "
    "three notes while the left plays two, or the tune floats in free groups of five or seven over a steady "
    "accompaniment. This unit teaches you to feel two rhythms at once.",
    "The secret is to keep one hand completely steady (usually the accompaniment) and let the other fit "
    "around it. Practise the combinations slowly with the rhymes below until they are automatic; then read "
    "the exercises at the speed shown.",
]

NEW_IDEAS = [
    ("Two against three", "Three triplet eighths in one hand, two eighths in the other: both hands play together "
                          "on the beat; the second eighth comes exactly between the 2nd and 3rd triplet notes. "
                          "Say \"nice cup of tea\": \"nice\" together, \"cup\" triplet, \"of\" eighth, \"tea\" "
                          "triplet."),
    ("Three against four", "Triplet eighths in one hand, sixteenths in the other: together on the beat, then "
                           "the notes interlock. Say \"pass the golden butter\": \"pass\" together, then "
                           "sixteenth, triplet, sixteenth, triplet, sixteenth."),
    ("Duplets", "In 6/8 the beat is a dotted quarter, normally three eighths. A duplet (marked 2) fits two "
                "equal notes into the beat: each one lasts one and a half eighths. The left hand's three "
                "eighths go on underneath: it is two against three again."),
    ("Runs of 5, 6 and 7", "A group of 5, 6 or 7 small notes marked with its number fills one beat. Do not "
                           "count them: start the run on the beat, aim for the note after it, and arrive on time. "
                           "The left hand keeps the beat."),
    ("Hemiola", "In 3/4, two bars can suddenly move in half notes: three half notes across the two bars, the "
                "middle one tied over the bar line. The music sounds as if it were in 3/2 for a moment. Accents "
                "show it; keep counting 1-2-3 and feel the slower beat on top."),
]

EXAMPLES = [
    {"title": "Two against three",
     "text": "Right hand triplets, left hand eighths. Both hands play on each beat; the left hand's second eighth "
             "falls exactly between the second and third notes of the triplet.",
     "time": "2/4",
     "rh": "\\tuplet 3/2 { e''8 d'' c'' } \\tuplet 3/2 { d''8 e'' f'' } | e''2",
     "lh": "c8 g e g | c2"},
    {"title": "Three against four",
     "text": "Triplet eighths against sixteenths: together on the beat, then sixteenth, triplet, sixteenth, "
             "triplet, sixteenth (\"pass the golden butter\").",
     "time": "2/4",
     "rh": "\\tuplet 3/2 { g'8 a' b' } \\tuplet 3/2 { c''8 b' a' } | g'2",
     "lh": "c16 g e g c g e g | c2"},
    {"title": "A duplet in 6/8, and a run of five",
     "text": "Bar 1: the duplet (two notes in the time of three eighths) against the left hand's eighths. Bar 2: "
             "five notes fill the first beat and lead into the half note.",
     "time": "6/8",
     "rh": "\\tuplet 2/3 { a'8 b' } c''4. | \\tuplet 5/6 { d''16 c'' b' a' b' } c''4.",
     "lh": "f8 a c' f a c' | f8 a c' f4."},
    {"title": "A hemiola",
     "text": "Bars 2-3 move in three half notes, the middle one tied over the bar line. Keep counting three beats "
             "in a bar, and let the accents carry the slower pulse.",
     "time": "3/4", "key": "d \\major", "wide": True,
     "rh": "d''4 fis'' a'' | g''2-> e''4->~ | e''4 cis''2-> | d''2.",
     "lh": "d4 <fis a> <fis a> | <e g b>2 <a, cis e>4~ | <a, cis e>4 <a, e g>2 | <d a>2."},
]

TIPS = [
    "Practise each new combination with one hand tapping and the other clapping before you read it.",
    "Keep the accompaniment perfectly even; fit the other hand around it.",
    "Look at where the two hands play together: those points are your anchors.",
    "In a run, look at the note after the run first: that is where you must arrive, on the beat.",
    "In a hemiola, do not change your counting: feel the half notes against it.",
]

PART_NOTES = {
    "A": "Two against three. In half of the exercises the right hand has the tune in eighths over the left hand's "
         "triplets; in the other half the left hand has the tune and the right hand plays the triplets.",
    "B": "Duplets in 6/8 (two notes in a dotted-quarter beat) over the left hand's eighths, alternating with 2/4 "
         "exercises in which right-hand triplets meet left-hand sixteenths (three against four).",
    "C": "Runs of 5, 6 or 7 notes (two in each exercise), alternating with 3/4 waltzes that end with a hemiola in "
         "bars 6-7.",
}

PIECES = [
    {
        "title": "Arabesque No. 1", "credit": "Claude Debussy (1888-91), Arabesque No. 1, L. 66 - bars 6-12, "
                                              "with a closing chord",
        "meter": "4/4", "tempo": 63, "key": "e \\major",
        "note": "Two against three all through: the right hand's triplets float over the left hand's even eighths. "
                "Keep the left hand quiet and perfectly steady; in bars 5-7 the right hand mixes triplets with "
                "plain eighths. Four sharps: E major. Debussy's piece goes on; the excerpt closes on an E major "
                "chord. Source: Mutopia Project no. 1777 (public domain).",
        "rh": "r4 \\tuplet 3/2 { e''8(\\p fis'' cis'' } \\tuplet 3/2 { e''8 b' cis'' } \\tuplet 3/2 { gis'8 b' fis' } | "
              "\\tuplet 3/2 { gis'8 e' gis' } dis'2 cis'4 | "
              "b8) r \\tuplet 3/2 { e''8( fis'' cis'' } \\tuplet 3/2 { e''8 b' cis'' } \\tuplet 3/2 { gis'8 b' fis' } | "
              "\\tuplet 3/2 { gis'8 e' gis' } dis'2 cis'4) | \\break "
              "\\tuplet 3/2 { b8( a b } cis'4~ cis'8 e' dis' e' | cis'4) gis'2( e'4) | "
              "\\tuplet 3/2 { dis'8( cis' dis' } e'4~ e'8 gis' fis' gis') | <gis b e'>1\\fermata",
        "lh": "e,8(\\pp b, e gis b gis e b,) | e,8( cis e gis cis' gis e b,) | e,8( b, e gis b gis e b,) | "
              "e,8( cis e gis cis' gis e b,) | fis,8(\\< cis e fis a fis e cis)\\! | gis,8( cis e gis b gis e cis) | "
              "a,8( e fis a cis' a fis e) | <e, b,>1\\fermata",
    },
    {
        "title": "Nocturne in E-flat", "credit": "Frederic Chopin (1830-32), Nocturne Op. 9 No. 2 - the first "
                                                "phrase",
        "meter": "12/8", "tempo": 44, "tempo_unit": "4.", "key": "ees \\major", "upbeat": "1/8", "allow_32": True,
        "note": "12/8: four beats of three eighths. The left hand keeps an even bass-and-chord pattern of eighths "
                "while the tune sings freely above it. In bar 2 the four quick notes are Chopin's turn written out "
                "(D-flat, C, B-natural, C, all in the time of one eighth); in bar 4 the sixteenths make two notes "
                "against each eighth of the left hand. Count four slow beats, not twelve. The excerpt ends with the "
                "first phrase. Notes retyped from the Mutopia Project engraving no. 1590 (Creative Commons "
                "Attribution-ShareAlike 3.0).",
        "rh": "\\partial 8 bes'8\\p | g''4.~ g''8 f''( g'' f''4. ees''4) bes'8( | "
              "g''4 des''32 c'' b' c'' c'''4 g''8 bes''4. aes''4 g''8) | \\break "
              "f''4. g''4( d''8) ees''4. c''4. | bes'8( d''') c'''( bes''16 aes'' g'' aes'') c''16( d'' ees''4.) r4.",
        "lh": "\\partial 8 r8 | ees,8 <g ees'>( <bes ees' g'>) ees <aes d'>( <ces' d' aes'>) ees, <g ees'>( <bes ees' g'>) "
              "d, <g ees'>( <bes ees' g'>) | "
              "c,8 <g e'>( <bes e' g'>) c <g e'>( <c' e' bes'>) f, <f des'>( <bes des' e'>) f, <f c'>( <aes c' f'>) | "
              "bes,8 <f d'>( <bes d' aes'>) b, <g f'>( <d' f' g'>) c <g ees'>( <c' ees' g'>) a, <ges ees'>( <c' ees' ges'>) | "
              "bes,8 <f ees'>( <bes ees' aes'>) bes,, <f d'>( <bes aes'>) ees, <g ees'>( <bes ees' g'>) <ees, ees>4.",
    },
    {
        "title": "Solace", "credit": "Scott Joplin (1909), Solace: A Mexican Serenade - the first strain",
        "meter": "2/4", "tempo": 60, "key": "c \\major",         "note": "A habanera: the left hand plays a dotted eighth, a sixteenth and two eighths in every bar, while the "
                "right hand's sixteenths are tied over the middle of the bar. The two rhythms never coincide after "
                "the first note: keep the left hand's pattern steady and fit the right hand's ties against it. "
                "Joplin marks it \"very slow march time\". Joplin writes each bass note held under the chord (for the pedal); here it is printed as the eighth the hand actually plays. Source: Mutopia Project no. 482 (public domain).",
        "rh": "b'16(\\mf bes' a' g'~ g' gis' a' ais') | b'16( <d'' f''> <cis'' g''> <d'' f''>)~ <d'' f''>( <cis'' g''> <d'' f''> b') | "
              "c''16( b' a' g')~ g'( gis' a' b') | c''16( <e'' g''> <dis'' a''> <e'' g''>)~ <e'' g''>( <dis'' a''> <e'' g''> cis'') | \\break "
              "d''16( f'' a'' <f'' d'''>)~ <f'' d'''> f''( e'' d'')~ | d''16 <c' d' aes'>8 <b d' g'>16~ <b d' g'>8( d'') | "
              "c''16( e'' g'' <e'' c'''>)~ <e'' c'''> e''( d'' c'')~ | c''16 <c' fis'>8 <c' e' g'>16~ <c' e' g'>8( c'') | \\break "
              "b'16( bes' a' g'~ g' gis' a' ais') | b'16( <d'' f''> <cis'' g''> <d'' f''>)~ <d'' f''>( <cis'' g''> <d'' f''> b') | "
              "c''16( b' a' g'~ g' gis' a' b') | c''16( <e'' g''> <dis'' a''> <e'' g''>)~ <e'' g''>( <dis'' a''> <e'' g''> bes') | \\break "
              "a'16 <f'' a''>8 <c'' f'' a'' c'''>16~ <c'' f'' a'' c'''>(\\< <b' b''> <c'' c'''> <d'' d'''>)\\! | "
              "<dis'' a'' c''' dis'''>4->~ <d'' a'' c''' d'''>8( <aes' c'' f'' aes''>) | "
              "<g' c'' e'' g''>4~ <g' c'' e'' g''>16 <d'' f'' d'''>8( <e'' g'' e'''>16) | <c'' e'' c'''>4 e''16( d'' c''8)",
        "lh": "d8. g16 <b f'>8 d | g,8. g16 <b f'>8 dis | "
              "e8. g16 <c' e'>8 g | c8. g16 <c' e'>8 e | "
              "d8. f16 <d' f'>8 a | f8 f d16( e f8) | "
              "e8. g16 <c' e'>8 g | dis8( e) c16( d e ees) | "
              "d8. g16 <b f'>8 d | g,8. g16 <b f'>8 dis | "
              "e8. g16 <c' e'>8 g | c8. g16 <c' e'>8 c | "
              "f8. a16 <c' f'>8 a | fis'4->( f') | "
              "r16 e( f fis) g8 g, | <c c'>4 r",
    },
    {
        "title": "Hemiola Waltz", "credit": "Original, written for this book",
        "meter": "3/4", "tempo": 104, "key": "d \\major",
        "note": "A waltz with two hemiolas. In bars 7-8 and 13-14 the music moves in three half notes across two bars "
                "(the accents show them; the middle one is tied over the bar line): the first time it stops on "
                "A, the dominant, the second time it leads home to D. Keep counting three in a bar and let the "
                "half notes sound broad and slow.",
        "rh": "d''4\\mp fis'' a'' | g''2 b'4 | cis''4 e'' g'' | fis''2. | a''4 fis''8 e'' d''4 | b'4 d''8 e'' g''4 | "
              "d''2-> b'4->~ | b'4 a'2-> | \\break "
              "d''4\\mf fis'' a'' | b''4 g'' d'' | fis''4 d'' b' | e''2 g''4 | g''2-> e''4->~ | e''4 cis''2-> | "
              "d''4 a' fis' | d'2.",
        "lh": "d4 <fis a> <fis a> | g,4 <b, d> <b, d> | a,4 <cis g> <cis g> | d4 <fis a> <fis a> | d4 <fis a> <fis a> | "
              "g,4 <b, d> <b, d> | <b, d g>2 <e gis d'>4~ | <e gis d'>4 <a, cis e>2 | "
              "d4 <fis a> <fis a> | g,4 <b, d> <b, d> | b,4 <d fis> <d fis> | g,4 <b, d> <b, d> | "
              "<e g b>2 <a, cis e>4~ | <a, cis e>4 <a, e g>2 | d4 <fis a> <fis a> | <d, a,>2.",
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if the hands keep their own rhythms: the triplets stay even against the eighths, the duplets are equal, "
    "and every run arrives on the beat.",
    "Pass if you can play the Hemiola Waltz at sight and the Arabesque excerpt after a few days.",
    "When you pass, move on to Unit 3.",
]
