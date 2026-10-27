"""Volume 2, Unit 1: Moving the hand (shifts between C and G positions)."""

KEYBOARDS = [["LH_C", "RH_C"], ["LH_G", "RH_G"]]

INTRO = [
    "So far each exercise kept the hand in one place. Real music moves. In this unit each hand moves between "
    "two homes, C position and G position. A finger number in the middle of a line is your signal: move the hand "
    "so that finger lands on that note.",
]

NEW_IDEAS = [
    ("Shift signals", "A finger number appears on the first note after every move. A 1 on G in the right hand means the thumb goes to G: you are now in G position."),
    ("Move early", "Move the hand during the note before the shift, or during a rest, so you arrive in time. The beat does not wait for the hand."),
    ("Where the positions meet", "The right hand's two positions overlap on G: finger 5 in C position, finger 1 in G position. The left hand's overlap on C and D."),
]

TIPS = [
    "In your 10-second scan, find every finger number. Each one after the first is a shift.",
    "Look at the note under each finger number and picture where your hand goes before you start.",
    "Keep your eyes on the music while you move. Feel the distance rather than looking down.",
    "If a shift goes wrong, keep counting and rejoin on the next note you can.",
]

PART_NOTES = {
    "A": "The right hand moves between C position and G position. Watch for finger numbers. Metronome 60.",
    "B": "The left hand moves between C position (C in the second space) and G position (G on the bottom line).",
    "C": "Eight-bar phrases with the hands taking turns, each moving between its two positions.",
}

PIECES = [
    {
        "title": "Climbing the Stairs", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The right hand walks up through C position, shifts so the thumb takes G in bar 3, and walks on to D. It comes back down with another shift in bar 7.",
        "rh": "c'4^1 d' e' f' | g'2 g' | g'4^1 a' b' c'' | d''1 | \\break d''4 c'' b' a' | g'2 g' | g'4^5 f' e' d' | c'1",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Yankee Doodle", "credit": "Traditional American", "meter": "4/4", "tempo": 84,
        "positions": ["LH_MC"],
        "note": "The tune dips below middle C three times. Those notes are written in the bass staff: play them with the left hand in middle C position (thumb on middle C).",
        "rh": "c'4^1 c' d' e' | c' e' d' r | c' c' d' e' | c'2 r | \\break c'4 c' d' e' | f' e' d' c' | R1 | c'2 c'",
        "lh": "R1 | r2 r4 g4_4 | R1 | r2 b2_2 | R1 | R1 | b4 g a b | R1",
    },
    {
        "title": "Two Homes for the Left Hand", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The left hand starts in C position, shifts down to G position in bar 3 (thumb on D), and moves back to C position in bar 7.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c4_5 e d f | e2 c | d4_1 c b, a, | g,1 | g,4 a, b, c | d2 d | e4_3 d c d | c1",
    },
    {
        "title": "Over the Hill", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "Hands together. The right hand shifts up to G position in bar 3 and back in bar 7. A new bass note appears in bars 3-4: F, under finger 2.",
        "rh": "e'4^3 f' g' e' | d'2 g' | a'4^2 b' c'' b' | a'2 g' | \\break b'4 a' g' a' | b'2 g' | f'4^4 e' d' e' | c'1",
        "lh": "c1_5 | g1 | f1 | f2 c2 | g1 | g1 | g1 | c1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if every shift lands on time, without looking down for more than an instant.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 2.",
]
