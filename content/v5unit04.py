"""Volume 5, Unit 4: Triplets and new time signatures."""

KEYBOARDS = []


def _tri(a, b, c):
    """A triplet shared between the hands: the first two notes on the bass staff, the third on the treble."""
    return f'\\tuplet 3/2 {{ \\change Staff = "down" {a}8 {b} \\change Staff = "up" {c} }}'


def _bars(*bars):
    return " | ".join(" ".join(_tri(*t) for t in bar) for bar in bars)


def _ch(top="g'", n=3):
    """Three repeated chords on C and E-flat (Ballade)."""
    c = f"<c' ees' {top}>8"
    return f"{c}-. {c}-. {c}" if top == "g'" else f"{c}-. {c}-. {c}-."


def _lines(bars, per):
    """Join bars, with a line break every `per` bars."""
    out = []
    for i, b in enumerate(bars):
        out.append(b)
        if i < len(bars) - 1:
            out.append("| \\break" if (i + 1) % per == 0 else "|")
    return " ".join(out)


INTRO = [
    "Two new ways of counting. A triplet squeezes three notes into the time of two: three eighth notes in one "
    "beat, marked with a small 3. And four new time signatures: 3/8 (one beat in a bar, three eighths), 9/8 and "
    "12/8 (three and four dotted-quarter beats), and 2/2, which counts two half-note beats in a bar and is "
    "often written as a C with a line through it (alla breve, 'cut time').",
]

NEW_IDEAS = [
    ("Triplets", "Three eighth notes with a 3 above or below them fill one quarter-note beat. Count "
                 "'1-trip-let 2-trip-let'. A triplet can also be a quarter and an eighth (long-short)."),
    ("3/8", "Three eighths in a bar, felt as one beat. Count 'one-and-a', one bar at a time. Für Elise is in 3/8."),
    ("9/8 and 12/8", "Like 6/8, but with three or four dotted-quarter beats in a bar. Look for the groups of three "
                     "eighths: each group is one beat."),
    ("2/2 (alla breve)", "Four quarter notes in a bar, as in 4/4, but counted in two half-note beats. The metronome "
                         "mark is for the half note. The sign is a C with a vertical line."),
]

EXAMPLES = [
    {"title": "Triplets in 4/4",
     "text": "Beats 1 and 3 have triplets; beat 2 has two ordinary eighths; beat 4 is a triplet quarter and eighth.",
     "staff": "treble", "time": "4/4",
     "rh": "\\tuplet 3/2 { c''8 d'' e'' } d''8 c'' \\tuplet 3/2 { b'8 c'' d'' } \\tuplet 3/2 { c''4 g'8 } | c''1 \\bar \"||\""},
    {"title": "3/8, 9/8 and 12/8",
     "text": "Each group of three eighths is one beat: one beat in 3/8, three in 9/8, four in 12/8.",
     "staff": "treble", "time": "3/8",
     "rh": "c''8 d'' e'' | f''4. \\bar \"||\" \\time 9/8 e''4. d''4 c''8 g'4. \\bar \"||\" "
           "\\time 12/8 c''8 d'' e'' f''4 e''8 d''4. c''4. \\bar \"||\""},
    {"title": "2/2: alla breve",
     "text": "The same notes as 4/4, counted in two: 'one - two -'.",
     "staff": "treble", "time": "2/2",
     "rh": "\\once \\override Staff.TimeSignature.style = #'C c''4 d'' e'' f'' | g''2 e'' | c''1 \\bar \"||\""},
]

TIPS = [
    "Before you play, find the time signature and decide what one beat is: a quarter, a dotted quarter or a half.",
    "Count triplets 'trip-let' only where they are; elsewhere count ordinary eighths 'and'.",
    "In 3/8, feel one strong beat per bar and read four bars at a time, like one bar of 12/8.",
    "In 2/2, set the metronome to the half note and keep the quarters light.",
]

PART_NOTES = {
    "A": "Triplets in the right hand over held chords (4/4) and waltz basses (3/4).",
    "B": "3/8 (one beat, waltz bass) and 9/8 (three dotted-quarter beats, broken chords). The metronome beats "
         "dotted quarters.",
    "C": "2/2 (two half-note beats; the metronome beats half notes) and 12/8 (four dotted-quarter beats).",
}

PIECES = [
    {
        "title": "Rowing Song", "credit": "Original", "meter": "12/8", "tempo": 52, "tempo_unit": "4.",
        "key": "f \\major",
        "note": "Four dotted-quarter beats in each bar: the left hand rows in groups of three eighths, one group to "
                "a beat. Count '1-and-a 2-and-a 3-and-a 4-and-a'.",
        "rh": "c''4.\\p a'4 c''8 f''4. e''4 d''8 | d''4. bes'4 d''8 c''4. a'4. | bes'4. g'4 bes'8 e''4. c''4. | "
              "a'4. c''4 a'8 f'2. | \\break c''4.\\mf f''4 c''8 a''4. g''4 f''8 | d''4. f''4 d''8 bes'4. d''4. | "
              "c''4.\\> a'4 f'8 g'4. e'4. | f'1.\\p",
        "lh": "f,8 c a f, c a f, c a f, c a | bes, d f bes, d f f, c a f, c a | c e g c e g c e g c e g | "
              "f,8 c a f, c a f, c a f, c a | f,8 c a f, c a f, c a f, c a | bes, d f bes, d f bes, d f bes, d f | "
              "f,8 c a f, c a c e g c e g | <f, c f>1.",
    },
    {
        "title": "Für Elise", "credit": "Ludwig van Beethoven (1810), Bagatelle in A minor, WoO 59 - the opening theme",
        "meter": "3/8", "tempo": 60, "tempo_unit": "4.", "key": "a \\minor", "upbeat": "1/8",
        "note": "3/8: feel one beat in each bar. The tune starts on an upbeat and passes from the right hand to the "
                "left and back: the left hand's broken chords (A minor and E major, with G-sharp) lead into the "
                "right hand's next notes. D-sharp is a chromatic neighbour of E. Play the theme twice. Pedal "
                "marks are left out until Unit 7. Source: Mutopia Project no. 931 (public domain).",
        "rh": "\\repeat volta 2 { \\partial 8 e''16\\pp dis'' | e'' dis'' e'' b' d'' c'' | a'8 r16 c' e' a' | "
              "b'8 r16 e' gis' b' | c''8 r16 e' e'' dis'' | \\break e'' dis'' e'' b' d'' c'' | a'8 r16 c' e' a' | "
              "b'8 r16 e' c'' b' | a'4 }",
        "lh": "\\repeat volta 2 { \\partial 8 r8 | R4. | a,16 e a r r8 | e,16 e gis r r8 | a,16 e a r r8 | R4. | "
              "a,16 e a r r8 | e,16 e gis r r8 | a,16 e a r }",
    },
    {
        "title": "Of Foreign Lands and Peoples",
        "credit": "Robert Schumann (1838), Scenes from Childhood, Op. 15 No. 1 - first part",
        "meter": "2/4", "tempo": 80, "key": "g \\major", "allow_span": 16,
        "note": "The tune (stems up) floats over triplets that are shared between the hands: the left hand plays the "
                "first two notes of each triplet (the beam crosses to the bass staff), the right hand the third. "
                "The left hand also plays the bass on the beat. C-sharp and B-flat are chromatic. Play the passage "
                "twice. Source: Mutopia Project no. 354 (public domain).",
        "rh": "\\repeat volta 2 { << { b'4\\p( g'' | fis''8. e''16 d''4) | b'4( g'' | fis''8. e''16 d''4) | \\break "
              "b'4( g'' | e''8. d''16 c''4 | a'4 d'' | b'2) } \\\\ { "
              + _bars([("b", "d'", "g'"), ("bes", "e'", "g'")], [("a", "d'", "fis'"), ("c'", "d'", "a'")],
                      [("b", "d'", "g'"), ("bes", "e'", "g'")], [("a", "d'", "fis'"), ("c'", "d'", "a'")],
                      [("b", "d'", "g'"), ("g", "d'", "g'")], [("g", "e'", "g'"), ("g", "c'", "g'")],
                      [("g", "c'", "g'"), ("fis", "c'", "fis'")], [("d", "b", "g'"), ("g", "b", "g'")])
              + " } >> }",
        "lh": "\\repeat volta 2 { \\voiceFour g8 r cis r | d8 r fis r | g8 r cis r | d8 r fis r | g8 r b, r | c8 r e r | "
              "d8 r d r | g,8 r g r }",
    },
    {
        "title": "Ballade", "credit": "Friedrich Burgmuller (1851), 25 Easy Studies, Op. 100 No. 15 - first part",
        "meter": "3/8", "tempo": 60, "tempo_unit": "4.", "key": "c \\minor", "long": True,
        "note": "The tune is in the left hand, low and mysterious, under quiet repeated chords. Read the left hand in "
                "groups of bars: two bars of sixteenths, two of eighths, four of long A-naturals under an F-sharp "
                "chord. The section ends on a G major chord, the dominant: in the whole piece a C major middle "
                "section follows. Source: Mutopia Project no. 227 (public domain).",
        "rh": _lines([_ch()] * 7 + [_ch("fis'"), _ch(), _ch("fis'")] + [_ch()] * 5 + [_ch("fis'"), _ch(), _ch("fis'")]
                     + ["<c' ees' g'>8-. <c' ees' g'>-. r", "<g' c''>8-.\\< <g' c''>-.\\! r", "<g' b'>8-. <g' b'>-. r",
                        "<g' f''>8-. <g' f''>-. r", "<g' ees''>8-. <g' ees''>-. r", "g''8-.\\f ees''-. c''-.",
                        "g'8-. ees'-. c'-.", "R4.", "R4.", "<ees' g'>4-^ r8", "g4-^ r8", "<d' g'>4-^ r8\\fermata"], 6),
        "lh": "R4. | R4. | c16\\mp( b, c g, a, b, | c b, c g, a, b, | c8)-. r ees-. | g8-. r c-. | a4.\\sf~ | "
              "a4 c8-. | a4.\\sf~ | a4 r8 | c16( b, c g, a, b, | c b, c g, a, b, | c8)-. r ees-. | g8-. r c-. | "
              "a4.\\sf~ | a4 c8-. | a4.\\sf~ | a4 r8 | g8 g r | <ees g>8 <ees g> r | <d g>8 <d g> r | "
              "<b, g>8 <b, g> r | <c g>8 <c g> r | R4. | R4. | g8-. ees-. c-. | g,4-^ r8 | <g c'>4-^ r8 | "
              "g,4-^ r8 | <g b>4-^ r8\\fermata",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 5?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if every triplet is even and fits its beat, and you can say how many beats each time signature has.",
    "Pass if you can play Rowing Song at sight and the opening of Für Elise after a few days.",
    "When you pass, move on to Unit 5.",
]
