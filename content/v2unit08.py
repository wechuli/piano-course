"""Volume 2, Unit 8: A minor."""

KEYBOARDS = [["LH_A", "RH_A"]]

INTRO = [
    "Minor keys have a darker, more serious sound. A minor uses the same notes as C major, with no sharps or flats in "
    "the key signature, but its home note is A. Pieces in A minor usually end on A, and the bass often plays A and E.",
]

NEW_IDEAS = [
    ("Major and minor", "In a major key the third note above home is four half-steps up (C to E). In a minor key it is three half-steps up (A to C). That one note changes the whole mood."),
    ("Relative keys", "A minor and C major share a key signature; they are called relative keys. To tell them apart, look at the last note and the bass: A means A minor, C means C major."),
    ("A position", "Right hand: thumb on the A above middle C (A B C D E). Left hand: finger 5 on the A in the bottom space of the bass staff (A B C D E)."),
    ("E position", "In Part C the right hand also moves down to E position: E F G A B, thumb on the E above middle C."),
]

TIPS = [
    "No sharps or flats? Check the last note and the bass to see whether the key is C major or A minor.",
    "Let minor music sing: aim for a smooth, legato tone in slurred phrases.",
    "Treble A position sits in the upper half of the staff; bass A position starts in the bottom space.",
    "Keep going even if a note goes wrong.",
]

PART_NOTES = {
    "A": "Right hand in A position, A minor. Metronome 60.",
    "B": "Left hand in A position, A minor.",
    "C": "Hands together in 3/4; the right hand also moves to E position.",
}

PIECES = [
    {
        "title": "Lament", "credit": "Original", "meter": "4/4", "tempo": 66, "key": "a \\minor",
        "note": "A slow, singing tune. Each two-bar slur is one breath; let the crescendo in bar 3 lead to mezzo forte.",
        "rh": "e''2\\p^5( d''4 c'' | b'2 c'') | d''4\\<( c'' b' c'' | b'1\\mf) | \\break "
              "c''2\\>( b'4 a' | b'2 c'') | b'4\\p( a' a' b' | a'1)",
        "lh": "a,1_5 | a,1 | e1 | e1 | a,1 | e1 | e1 | a,1",
    },
    {
        "title": "Shadow Dance", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "a \\minor",
        "note": "A minor waltz that climbs the chain A-C-E in the first bar.",
        "rh": "a'4^1 c'' e'' | d''2 c''4 | b'4 c'' d'' | e''2. | \\break e''4 d'' c'' | b'2 c''4 | b'4 a' b' | a'2.",
        "lh": "a,2._5 | a,2. | e2. | e2. | a,2. | e2. | e2. | a,2.",
    },
    {
        "title": "Low Road in A Minor", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "a \\minor",
        "note": "For the left hand alone, in A position from the bottom space of the bass staff.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "a,4_5 b, c d | e2 c | d4 c b, c | a,1 | c4 d e d | c2 b, | a,4 b, c b, | a,1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 72 beats per minute.",
    "Pass if you name the key (A minor) before you start, and the shifts to E position land on time.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 9.",
]
