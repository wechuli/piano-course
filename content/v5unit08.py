"""Volume 5, Unit 8: Counterpoint, ornaments and review."""

KEYBOARDS = []


def _wtc(rh, tenor, bass):
    """One bar of Bach's C major Prelude: a broken chord in the right hand, tenor and bass in the left."""
    a, b, c = rh
    half_rh = f"r8 {a}16 {b} {c} {a} {b} {c}"
    return (f"{half_rh} {half_rh}", f"<< {{ r16 {tenor}8.~ {tenor}4 r16 {tenor}8.~ {tenor}4 }} \\\\ {{ {bass}2 {bass} }} >>")


_WTC = [_wtc(*b) for b in [
    (("g'", "c''", "e''"), "e'", "c'"), (("a'", "d''", "f''"), "d'", "c'"), (("g'", "d''", "f''"), "d'", "b"),
    (("g'", "c''", "e''"), "e'", "c'"), (("a'", "e''", "a''"), "e'", "c'"), (("fis'", "a'", "d''"), "d'", "c'"),
    (("g'", "d''", "g''"), "d'", "b"), (("e'", "g'", "c''"), "c'", "b"), (("e'", "g'", "c''"), "c'", "a"),
    (("d'", "fis'", "c''"), "a", "d"), (("d'", "g'", "b'"), "b", "g"), (("e'", "g'", "cis''"), "bes", "g"),
    (("d'", "a'", "d''"), "a", "f"), (("d'", "f'", "b'"), "aes", "f"), (("c'", "g'", "c''"), "g", "e"),
    (("a", "c'", "f'"), "f", "e"), (("a", "c'", "f'"), "f", "d"), (("g", "b", "f'"), "d", "g,"),
    (("g", "c'", "e'"), "e", "c")]]


def _lines(bars, per):
    out = []
    for i, b in enumerate(bars):
        out.append(b)
        if i < len(bars) - 1:
            out.append("| \\break" if (i + 1) % per == 0 else "|")
    return " ".join(out)


INTRO = [
    "The last unit brings together the oldest and the newest skills. Baroque music is built from lines that "
    "imitate each other and from short patterns repeated a step higher or lower (sequences); it is decorated "
    "with ornaments: small signs that tell you to add quick notes around a main note. And the review exercises "
    "are sixteen bars long, in any key, with everything from this volume.",
]

NEW_IDEAS = [
    ("Sequences", "A short figure repeated a step lower (or higher) each time. Once you have read it once, read only "
                  "the first note of each repetition and let the pattern do the rest."),
    ("Imitation", "One hand plays a tune; then the other hand plays the same tune, often an octave lower, while the "
                  "first hand goes on with a new line. Look for the tune you have just played."),
    ("Ornaments", "Trill, mordent, turn and grace notes: the box of examples shows how each is played. At sight, "
                  "keep the beat first; an ornament can be left out the first time through."),
]

EXAMPLES = [
    {"title": "Ornaments: written, then played",
     "text": "Trill (tr): alternate quickly with the note above, starting on the upper note in Baroque music. "
             "Mordent (with a line): main note, the note below, main note. Short trill (no line): main note, the "
             "note above, main note. Turn: the note above, the main note, the note below, the main note.",
     "staff": "treble", "time": "4/4", "wide": True,
     "rh": "d''4\\trill c''2. | e''16 d'' e'' d'' c''2. \\bar \"||\" c''4\\mordent g'2. | c''32 b' c''16~ c''8 g'2. \\bar \"||\" "
           "c''4\\prall g'2. | c''32 d'' c''16~ c''8 g'2. \\bar \"||\" d''4\\turn c''2. | e''16 d'' c'' d'' c''2. \\bar \"||\""},
    {"title": "Grace notes: written, then played",
     "text": "A small note with a slash (acciaccatura) is crushed in just before the beat. A small note without a "
             "slash (appoggiatura) leans on the beat and takes time from the main note: usually half of it.",
     "staff": "treble", "time": "2/4",
     "rh": "\\acciaccatura d''8 c''4 r | d''32 c''8.. r4 \\bar \"||\" \\appoggiatura d''8 c''4 r | d''8 c'' r4 \\bar \"||\""},
]

TIPS = [
    "In a sequence, check the first note of each repetition and the size of the step between them.",
    "In imitation, the left hand often plays what the right hand played a bar earlier: look back as well as ahead.",
    "Ornaments are decoration. If one would break the beat, leave it out and add it when you practise.",
    "For the review, use the full scan before each exercise: key, time, the left hand's pattern, accidentals, "
    "pedal, ornaments.",
]

PART_NOTES = {
    "A": "Two-part sequences: the right hand plays a one-bar motive; the left hand imitates it while the right hand "
         "plays a counter-line, and the pair moves down a step each bar. C, G, F major and A minor.",
    "B": "Ornaments: a trill on the note before the last, mordents, turns and grace notes.",
    "C": "Review: sixteen bars in many keys and textures (held voices, chromatic notes, the pedal, 6/8, triplets, "
         "ornaments). The first eight bars end on V; bars 9-12 often repeat bars 1-4.",
}

PIECES = [
    {
        "title": "Invention No. 8", "credit": "J. S. Bach, Two-Part Invention in F, BWV 779 - the first twelve bars, "
                                         "with the last bar shortened",
        "meter": "3/4", "tempo": 72, "key": "f \\major",
        "note": "The right hand states the theme (a rising F major chord, then running sixteenths); one bar later the "
                "left hand imitates it an octave lower. From bar 4 the hands play sequences: one-bar patterns moved "
                "down a step each time. The left hand moves into the treble clef for three bars. The excerpt ends in "
                "C major, where Bach's first section closes. Source: Mutopia Project no. 61 (public domain).",
        "rh": "r8 f' a' f' c'' f' | f''8 e''16 d'' c'' d'' c'' bes' a' bes' a' g' | f'8 a' c'' a' f'' c'' | \\break "
              "a''16 c''' bes'' c''' a'' c''' bes'' c''' a'' c''' bes'' c''' | f''16 a'' g'' a'' f'' a'' g'' a'' f'' a'' g'' a'' | "
              "d''16 f'' e'' f'' d'' f'' e'' f'' d'' f'' e'' f'' | \\break b'8 g' d'' b' f'' d'' | "
              "g''16 a'' g'' f'' e'' f'' e'' d'' c'' d'' c'' bes' | a'8 d''16 c'' b' c'' b' a' g' a' g' f' | \\break "
              "e'16 f' e' d' c'8 c''16 b' c''8 e' | f'8 c'' e' c'' d' b' | c''4 r r",
        "lh": "R2. | r8 f a f c' f | f'8 e'16 d' c' d' c' bes a bes a g | f8 a c' a f' c' | "
              "\\clef treble a'16 c'' bes' c'' a' c'' bes' c'' a' c'' bes' c'' | f'16 a' g' a' f' a' g' a' f' a' g' a' | "
              "d'16 f' e' f' d' f' e' f' d' f' e' f' | \\clef bass b8 g c' g e' c' | f'16 g' f' e' d' e' d' c' b c' b a | "
              "g8 c'16 b a b a g f g f e | d16 e d c g f e f g8 g, | c4 r r",
    },
    {
        "title": "Polonaise in D minor", "credit": "From the Notebook for Anna Magdalena Bach, BWV Anh. 128 - complete",
        "meter": "3/4", "tempo": 72, "key": "d \\minor", "allow_32": True,
        "note": "A polonaise full of ornaments: mordents (the zig-zag with a line: main note, the note below, main note), "
                "trills (tr) and appoggiaturas (small notes that lean on the beat). The two thirty-second notes in bars "
                "1, 3 and 9 are a quick 'snap' up to the next note. Both halves are repeated. Source: Mutopia Project "
                "no. 1615 (public domain).",
        "rh": "\\repeat volta 2 { d''8\\mf d''16 cis'' d''4\\mordent d''32 e'' f''8. | \\appoggiatura f''16 e''16 d'' e''8 a'2 | "
              "e''8 e''16 d'' e''4\\mordent e''32 f'' g''8. | f''8 f''16 e'' f''8 f''16 e'' d''4\\mordent | \\break "
              "f''8 \\tuplet 3/2 { f''16 g'' a'' } g''8 e'' \\appoggiatura d''8 c''4 | g''8 g''16 a'' bes''8 a'' bes''4 | "
              "a''8 g''16 f'' g''4\\mordent e''4\\trill | f''8 f''16 e'' f''4\\mordent f'4 } \\break "
              "\\repeat volta 2 { a''8 a''16 g'' a''4\\mordent a''32 bes'' c'''8. | a''8 a''16 g'' a''8 a''16 g'' f''4\\mordent | "
              "c''8 bes'16 a' d''8 c'' bes'8\\trill a' | g'8 g'' \\appoggiatura f''8 e''2\\trill | \\break "
              "g'16 c'' e'' c'' g' c'' e'' c'' g' c'' e'' d'' | c''8 \\tuplet 3/2 { e''16 f'' g'' } bes'2\\mordent | "
              "\\appoggiatura c''16 bes'16 a' bes' g' a'2\\mordent | a'8. d''16 \\appoggiatura d''8 cis''2\\trill | \\break "
              "d''8. e''16 f''8 a'' d''' a'' | g''16 f'' e'' f'' d''4\\mordent d'4 }",
        "lh": "\\repeat volta 2 { d4 f d | a,4 a e | cis4 a, cis | d4 a, d, | d4 e e | c4 c e | f4 bes, c | f,2. } "
              "\\repeat volta 2 { f,4 f e | f4 c f, | a4 bes g | bes4 c' c | c4 c c | c4 e d | c4 f e | d4 a g | "
              "f4 d f | a4 d2 }",
    },
    {
        "title": "Pastorale", "credit": "Friedrich Burgmuller (1851), 25 Easy Studies, Op. 100 No. 3 - complete",
        "meter": "6/8", "tempo": 50, "tempo_unit": "4.", "key": "g \\major", "long": True,
        "note": "A shepherd's tune in 6/8 with grace notes: crush each small note in just before the main note. The "
                "left hand rocks on G major chords; in the middle section it moves into the treble clef and holds "
                "low notes under its own moving line. The first section is repeated. Source: Mutopia Project no. "
                "218 (public domain).",
        "rh": "g'8\\p( b' c'' d'' b' e'' | d''8 g'' e'' d'' b' c'' | \\break \\repeat volta 2 { d''4.) b'8( d'' "
              "\\grace fis''8 e'' | d''4. g''8) d''( b' | a'4. \\grace { a'16 b' } c''8 a' b' | g'4.) g'8( b' c'' | \\break "
              "d''4. b'8 d'' \\grace fis''8 e'' | d''4. d''8) b'( g'' | fis''4.\\< e''8\\! fis'' e'' | d''4. d'''4) r8 } \\break "
              "a''4.\\mf( c''8 e'' d'' | b'4.) d''8( cis'' d'' | a''4. c''8 e'' d'' | b'4.) d''8( e'' d'' | \\break "
              "cis''2. | d''8) ees''\\> ees'' ees''( d'' c''\\! | b'8\\> c'' d''\\! fis''\\> e'' c''\\! | b'4. a'8) d'' d'' | \\break "
              "d''4.\\p( b'8 d'' \\grace fis''8 e'' | d''4. g''8) d''( b' | a'4. \\grace { a'16 b' } c''8 a' b' | "
              "g'4.) g'8( b' c'' | \\break d''4. b'8 d'' e'' | d''4. c''8)\\>( e'' g''-.\\! | g''8\\> d'' b')\\! b'4( a'8 | "
              "g'4.)\\p \\grace b'8 a'8( e' fis' | \\break g'4.) \\grace b'8 a'8( e' fis' | g'8-.) b'-. d''-. g''-. b''-. d'''-. | "
              "g'''4\\pp r8 r4 r8",
        "lh": "R2. | R2. | \\repeat volta 2 { <g b d'>8 q q q4. | <g b d'>8 q q q4. | <g c' d'>8 q q q4. | "
              "<g b d'>8 q q q4. | <g b d'>8 q q q4. | <g b d'>8 q q q4. | \\clef treble a8( a') a' g'( a' g') | "
              "fis'8( a' fis') d'4 r8 } \\clef bass << { r8 d' d' d'4. | r8 d' d' d'4. | r8 d' d' d'4. | r8 d' d' d'4. } "
              "\\\\ { <fis c'>2. | <g b>2. | <fis c'>2. | <g b>2. } >> | \\clef treble r8 bes' bes' bes'( a' g' | "
              "fis'2.) | g'4. <c' e'>4. | << { r8 g' g' fis'4 r8 } \\\\ { d'4.~ d'4 s8 } >> | \\clef bass "
              "<g b d'>8 q q q4. | <g b d'>8 q q q4. | <g c' d'>8 q q q4. | <g b d'>8 q q q4. | <f g b d'>8 q q q4. | "
              "<e g c'>8 q q q4. | <d g b>4. d8( d' c') | <g b>8 <g b d'> q <g c' d'>4. | <g b d'>8 q q <g c' d'>4. | "
              "<g b d'>4 r8 <g b d'>4 r8 | g,4 r8 r4 r8",
    },
    {
        "title": "Prelude in C", "credit": "J. S. Bach, The Well-Tempered Clavier I, Prelude in C, BWV 846 - bars 1-19",
        "meter": "4/4", "tempo": 66,
        "note": "A whole piece made of one pattern: each bar is one chord, spread out in the same shape twice. Read it "
                "as a chord a bar: find the bass, the left hand's held note and the right hand's three notes, and let "
                "the pattern play itself. Bars 1-19 make a complete journey from C major and back. Source: Mutopia "
                "Project no. 5 (public domain).",
        "rh": _lines([b[0] for b in _WTC], 4),
        "lh": " | ".join(b[1] for b in _WTC),
    },
    {
        "title": "Prelude in C minor", "credit": "Frederic Chopin (1839), Prelude, Op. 28 No. 20 - complete",
        "meter": "4/4", "tempo": 42, "key": "c \\minor", "allow_span": 14,
        "note": "The last piece of the course: thirteen bars of solemn four-part chords. Read each chord from the bass "
                "up, and keep the dotted rhythm on beat 3 exact. A few right-hand chords stretch a ninth; roll them quickly if you must. The right hand starts in the bass clef and moves up to "
                "the treble clef; both hands change clef again in bar 8. The pedal changes with every chord (Chopin "
                "writes it out in the first bars, then 'simile': go on in the same way). Source: Mutopia Project no. "
                "472 (public domain).",
        "rh": "\\clef bass <g c' ees' g'>4\\ff <aes c' ees' aes'> << { <ees' g'>8. <d' f'>16 } \\\\ { <g b>4 } >> "
              "<ees g c' ees'>4 | <ees aes c' ees'>4 <f aes des' f'> << { <c' ees'>8. <bes des'>16 } \\\\ { <des ees g>4 } >> "
              "<c ees aes c'>4 | <d f b d'>4\\< <e g bes c' e'> << { g'8. f'16 } \\\\ { <aes c'>4 } >> <g c' ees'>4 | "
              "<fis c' d'>4 <g b d' g'> \\clef treble << { b'8. a'16 } \\\\ { <c' d' fis'>4 } >> <b d' g'>4\\! | \\break "
              "<ees' g' ees''>4\\p <ees' aes' ees''> << { <d' d''>4 } \\\\ { aes'8. fis'16 } >> <d' g' d''>4 | "
              "<c' g' c''>4 <c' d' fis' d''> <d' g' b'>8. <c' a'>16 <b d' g'>4 | "
              "<c' g' c''>4 <aes c' aes'> << { <g d'>4 } \\\\ { g'8. f'16 } >> <g c' ees'>4 | "
              "\\clef bass <ees aes c' ees'>4 <f aes des' f'> << { ees'8. d'16 } \\\\ { <f g b>4 } >> <ees g c'>4 | \\break "
              "\\clef treble <ees' g' ees''>4\\pp <ees' aes' ees''> << { <d' d''>4 } \\\\ { aes'8. fis'16 } >> <d' g' d''>4 | "
              "<c' g' c''>4 <c' d' fis' d''> <d' g' b'>8. <c' a'>16 <b d' g'>4 | "
              "<c' g' c''>4 <aes c' aes'> << { <g d'>4 } \\\\ { g'8. f'16 } >> <g c' ees'>4 | "
              "\\clef bass <ees aes c' ees'>4\\< <f aes des' f'> << { ees'8. d'16 } \\\\ { <f g b>4 } >> <ees g c'>4\\! | \\break "
              "\\clef treble <c' ees' g' c''>1->\\fermata",
        "lh": "<c, c>4\\sustainOn <f,, f,>\\sustainOff\\sustainOn <g,, g,>\\sustainOff\\sustainOn <c, g, c>\\sustainOff\\sustainOn | "
              "<aes,, aes,>4\\sustainOff\\sustainOn <des,, des,>\\sustainOff-\\markup \\italic simile <ees,, ees,> <aes,, aes,> | "
              "<g,, g,>4 <c,, c,> <f,, f,> <c, c> | <d, a, d>4 <g,, g,> <d,, d,> <g,, g,> | "
              "<c, c>4 <c c'> <b, b> <bes, bes> | <a, a>4 <aes, aes> <g, g> <f, f> | <ees, ees>4 <f, f> <b,, b,> <c, c> | "
              "<aes,, aes,>4 <des,, des,> <g,, g,> <c,, c,> | <c, c>4 <c c'> <b, b> <bes, bes> | "
              "<a, a>4 <aes, aes> <g, g> <f, f> | <ees, ees>4 <f, f> <b,, b,> <c, c> | "
              "<aes,, aes,>4 <des,, des,> <g,, g,> <c,, c,>\\sustainOn | <c g>1->\\sustainOff\\fermata",
    },
]

CHECKPOINT_TITLE = "Checkpoint: the end of the course"
CHECKPOINT = [
    "Play two review exercises (Part C) a day for two weeks, in as many keys as you can: no more than one stop "
    "each, every accidental, pedal and ornament in place.",
    "Pass if you can read the Prelude in C and the Polonaise at sight, steadily, and the Prelude in C minor after "
    "a few days.",
    "You have finished Read at Sight. Keep reading new music every day: hymn books, Bach chorales, the easier pieces "
    "of Schumann, Chopin, Grieg and Bartok. The habit is the skill.",
]
