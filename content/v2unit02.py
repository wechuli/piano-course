"""Volume 2, Unit 2: Stretching one key beyond the position."""

KEYBOARDS = [["RH_C"], ["LH_C"]]
# (step, finger, hand): keys reached by a stretch, drawn in a paler colour
STRETCH = [(27, "1", "RH"), (33, "5", "RH"), (20, "5", "LH"), (26, "1", "LH")]

INTRO = [
    "Sometimes a melody goes just one note beyond the hand position. Instead of moving the whole hand, stretch: "
    "the thumb slides one key below the position, or the little finger reaches one key above it, and then the hand "
    "settles back. The pale keys in the picture are the stretch notes.",
]

NEW_IDEAS = [
    ("Stretch or shift?", "A stretch is for a single note just outside the position, after which the hand comes back. A shift moves the whole hand to a new home."),
    ("Right-hand stretches", "From C position the thumb slides down to B, and finger 5 reaches up to A."),
    ("Left-hand stretches", "From C position finger 5 reaches down to B, and the thumb slides up to A."),
    ("Stay relaxed", "Open the hand for the stretch, then let it close again. Don't hold it stretched."),
]

TIPS = [
    "In your 10-second scan, find the highest and lowest notes. If one is just outside the position, plan a stretch.",
    "A stretch note is only ever one key outside the position, so it is always played by finger 1 or finger 5.",
    "On the staff, a stretch note sits just beyond the notes under fingers 1 and 5.",
    "Keep the beat steady; a stretch should not cost any time.",
]

PART_NOTES = {
    "A": "Right hand in C position, with stretches to B (thumb) and A (finger 5). Metronome 60.",
    "B": "Left hand in C position, with stretches to B (finger 5) and A (thumb).",
    "C": "Hands together: stretches in the right hand, the bass on C or G.",
}

PIECES = [
    {
        "title": "Twinkle, Twinkle, Little Star", "credit": "Traditional (French melody 'Ah! vous dirai-je, maman')",
        "meter": "4/4", "tempo": 80,
        "note": "Finger 5 stretches up to A in bars 2 and 10, then comes straight back to G. Twelve bars on three lines.",
        "rh": "c'4^1 c' g'^5 g' | a'^5 a' g'2 | f'4 f' e' e' | d' d' c'2 | \\break "
              "g'4 g' f' f' | e' e' d'2 | g'4 g' f' f' | e' e' d'2 | \\break "
              "c'4 c' g' g' | a' a' g'2 | f'4 f' e' e' | d' d' c'2",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Stretch and Return", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The thumb slides down to B in bars 1 and 7; finger 5 reaches up to A in bars 2 and 5.",
        "rh": "c'4^1 b c' d' | e' f' g' a' | g'2 e' | d'1 | \\break e'4 f' g' a' | g' f' e' d' | c' b c' d' | c'1",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Left-Hand Stretch", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The same tune as 'Stretch and Return', one octave lower. Finger 5 reaches down to B; the thumb slides up to A.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c4_5 b, c d | e f g a | g2 e | d1 | e4 f g a | g f e d | c b, c d | c1",
    },
    {
        "title": "Stretching Together", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "Hands together. The right hand stretches up to A in bars 1 and 5 and down to B in bars 3 and 7.",
        "rh": "e'4^3 g' a' g' | f'2 d' | e'4 c' b c' | d'1 | \\break e'4 g' a' g' | f'2 d' | e'4 d' c' b | c'1",
        "lh": "c1_5 | g1 | c1 | g1 | c1 | g1 | c2 g2 | c1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 60 beats per minute.",
    "Pass if the stretch notes come in time and the hand returns to its position afterwards.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 3.",
]
