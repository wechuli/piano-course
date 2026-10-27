"""Volume 2, Unit 10: Review."""

KEYBOARDS = [["LH_G", "RH_G"]]

INTRO = [
    "This unit mixes everything in Volume 2: shifts, stretches, dotted rhythms, legato and staccato, dynamics, and the "
    "keys of C, G and F major and A, E and D minor. The last piece, a famous minuet, is a challenge that uses four "
    "hand positions.",
]

NEW_IDEAS = [
    ("1. Key", "Key signature and last note: which key is it, and which black keys does it use?"),
    ("2. Positions", "The first finger number, and every later one: each is a shift or a stretch."),
    ("3. Rhythm", "Dotted quarters, eighths, rests and ties."),
    ("4. Sound", "Dynamics, hairpins, slurs and staccato dots."),
]

TIPS = [
    "Use this four-point scan before every review exercise: key, positions, rhythm, sound.",
    "Read in phrases of two or four bars, not note by note.",
    "If something goes wrong, keep the beat and rejoin at the next bar line.",
    "This is Level 2 reading. Enjoy how far you have come.",
]

PART_NOTES = {
    "A": "G major, hands together, with shifts, dotted rhythms, articulation and dynamics.",
    "B": "F major, hands taking turns and moving between positions.",
    "C": "A minor waltzes with dynamics.",
    "D": "C major with everything: stretches, shifts, eighths, dots, ties and rests.",
}

PIECES = [
    {
        "title": "Farewell March", "credit": "Original", "meter": "4/4", "tempo": 76, "key": "g \\major",
        "note": "Dotted rhythms, slurs, staccato and dynamics. The right hand shifts to D position in bar 5 and back to G position in bar 7.",
        "rh": "g'4.^1\\mf( a'8 b'4 g') | d''4.( c''8 b'2) | c''4-. a'-. b'-. g'-. | a'2 r | \\break "
              "fis'4.^3\\p( g'8 a'4 fis') | e'4.( fis'8 g'2) | a'4^2\\< b' c'' a' | g'1\\f",
        "lh": "g,1_5 | g,1 | c2 d | d1 | d1 | c1 | d1 | g,1",
    },
    {
        "title": "Minor Farewell", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "a \\minor",
        "note": "An A minor waltz that grows to forte in bar 4 and fades back to piano.",
        "rh": "a'4\\p^1 b' c'' | d''2 c''4 | b'4\\< c'' d'' | e''2.\\f | \\break e''4\\> d'' c'' | b'2 a'4 | b'4\\p a' b' | a'2.",
        "lh": "a,2._5 | a,2. | e2. | e2. | a,2. | e2. | e2. | a,2.",
    },
    {
        "title": "Minuet in G", "credit": "Christian Petzold (1725), BWV Anh. 114 - melody with a simplified bass",
        "meter": "3/4", "tempo": 92, "key": "g \\major", "allow_range": True, "allow_leap": 7,
        "note": "A challenge: one of the best-known pieces for students, once thought to be by J. S. Bach. The right hand moves through four positions; the finger numbers show each move. Learn it a line at a time.",
        "rh": "d''4^5 g'8^1 a' b' c'' | d''4 g' g' | e''4^3 c''8^1 d'' e'' fis'' | g''4^5 g'^1 g' | \\break "
              "c''4^4 d''8 c'' b' a' | b'4 c''8 b' a' g' | fis'4^1 g'8 a' b' g' | a'2. | \\break "
              "d''4^5 g'8^1 a' b' c'' | d''4 g' g' | e''4^3 c''8^1 d'' e'' fis'' | g''4^5 g'^1 g' | \\break "
              "c''4^4 d''8 c'' b' a' | b'4 c''8 b' a' g' | a'4^3 b'8 a' g' fis' | g'2.",
        "lh": "g,2._5 | b,2. | c2. | b,2. | a,2. | g,2. | d2. | d2. | g,2. | b,2. | c2. | b,2. | a,2. | g,2. | d2. | g,2.",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Volume 3?"
CHECKPOINT = [
    "Play two exercises from each part (A to D) that you have not played before, at the speeds shown.",
    "Pass if you keep the beat with no more than one stop per exercise, and name the key of each before you start.",
    "Pass if at least 9 notes out of 10 are right, and the dynamics and articulation can be heard.",
    "When you pass, you have finished Volume 2. If one skill keeps tripping you up, go back to its unit for a week.",
]
