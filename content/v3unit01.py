"""Volume 3, Unit 1: Broken chords (I, IV and V7 in the left hand)."""

KEYBOARDS = []  # the right-hand positions are old friends; this unit shows the left hand's chord shapes
CHORD_SHAPES = [
    ("C major", "LH_C", "c \\major", {}),
    ("G major", "LH_G", "g \\major", {"f": "is"}),
    ("F major", "LH_F", "f \\major", {"b": "es"}),
]

INTRO = [
    "Until now the left hand mostly held one long note while the right hand played the tune. In this unit the "
    "left hand plays chords, one note at a time. A chord played one note after another is called a broken chord. "
    "Broken chords fill out the music and keep it moving, and they are easy to read once you know their shapes.",
    "Each key uses three chord shapes. Learn them on the keyboard below before you start: in every exercise the "
    "left hand plays only these notes.",
]

NEW_IDEAS = [
    ("Triad", "Three notes stacked in thirds: a note, the note a third above it, and the note a third above that. "
              "On the staff a triad sits on three lines in a row or in three spaces in a row: C E G, F A C, G B D."),
    ("I, IV and V7", "Chords are named by the scale note they are built on: I on the first note of the key (C in "
                     "C major), IV on the fourth (F) and V on the fifth (G). V7 adds a fourth note, a seventh above "
                     "the bottom note (G B D F). The three chords together can play under most simple tunes."),
    ("Shapes that stay close", "The hand does not jump to each new chord. It keeps finger 5 near the tonic and "
                               "changes shape: I is C E G (fingers 5 3 1), IV is C F A (5 2 1) and V7 is B F G "
                               "(5 2 1), which is G7 without its D. Finger 5 moves down one key for V7."),
    ("Broken-chord patterns", "In 4/4 the left hand plays bottom, middle, top, middle in quarter notes. In 3/4 it "
                              "plays bottom, middle, top. The last bar holds the tonic."),
    ("Finger numbers in the bass", "A finger number under a bass note marks a new chord shape. Change the shape "
                                   "of your hand there, not before."),
]

TIPS = [
    "Read the left hand in shapes, not note by note: three lines or three spaces in a row is I; a wider shape is IV or V7.",
    "In your 10-second scan, follow the left hand's finger numbers and name each chord: I, IV or V7.",
    "The first note of each bar in the right hand belongs to that bar's chord, so the hands always fit together on beat 1.",
    "Keep the left hand soft and even. The tune is in the right hand.",
]

PART_NOTES = {
    "A": "C major. The right hand plays half and whole notes; the left hand plays I and V7. Metronome 60.",
    "B": "C major with all three chords. Every exercise goes I, IV, V7 and back to I.",
    "C": "G major waltzes: the left hand plays bottom, middle, top. F-sharp is the bottom note of the V7 shape.",
    "D": "F major in eight bars. B-flat is the middle note of IV and V7. Watch the slurs and staccato dots.",
}

PIECES = [
    {
        "title": "Ode to Joy", "credit": "Ludwig van Beethoven, theme from Symphony No. 9 - simplified",
        "meter": "4/4", "tempo": 76,
        "note": "Two chords only, I and V7. In bar 4 the chord changes halfway through the bar, and in bar 8 the "
                "left hand settles on C for the last two beats.",
        "rh": "e'4^3 e' f' g' | g' f' e' d' | c' c' d' e' | e'4. d'8 d'2 | \\break "
              "e'4 e' f' g' | g' f' e' d' | c' c' d' e' | d'4. c'8 c'2",
        "lh": "c4_5 e g e | b,_5 f g f | c_5 e g e | c4 e b,_5 f | c_5 e g e | b,_5 f g f | c_5 e g e | b,4_5 f c2_5",
    },
    {
        "title": "Jingle Bells", "credit": "James Lord Pierpont (1857), chorus - simplified",
        "meter": "4/4", "tempo": 92,
        "note": "The chorus of a famous winter song, with all three chords. Find the IV shape (C F A) in bars 5 and 13 "
                "and the V7 shape (B F G) in bars 8 and 15 before you start.",
        "rh": "e'4^3 e' e'2 | e'4 e' e'2 | e'4 g' c'4. d'8 | e'1 | \\break "
              "f'4 f' f'4. f'8 | f'4 e' e' e'8 e' | e'4 d' d' e' | d'2 g' | \\break "
              "e'4 e' e'2 | e'4 e' e'2 | e'4 g' c'4. d'8 | e'1 | \\break "
              "f'4 f' f'4. f'8 | f'4 e' e' e'8 e' | g'4 g' f' d' | c'1",
        "lh": "c4_5 e g e | c e g e | c e g e | c e g e | c_5 f_2 a f | c_5 e_3 g e | c e g e | b,_5 f_2 g f | "
              "c_5 e_3 g e | c e g e | c e g e | c e g e | c_5 f_2 a f | c_5 e_3 g e | b,_5 f_2 g f | c1",
    },
    {
        "title": "Little Waltz in G", "credit": "Original", "meter": "3/4", "tempo": 96, "key": "g \\major",
        "note": "A waltz with the bass going bottom, middle, top. In bars 4 and 7 the V7 shape is played from the top "
                "down (D C F-sharp), so the hand moves only a short way.",
        "rh": "b'4^3\\p a' b' | d''2 b'4 | c''4 b' c'' | a'2. | \\break b'4\\mf a' b' | c'' d'' c'' | a'4 b' c'' | g'2.",
        "lh": "g,4_5 b, d | g, b, d | g,_5 c_2 e | d c fis, | g,_5 b,_3 d | g,_5 c_2 e | d c fis, | g,2.",
    },
    {
        "title": "Evening Song", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "f \\major",
        "note": "F major, with B-flat in the right hand and in the IV and V7 shapes. The left hand's top note in IV is "
                "D above middle C, on a ledger line.",
        "rh": "a'4^3\\mp g' f' a' | bes'2 a'4 g' | g'4 a' bes' g' | a'2 f' | \\break "
              "c''4\\mf bes' a' c'' | bes'4 a' bes' c'' | bes'2\\> g' | f'1\\p",
        "lh": "f4_5 a c' a | f_5 bes_2 d' bes | e_5 bes c' bes | f_5 a_3 c' a | f a c' a | f_5 bes_2 d' bes | "
              "e_5 bes c' bes | f1",
    },
]

CHECKPOINT = [
    "Play five new Part C or D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Name the chord in every bar (I, IV or V7) from the left-hand shape alone.",
    "When you pass, move on to Unit 2.",
]
