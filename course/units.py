"""Volume 1 course specification (Levels 0-1).

Each unit introduces ONE new idea. Each unit has parts; each part is a block of
generated exercises with its own rules. The generator reads these specs.

Pitch notation: diatonic step numbers, C4 (middle C) = 28.
    step = octave * 7 + index, where index is C=0 D=1 E=2 F=3 G=4 A=5 B=6
    C3 = 21, G3 = 25, C4 = 28, G4 = 32, C5 = 35.
Durations are in EIGHTH notes: 8 = whole, 6 = dotted half, 4 = half,
    3 = dotted quarter, 2 = quarter, 1 = eighth.
"""

C3, D3, E3, F3, G3, A3, B3 = 21, 22, 23, 24, 25, 26, 27
C4, D4, E4, F4, G4, A4, B4 = 28, 29, 30, 31, 32, 33, 34
C5, D5 = 35, 36
G2, D3_ = 18, 22

# Hand positions: lowest step, finger on that lowest step, which hand.
# RH fingers ascend 1..5 from the lowest note; LH fingers descend 5..1.
POSITIONS = {
    "RH_C": {"hand": "RH", "low": C4, "high": G4, "label": "Right hand C position"},
    "LH_C": {"hand": "LH", "low": C3, "high": G3, "label": "Left hand C position"},
    "RH_G": {"hand": "RH", "low": G4, "high": D5, "label": "Right hand G position"},
    "LH_G": {"hand": "LH", "low": G2, "high": D3, "label": "Left hand G position"},
    # Middle-C position: both thumbs share middle C.
    "RH_MC": {"hand": "RH", "low": C4, "high": G4, "label": "Middle C position (RH)"},
    "LH_MC": {"hand": "LH", "low": F3, "high": C4, "label": "Middle C position (LH)"},
    # Positions with a black key. "acc" marks which white-key step is raised/lowered
    # (for the keyboard picture); the generator itself uses the part's key_acc.
    "RH_D": {"hand": "RH", "low": D4, "high": A4, "label": "Right hand D position", "acc": {F4: "is"}},
    "LH_D": {"hand": "LH", "low": D3, "high": A3, "label": "Left hand D position", "acc": {F3: "is"}},
    "RH_F": {"hand": "RH", "low": F4, "high": C5, "label": "Right hand F position", "acc": {B4: "es"}},
    "LH_F": {"hand": "LH", "low": F3, "high": C4, "label": "Left hand F position", "acc": {B3: "es"}},
}

KEY_D = {"key": "d \\major", "key_acc": {"f": "is", "c": "is"}}
KEY_F = {"key": "f \\major", "key_acc": {"b": "es"}}

# --- Volume 2 positions and keys
A2, B2 = 19, 20
E5 = 37
POSITIONS.update({
    "RH_A": {"hand": "RH", "low": A4, "high": E5, "label": "Right hand A position"},
    "LH_A": {"hand": "LH", "low": A2, "high": E3, "label": "Left hand A position"},
    "RH_E": {"hand": "RH", "low": E4, "high": B4, "label": "Right hand E position", "acc": {F4: "is"}},
    "LH_E": {"hand": "LH", "low": E3, "high": B3, "label": "Left hand E position", "acc": {F3: "is"}},
    "RH_Enat": {"hand": "RH", "low": E4, "high": B4, "label": "Right hand E position"},
    "RH_Dm": {"hand": "RH", "low": D4, "high": A4, "label": "Right hand D position"},
    "LH_Dm": {"hand": "LH", "low": D3, "high": A3, "label": "Left hand D position"},
})
KEY_G = {"key": "g \\major", "key_acc": {"f": "is"}}
KEY_AM = {"key": "a \\minor", "key_acc": {}}
KEY_EM = {"key": "e \\minor", "key_acc": {"f": "is"}}
KEY_DM = {"key": "d \\minor", "key_acc": {"b": "es"}}

# Rhythm vocabularies (one entry = one bar, in eighths).
R44 = {
    "whole":   [[8]],
    "half":    [[4, 4], [8]],
    "quarter": [[2, 2, 2, 2], [4, 2, 2], [2, 2, 4], [4, 4], [2, 2, 2, 2]],
    "q_rich":  [[2, 2, 2, 2], [4, 2, 2], [2, 2, 4], [2, 4, 2], [4, 4], [8]],
    "eighths": [[1, 1, 2, 2, 2], [2, 2, 1, 1, 2], [1, 1, 1, 1, 2, 2], [2, 1, 1, 4], [4, 1, 1, 2]],
    "dotted":  [[3, 1, 2, 2], [2, 2, 3, 1], [3, 1, 4], [4, 3, 1], [2, 2, 2, 2], [4, 2, 2]],
}
R34 = {
    "basic":   [[6], [4, 2], [2, 2, 2], [2, 4]],
    "dotted34": [[3, 1, 2], [2, 3, 1], [4, 2], [2, 2, 2], [6]],
    "e34":     [[2, 1, 1, 2], [1, 1, 2, 2], [2, 2, 1, 1], [4, 2], [6]],
}
# Bars that may end a phrase (last note at least a half note).
CADENCE44 = [[8], [4, 4], [2, 2, 4]]
CADENCE34 = [[6], [2, 4]]
FINAL44 = [[8]]
FINAL34 = [[6]]

# Melodic motion weights: interval (in diatonic steps) -> weight.
STEPS_ONLY = {0: 2.0, 1: 5.0}            # repeats and steps
STEPS_SKIPS = {0: 1.5, 1: 5.0, 2: 2.5}   # + thirds
UP_TO_FIFTH = {0: 1.5, 1: 5.0, 2: 2.5, 3: 1.0, 4: 0.8}

VOLUME1 = [
    {
        "id": 1, "title": "The Right Hand Finds Its Home",
        "new": "Treble clef, right hand C position, whole / half / quarter notes, 4/4",
        "parts": [
            {"name": "A", "title": "Whole and half notes", "count": 8, "bars": 4,
             "mode": "RH", "rh": "RH_C", "meter": "4/4",
             "rhythms": "half", "motion": STEPS_ONLY, "tempo": 60},
            {"name": "B", "title": "Quarter notes join in", "count": 10, "bars": 4,
             "mode": "RH", "rh": "RH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_ONLY, "tempo": 60},
            {"name": "C", "title": "Eight-bar phrases", "count": 12, "bars": 8,
             "mode": "RH", "rh": "RH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_ONLY, "tempo": 66, "repeat_prob": 0.5},
        ],
    },
    {
        "id": 2, "title": "The Left Hand and the Bass Clef",
        "new": "Bass clef, left hand C position (C3-G3)",
        "parts": [
            {"name": "A", "title": "Long notes in the bass", "count": 8, "bars": 4,
             "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "half",
             "motion": STEPS_ONLY, "tempo": 60},
            {"name": "B", "title": "Quarter notes in the bass", "count": 10, "bars": 4,
             "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "quarter",
             "motion": STEPS_ONLY, "tempo": 60},
            {"name": "C", "title": "Eight-bar phrases", "count": 12, "bars": 8,
             "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "quarter",
             "motion": STEPS_ONLY, "tempo": 66, "repeat_prob": 0.5},
        ],
    },
    {
        "id": 3, "title": "Hands Take Turns",
        "new": "Melody passes between hands; 3/4 time and the dotted half note",
        "parts": [
            {"name": "A", "title": "Two bars each", "count": 10, "bars": 4,
             "mode": "alt", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_ONLY, "tempo": 60},
            {"name": "B", "title": "Three beats in a bar", "count": 10, "bars": 4,
             "mode": "RH", "rh": "RH_C", "meter": "3/4", "rhythms": "basic",
             "motion": STEPS_ONLY, "tempo": 72},
            {"name": "C", "title": "Turns in 3/4", "count": 10, "bars": 8,
             "mode": "alt", "rh": "RH_C", "lh": "LH_C", "meter": "3/4",
             "rhythms": "basic", "motion": STEPS_ONLY, "tempo": 72, "repeat_prob": 0.4},
        ],
    },
    {
        "id": 4, "title": "Skips",
        "new": "Thirds: line-to-line and space-to-space",
        "parts": [
            {"name": "A", "title": "Right-hand skips", "count": 10, "bars": 4,
             "mode": "RH", "rh": "RH_C", "meter": "4/4", "rhythms": "quarter",
             "motion": STEPS_SKIPS, "tempo": 60},
            {"name": "B", "title": "Left-hand skips", "count": 10, "bars": 4,
             "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "quarter",
             "motion": STEPS_SKIPS, "tempo": 60},
            {"name": "C", "title": "Skips, hands taking turns", "count": 12, "bars": 8,
             "mode": "alt", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_SKIPS, "tempo": 66, "repeat_prob": 0.4},
        ],
    },
    {
        "id": 5, "title": "Hands Together",
        "new": "Left hand holds C or G while the right hand moves",
        "parts": [
            {"name": "A", "title": "Whole-note bass", "count": 10, "bars": 4,
             "mode": "together", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_ONLY, "bass": "whole", "tempo": 56},
            {"name": "B", "title": "Half-note bass", "count": 10, "bars": 4,
             "mode": "together", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_SKIPS, "bass": "half", "tempo": 56},
            {"name": "C", "title": "Eight-bar duets for two hands", "count": 10, "bars": 8,
             "mode": "together", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
             "rhythms": "quarter", "motion": STEPS_SKIPS, "bass": "half", "tempo": 60,
             "repeat_prob": 0.5},
        ],
    },
    # Units 6-10 are specified here so later builds follow the same plan.
    {"id": 6, "title": "Middle C Position", "new": "Both thumbs on middle C; notes near the middle of the grand staff",
     "parts": [
         {"name": "A", "title": "Reading across the middle", "count": 12, "bars": 4,
          "mode": "alt", "rh": "RH_MC", "lh": "LH_MC", "meter": "4/4",
          "rhythms": "quarter", "motion": STEPS_SKIPS, "tempo": 60},
         {"name": "B", "title": "Longer phrases", "count": 12, "bars": 8,
          "mode": "alt", "rh": "RH_MC", "lh": "LH_MC", "meter": "3/4",
          "rhythms": "basic", "motion": STEPS_SKIPS, "tempo": 72, "repeat_prob": 0.4},
         {"name": "C", "title": "Eight bars in 4/4", "count": 8, "bars": 8,
          "mode": "alt", "rh": "RH_MC", "lh": "LH_MC", "meter": "4/4",
          "rhythms": "q_rich", "motion": STEPS_SKIPS, "tempo": 66, "repeat_prob": 0.4},
     ]},
    {"id": 7, "title": "Rests and Ties", "new": "Quarter, half and whole rests; ties across the bar line",
     "parts": [
         {"name": "A", "title": "Rests in the right hand", "count": 10, "bars": 4,
          "mode": "RH", "rh": "RH_C", "meter": "4/4", "rhythms": "q_rich",
          "motion": STEPS_SKIPS, "tempo": 60, "rest_prob": 0.18},
         {"name": "B", "title": "Rests in the left hand", "count": 10, "bars": 4,
          "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "q_rich",
          "motion": STEPS_SKIPS, "tempo": 60, "rest_prob": 0.18},
         {"name": "C", "title": "Ties across the bar line", "count": 10, "bars": 8,
          "mode": "alt", "rh": "RH_C", "lh": "LH_C", "meter": "4/4", "rhythms": "q_rich",
          "motion": STEPS_SKIPS, "tempo": 66, "tie_prob": 0.35, "rest_prob": 0.08,
          "repeat_prob": 0.3},
         {"name": "D", "title": "Rests and ties, hands together", "count": 8, "bars": 8,
          "mode": "together", "rh": "RH_C", "lh": "LH_C", "meter": "3/4", "rhythms": "basic",
          "motion": STEPS_SKIPS, "bass": "whole", "tempo": 72, "tie_prob": 0.3,
          "rest_prob": 0.1, "repeat_prob": 0.3},
     ]},
    {"id": 8, "title": "G Position", "new": "Moving the hands to G; fourths and fifths",
     "parts": [
         {"name": "A", "title": "Right hand in G", "count": 10, "bars": 4,
          "mode": "RH", "rh": "RH_G", "meter": "4/4", "rhythms": "quarter",
          "motion": UP_TO_FIFTH, "tempo": 60, "tonic": G4},
         {"name": "B", "title": "Hands together in G", "count": 12, "bars": 8,
          "mode": "together", "rh": "RH_G", "lh": "LH_G", "meter": "4/4",
          "rhythms": "quarter", "motion": UP_TO_FIFTH, "bass": "half", "tempo": 60,
          "tonic": G4, "repeat_prob": 0.4},
         {"name": "C", "title": "Left hand in G", "count": 8, "bars": 4,
          "mode": "LH", "lh": "LH_G", "meter": "3/4", "rhythms": "basic",
          "motion": UP_TO_FIFTH, "tempo": 72, "tonic": G4},
     ]},
    {"id": 9, "title": "Eighth Notes", "new": "Two eighths per beat; counting 1-and-2-and",
     "parts": [
         {"name": "A", "title": "Eighths in the right hand", "count": 12, "bars": 4,
          "mode": "RH", "rh": "RH_C", "meter": "4/4", "rhythms": "eighths",
          "motion": STEPS_SKIPS, "tempo": 60},
         {"name": "B", "title": "Eighths, hands together", "count": 12, "bars": 8,
          "mode": "together", "rh": "RH_C", "lh": "LH_C", "meter": "4/4",
          "rhythms": "eighths", "motion": STEPS_SKIPS, "bass": "half", "tempo": 60,
          "repeat_prob": 0.4},
         {"name": "C", "title": "Eighths in the left hand", "count": 8, "bars": 4,
          "mode": "LH", "lh": "LH_C", "meter": "4/4", "rhythms": "eighths",
          "motion": STEPS_SKIPS, "tempo": 60},
     ]},
    {"id": 10, "title": "Sharps, Flats and Review",
     "new": "Sharps, flats and key signatures (D and F positions); review of Units 1-9",
     "parts": [
         dict(name="A", title="D position: F-sharp", count=10, bars=4, mode="RH", rh="RH_D",
              meter="4/4", rhythms="quarter", motion=STEPS_SKIPS, tempo=60, tonic=D4, **KEY_D),
         dict(name="B", title="D position, left hand", count=8, bars=4, mode="LH", lh="LH_D",
              meter="4/4", rhythms="quarter", motion=STEPS_SKIPS, tempo=60, tonic=D4, **KEY_D),
         dict(name="C", title="F position: B-flat", count=10, bars=4, mode="RH", rh="RH_F",
              meter="4/4", rhythms="quarter", motion=STEPS_SKIPS, tempo=60, tonic=F4, **KEY_F),
         dict(name="D", title="Review: everything together", count=10, bars=8, mode="together",
              rh="RH_C", lh="LH_C", meter="4/4", rhythms=["q_rich", "eighths"], motion=UP_TO_FIFTH,
              bass="half", tempo=60, tie_prob=0.15, rest_prob=0.06, repeat_prob=0.4),
     ]},
]


# =========================================================================== Volume 2
# Level 2: the hands leave the five-finger position. New part options:
#   rh_positions / lh_positions: positions the hand moves between (first = home)
#   shift_every (bars, default 2), shift_prob, shift_motion (intervals allowed at a shift)
#   extend: 1 lets each hand stretch one key beyond its position (finger 1 or 5)
#   artic: {"slur": p, "stacc": p} per two-bar segment; dynamics: True
C_SHIFT_RH = ["RH_C", "RH_G"]
C_SHIFT_LH = ["LH_C", "LH_G"]
ART = {"slur": 0.5, "stacc": 0.35}
ART_LIGHT = {"slur": 0.35, "stacc": 0.2}

VOLUME2 = [
    {"id": 1, "title": "Moving the Hand", "new": "Hand shifts between C and G positions; a finger number marks every move",
     "parts": [
         dict(name="A", title="Right hand moves between C and G", count=10, bars=4, mode="RH",
              rh_positions=C_SHIFT_RH, shift_prob=0.9, meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Left hand moves between C and G", count=10, bars=4, mode="LH",
              lh_positions=C_SHIFT_LH, shift_prob=0.9, meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Both hands on the move", count=10, bars=8, mode="alt",
              rh_positions=C_SHIFT_RH, lh_positions=C_SHIFT_LH, meter="4/4", rhythms="q_rich",
              motion=UP_TO_FIFTH, tempo=66, repeat_prob=0.3),
     ]},
    {"id": 2, "title": "Stretching", "new": "Reaching one key beyond the position with the thumb or little finger",
     "parts": [
         dict(name="A", title="Right-hand stretches", count=10, bars=4, mode="RH", rh="RH_C", extend=1,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Left-hand stretches", count=10, bars=4, mode="LH", lh="LH_C", extend=1,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Stretches, hands together", count=10, bars=8, mode="together", rh="RH_C",
              lh="LH_C", extend=1, bass="half", meter="4/4", rhythms="q_rich", motion=UP_TO_FIFTH,
              tempo=60, repeat_prob=0.4),
     ]},
    {"id": 3, "title": "Dotted Quarter Notes", "new": "The dotted quarter note followed by an eighth: 'long-short'",
     "parts": [
         dict(name="A", title="Dotted rhythms, right hand", count=10, bars=4, mode="RH", rh="RH_C",
              meter="4/4", rhythms="dotted", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Dotted rhythms, left hand", count=8, bars=4, mode="LH", lh="LH_C",
              meter="4/4", rhythms="dotted", motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Dotted rhythms in 3/4", count=6, bars=4, mode="RH", rh="RH_C",
              meter="3/4", rhythms="dotted34", motion=STEPS_SKIPS, tempo=72),
         dict(name="D", title="Hands together, with shifts", count=8, bars=8, mode="together",
              rh_positions=C_SHIFT_RH, lh="LH_C", bass="half", meter="4/4", rhythms=["dotted", "q_rich"],
              motion=UP_TO_FIFTH, tempo=60, repeat_prob=0.4),
     ]},
    {"id": 4, "title": "Legato and Staccato", "new": "Slurs (smooth and connected) and staccato dots (short and detached)",
     "parts": [
         dict(name="A", title="Slurs and dots, right hand", count=10, bars=4, mode="RH",
              rh_positions=C_SHIFT_RH, shift_prob=0.5, meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS,
              tempo=66, artic=ART),
         dict(name="B", title="Slurs and dots, hands taking turns", count=10, bars=8, mode="alt",
              rh_positions=C_SHIFT_RH, lh_positions=C_SHIFT_LH, shift_prob=0.4, meter="4/4",
              rhythms="q_rich", motion=UP_TO_FIFTH, tempo=66, artic=ART, repeat_prob=0.3),
         dict(name="C", title="Hands together in 3/4", count=10, bars=8, mode="together", rh="RH_C",
              lh="LH_C", bass="whole", meter="3/4", rhythms=["basic", "e34"], motion=STEPS_SKIPS,
              tempo=72, artic=ART, repeat_prob=0.4),
     ]},
    {"id": 5, "title": "Loud and Soft", "new": "Dynamics: p, mp, mf, f; getting louder and softer",
     "parts": [
         dict(name="A", title="Dynamics, right hand", count=10, bars=4, mode="RH",
              rh_positions=C_SHIFT_RH, shift_prob=0.5, meter="4/4", rhythms=["q_rich", "dotted"],
              motion=STEPS_SKIPS, tempo=66, dynamics=True, artic=ART_LIGHT),
         dict(name="B", title="Dynamics, left hand", count=8, bars=4, mode="LH",
              lh_positions=C_SHIFT_LH, shift_prob=0.5, meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=66, dynamics=True),
         dict(name="C", title="Shaping a phrase, hands together", count=12, bars=8, mode="together",
              rh_positions=C_SHIFT_RH, lh="LH_C", bass="half", meter="4/4", rhythms=["q_rich", "dotted"],
              motion=UP_TO_FIFTH, tempo=66, dynamics=True, artic=ART_LIGHT, repeat_prob=0.4),
     ]},
    {"id": 6, "title": "G Major", "new": "Key signature of one sharp (F-sharp); G and D positions",
     "parts": [
         dict(name="A", title="Right hand in G major", count=10, bars=4, mode="RH",
              rh_positions=["RH_G", "RH_D"], meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS,
              tempo=60, tonic=G4, **KEY_G),
         dict(name="B", title="Left hand in G major", count=8, bars=4, mode="LH",
              lh_positions=["LH_G", "LH_D"], meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS,
              tempo=60, tonic=G4, **KEY_G),
         dict(name="C", title="G major, hands together", count=12, bars=8, mode="together",
              rh_positions=["RH_G", "RH_D"], lh="LH_G", bass="half", meter="4/4",
              rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH, tempo=66, tonic=G4,
              dynamics=True, artic=ART_LIGHT, repeat_prob=0.4, **KEY_G),
     ]},
    {"id": 7, "title": "F Major", "new": "Key signature of one flat (B-flat); F and C positions",
     "parts": [
         dict(name="A", title="Right hand in F major", count=10, bars=4, mode="RH",
              rh_positions=["RH_F", "RH_C"], meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS,
              tempo=60, tonic=F4, **KEY_F),
         dict(name="B", title="Left hand in F major", count=8, bars=4, mode="LH",
              lh_positions=["LH_F", "LH_C"], meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS,
              tempo=60, tonic=F4, **KEY_F),
         dict(name="C", title="F major, hands together", count=12, bars=8, mode="together",
              rh_positions=["RH_F", "RH_C"], lh="LH_F", bass="half", meter="4/4",
              rhythms=["q_rich", "eighths"], motion=UP_TO_FIFTH, tempo=66, tonic=F4,
              dynamics=True, artic=ART_LIGHT, repeat_prob=0.4, **KEY_F),
     ]},
    {"id": 8, "title": "A Minor", "new": "Minor keys; A minor, the relative minor of C major",
     "parts": [
         dict(name="A", title="Right hand in A minor", count=10, bars=4, mode="RH", rh="RH_A",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=A4, **KEY_AM),
         dict(name="B", title="Left hand in A minor", count=8, bars=4, mode="LH", lh="LH_A",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=A4, **KEY_AM),
         dict(name="C", title="A minor, hands together in 3/4", count=12, bars=8, mode="together",
              rh_positions=["RH_A", "RH_Enat"], lh="LH_A", bass="whole", meter="3/4",
              rhythms=["basic", "dotted34"], motion=UP_TO_FIFTH, tempo=72, tonic=A4,
              dynamics=True, artic=ART_LIGHT, repeat_prob=0.4, **KEY_AM),
     ]},
    {"id": 9, "title": "E Minor and D Minor", "new": "The relative minors of G major (E minor) and F major (D minor)",
     "parts": [
         dict(name="A", title="E minor, right hand", count=8, bars=4, mode="RH", rh="RH_E",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=E4, **KEY_EM),
         dict(name="B", title="E minor, hands together", count=8, bars=8, mode="together", rh="RH_E",
              lh="LH_E", bass="half", meter="4/4", rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH,
              tempo=66, tonic=E4, dynamics=True, repeat_prob=0.4, **KEY_EM),
         dict(name="C", title="D minor, right hand", count=8, bars=4, mode="RH", rh="RH_Dm",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=D4, **KEY_DM),
         dict(name="D", title="D minor, hands together", count=8, bars=8, mode="together", rh="RH_Dm",
              lh="LH_Dm", bass="whole", meter="3/4", rhythms=["basic", "dotted34"], motion=UP_TO_FIFTH,
              tempo=72, tonic=D4, dynamics=True, artic=ART_LIGHT, repeat_prob=0.4, **KEY_DM),
     ]},
    {"id": 10, "title": "Review", "new": "Everything in Volume 2 together",
     "parts": [
         dict(name="A", title="G major: shifts, dots and dynamics", count=8, bars=8, mode="together",
              rh_positions=["RH_G", "RH_D"], lh="LH_G", bass="half", meter="4/4",
              rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH, tempo=66, tonic=G4, dynamics=True,
              artic=ART, repeat_prob=0.3, **KEY_G),
         dict(name="B", title="F major: hands taking turns", count=8, bars=8, mode="alt",
              rh_positions=["RH_F", "RH_C"], lh_positions=["LH_F", "LH_C"], meter="4/4",
              rhythms=["q_rich", "eighths"], motion=UP_TO_FIFTH, tempo=66, tonic=F4, artic=ART,
              repeat_prob=0.3, **KEY_F),
         dict(name="C", title="A minor waltzes", count=8, bars=8, mode="together",
              rh_positions=["RH_A", "RH_Enat"], lh="LH_A", bass="whole", meter="3/4",
              rhythms=["basic", "dotted34", "e34"], motion=UP_TO_FIFTH, tempo=72, tonic=A4,
              dynamics=True, artic=ART_LIGHT, repeat_prob=0.3, **KEY_AM),
         dict(name="D", title="C major: everything", count=8, bars=8, mode="together",
              rh_positions=C_SHIFT_RH, lh="LH_C", extend=1, bass="half", meter="4/4",
              rhythms=["q_rich", "eighths", "dotted"], motion=UP_TO_FIFTH, tempo=66, dynamics=True,
              artic=ART_LIGHT, tie_prob=0.15, rest_prob=0.06, repeat_prob=0.3),
     ]},
]


# =========================================================================== Volume 3
# Level 3: two voices. The left hand gets its own music. New part options:
#   chords: chords the left hand may use, from CHORDS (e.g. ["I", "IV", "V7"])
#   bass: "broken" (4/4: low-middle-high-middle quarters; 3/4: low-middle-high), one chord per bar
#   require_chords: chords that must appear in every exercise
#   chord_fingers: True prints a finger number on the first note of every new chord shape
# Chord shapes are built on the left-hand position's lowest note (the tonic): "voicing" lists the
# three notes in steps above it, "tones" the scale degrees (0 = tonic) that belong to the chord.
CHORDS = {
    "I":  {"tones": (0, 2, 4), "voicing": (0, 2, 4)},      # C E G   fingers 5 3 1
    "IV": {"tones": (3, 5, 0), "voicing": (0, 3, 5)},      # C F A   fingers 5 2 1
    "V7": {"tones": (4, 6, 1, 3), "voicing": (-1, 3, 4)},  # B F G   fingers 5 2 1 (G7 without its D)
}
CHORD_ORDER = ["I", "V7", "IV"]
# Chord progressions are chosen bar by bar with these weights (V7 never goes to IV).
CHORD_MOVES = {"I": {"I": 1.0, "IV": 2.0, "V7": 2.0},
               "IV": {"I": 1.5, "IV": 0.7, "V7": 2.5},
               "V7": {"I": 3.0, "V7": 1.0}}
# Bass patterns: (durations in eighths, index into the chord's voicing: 0 low, 1 middle, 2 high)
BASS_PATTERNS = {
    ("broken", "4/4"): ([2, 2, 2, 2], [0, 1, 2, 1]),
    ("broken", "3/4"): ([2, 2, 2], [0, 1, 2]),
}
CHORD_MAX_LEAP = 5  # largest leap (a sixth) in a broken-chord bass, including into the next bar
BASS_PATTERNS.update({
    ("alberti", "4/4"): ([1] * 8, [0, 2, 1, 2, 0, 2, 1, 2]),   # C G E G C G E G
    ("alberti", "3/4"): ([1] * 6, [0, 2, 1, 2, 1, 2]),         # C G E G E G
    ("broken", "6/8"): ([1] * 6, [0, 1, 2, 1, 2, 1]),          # C E G E G E (rolling eighths)
    ("lilt", "6/8"): ([2, 1, 2, 1], [0, 2, 1, 2]),             # C(quarter) G(eighth) E G: long-short
})

# 6/8: two beats of three eighths. Durations are in eighths, so a bar is 6.
R68 = {
    "basic68": [[3, 3], [6], [2, 1, 3], [3, 2, 1], [2, 1, 2, 1]],
    "e68":     [[1, 1, 1, 3], [3, 1, 1, 1], [1, 1, 1, 2, 1], [2, 1, 3], [3, 3]],
}
CADENCE68 = [[6], [3, 3], [2, 1, 3]]
FINAL68 = [[6]]

# Volume 3 keys and positions
A2_ = 19
E5_, F5 = 37, 38
POSITIONS.update({
    "RH_Bb": {"hand": "RH", "low": B4, "high": F5, "label": "Right hand B-flat position", "acc": {B4: "es", E5_: "es"}},
    "LH_Bb": {"hand": "LH", "low": B2, "high": F3, "label": "Left hand B-flat position", "acc": {B2: "es", E3: "es"}},
    "RH_Bm": {"hand": "RH", "low": B4, "high": F5, "label": "Right hand B position", "acc": {C5: "is", F5: "is"}},
    "LH_Bm": {"hand": "LH", "low": B2, "high": F3, "label": "Left hand B position", "acc": {C3: "is", F3: "is"}},
    "RH_Gm": {"hand": "RH", "low": G4, "high": D5, "label": "Right hand G position", "acc": {B4: "es"}},
    "LH_Gm": {"hand": "LH", "low": G2, "high": D3, "label": "Left hand G position", "acc": {B2: "es"}},
})
KEY_BB = {"key": "bes \\major", "key_acc": {"b": "es", "e": "es"}}
KEY_BM = {"key": "b \\minor", "key_acc": {"f": "is", "c": "is"}}
KEY_GM = {"key": "g \\minor", "key_acc": {"b": "es", "e": "es"}}

VOLUME3 = [
    {"id": 1, "title": "Broken Chords", "new": "Triads; the left hand plays I, IV and V7 one note at a time",
     "parts": [
         dict(name="A", title="Two chords under long notes", count=8, bars=4, mode="together", rh="RH_C",
              lh="LH_C", chords=["I", "V7"], bass="broken", chord_fingers=True, meter="4/4",
              rhythms="half", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Adding the IV chord", count=10, bars=4, mode="together", rh="RH_C",
              lh="LH_C", chords=["I", "IV", "V7"], require_chords=["IV"], bass="broken", chord_fingers=True,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Waltz bass in G major", count=10, bars=8, mode="together", rh="RH_G",
              lh="LH_G", chords=["I", "IV", "V7"], bass="broken", chord_fingers=True, meter="3/4",
              rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=72, tonic=G4, dynamics=True,
              repeat_prob=0.4, **KEY_G),
         dict(name="D", title="Eight bars in F major", count=8, bars=8, mode="together", rh="RH_F",
              lh="LH_F", chords=["I", "IV", "V7"], bass="broken", chord_fingers=True, meter="4/4",
              rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH, tempo=66, tonic=F4, artic=ART_LIGHT,
              repeat_prob=0.4, **KEY_F),
     ]},
    # Units 2-10 are planned here (titles feed the contents page); each gets its parts when it is built.
    {"id": 2, "title": "The Alberti Bass", "new": "Broken chords in eighth notes: low, high, middle, high",
     "parts": [
         dict(name="A", title="Alberti bass under long notes", count=8, bars=4, mode="together", rh="RH_C",
              lh="LH_C", chords=["I", "V7"], bass="alberti", bass_leap=6, chord_fingers=True, meter="4/4",
              rhythms="half", motion=STEPS_SKIPS, tempo=56),
         dict(name="B", title="I, IV and V7 in C major", count=10, bars=8, mode="together", rh="RH_C",
              lh="LH_C", chords=["I", "IV", "V7"], bass="alberti", bass_leap=6, chord_fingers=True,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, dynamics=True, repeat_prob=0.4),
         dict(name="C", title="Alberti bass in 3/4", count=8, bars=8, mode="together", rh="RH_G",
              lh="LH_G", chords=["I", "IV", "V7"], bass="alberti", bass_leap=6, chord_fingers=True,
              meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=66, tonic=G4,
              artic=ART_LIGHT, repeat_prob=0.4, **KEY_G),
         dict(name="D", title="F major, the right hand on the move", count=8, bars=8, mode="together",
              rh_positions=["RH_F", "RH_C"], lh="LH_F", chords=["I", "IV", "V7"], bass="alberti", bass_leap=6,
              chord_fingers=True, meter="4/4", rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH, tempo=60,
              tonic=F4, dynamics=True, artic=ART_LIGHT, repeat_prob=0.3, **KEY_F),
     ]},
    {"id": 3, "title": "Six-Eight Time", "new": "6/8: two beats in a bar, each beat split into three eighths",
     "parts": [
         dict(name="A", title="Two beats in a bar", count=10, bars=4, mode="RH", rh="RH_C", meter="6/8",
              rhythms="basic68", motion=STEPS_SKIPS, tempo=50, tempo_unit="4."),
         dict(name="B", title="6/8 in the left hand", count=8, bars=4, mode="LH", lh="LH_C", meter="6/8",
              rhythms="basic68", motion=STEPS_SKIPS, tempo=50, tempo_unit="4."),
         dict(name="C", title="A lilting bass in G major", count=10, bars=8, mode="together", rh="RH_G",
              lh="LH_G", chords=["I", "IV", "V7"], bass="lilt", bass_leap=6, chord_fingers=True, meter="6/8",
              rhythms="basic68", motion=STEPS_SKIPS, tempo=50, tempo_unit="4.", tonic=G4, repeat_prob=0.4, **KEY_G),
         dict(name="D", title="Rolling eighths in F major", count=8, bars=8, mode="together", rh="RH_F",
              lh="LH_F", chords=["I", "IV", "V7"], bass="broken", bass_leap=6, chord_fingers=True, meter="6/8",
              rhythms=["basic68", "e68"], motion=STEPS_SKIPS, tempo=46, tempo_unit="4.", tonic=F4, dynamics=True,
              artic=ART_LIGHT, repeat_prob=0.3, **KEY_F),
     ]},
    {"id": 4, "title": "D Major", "new": "Two sharps (F-sharp and C-sharp); D major and its chords",
     "parts": [
         dict(name="A", title="Right hand in D major", count=8, bars=4, mode="RH", rh="RH_D", extend=1,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=D4, **KEY_D),
         dict(name="B", title="D major with an Alberti bass", count=10, bars=8, mode="together",
              rh_positions=["RH_D", "RH_A"], lh="LH_D", chords=["I", "IV", "V7"], bass="alberti", bass_leap=6,
              chord_fingers=True, meter="4/4", rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=60,
              tonic=D4, dynamics=True, repeat_prob=0.4, **KEY_D),
         dict(name="C", title="A waltz in D major", count=8, bars=8, mode="together", rh="RH_D", extend=1,
              lh="LH_D", chords=["I", "IV", "V7"], bass="broken", chord_fingers=True, meter="3/4",
              rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=72, tonic=D4, artic=ART_LIGHT,
              repeat_prob=0.4, **KEY_D),
         dict(name="D", title="D major in 6/8", count=8, bars=8, mode="together", rh="RH_D", extend=1,
              lh="LH_D", chords=["I", "IV", "V7"], bass="lilt", bass_leap=6, chord_fingers=True, meter="6/8",
              rhythms=["basic68", "e68"], motion=STEPS_SKIPS, tempo=50, tempo_unit="4.", tonic=D4,
              dynamics=True, repeat_prob=0.3, **KEY_D),
     ]},
    {"id": 5, "title": "B-flat Major", "new": "Two flats (B-flat and E-flat); B-flat major and its chords",
     "parts": [
         dict(name="A", title="Right hand in B-flat major", count=8, bars=4, mode="RH",
              rh_positions=["RH_Bb", "RH_F"], shift_prob=0.6, meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=60, tonic=B4, **KEY_BB),
         dict(name="B", title="Left hand in B-flat major", count=8, bars=4, mode="LH", lh="LH_Bb",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=B4, **KEY_BB),
         dict(name="C", title="Alberti bass in B-flat major", count=10, bars=8, mode="together", rh="RH_Bb",
              lh="LH_Bb", chords=["I", "IV", "V7"], bass="alberti", bass_leap=6, chord_fingers=True,
              meter="4/4", rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=60, tonic=B4,
              dynamics=True, repeat_prob=0.4, **KEY_BB),
         dict(name="D", title="A B-flat waltz on the move", count=8, bars=8, mode="together",
              rh_positions=["RH_F", "RH_Bb"], lh="LH_Bb", chords=["I", "IV", "V7"], bass="broken", bass_leap=6,
              chord_fingers=True, meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=72,
              tonic=B4, artic=ART_LIGHT, repeat_prob=0.3, **KEY_BB),
     ]},
    {"id": 6, "title": "Accidentals", "new": "Sharps, flats and naturals inside the bar; the raised 7th in minor keys", "parts": []},
    {"id": 7, "title": "Two Notes at Once", "new": "Right-hand thirds and sixths: reading two notes together", "parts": []},
    {"id": 8, "title": "Two Independent Voices", "new": "A left-hand melody against the right hand: contrary and parallel motion", "parts": []},
    {"id": 9, "title": "Imitation", "new": "Simple counterpoint: one hand answers the other with the same tune", "parts": []},
    {"id": 10, "title": "Review", "new": "Everything in Volume 3 together", "parts": []},
]
