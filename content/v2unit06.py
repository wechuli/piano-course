"""Volume 2, Unit 6: G major."""

KEYBOARDS = [["LH_G", "RH_G"], ["LH_D", "RH_D"]]

INTRO = [
    "G major has one sharp in its key signature: F-sharp. Every F in the piece is played as F-sharp, on the black key. "
    "In this unit the hands use G position (which has no F at all) and D position (D E F-sharp G A). "
    "Both belong to G major.",
]

NEW_IDEAS = [
    ("The key signature of G major", "One sharp, on the top line of the treble staff and the fourth line of the bass staff. Both lines are F, so every F is F-sharp."),
    ("Home note", "Pieces in G major usually end on G, and the bass often plays G and D."),
    ("Two positions", "G position is G A B C D. D position is D E F-sharp G A, with finger 3 on the black key. The right hand's two positions overlap on G and A."),
    ("Moving between them", "From G position down to D position the thumb moves from G to D, a 4th lower; the finger numbers show each move."),
]

TIPS = [
    "Check the key signature first. One sharp means G major (or E minor, which comes in Unit 9).",
    "In D position, finger 3 lives on F-sharp. Put it there before you play.",
    "Look for the shift signs (finger numbers), just as in Unit 1.",
    "Keep going even if you miss an F-sharp.",
]

PART_NOTES = {
    "A": "Right hand in G major, moving between G and D positions. Metronome 60.",
    "B": "Left hand in G major: G position (G on the bottom line) and D position (D on the middle line).",
    "C": "Hands together in G major, with dynamics and articulation.",
}

PIECES = [
    {
        "title": "Twinkle, Twinkle in G", "credit": "Traditional (French melody 'Ah! vous dirai-je, maman')",
        "meter": "4/4", "tempo": 80, "key": "g \\major",
        "note": "The little finger stretches up to E in bars 2 and 10. The left hand adds C (finger 2) and D (finger 1) to its G.",
        "rh": "g'4^1 g' d''^5 d'' | e''^5 e'' d''2 | c''4 c'' b' b' | a' a' g'2 | \\break "
              "d''4 d'' c'' c'' | b' b' a'2 | d''4 d'' c'' c'' | b' b' a'2 | \\break "
              "g'4 g' d'' d'' | e'' e'' d''2 | c''4 c'' b' b' | a' a' g'2",
        "lh": "g,1_5 | c2 g, | c2 g, | d2 g, | g,2 c | g,2 d | g,2 c | g,2 d | g,1 | c2 g, | c2 g, | d2 g,",
    },
    {
        "title": "Country Dance in G", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "g \\major",
        "note": "In bar 5 the right hand shifts down to D position, bringing finger 3 onto F-sharp; in bar 7 it moves back to G position.",
        "rh": "b'4^3 a' g' | d''2 b'4 | c''4 b' a' | b'2. | \\break a'4^5 g' fis' | e'4 fis' g' | a'4^2 b' a' | g'2.",
        "lh": "g,2._5 | g,2. | d2. | g,2. | d2. | c2. | d2. | g,2.",
    },
    {
        "title": "Left-Hand Walk in G", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "g \\major",
        "note": "For the left hand alone. It shifts up to D position in bar 5 (F-sharp under finger 3) and back to G position in bar 7.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "g,4_5 a, b, c | d2 b, | c4 b, a, b, | g,1 | d4_5 e fis g | a2 fis | d4_1 c b, a, | g,1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if every F is played as F-sharp without hesitation.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 7.",
]
