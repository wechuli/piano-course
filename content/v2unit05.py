"""Volume 2, Unit 5: Dynamics."""

KEYBOARDS = [["LH_C", "RH_C"], ["LH_G", "RH_G"]]

INTRO = [
    "Music has loud and soft. Dynamics are the letters and signs that tell you how loudly to play. "
    "They are written below the staff, and each one lasts until the next.",
]

NEW_IDEAS = [
    ("p and f", "p (piano) means soft; f (forte) means loud."),
    ("mp and mf", "mp (mezzo piano) is medium soft; mf (mezzo forte) is medium loud. From soft to loud: p, mp, mf, f."),
    ("Hairpins", "A widening wedge means get gradually louder (crescendo). A narrowing wedge means get gradually softer (diminuendo). Each leads to the next dynamic mark."),
    ("How to play louder", "Use more arm weight and a quicker key stroke, not a harder finger. Soft playing still needs a full, clear sound."),
]

TIPS = [
    "Find the first dynamic before you start, and set your sound before the first note.",
    "A dynamic lasts until the next one. Keep it steady until the music asks for a change.",
    "Make a crescendo gradual: start soft enough that there is room to grow.",
    "Never let a dynamic change the tempo. Loud is not faster, and soft is not slower.",
]

PART_NOTES = {
    "A": "Dynamics in the right hand, with slurs, dots and shifts. Metronome 66.",
    "B": "Dynamics in the left hand.",
    "C": "Shaping eight-bar phrases, hands together: one level, a hairpin, then a new level.",
}

PIECES = [
    {
        "title": "Echo Valley", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "A loud call answered by a soft echo, then a crescendo to forte and a diminuendo to the end.",
        "rh": "c'4\\f^1 e' g' e' | d'2 g' | c'4\\p e' g' e' | d'2 g' | \\break e'4\\mf\\< f' g' f' | e'2 d'\\f | e'4\\> d' c' d' | c'1\\p",
        "lh": "c1_5 | g1 | c1 | g1 | c1 | g1 | c2 g2 | c1",
    },
    {
        "title": "Storm and Calm", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "In G position. The storm builds to forte in bar 4, then calms down again.",
        "rh": "g'4\\p^1 a' b' c'' | d''2 d'' | d''4\\< c'' b' c'' | d''1\\f | \\break d''4\\> c'' b' a' | g'2 a' | b'4\\p a' a' b' | g'1",
        "lh": "g,1_5 | d1 | g,1 | g,1 | g,1 | g,1 | d1 | g,1",
    },
    {
        "title": "Waltz in Waves", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "Each half of the waltz swells like a wave: grow towards bar 4, then fade towards the end.",
        "rh": "c'4\\p^1 d' e' | f'2 e'4 | d'4\\< e' f' | g'2.\\f | \\break g'4\\> f' e' | d'2 e'4 | d'4\\p e' d' | c'2.",
        "lh": "c2._5 | g2. | g2. | c2. | c2. | g2. | g2. | c2.",
    },
    {
        "title": "Distant Drums", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "For the left hand alone: drums approach (crescendo) and fade away (diminuendo).",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c4\\p_5 c g c | c2 g | c4\\< d e f | g1\\f | g4\\> f e d | e2 d | c4\\p d e d | c1",
    },
]

CHECKPOINT = [
    "Play five Part C exercises you have not played before, at 66 beats per minute.",
    "Pass if a listener could hear every dynamic level and each crescendo or diminuendo.",
    "Pass if the tempo stays steady through every dynamic change, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 6.",
]
