"""Volume 2, Unit 4: Legato and staccato."""

KEYBOARDS = [["LH_C", "RH_C"], ["LH_G", "RH_G"]]

INTRO = [
    "Notes can be joined smoothly or played short and separate. A curved line over or under a group of different "
    "notes is a slur: play them legato, smoothly connected. A dot above or below a note means staccato: short and "
    "detached, with a little silence after it.",
]

NEW_IDEAS = [
    ("Slur", "A curved line joining different notes. Play legato: hold each key until the next one goes down, so there is no gap. Lift the hand gently at the end of the slur."),
    ("Slur or tie?", "A tie joins two notes of the same pitch: play once and hold. A slur joins different notes: play them all, smoothly."),
    ("Staccato", "A dot above or below the notehead. Play the note short, as if the key were hot, but keep the beat: the note still takes its full share of time."),
    ("No marking", "With no slur or dot, play the notes in an ordinary, slightly separated way."),
]

TIPS = [
    "During the 10-second scan, notice where slurs begin and end, and which notes have dots.",
    "Staccato is about the sound, not the speed. Don't rush staccato notes.",
    "At the end of a slur, lift the hand. That small breath shapes the phrase.",
    "Reading the marks matters, but keeping the beat matters more. If you miss a marking, keep going.",
]

PART_NOTES = {
    "A": "Slurs and staccato in the right hand, with some shifts. Metronome 66.",
    "B": "The hands take turns; each two-bar phrase is legato, staccato or plain.",
    "C": "Hands together in 3/4; the marks are in the right hand.",
}

PIECES = [
    {
        "title": "Smooth and Bouncy", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "Two bars smooth, two bars bouncy, and again. Make the difference clear.",
        "rh": "c'4^1( d' e' f' | g'1) | g'4-. f'-. e'-. d'-. | c'2 r | \\break e'4^3( f' g' e' | d'1) | d'4-. e'-. d'-. e'-. | c'1",
        "lh": "c1_5 | g1 | g1 | c1 | c1 | g1 | g1 | c1",
    },
    {
        "title": "Little Minuet", "credit": "Original", "meter": "3/4", "tempo": 84,
        "note": "Slurred pairs: play the first note of each pair a little stronger and the second lighter, then a short staccato.",
        "rh": "c'4^1( d') e'-. | f'( e') d'-. | e'( d') c'-. | d'2. | \\break e'4( f') g'-. | f'( e') d'-. | e'( d') d'-. | c'2.",
        "lh": "c2._5 | g2. | c2. | g2. | c2. | g2. | g2. | c2.",
    },
    {
        "title": "Raindrops", "credit": "Original", "meter": "4/4", "tempo": 80,
        "note": "In G position. Light staccato raindrops, then a smooth slurred phrase in bars 5-6.",
        "rh": "g'4-.^1 b'-. d''-. b'-. | c''-. a'-. b'2 | a'4-. c''-. b'-. a'-. | g'2 r | \\break d''4^5( c'' b' a' | g'1) | a'4-. b'-. a'-. b'-. | g'1",
        "lh": "g,1_5 | d1 | d1 | g,1 | g,1 | g,1 | d1 | g,1",
    },
    {
        "title": "Legato Song", "credit": "Original", "meter": "4/4", "tempo": 72,
        "note": "For the left hand alone: four slurred phrases. Connect every note inside a slur, and lift at its end.",
        "rh": "R1 | R1 | R1 | R1 | \\break R1 | R1 | R1 | R1",
        "lh": "c4_5( d e f | g2 e) | f4( e d e | c1) | e4( f g e | d2 g) | f4( e d d | c1)",
    },
]

CHECKPOINT = [
    "Play five Part B or C exercises you have not played before, at 66 beats per minute.",
    "Pass if a listener could hear which phrases were legato and which staccato.",
    "Pass if you play no more than one stop per exercise, and at least 9 notes out of 10 are right.",
    "When you pass, move on to Unit 5.",
]
