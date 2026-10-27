"""Volume 3, Unit 7: Two notes at once (right-hand thirds and sixths)."""

KEYBOARDS = []

INTRO = [
    "So far the right hand has played one note at a time. Now it plays two together. Two notes a third apart "
    "look like a little snowman on the staff: both on lines or both in spaces, one just above the other. Read "
    "the top note as the tune, and let the lower note come along with it.",
]

NEW_IDEAS = [
    ("Thirds", "Line-line or space-space, touching: C-E, D-F, E-G. In a five-finger position you play them with "
               "fingers 1-3, 2-4 or 3-5."),
    ("Sixths", "Further apart: one note on a line and the other in a space, with two lines between them, such as "
               "C-A or D-B. The hand stretches: thumb on the lower note, finger 5 on the upper one."),
    ("Which note is the tune?", "The top note. Play it a little louder than the lower note, so the melody still "
                                "sings."),
    ("Reading two notes", "Don't read the two notes separately. Read the top note, then recognise the shape "
                          "below it: a third (touching) or a sixth (wide)."),
]

TIPS = [
    "In your scan, find the two-note chords and decide which fingers will play each one.",
    "Keep both notes exactly together: drop the hand, not two separate fingers.",
    "If a two-note chord trips you up, play only its top note and keep going.",
]

PART_NOTES = {
    "A": "Right hand alone in C position, with some thirds. Metronome 56.",
    "B": "Thirds over broken chords in C major.",
    "C": "F major in 3/4. The right hand stretches to E and D, which makes a few sixths possible.",
    "D": "D major in 6/8, with thirds and sixths.",
}

PIECES = [
    {
        "title": "London Bridge", "credit": "Traditional English nursery rhyme",
        "meter": "4/4", "tempo": 84,
        "note": "The long notes are doubled a third below. Play them with fingers 3 and 5 (E-G) or 2 and 4 (D-F), "
                "and keep the tune on top.",
        "rh": "g'4.^5\\mf a'8 g'4 f' | e' f' <e' g'>2^3 | d'4 e' <d' f'>2 | e'4 f' <e' g'>2 | \\break "
              "g'4. a'8 g'4 f' | e' f' <e' g'>2 | d'2 g' | e'4 <c' e'>2.",
        "lh": "c4_5 e_3 g_1 e | c e g e | b,_5 f_2 g f | c_5 e_3 g e | c e g e | c e g e | b,_5 f_2 g f | c1_5",
    },
    {
        "title": "Two by Two", "credit": "Original", "meter": "3/4", "tempo": 76, "positions": ["RH_G"],
        "note": "Thirds and sixths in G position. The sixths G-E (bars 1 and 6) and F-D (bars 2 and 7) need a "
                "stretch: thumb on the lower note, finger 5 on the upper one.",
        "rh": "<g' e''>2^5\\p <c'' e''>4 | <f' d''>2 <b' d''>4 | <c'' e''>4 <b' d''> <a' c''> | <g' b'>2. | \\break "
              "<a' c''>2\\mf a'4 | <c'' e''>2 <g' e''>4 | <f' d''>2 <g' b'>4 | c''2.",
        "lh": "c4_5 e_3 g_1 | b,_5 f_2 g | c_5 e_3 g | b,_5 f_2 g | c_5 f_2 a | c_5 e_3 g | b,_5 f_2 g | c2._5",
    },
    {
        "title": "Barcarolle in D", "credit": "Original", "meter": "6/8", "tempo": 52, "tempo_unit": "4.",
        "key": "d \\major",
        "note": "A barcarolle is a boat song, in a gently rocking 6/8. The right hand plays thirds and three sixths: "
                "D-B in bars 2 and 6, C-sharp-A in bars 3 and 7.",
        "rh": "<d' fis'>4^3\\p <fis' a'>8 <d' fis'>4. | <g' b'>4 <g' b'>8 <d' b'>4. | "
              "<e' g'>4 <cis' e'>8 <cis' a'>4. | <d' fis'>2. | \\break "
              "<fis' a'>4\\mf fis'8 <d' fis'>4. | <g' b'>4 a'8 <d' b'>4. | <e' g'>4\\> <cis' e'>8 <cis' a'>4. | "
              "<d' fis'>2.\\p",
        "lh": "d4_5 a8_1 fis4_3 a8 | d4_5 b8_1 g4_2 b8 | cis4_5 a8_1 g4_2 a8 | d4_5 a8_1 fis4_3 a8 | "
              "d4 a8 fis4 a8 | d4_5 b8_1 g4_2 b8 | cis4_5 a8_1 g4_2 a8 | d2._5",
    },
]

CHECKPOINT = [
    "Play five new exercises from Parts B to D at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "Both notes of every two-note chord sound together, and the top note sings.",
    "When you pass, move on to Unit 8.",
]
