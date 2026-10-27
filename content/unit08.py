"""Unit 8: G position; fourths and fifths."""

KEYBOARDS = [["LH_G", "RH_G"]]

INTRO = [
    "Both hands now move to a new home: G position. Right thumb on the G above middle C, fingers on G A B C D. "
    "Left little finger on the G that sits on the bottom line of the bass staff, fingers on G A B C D. "
    "You will also read bigger leaps: fourths and fifths.",
]

NEW_IDEAS = [
    ("New treble notes", "G on the second line (where the clef curls), A in the second space, B on the middle line, C in the third space, D on the fourth line."),
    ("New bass notes", "G on the bottom line, A in the bottom space, B on the second line, C in the second space, D on the middle line."),
    ("Naming intervals", "Count the letter names, including both ends: C to D is a 2nd (a step), C to E a 3rd (a skip), C to F a 4th, C to G a 5th."),
    ("4ths and 5ths on the staff", "A 4th goes from a line to a space (or a space to a line), jumping over two notes. A 5th goes from a line to the line after next, or a space to the space after next."),
    ("5ths in the hand", "In a five-finger position a 5th is always thumb to little finger, so you can play it without naming the second note."),
]

TIPS = [
    "Your hands have moved. Before each exercise, use the finger number on the first note to check which key you start on.",
    "Use the G landmarks: the treble clef curls around G, and the bass staff's bottom line is G.",
    "Read 4ths and 5ths as shapes: line-to-space jumps, and line-to-line or space-to-space jumps with one line or space in between.",
    "Bigger leaps tempt you to look down. Trust the position: every note is still under a finger.",
]

PART_NOTES = {
    "A": "Right hand in G position, with intervals up to a 5th. Metronome 60.",
    "B": "Hands together in G position: the left hand holds G (finger 5) or D (finger 1).",
    "C": "Left hand in G position, in 3/4.",
}

PIECES = [
    {
        "title": "Ode to Joy in G", "credit": "Ludwig van Beethoven (1824), simplified", "meter": "4/4", "tempo": 76,
        "note": "The tune you know, starting a new position: right thumb on G, so the melody starts with finger 3 on B.",
        "rh": "b'4^3 b' c'' d'' | d'' c'' b' a' | g' g' a' b' | b' a' a'2 | \\break b'4 b' c'' d'' | d'' c'' b' a' | g' g' a' b' | a' g' g'2",
        "lh": "g,1_5 | d1 | g,1 | d1 | g,1 | d1 | g,1 | g,1",
    },
    {
        "title": "Fanfare", "credit": "Original", "meter": "4/4", "tempo": 80,
        "note": "A trumpet call built from 5ths and skips. The left hand plays the same call two octaves lower.",
        "rh": "g'4^1 d'' b' g' | d''2 g' | a'4 c'' b' a' | g'1 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | g,4_5 d b, g, | d2 g, | a,4 c b, a, | g,1",
    },
    {
        "title": "Evening Song in G", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "A calm tune that starts with the little finger on D. The bass holds G nearly all the time.",
        "rh": "d''2^5 b' | c''4 b' a'2 | b'4 a' g' a' | b'1 | \\break d''2 b' | c''4 b' a' g' | a'2 b' | g'1",
        "lh": "g,1_5 | d1 | g,1 | g,1 | g,1 | g,1 | d1 | g,1",
    },
    {
        "title": "Horn Call", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "For the left hand alone: a hunting horn echoing in the low register. The first leap is a 5th, from finger 5 to finger 1.",
        "rh": "R2. | R2. | R2. | R2. | \\break R2. | R2. | R2. | R2.",
        "lh": "g,2._5 | d2. | b,4 c d | g,2. | d2 b,4 | c2 a,4 | b,4 a, a, | g,2.",
    },
]

CHECKPOINT = [
    "Play five Part B exercises you have not played before, at 60 beats per minute.",
    "Pass if you find G position without looking at the keyboard for more than a moment.",
    "Pass if you play 4ths and 5ths without stopping, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 9.",
]
