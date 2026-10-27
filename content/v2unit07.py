"""Volume 2, Unit 7: F major."""

KEYBOARDS = [["LH_F", "RH_F"], ["LH_C", "RH_C"]]

INTRO = [
    "F major has one flat in its key signature: B-flat. Every B is played as B-flat. The hands use F position "
    "(F G A B-flat C) and C position (C D E F G). Both belong to F major.",
]

NEW_IDEAS = [
    ("The key signature of F major", "One flat, on the middle line of the treble staff and the second line of the bass staff. Both lines are B, so every B is B-flat."),
    ("F position", "F G A B-flat C. The black key is finger 4 in the right hand and finger 2 in the left hand."),
    ("Where the positions meet", "The right hand's F and C positions overlap on F and G; the left hand's overlap on F and G too."),
    ("Home note", "Pieces in F major usually end on F, and the bass often plays F and C."),
]

TIPS = [
    "One flat in the key signature means F major (or D minor, which comes in Unit 9).",
    "In F position, put finger 4 (right hand) or finger 2 (left hand) on B-flat before you start.",
    "C position has no B at all, so after a shift into it there is nothing to remember.",
    "Keep going even if you miss a B-flat.",
]

PART_NOTES = {
    "A": "Right hand in F major, moving between F and C positions. Metronome 60.",
    "B": "Left hand in F major: F position (F on the fourth line) and C position.",
    "C": "Hands together in F major, with dynamics and articulation.",
}

PIECES = [
    {
        "title": "Frere Jacques in F", "credit": "Traditional French round", "meter": "4/4", "tempo": 84,
        "key": "f \\major",
        "note": "A round: several voices can sing it, starting two bars apart. Bars 5-6 stretch up to D; in bar 7 the hand shifts down to C position for the low C. The bass drones F and C.",
        "rh": "f'4^1 g' a' f' | f' g' a' f' | a'^3 bes' c''2 | a'4 bes' c''2 | \\break "
              "c''8^4 d''^5 c'' bes' a'4 f' | c''8 d'' c'' bes' a'4 f' | f'^4 c' f'2 | f'4 c' f'2",
        "lh": "f2_5 c' | f2 c' | f2 c' | f2 c' | f2 c' | f2 c' | f1 | f1",
    },
    {
        "title": "Au clair de la lune in F", "credit": "Traditional French song (opening)", "meter": "4/4", "tempo": 76,
        "key": "f \\major",
        "note": "The right hand plays the phrase in F position, then the left hand repeats it in its own F position.",
        "rh": "f'4^1 f' f' g' | a'2 g' | f'4 a' g' g' | f'1 | \\break R1 | R1 | R1 | R1",
        "lh": "R1 | R1 | R1 | R1 | f4_5 f f g | a2 g | f4 a g g | f1",
    },
    {
        "title": "Evening in F", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "f \\major",
        "note": "Hands together. Finger 4 plays every B-flat; the bass moves between F (finger 5) and middle C (finger 1).",
        "rh": "a'4^3 bes' c'' a' | g'2 f' | g'4 a' bes' g' | a'1 | \\break c''4 bes' a' bes' | c''2 a' | g'4 a' g' g' | f'1",
        "lh": "f1_5 | c'1 | c'1 | f1 | c'1 | f1 | c'1 | f1",
    },
    {
        "title": "Low Bells in F", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "f \\major",
        "note": "For the left hand alone: F position, then C position from bar 3 (thumb on G), then back to F position in bar 7.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c'4_1 bes a g | f2 a | g4_1 f e d | c1 | c4 e g f | e2 g | a4_3 g f g | f1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if every B is played as B-flat without hesitation.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 8.",
]
