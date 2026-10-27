"""Volume 6, Unit 6: Accompanying."""

KEYBOARDS = []

INTRO = [
    "Most pianists who read at sight do it for someone else: a singer, a violinist, a choir. The score then has "
    "three staves: the soloist's line on top (smaller, or with words under it) and the two piano staves "
    "below. The pianist plays the piano part and reads the soloist's line at the same time, to know where the "
    "music is going, to breathe with the soloist, and to wait at a pause.",
    "In this unit the singer's line is sung to \"la\" in the exercises, and to the poet's words in the songs. "
    "Read the top line as part of the music, not as decoration: it is the tune your accompaniment supports.",
]

NEW_IDEAS = [
    ("The soloist's staff", "The top staff, joined to the piano by a bar line or a separate bracket, is the "
                            "soloist's. The piano's two staves are joined by the brace. Your hands play only the "
                            "braced staves; your eyes read all three."),
    ("Introductions and interludes", "When the soloist rests, the piano leads: the introduction sets the speed "
                                     "and the mood, an interlude joins two phrases. Play them in time, and give "
                                     "the soloist a clear beat to come in on."),
    ("After-beats", "A bass note on the beat and chords on the off-beats (oom-pah, oom-pah-pah) keep a song "
                    "moving. Keep the chords light and the bass clear."),
    ("Doubling the tune", "In some bars the piano's top note plays the singer's tune; in others it does not. "
                          "Where it doubles, play it gently: the singer has it already."),
    ("Following the soloist", "At a pause (fermata) in the voice, the pianist waits and watches; a rest in the "
                              "voice is counted exactly. Breathe with the singer at the ends of phrases."),
]

EXAMPLES = [
    {"title": "An introduction, then an after-beat accompaniment",
     "text": "Two bars of piano set the speed; the voice (top line in the songs) comes in on bar 3. Bass on the beat, "
             "chords after it.",
     "time": "3/4", "key": "g \\major", "wide": True,
     "rh": "r4 <b d' g'>4 <b d' g'> | r4 <c' d' fis'>4 <c' d' fis'> | r4 <b d' g'>4 <b d' g'>",
     "lh": "g,4 r r | d4 r r | g,4 r r"},
]

TIPS = [
    "Before you play, read the soloist's line: where does it rest, where does it pause, where is its high note?",
    "Count the soloist's rests aloud in your head; come in with the soloist, not after.",
    "Keep the accompaniment softer than the tune: the singer must be heard.",
    "At a fermata in the voice, hold your chord and watch for the next breath.",
    "If you must simplify, keep the bass and the rhythm of the accompaniment; drop inner notes.",
]

PART_NOTES = {
    "A": "A singer's line (sung to \"la\") above block chords on every beat, the bass in long notes. 4/4 and 3/4. "
         "The singer breathes (a quarter rest) in bar 4.",
    "B": "Two bars of piano introduction, the first phrase, a bar of piano interlude, the second phrase. 3/4 "
         "exercises use an after-beat accompaniment, 4/4 exercises broken chords in eighths.",
    "C": "In bars 3-4 and 7-8 of the singer's line the piano's right hand doubles the tune; in the other bars it "
         "plays chords. A bar of interlude in the middle: count the singer's rests.",
}

PIECES = [
    {
        "title": "Heidenroslein", "credit": "Franz Schubert (1815), Heidenroslein D. 257 (words by Goethe) - the "
                                             "first verse",
        "meter": "2/4", "tempo": 69, "key": "g \\major",
        "note": "A singer's line over a light after-beat accompaniment (rests on the beat, chords after it). The "
                "singer's paired sixteenths (beamed together) carry one syllable each. Bars 10 and 12 have "
                "pauses: the piano waits for the singer. The last two bars are the piano's postlude, with two "
                "grace notes. Words: \"A boy saw a little rose on the heath ...\" Source: Mutopia Project no. "
                "1555 (public domain).",
        "staves": [
            {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
             "music": "\\autoBeamOff b'8 b' b' b' | d''16[ c''] c''[ b'] a'4 | a'8 a' b' c'' | d''4 g''8 r | \\break "
                      "b'8 b' b' b' | d''16[ cis''] cis''[ b'] a'4 | d''8 d'' e''8. d''16 | cis''16[ d''] e''[ fis''] d''4 | \\break "
                      "d''16[ fis''] e''[ d''] cis''[ b'] ais'[ b'] | g''8.[ cis''16] d''4\\fermata | a'8 a' b' c''! | "
                      "d''8 e''16[ fis''] g''4\\fermata | \\break e''8 g'' c'' e'' | g'8[ b'16 a'] g'4 | R2 | R2",
             "lyrics": "Sah ein Knab ein Rös -- lein stehn, Rös -- lein auf der Hei -- den, War so jung und mor -- gen -- "
                       "schön, Lief er schnell, es nah zu sehn, Sah's mit vie -- len Freu -- den. Rös -- lein, Rös -- "
                       "lein, Rös -- lein rot, Rös -- lein auf der Hei -- den."},
            {"name": "up", "clef": "treble", "hand": "rh",
             "music": "r8 <d' g' b'> r <d' g' b'> | r8 <e' a' c''> r <e' a' c''> | r8 <d' a' c''> r <d' fis' a'> | "
                      "r8 <d' g' d''> r <d' g' b'> | r8 <d' g' b'> r <d' g' b'> | r8 <e' a' cis''> r <e' a' cis''> | "
                      "r8 <a' d''> r <b' e''> | r8 <g' cis''> r <fis' d''> | r8 <a' d''> r <b' e''> | "
                      "r8 <g' cis''> r <fis' d''>\\fermata | r8 <fis' a'> r <d' fis' a'> | r8 <d' g' d''> r <d' g' b'>\\fermata | "
                      "r8 <e' g' c''> r <c' g' c''> | <g' b'>8( <fis' a'>) g'16-. b'( c'' d'') | "
                      "<< { e''8-. \\appoggiatura e''16 g''8( c''-.) \\appoggiatura c''16 e''8( | g'8-.) a'16.( b'32) g'4 } "
                      "\\\\ { s2 | g'8 fis'( g'4) } >>"},
            {"name": "down", "clef": "bass", "hand": "lh",
             "music": "g8 r g r | g8 r g r | fis8 r c r | b,8 r g, r | g8 r g r | g8 r g r | fis8 r g r | a8 r b r | "
                      "fis8 r g r | a8 r d r\\fermata | d8 r c! r | b,8 r g,4\\fermata | c8 r e r | "
                      "<< { d'8( c') b16 s8. } \\\\ { d4( g16) g( a b) } >> | c'8-. \\appoggiatura c'16 e'8( a-.) "
                      "\\appoggiatura a16 c'8( | <d b>8-.) <d c'>( <g b>4)"},
        ],
        "allow_32": True,
    },
    {
        "title": "An die Musik", "credit": "Franz Schubert (1817), An die Musik D. 547 (words by Franz von Schober) - "
                                           "the first verse",
        "meter": "2/2", "cut": True, "tempo": 36, "tempo_unit": "2", "key": "d \\major",
        "note": "\"To music\": a hymn of thanks. The piano's right hand repeats its chords in eighths while the "
                "left hand's bass line sings against the voice (in bars 7-18 it moves in long notes, often by "
                "half steps). Two bars of introduction; the voice rests in bar 10 (count it) and the piano closes "
                "the verse alone. Words: \"You lovely art, in how many grey hours ... you have carried me into a "
                "better world.\" Source: Mutopia Project no. 1001 (public domain).",
        "staves": [
            {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
             "music": "R1 | R1 | r4 a' d'' d'' | fis'2. b'4 | \\appoggiatura b'8 d'4. d'8 fis'8( e') d'( e') | "
                      "fis'4 d' r2 | \\break r4 a' b' b' | cis'4. cis'8 d'4. d'8 | fis'8( e') d'( e') fis'2 | R1 | "
                      "r4 d'' e''4. g'8 | \\break fis'4( a'2) b'8( cis'') | d''4. fis''8 e''( cis'') a'( g') | "
                      "\\appoggiatura g'8 fis'4 fis' r a' | b'4. b'8 b'4 cis''8( d'') | \\break d''4. d''8 fis''4. e''8 | "
                      "\\appoggiatura e''4 d''2 r8 b' cis'' d'' | d''4( fis'8) fis' a'4( cis'8) cis' | d'2 r2 | \\break "
                      "R1 | R1 | R1 | R1",
             "lyrics": "Du hol -- de Kunst, in wie -- viel grau -- en Stun -- den, Wo mich des Le -- bens wil -- der "
                       "Kreis um -- strickt, Hast du mein Herz zu war -- mer Lieb ent -- zun -- den, Hast mich in "
                       "ei -- ne beß -- re Welt ent -- rückt, in ei -- ne beß -- re Welt ent -- rückt."},
            {"name": "up", "clef": "treble", "hand": "rh",
             "music": "<a d' fis'>8\\p <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> | "
                      "<a d' a'>8-> <a d' a'> <a d' a'> <a d' a'> <a cis' g'> <a cis' g'> <g a cis' e'> <g a cis' e'> | "
                      "<fis a d'>8 <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> | "
                      "<a d' fis'>8 <a d' fis'> <a d' fis'> <a d' fis'> <fis d' fis'> <fis d' fis'> <b d' fis'> <b d' fis'> | "
                      "r8 <a d' fis'> <a d' fis'> <a d' fis'> r <a cis' g'> <a cis' g'> <a cis' g'> | "
                      "r8 <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> <a d' fis'> | "
                      "<a d' a'>8 <a d' a'> <a d' a'> <a d' a'> <b d' b'> <b d' b'> <b d' b'> <b d' b'> | "
                      "\\clef bass r8 <e g cis'> <e g cis'> <e g cis'> r <d fis d'> <d fis d'> <d fis d'> | \\clef treble "
                      "r8 <g a e'> <g a e'> <g a e'> r <fis a fis'> <fis a fis'> <fis a fis'> | "
                      "<a cis' e'>8 <a cis' e'> <a cis' a'> <a cis' a'> <b d' a'> <b d' a'> <cis' e' a'> <cis' e' a'> | "
                      "<d' fis' a'>8 <d' fis' a'> <d' fis' a'> <d' fis' a'> <e' g' a'> <e' g' a'> <e' g' a'> <e' g' a'> | "
                      "<d' fis' a'>8 <d' fis' a'> <cis' e' a'> <cis' e' a'> <b d' a'> <b d' a'> <cis' e' a'> <cis' e' a'> | "
                      "<d' fis' a'>8 <d' fis' a'> <d' fis' a'> <d' fis' a'> <e' g' a'> <e' g' a'> <e' g' a'> <e' g' a'> | "
                      "r8 <a d' fis'> <a d' fis'> <a d' fis'> <a cis' g'> <a cis' g'> <c' d' a'> <c' d' a'> | "
                      "r8 <b d' b'> <b d' b'> <b d' b'> r <d' f' b'> <d' f' b'> <d' f' b'> | "
                      "r8 <d' fis' a'> <d' fis' a'> <d' fis' a'> r <e' fis' cis''> <e' fis' cis''> <e' g' cis''> | "
                      "r8 <d' fis' d''> <d' fis' d''> <d' fis' d''> r <d' f' b'> <d' f' b'> <d' f' b'> | "
                      "r8 <d' fis' a'> <d' fis' a'> <d' fis' a'> r <g a cis'> <g a cis'> <g a cis'> | "
                      "<fis a d'>8 <d' fis' d''> <d' fis' d''> <d' fis' d''> <d' fis' d''> <d' fis' d''> <e' g' cis''> <fis' a' d''> | "
                      "<< { <a' cis''>8->( <g' b'>) <d' g' b'>-. <d' g' b'>-. <d' g' b'> <b g' b'> <d' g' b'> <e' g' b'> } \\\\ { d'4 s2. } >> | "
                      "<g' b'>8( <a fis' a'>) <a fis' a'>-. <a fis' a'>-. <a fis' a'> <a fis' a'> <cis' fis' a'> <d' fis' a'> | "
                      "<< { <dis' fis' a'>8->( <e' g'>) <b e' g'>-. <b e' g'>-. <cis' e' g'>->( <g a cis' e'>) <g a cis' e'>-. <g a cis' e'>-. } \\\\ { b4 s2. } >> | "
                      "<g a cis' e'>8->( <fis a d'>) <fis a d'>-. <fis a d'>-. <fis a d'>4 r4"},
            {"name": "down", "clef": "bass", "hand": "lh",
             "music": "r4 a,( d) d-. | fis,2 a,4-. a,,-. | d,4 r r2 | r4 fis,( b,) gis,-. | a,4 r a, r | d4-. a,( d) d-. | "
                      "fis,2( g,) | a,4( ais, b,2) | cis2( d) | a,4( a gis g) | fis4( d cis a,) | d4( a,8 a gis4 g) | "
                      "fis4( d cis4. a,8) | d2( e4 fis) | g2( gis) | a2( ais) | b2( gis) | a2( a,) | d4 r r2 | "
                      "<g,, g,>2 r8 g,-. b,-. cis-. | <d, d>2 r8 d-. e-. fis-. | <g, g>2 a, | <d, d>2. r4"},
        ],
    },
    {
        "title": "Ich liebe dich", "credit": "Edvard Grieg (1864), Ich liebe dich Op. 5 No. 3 (German words by F. von "
                                             "Holstein) - the verse, from bar 3",
        "meter": "3/4", "tempo": 60, "key": "bes \\major", "allow_span": 14,
        "note": "\"I love you\": a romantic song in which the piano breathes with the singer. The right hand's chords "
                "move in eighths, the left hand sings its own line (bars 2 and 9) and holds long basses with the "
                "pedal. From bar 11 the music grows (cresc. sempre) to the top of the phrase in bar 15; then a "
                "short ritardando. The excerpt starts with the singer's first upbeat and ends with the song's "
                "last bar. Source: Mutopia Project no. 586 (public domain).",
        "staves": [
            {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
             "music": "\\autoBeamOff \\dynamicUp r4 r8 f'8\\p fis' a' | a'8 g' d' e' f'! g' | f'4 ees'! r | r4 d'\\pp ees'8 f' | "
                      "g'8 d' bes'4. g'8 | \\break d''8.\\f g'16 g'4 r | R2. | r4 r8 f'\\p fis' a' | a'8 g' d' e' f'! g' | "
                      "f'4 ees'! r8 ees' | \\break g'8. d'16 d'4 r8 g' | bes'8. g'16 g'4 r8 bes' | d''8. g'16 g'8 g' a' bes' | "
                      "d''8. c''16 c''4 r8 c''\\ff | \\break ees''8. ges'16 ges'8 f' a' d'' | c''8. bes'16 bes'4 r | R2. | R2. | "
                      "r4 r8\\fermata",
             "lyrics": "Du mein Ge -- dan -- ke, du mein Sein und Wer -- den! Du mei -- nes Her -- zens er -- ste "
                       "Se -- lig -- keit! Ich lie -- be dich wie nichts auf die -- ser Er -- den, ich lie -- be dich, "
                       "ich lie -- be dich, ich lie -- be dich in Zeit und E -- wig -- keit! Ich lie -- be dich in "
                       "Zeit und E -- wig -- keit!"},
            {"name": "up", "clef": "treble", "hand": "rh",
             "music": "<d' bes'>8 <bes d'> <bes d'> <bes d'> <bes d'> <bes d'> | "
                      "<bes d'>8 <bes d'> <bes d'> <bes d'> <a c'> <aes d'> | "
                      "<g c' f'>8 <g c' f'> <g c' ees'> <g c' ees'> <fis a ees'> <fis a ees'> | "
                      "<f b ees'>8 <f b ees'> <f b d'> <f b d'> <f b d'> <f b d'> | <e bes d'>8 <e bes d'> <e bes d'> <e bes d'> <e bes d'> <e bes d'> | "
                      "r8 <f' bes' g''> <f' bes' g''> <f' bes'> <f' c''> <f' d''> | "
                      "<< { d''8. c''16 <ees' c''>4.( f'8) } \\\\ { r8 ees' aes' g' ges' ees' } >> | "
                      "<< { r4 r8 f' fis' a' } \\\\ { r8 <bes d'> <bes d'> <bes d'> <bes d'> <bes d'> } >> | "
                      "<bes d' a'>8 <bes d' g'> <bes d'> <bes d' e'> <bes c' f'!> <aes d' g'> | "
                      "<g c' f'>8 <g c' f'> <g c' ees'!> <g c' ees'> <fis a ees'> <fis a ees'> | "
                      "<f b ees'>8 <f b ees'> <f b d'> <f b d'> <f b d'> <f b d'> | <e bes d'>8 <e bes d'> <e bes d'> <e bes d'> <e bes d'> <e bes d'> | "
                      "r8 <f' bes' g''> <f' bes' g''> <f' bes'> <f' c''> <f' d''> | "
                      "r8 <ees' g' ees''> <ees' g' ees''> <ees' g' ees''> <ees' g' ees''> <ees' g' ees''> | "
                      "r8 <ees' ges' bes' ees''> <ees' ges' bes' ees''> <ees' f' bes' ees''> <ees' f' a' ees''>4 | "
                      "r8 <bes d' f'> <bes d' f'> <bes d' f'> <bes d' fis'> <bes d' a'> | "
                      "<bes d' a'>8 <bes d' g'> <bes d'> <bes d' e'> <a c' f'> <aes d' g'> | "
                      "<g c' f'>4\\arpeggio r <ees a ees'>\\arpeggio | <d f bes d'>4\\arpeggio~ <d f bes d'>8\\fermata"},
            {"name": "down", "clef": "bass", "hand": "lh",
             "music": "<bes, f>4 r8 f fis a | a8 g d e f! b, | c2. | g,2. | g,2. | "
                      "c,8\\sustainOn <c bes d'> <c bes d'> <c bes d'> <c a c'>\\sustainOff <c g bes> | "
                      "<< { s8 bes fis g aes a } \\\\ { <f,, f,>8\\sustainOn <c f>~ c4.\\sustainOff f8 } >> | "
                      "<bes,, f,>4 r8 f fis a | a8 g d e f! b, | c2. | g,2. | g,2. | "
                      "c,8\\sustainOn <c bes d'> <c bes d'> <c bes d'> <c a c'>\\sustainOff <c g bes> | "
                      "f,8\\sustainOn <c g bes> <c g bes> <c g bes> <c g bes> <c g bes>\\sustainOff | "
                      "<f,, f,>8\\sustainOn <c ges bes> <c ges bes> <c ges bes>\\sustainOff <c f a!>4 | "
                      "<bes,, f,>8\\sustainOn f f f fis\\sustainOff a | a8 g d e f! b, | c4 r <f, c>\\arpeggio | "
                      "<bes,, f, bes,>4\\arpeggio~ <bes,, f, bes,>8\\fermata"},
        ],
    },
    {
        "title": "Evening Song", "credit": "Original, written for this book",
        "meter": "4/4", "tempo": 66, "key": "f \\major",
        "note": "A song for a singer and a pianist, to be played with a friend if you can (or sing the top line while "
                "you play). Two bars of introduction in broken chords; the singer comes in on bar 3. In bar 8 the "
                "singer holds a pause (fermata): the pianist holds the chord, watches, and starts bar 9 with the "
                "singer's next breath.",
        "staves": [
            {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
             "music": "R1 | R1 | c''4\\mp a'8 bes' c''4 f'' | e''4. d''8 c''2 | \\break d''4 bes'8 c'' d''4 g'' | "
                      "f''2 e''4 r | a'4 c''8 a' g'4 bes' | a'2\\fermata r2 | \\break g'4 a'8 bes' c''4 e'' | "
                      "f''2( d''4) bes' | a'4. g'8 c''4 e' | f'1",
             "lyrics": "la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la "
                       "la la"},
            {"name": "up", "clef": "treble", "hand": "rh",
             "music": "f'8\\p a' c'' a' f' a' c'' a' | e'8 g' bes' g' e' g' bes' g' | f'8 a' c'' a' f' a' c'' a' | "
                      "e'8 g' bes' g' e' g' bes' g' | d'8 f' bes' f' d' f' bes' f' | c'8 f' a' f' c' e' g' e' | "
                      "c'8 f' a' f' c' e' g' bes' | <c' f' a'>2\\fermata r2 | e'8 g' bes' g' e' g' bes' g' | "
                      "d'8 f' bes' f' d' f' bes' f' | c'8 f' a' f' c' e' g' bes' | <c' f' a'>1"},
            {"name": "down", "clef": "bass", "hand": "lh",
             "music": "f,1 | c1 | f,1 | c1 | bes,1 | a,2 c | f,2 c | f,2\\fermata r2 | c1 | bes,1 | c2 c, | <f, c>1"},
        ],
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speed shown, with no more than one stop each, reading the "
    "singer's line as you go.",
    "Pass if every introduction and interlude is in time, and you can say at any moment which word or note the "
    "singer has reached.",
    "Pass if you can play Heidenroslein and the Evening Song at sight (with a singer if possible), and An die "
    "Musik after a few days.",
    "When you pass, move on to Unit 7.",
]
