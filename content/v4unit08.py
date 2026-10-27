"""Volume 4, Unit 8: Changing key; review of Volume 4."""

KEYBOARDS = []

INTRO = [
    "Music often travels to a new key and settles there for a while: this is called modulation. Sometimes the "
    "composer writes a new key signature after a double bar line; more often the new key shows itself only "
    "through accidentals. Either way, a good reader notices the change before it arrives and moves the hand's "
    "black keys with it. This unit is also the review of Volume 4.",
]

NEW_IDEAS = [
    ("A new key signature", "A double bar line followed by a new key signature: from here on, read with the new "
                            "sharps or flats. Cancelled sharps or flats are shown with natural signs."),
    ("Modulation by accidentals", "With no new signature, the new key arrives as an accidental: its leading note. "
                                  "C-sharp in a piece in F major means D minor is near; F-sharp in C major means "
                                  "G major."),
    ("The pivot", "Just before a change, the left hand usually plays the new key's V7 chord: its bottom note is "
                  "the new leading note. Spot that shape and you know where the music is going."),
]

TIPS = [
    "In your scan, look for double bar lines, new key signatures and repeated accidentals: they mark a new key.",
    "When the key changes, say the new key aloud in your head and prepare the black keys for it.",
    "In the review part, use the full scan: key, time, left-hand pattern, right-hand chords, rhythm.",
]

PART_NOTES = {
    "A": "C major to G major: a new key signature halfway through.",
    "B": "F major to D minor in 3/4, shown only by accidentals: C-sharp is the new leading note.",
    "C": "G major to D major for two bars, and back home to G.",
    "D": "Review: an E-flat major march in 2/4 with right-hand chords and syncopation.",
}

PIECES = [
    {
        "title": "A Change of Scene", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "Four bars in C major, then a double bar and the key signature of G major. The left hand's first "
                "shape in the new key (F-sharp, C, D) is the V7 of G.",
        "rh": "e'4^3\\mp g' e' c' | d'4 f' e' d' | c'4^1 e' g' e' | c'1 | \\break "
              "\\bar \"||\" \\key g \\major a'4^2\\mf c'' a' fis'^1 | g'4 b' d'' b' | c''4\\> a' fis' a' | g'1\\p",
        "lh": "c4_5 e_3 g_1 e | b,_5 f_2 g_1 f | c_5 e_3 g e | c1 | "
              "\\bar \"||\" \\key g \\major fis,4_5 c_2 d_1 c | g,_5 b,_3 d b, | fis,_5 c d c | g,1",
    },
    {
        "title": "Minuet in G minor", "credit": "Christian Petzold (attributed), BWV Anh. 115 - first part",
        "meter": "3/4", "tempo": 100, "key": "g \\minor", "positions": ["RH_D5", "RH_Gm", "LH_D"],
        "allow_leap": 8,
        "note": "From the Notebook for Anna Magdalena Bach. The first eight bars stay in G minor (F-sharp in bar 7); "
                "the next eight travel to B-flat major, the relative major, and end there. The B-naturals in bars "
                "12 and 13 lead into C minor on the way. Ornaments are left out. Source: Mutopia Project no. 76.",
        "rh": "bes''4^5\\mf a'' g'' | a'' d'' d'' | g'' g'8^1 a' bes' c'' | d''2. | \\break "
              "ees''4 f''8 ees'' d'' c'' | d''4 ees''8 d'' c'' bes' | c''4 d''8 c'' bes' c'' | a'2. | \\break "
              "bes''4^5\\p a'' g'' | a'' d'' d'' | g'' g'8 a' bes' c'' | d''2. | \\break "
              "f''4\\< g''8 f'' ees'' d'' | ees''4 f''8 ees'' d'' c'' | d''4\\f g'' c'' | <d' f' bes'>2.",
        "lh": "g2. | f | ees | d4 d'8 c' bes a | <g bes>2 a4 | bes2 g4 | a fis g | d d'8 c' bes a | "
              "g2. | f | ees | d4 d'8 c' b a | <b d'>2 g4 | c' a f | bes ees <f a> | bes bes,2",
    },
    {
        "title": "Old French Song", "credit": "Pyotr Ilyich Tchaikovsky, Op. 39 No. 16 (opening) - simplified",
        "meter": "2/4", "tempo": 60, "key": "g \\minor",
        "note": "A review of Volume 4: G minor in 2/4, a sixteenth-note turn in bar 7 and block chords in the left "
                "hand, with the F-sharp of the V7 chord in bar 8. Tchaikovsky's inner voices are left out and the "
                "rhythm of bar 8 is simplified. Source: Mutopia Project no. 2080.",
        "rh": "r4 r8 d'8^1\\p | g'8^2( a' bes' c'' | d''4.) d''8( | c''8 d'' ees'' c'' | d''4.) d''8( | \\break "
              "c''8 d'' ees'' c'' | d''8 ees''16 d'' c''8 bes' | a'4. g'8 | g'2)",
        "lh": "R2 | <g,-5 bes,-3 d-1>2 | <g, bes, d>2 | <g,-5 c-2 ees-1>2 | <g, bes, d>2 | <g, c ees>2 | "
              "<g, bes, d>4 <g, c ees> | <fis,-5 c-2 d-1>2 | <g, bes, d>2",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Volume 5?"
CHECKPOINT = [
    "Play two new exercises from each part (A to D) at the speeds shown, naming every key change before you start.",
    "Pass if you keep the beat with no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, you have finished Volume 4. If one skill keeps tripping you up, go back to its unit for a week.",
]
