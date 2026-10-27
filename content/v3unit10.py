"""Volume 3, Unit 10: Review."""

KEYBOARDS = []

INTRO = [
    "This unit mixes everything in Volume 3: broken chords and Alberti basses, 6/8, the keys of D major and "
    "B-flat major, B minor with its raised 7th, two notes at once, two independent voices and imitation. Before "
    "each exercise, use the five-point scan below.",
]

NEW_IDEAS = [
    ("1. Key", "Two sharps, two flats, or a minor key? In a minor key, look for the raised 7th."),
    ("2. Time", "4/4, 3/4 or 6/8? In 6/8, feel two beats in a bar."),
    ("3. Left hand", "Broken chords, Alberti bass, lilting bass, or a melody of its own? Find the first chord "
                     "shape or the first note and finger."),
    ("4. Right hand", "Two-note chords, stretches, and accidentals."),
    ("5. Entries", "In imitation, where does the left hand come in, and with which tune?"),
]

TIPS = [
    "Read in two-bar phrases, not note by note: most patterns repeat.",
    "Keep the accompaniment softer than the tune, whichever hand has it.",
    "If something goes wrong, keep the beat and rejoin at the next bar line.",
]

PART_NOTES = {
    "A": "D major: an Alberti bass under a tune with some thirds.",
    "B": "B-flat major in 6/8, with the lilting bass.",
    "C": "A B minor waltz: watch for A-sharp in both hands.",
    "D": "G major. The tune is in the left hand, and the right hand plays a second melody above it.",
    "E": "B-flat major imitation in 3/4.",
}

PIECES = [
    {
        "title": "Spring Rondo", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "d \\major",
        "note": "An Alberti bass in D major under a tune with thirds. In bar 3 the right-hand thumb stretches down "
                "to C-sharp, and in bar 6 finger 5 stretches up to B.",
        "rh": "fis'4^3\\mf a' <d' fis'>2 | <g' b'>2 g'4 e' | <e' g'>2 cis'4^1 e' | <d' fis'>1 | \\break "
              "a'4^5\\p fis' <fis' a'>2 | b'4 g' <g' b'>2 | a'4\\< g' <e' g'>2 | d'1\\mf",
        "lh": "d8_5 a_1 fis_3 a d a fis a | d_5 b_1 g_2 b d b g b | cis_5 a_1 g_2 a cis a g a | "
              "d_5 a_1 fis_3 a d a fis a | d a fis a d a fis a | d_5 b_1 g_2 b d b g b | "
              "cis_5 a_1 g_2 a cis a g a | d1_5",
    },
    {
        "title": "Night Song", "credit": "Original", "meter": "6/8", "tempo": 48, "tempo_unit": "4.",
        "key": "b \\minor",
        "note": "B minor in 6/8 over rolling eighths. A-sharp, the raised 7th, comes in bars 3 and 7 in both hands.",
        "rh": "d''4^3\\p cis''8 b'4 d''8 | e''4 fis''8 e''4 b'8 | cis''4 e''8 ais'4.^1 | b'2. | \\break "
              "fis''4^5\\mf e''8 d''4 b'8 | e''4 d''8 b'4. | ais'4^1\\> cis''8 e''4 cis''8 | b'2.\\pp",
        "lh": "b,8_5 d_3 fis_1 d fis d | b,_5 e_2 g_1 e g e | ais,_5 e_2 fis_1 e fis e | b,_5 d_3 fis_1 d fis d | "
              "b, d fis d fis d | b,_5 e_2 g_1 e g e | ais,_5 e_2 fis_1 e fis e | b,2._5",
    },
    {
        "title": "Little Canon in F", "credit": "Original", "meter": "4/4", "tempo": 76, "key": "f \\major",
        "positions": ["LH_F", "RH_F"],
        "note": "Both hands in F position, as in Units 1 and 7. Two short tunes, each copied an octave lower by "
                "the left hand two bars later. In bars 5 and 6 the left hand plays a counter-melody under the "
                "second tune.",
        "rh": "c''4^5\\mf a' bes' g' | a'2 f' | a'2\\p g' | f'2 a' | \\break "
              "a'4^3\\mf bes' c'' a' | g'2 f' | f'2\\p e'^1 | e'2 f'",
        "lh": "R1 | R1 | c'4_1 a bes g | a2 f_5 | f2_5 a_3 | bes_2 a | a4_3 bes c' a | g2 f_5",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Volume 4?"
CHECKPOINT = [
    "Play two new exercises from each part (A to E) at the speeds shown, naming the key and time before you start.",
    "Pass if you keep the beat with no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, you have finished Volume 3. If one skill keeps tripping you up, go back to its unit for a week.",
]
