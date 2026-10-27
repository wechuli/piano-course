"""Volume 3, Unit 2: The Alberti bass."""

KEYBOARDS = []
CHORD_SHAPES = [
    ("C major", "LH_C", "c \\major", {}),
]

INTRO = [
    "The Alberti bass is a broken chord in eighth notes: bottom, top, middle, top, over and over. It is named "
    "after Domenico Alberti, an Italian composer of the early 1700s, and you will hear it in countless pieces by "
    "Haydn, Mozart and Clementi. It keeps the music moving gently while the right hand sings above it. The chord shapes are the same as "
    "in Unit 1; only the order of the notes is new.",
]

NEW_IDEAS = [
    ("Bottom, top, middle, top", "In C major the I chord becomes C G E G, C G E G. The thumb plays every second "
                                 "note, so the pattern rocks between finger 5, the thumb, finger 3 and the thumb."),
    ("IV and V7", "IV becomes C A F A (fingers 5 1 2 1) and V7 becomes B G F G (5 1 2 1). The thumb stays on top; "
                  "only fingers 5 and 2 or 3 change."),
    ("Eighths against quarters", "The left hand plays two notes for every right-hand quarter note. Count "
                                 "1-and-2-and: the right hand plays on the numbers only."),
]

TIPS = [
    "Before you start, find each new chord shape: a finger number under the bass marks it.",
    "Keep the thumb light. The bottom note of each group carries the harmony; the thumb notes are softer.",
    "Read the first four eighths of a bar as one shape; the rest of the bar repeats it, so your eyes can go back "
    "to the right hand.",
]

PART_NOTES = {
    "A": "C major. The right hand plays half and whole notes over an Alberti bass on I and V7. Metronome 56.",
    "B": "Eight bars in C major with I, IV and V7, and dynamics.",
    "C": "G major in 3/4: the bass plays bottom, top, middle, top, middle, top - six eighths in a bar.",
    "D": "F major. The right hand moves between F position and C position; watch for its finger numbers.",
}

PIECES = [
    {
        "title": "Twinkle, Twinkle, Little Star",
        "credit": "French folk tune 'Ah! vous dirai-je, maman' (18th century) - simplified",
        "meter": "4/4", "tempo": 76,
        "note": "Mozart wrote twelve variations on this tune. Here the chord changes halfway through most bars, so "
                "each half bar has its own group of four eighths. The right hand stretches finger 5 up to A.",
        "rh": "c'4^1 c' g'^4 g' | a'^5 a' g'2^4 | f'4^3 f' e' e' | d' d' c'2 | \\break "
              "g'4^4 g' f' f' | e' e' d'2 | g'4 g' f' f' | e' e' d'2 | \\break "
              "c'4^1 c' g'^4 g' | a'^5 a' g'2^4 | f'4^3 f' e' e' | d' d' c'2",
        "lh": "c8_5 g_1 e_3 g c g e g | c_5 a_1 f_2 a c g e g | c a f a c g e g | b,_5 g_1 f_2 g c g e g | "
              "c g e g b, g f g | c g e g b, g f g | c g e g b, g f g | c g e g b, g f g | "
              "c g e g c g e g | c a f a c g e g | c a f a c g e g | b, g f g c2",
    },
    {
        "title": "Little Sonata Theme", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "A tune in the style of a classical sonata. In bar 6 the right hand stretches finger 5 to A, and in "
                "bar 7 the chord changes halfway through the bar.",
        "rh": "e'2^3\\p g'4 e' | d'2 f' | e'4 d' c' e' | d'1 | \\break "
              "e'2\\mf g'4 e' | f'4 a'^5 g' f' | e'2\\> d' | c'1\\p",
        "lh": "c8_5 g_1 e_3 g c g e g | b,_5 g_1 f_2 g b, g f g | c_5 g_1 e_3 g c g e g | b,_5 g_1 f_2 g b, g f g | "
              "c_5 g_1 e_3 g c g e g | c_5 a_1 f_2 a c a f a | c_5 g_1 e_3 g b,_5 g_1 f_2 g | c1_5",
    },
    {
        "title": "Alberti Waltz", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "g \\major",
        "note": "In 3/4 the Alberti pattern has six eighths: bottom, top, middle, top, middle, top. F-sharp is the "
                "bottom note of the V7 shape in bars 4 and 7.",
        "rh": "d''2^5\\mp b'4 | g'4 a' b' | c''2 c''4 | a'2. | \\break "
              "b'4\\mf c'' d'' | c''4 b' a' | a'4 c'' a' | g'2.",
        "lh": "g,8_5 d_1 b,_3 d b, d | g, d b, d b, d | g,_5 e_1 c_2 e c e | fis,_5 d_1 c_2 d c d | "
              "g,_5 d_1 b,_3 d b, d | g,_5 e_1 c_2 e c e | fis,_5 d_1 c_2 d c d | g,2.",
    },
    {
        "title": "Sunrise in F", "credit": "Original", "meter": "4/4", "tempo": 66, "key": "f \\major",
        "note": "Dotted rhythms over an Alberti bass in F major. B-flat is in both hands; in bar 6 the IV shape "
                "reaches up to D above middle C.",
        "rh": "a'4.^3\\p( g'8 f'4 a') | bes'2 g' | a'4.( bes'8 c''4 a') | g'1 | \\break "
              "c''4.^5\\mf( bes'8 a'4 f') | bes'4 a' g' bes' | g'4\\> bes' a' g' | f'1\\p",
        "lh": "f8_5 c'_1 a_3 c' f c' a c' | e_5 c'_1 bes_2 c' e c' bes c' | f_5 c'_1 a_3 c' f c' a c' | "
              "e_5 c'_1 bes_2 c' e c' bes c' | f_5 c'_1 a_3 c' f c' a c' | f_5 d'_1 bes_2 d' f d' bes d' | "
              "e_5 c'_1 bes_2 c' e c' bes c' | f1_5",
    },
]

CHECKPOINT = [
    "Play five new Part B or D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "The Alberti bass stays even and softer than the tune.",
    "When you pass, move on to Unit 3.",
]
