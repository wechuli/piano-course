"""Unit 7: Rests and ties."""

KEYBOARDS = [["LH_C", "RH_C"]]

INTRO = [
    "Music is made of sound and silence. A rest tells you to be silent for a number of beats, and you count "
    "those beats just as carefully as notes. A tie does the opposite: it makes one note last longer, even across a bar line.",
]

NEW_IDEAS = [
    ("Quarter rest", "One beat of silence: the zig-zag sign."),
    ("Half rest", "Two beats of silence: a small block sitting on top of the middle line, like a hat."),
    ("Whole rest", "A small block hanging under the fourth line. It means a whole bar of silence, in any time signature."),
    ("The tie", "A curved line joining two notes of the same pitch. Play the first note and hold it through the second; don't play the second again. It lasts as long as both values added together."),
    ("Tie or not?", "A curve joining two different notes is not a tie (that is a slur, which comes later). In this unit every curve joins equal notes."),
]

TIPS = [
    "Count rests aloud just like notes. Saying 'rest' quietly on the silent beat helps.",
    "Lift the finger during a rest so the sound really stops, but keep the hand on its keys.",
    "When you see a tie crossing a bar line, start counting the new bar while you are still holding the note.",
    "Rests are where most people lose the beat. Keep the metronome on.",
]

PART_NOTES = {
    "A": "Quarter and half rests in the right hand. Silence counts too. Metronome 60.",
    "B": "Rests in the left hand.",
    "C": "Ties across the bar line, with the hands taking turns. Hold the tied note; don't play it again.",
    "D": "Hands together in 3/4, with rests and ties in the right hand.",
}

PIECES = [
    {
        "title": "Stop and Go", "credit": "Original", "meter": "4/4", "tempo": 80,
        "note": "Three notes, then a one-beat stop, like traffic lights. Lift the finger on every rest.",
        "rh": "c'4^1 d' e' r | e' f' g' r | g' f' e' d' | e'2 r | \\break c'4 d' e' r | e' f' g' r | f' e' d' e' | c'1",
        "lh": "R1 | R1 | R1 | R1 | R1 | R1 | R1 | R1",
    },
    {
        "title": "Long Notes", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "The ties in bars 2 and 6 make notes six beats long. Count all six beats.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c2_5 d | e1~ | e2 d | c1 | e2 f | g1~ | g2 f4 e | d2 c",
    },
    {
        "title": "Hide and Seek", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "Notes and rests alternate, and the hands take turns. Keep counting through every silent beat.",
        "rh": "e'4^3 r g' r | e' d' c'2 | R1 | R1 | \\break g'4^5 r e' r | f' e' d'2 | R1 | R1",
        "lh": "R1 | R1 | c4_5 r e r | g f e2 | R1 | R1 | g4_1 f e d | c1",
    },
    {
        "title": "Clock Tower", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "Big, ringing bell notes. Tied notes hold across the bar line; the left hand rings once in every bar.",
        "rh": "g'2.^5~ | g'2 f'4 | e'2. | r4 e' d' | \\break c'2.~ | c'2 d'4 | e'4 d' c' | c'2.",
        "lh": "c2._5 | g2. | c2. | g2. | c2. | g2. | c2. | c2.",
    },
]

CHECKPOINT = [
    "Play five Part C or D exercises you have not played before, at the speed shown.",
    "Pass if every rest gets its full length, with no rushing to the next note.",
    "Pass if no tied note is played twice, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 8, where your hands move to a new position.",
]
