"""Unit 6: Middle C position."""

INTRO = [
    "In the middle C position both thumbs share middle C. The right hand plays C D E F G as before. "
    "The left hand moves up so that fingers 5-4-3-2-1 sit on F G A B C, finishing on middle C. "
    "The hands are now right next to each other, and you read notes near the middle of the grand staff.",
]

NEW_IDEAS = [
    ("One key, two ways to write it", "Middle C can sit on a ledger line below the treble staff, or on a ledger line above the bass staff. It is the same key either way. The staff tells you which hand plays it."),
    ("New left-hand notes", "F is the fourth line (between the clef's dots), G the top space, A the top line, B the space just above the staff, and C the ledger line above that."),
    ("Ledger lines", "Short extra lines for notes beyond the staff. One ledger line above the bass staff, or below the treble staff, is middle C."),
]

TIPS = [
    "Don't confuse the top line of the bass staff (A) with the top space (G). Find the F line first and count up from it.",
    "When the melody passes between the hands around middle C, the hands are next to each other. There is no jump.",
    "Middle C written on the bass staff means left thumb; written on the treble staff, right thumb.",
    "Keep the beat going, and keep your eyes on the page.",
]

PART_NOTES = {
    "A": "Hands take turns across middle C. Metronome 60.",
    "B": "Eight-bar phrases in 3/4.",
    "C": "Eight-bar phrases in 4/4, including whole notes and quarter-half-quarter rhythms.",
}

PIECES = [
    {
        "title": "Over the Bridge", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The tune walks down from the right hand, crosses middle C into the left hand, and comes back up again.",
        "rh": "g'4^5 f' e' d' | c'2 d' | R1 | R1 | \\break R1 | R1 | e'4^3 d' e' d' | c'1",
        "lh": "R1 | R1 | c'4_1 b a g | f1 | g4 a b c' | b2 c' | R1 | R1",
    },
    {
        "title": "Sharing Middle C", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "Both hands start on middle C. Watch which staff it is written on.",
        "rh": "c'4^1 d' e' | f'2 e'4 | d'2. | R2. | \\break c'4 e' g' | f' e' d' | R2. | R2.",
        "lh": "R2. | R2. | R2. | c'4_1 b a | R2. | R2. | g4_4 a b | c'2.",
    },
    {
        "title": "Echo Across Middle C", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "The right hand climbs, the left hand answers by stepping down from middle C, and the two hands meet on middle C at the end.",
        "rh": "c'4^1 d' e' f' | g'1 | R1 | R1 | \\break g'4^5 f' e' d' | e'1 | R1 | R1",
        "lh": "R1 | R1 | c'4_1 b a g | f1 | R1 | R1 | f4_5 g a b | c'1",
    },
]

CHECKPOINT = [
    "Play five Part B or C exercises you have not played before, at the speed shown.",
    "Pass if you never hesitate over A, B or C at the top of the bass staff.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 7.",
]
