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
    {"id": 6, "title": "Accidentals", "new": "Sharps, flats and naturals inside the bar; the raised 7th in minor keys",
     "parts": [
         dict(name="A", title="A minor: G-sharp", count=8, bars=4, mode="together", rh="RH_A", extend=1,
              lh="LH_A", chords=["I", "IV", "V7"], minor=True, beat_tones=True, lead_weight=20, bass="broken",
              chord_fingers=True, meter="4/4", rhythms=["quarter", "q_rich"], motion=STEPS_SKIPS, tempo=60, tonic=A4, **KEY_AM),
         dict(name="B", title="E minor: D-sharp", count=8, bars=8, mode="together", rh="RH_E", extend=1,
              lh="LH_E", chords=["I", "IV", "V7"], minor=True, beat_tones=True, lead_weight=20, bass="broken", bass_leap=6, chord_fingers=True,
              meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=72, tonic=E4,
              dynamics=True, repeat_prob=0.4, **KEY_EM),
         dict(name="C", title="B minor: A-sharp", count=8, bars=8, mode="together", rh="RH_Bm", extend=1,
              lh="LH_Bm", chords=["I", "IV", "V7"], minor=True, beat_tones=True, lead_weight=6, bass="alberti", bass_leap=6, chord_fingers=True,
              meter="4/4", rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=60, tonic=B4,
              repeat_prob=0.4, **KEY_BM),
         dict(name="D", title="G minor: F-sharp", count=8, bars=8, mode="together", rh="RH_Gm", extend=1,
              lh="LH_Gm", chords=["I", "IV", "V7"], minor=True, beat_tones=True, lead_weight=6, bass="lilt", bass_leap=6, chord_fingers=True,
              meter="6/8", rhythms=["basic68", "e68"], motion=STEPS_SKIPS, tempo=50, tempo_unit="4.", tonic=G4,
              artic=ART_LIGHT, dynamics=True, repeat_prob=0.3, **KEY_GM),
     ]},
    {"id": 7, "title": "Two Notes at Once", "new": "Right-hand thirds and sixths: reading two notes together",
     "parts": [
         dict(name="A", title="Thirds in the right hand", count=10, bars=4, mode="RH", rh="RH_C", meter="4/4",
              rhythms="q_rich", motion=STEPS_SKIPS, tempo=56, dyads={"prob": 0.4, "intervals": (2,), "min": 2}),
         dict(name="B", title="Thirds over broken chords", count=8, bars=8, mode="together", rh="RH_C",
              lh="LH_C", chords=["I", "IV", "V7"], beat_tones=True, bass="broken", chord_fingers=True,
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, dynamics=True, repeat_prob=0.4,
              dyads={"prob": 0.4, "intervals": (2,), "min": 3}),
         dict(name="C", title="Thirds and sixths in F major", count=8, bars=8, mode="together", rh="RH_F",
              extend=1, lh="LH_F", chords=["I", "IV", "V7"], beat_tones=True, bass="broken", bass_leap=6,
              chord_fingers=True, meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=69,
              tonic=F4, artic=ART_LIGHT, repeat_prob=0.4,
              dyads={"prob": 0.5, "intervals": (2, 5), "weights": {5: 4.0}, "min": 3}, **KEY_F),
         dict(name="D", title="Two notes at once in 6/8", count=8, bars=8, mode="together", rh="RH_D",
              extend=1, lh="LH_D", chords=["I", "IV", "V7"], beat_tones=True, bass="lilt", bass_leap=6,
              chord_fingers=True, meter="6/8", rhythms="basic68", motion=STEPS_SKIPS, tempo=50, tempo_unit="4.",
              tonic=D4, dynamics=True, repeat_prob=0.3, dyads={"prob": 0.45, "intervals": (2, 5), "weights": {5: 4.0}, "min": 3}, **KEY_D),
     ]},
    {"id": 8, "title": "Two Independent Voices", "new": "A left-hand melody against the right hand: contrary and parallel motion",
     "parts": [
         dict(name="A", title="A second voice in the left hand", count=10, bars=4, mode="duet", rh="RH_C",
              lh="LH_C", meter="4/4", rhythms="q_rich", counter_rhythms="half", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="The tune in the left hand", count=8, bars=4, mode="duet", lead="LH", rh="RH_C",
              lh="LH_C", meter="4/4", rhythms="q_rich", counter_rhythms="half", motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Two voices in 3/4", count=8, bars=8, mode="duet", rh="RH_G", lh="LH_G",
              meter="3/4", rhythms=["basic", "dotted34"], counter_rhythms="basic", motion=STEPS_SKIPS, tempo=72,
              tonic=G4, dynamics=True, repeat_prob=0.3, **KEY_G),
         dict(name="D", title="Quarter against quarter", count=8, bars=8, mode="duet", rh="RH_F", lh="LH_F",
              meter="4/4", rhythms="q_rich", counter_rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=F4,
              dynamics=True, artic=ART_LIGHT, repeat_prob=0.3, **KEY_F),
     ]},
    {"id": 9, "title": "Imitation", "new": "Simple counterpoint: one hand answers the other with the same tune",
     "parts": [
         dict(name="A", title="The left hand answers", count=10, bars=4, mode="imitate", rh="RH_C", lh="LH_C",
              meter="4/4", rhythms="q_rich", counter_rhythms="half", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Two tunes, two answers", count=8, bars=8, mode="imitate", rh="RH_G", lh="LH_G",
              meter="4/4", rhythms="q_rich", counter_rhythms="half", motion=STEPS_SKIPS, tempo=60, tonic=G4,
              **KEY_G),
         dict(name="C", title="Imitation in 3/4", count=8, bars=8, mode="imitate", rh="RH_F", lh="LH_F",
              meter="3/4", rhythms=["basic", "dotted34"], counter_rhythms="basic", motion=STEPS_SKIPS, tempo=72,
              tonic=F4, dynamics=True, **KEY_F),
         dict(name="D", title="Imitation in 6/8", count=8, bars=8, mode="imitate", rh="RH_D", lh="LH_D",
              meter="6/8", rhythms="basic68", counter_rhythms="basic68", motion=STEPS_SKIPS, tempo=50,
              tempo_unit="4.", tonic=D4, dynamics=True, **KEY_D),
     ]},
    {"id": 10, "title": "Review", "new": "Everything in Volume 3 together",
     "parts": [
         dict(name="A", title="D major: Alberti bass and thirds", count=8, bars=8, mode="together", rh="RH_D",
              extend=1, lh="LH_D", chords=["I", "IV", "V7"], beat_tones=True, bass="alberti", bass_leap=6,
              chord_fingers=True, meter="4/4", rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=60,
              tonic=D4, dynamics=True, repeat_prob=0.3, dyads={"prob": 0.3, "intervals": (2,), "min": 2},
              **KEY_D),
         dict(name="B", title="B-flat major in 6/8", count=8, bars=8, mode="together", rh="RH_Bb", lh="LH_Bb",
              chords=["I", "IV", "V7"], beat_tones=True, bass="lilt", bass_leap=6, chord_fingers=True,
              meter="6/8", rhythms=["basic68", "e68"], motion=STEPS_SKIPS, tempo=50, tempo_unit="4.", tonic=B4,
              artic=ART_LIGHT, repeat_prob=0.3, **KEY_BB),
         dict(name="C", title="A B minor waltz", count=6, bars=8, mode="together", rh="RH_Bm", extend=1,
              lh="LH_Bm", chords=["I", "IV", "V7"], minor=True, beat_tones=True, lead_weight=20, bass="broken",
              bass_leap=6, chord_fingers=True, meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS,
              tempo=72, tonic=B4, dynamics=True, repeat_prob=0.3, **KEY_BM),
         dict(name="D", title="Two voices, the tune below", count=6, bars=8, mode="duet", lead="LH", rh="RH_G",
              lh="LH_G", meter="4/4", rhythms="q_rich", counter_rhythms="q_rich", motion=STEPS_SKIPS, tempo=60,
              tonic=G4, dynamics=True, repeat_prob=0.3, **KEY_G),
         dict(name="E", title="Imitation in B-flat major", count=6, bars=8, mode="imitate", rh="RH_Bb",
              lh="LH_Bb", meter="3/4", rhythms=["basic", "dotted34"], counter_rhythms="basic",
              motion=STEPS_SKIPS, tempo=72, tonic=B4, dynamics=True, **KEY_BB),
     ]},
]


# =========================================================================== Volume 4
# Level 4: patterns and keys. New part options (see README):
#   bass "block" / "block2" / "oompah" / "waltz" (LH chords), rh_chords (RH three-note chords),
#   mode "lhtune" + accomp (LH tune, RH after-beat chords), grid=2 (count in sixteenths) + fast_steps,
#   anticip_prob + accents (syncopation), modulate (key changes), meter "2/4".
BASS_PATTERNS.update({
    # "c" = the whole chord, "u" = its upper two notes; the "oom" is the shape's bottom note
    ("block", "4/4"): ([8], ["c"]),
    ("block", "3/4"): ([6], ["c"]),
    ("block", "2/4"): ([4], ["c"]),
    ("block2", "4/4"): ([4, 4], ["c", "c"]),
    ("oompah", "4/4"): ([2, 2, 2, 2], [0, "u", 0, "u"]),
    ("oompah", "2/4"): ([2, 2], [0, "u"]),
    ("waltz", "3/4"): ([2, 2, 2], [0, "u", "u"]),
    ("broken", "2/4"): ([1, 1, 1, 1], [0, 1, 2, 1]),
    ("alberti", "2/4"): ([1, 1, 1, 1], [0, 2, 1, 2]),
})
# Right-hand accompaniment for mode "lhtune": durations in eighths, 1 = chord, 0 = rest
RH_PATTERNS = {
    ("afterbeat", "4/4"): ([2, 2, 2, 2], [0, 1, 0, 1]),
    ("afterbeat", "3/4"): ([2, 2, 2], [0, 1, 1]),
    ("afterbeat", "2/4"): ([2, 2], [0, 1]),
}

# 2/4: two quarter beats (a bar is 4 eighths)
R24 = {
    "basic24": [[4], [2, 2], [3, 1], [2, 1, 1], [1, 1, 2]],
    "e24":     [[1, 1, 1, 1], [2, 1, 1], [1, 1, 2], [2, 2], [3, 1]],
    "synco24": [[1, 2, 1], [1, 3], [1, 2, 1], [2, 2], [1, 1, 2]],
}
CADENCE24 = [[4], [2, 2]]
FINAL24 = [[4]]
# Syncopation in 4/4: notes start between the beats, but the middle of the bar stays visible
R44["synco"] = [[1, 2, 1, 4], [1, 2, 1, 2, 2], [2, 2, 1, 2, 1], [4, 1, 2, 1], [1, 2, 1, 1, 2, 1], [2, 2, 2, 2]]

# Sixteenth-note grid (grid=2): durations in sixteenths; a 2/4 bar is 8, a 4/4 bar 16
R24_16 = {
    "s24":   [[1, 1, 1, 1, 4], [4, 1, 1, 1, 1], [2, 1, 1, 4], [4, 2, 1, 1], [2, 1, 1, 2, 2], [2, 2, 4], [4, 4]],
    "dot24": [[3, 1, 4], [4, 3, 1], [3, 1, 3, 1], [2, 2, 3, 1], [4, 4]],
}
R44_16 = {
    "s44":   [[1, 1, 1, 1, 4, 4, 4], [4, 1, 1, 1, 1, 4, 4], [4, 4, 2, 1, 1, 4], [2, 1, 1, 4, 8],
              [4, 4, 1, 1, 1, 1, 4], [4, 4, 4, 4]],
    "dot44": [[3, 1, 4, 4, 4], [4, 4, 3, 1, 4], [3, 1, 3, 1, 8], [8, 3, 1, 4], [4, 3, 1, 8], [4, 4, 8]],
}
CADENCE24_16 = [[8], [4, 4]]
FINAL24_16 = [[8]]
CADENCE44_16 = [[16], [8, 8], [4, 4, 8]]
FINAL44_16 = [[16]]

# Positions with ledger lines, and positions for three sharps and three flats
C2, D2, E2, F2 = 14, 15, 16, 17
F5_, G5, A5, C6, D6 = 38, 39, 40, 42, 43
POSITIONS.update({
    "RH_C5": {"hand": "RH", "low": C5, "high": G5, "label": "Right hand high C position"},
    "RH_G5": {"hand": "RH", "low": G5, "high": D6, "label": "Right hand high G position"},
    "RH_D5": {"hand": "RH", "low": D5, "high": A5, "label": "Right hand high D position", "acc": {F5_: "is"}},
    "RH_A3": {"hand": "RH", "low": A3, "high": E4, "label": "Right hand below middle C"},
    "LH_C2": {"hand": "LH", "low": C2, "high": G2, "label": "Left hand low C position"},
    "LH_F2": {"hand": "LH", "low": F2, "high": C3, "label": "Left hand low F position"},
    "LH_C4": {"hand": "LH", "low": C4, "high": G4, "label": "Left hand above middle C"},
    "RH_AM": {"hand": "RH", "low": A4, "high": E5, "label": "Right hand A position", "acc": {C5: "is"}},
    "LH_AM": {"hand": "LH", "low": A2, "high": E3, "label": "Left hand A position", "acc": {C3: "is"}},
    "RH_Eb": {"hand": "RH", "low": E4, "high": B4, "label": "Right hand E-flat position",
              "acc": {E4: "es", A4: "es", B4: "es"}},
    "LH_Eb": {"hand": "LH", "low": E3, "high": B3, "label": "Left hand E-flat position",
              "acc": {E3: "es", A3: "es", B3: "es"}},
    "RH_Fsm": {"hand": "RH", "low": F4, "high": C5, "label": "Right hand F-sharp position",
               "acc": {F4: "is", G4: "is", C5: "is"}},
    "LH_Fsm": {"hand": "LH", "low": F3, "high": C4, "label": "Left hand F-sharp position",
               "acc": {F3: "is", G3: "is", C4: "is"}},
    "RH_Cm": {"hand": "RH", "low": C4, "high": G4, "label": "Right hand C minor position", "acc": {E4: "es"}},
    "LH_Cm": {"hand": "LH", "low": C3, "high": G3, "label": "Left hand C minor position", "acc": {E3: "es"}},
})
KEY_A = {"key": "a \\major", "key_acc": {"f": "is", "c": "is", "g": "is"}}
KEY_EB = {"key": "ees \\major", "key_acc": {"b": "es", "e": "es", "a": "es"}}
KEY_FSM = {"key": "fis \\minor", "key_acc": {"f": "is", "c": "is", "g": "is"}}
KEY_CM = {"key": "c \\minor", "key_acc": {"b": "es", "e": "es", "a": "es"}}
OCTAVE_SHIFT = {0: 1.0, 1: 2.0, 2: 2.0, 7: 5.0}   # moving the hand up or down an octave

V4C = ["I", "IV", "V7"]
VOLUME4 = [
    {"id": 1, "title": "Block Chords", "new": "The left hand plays I, IV and V7 as three-note chords: held, oom-pah and waltz",
     "parts": [
         dict(name="A", title="Held chords under a tune", count=8, bars=4, mode="together", rh="RH_C", lh="LH_C",
              chords=V4C, beat_tones=True, bass="block", chord_fingers=True, meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Oom-pah in G major", count=10, bars=8, mode="together", rh="RH_G", lh="LH_G",
              chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="4/4",
              rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=72, tonic=G4, dynamics=True,
              repeat_prob=0.3, **KEY_G),
         dict(name="C", title="Waltz bass in F major", count=8, bars=8, mode="together", rh="RH_F", lh="LH_F",
              chords=V4C, beat_tones=True, bass="waltz", chord_fingers=True, meter="3/4",
              rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=84, tonic=F4, artic=ART_LIGHT,
              repeat_prob=0.3, **KEY_F),
         dict(name="D", title="D major, the right hand on the move", count=8, bars=8, mode="together",
              rh_positions=["RH_D", "RH_A"], lh="LH_D", chords=V4C, beat_tones=True, bass="oompah",
              chord_fingers=True, meter="4/4", rhythms=["q_rich", "dotted"], motion=UP_TO_FIFTH, tempo=72,
              tonic=D4, dynamics=True, repeat_prob=0.3, **KEY_D),
     ]},
    {"id": 2, "title": "Chords in Both Hands", "new": "Right-hand three-note chords; 2/4 time",
     "parts": [
         dict(name="A", title="Chords on the long notes", count=8, bars=4, mode="together", rh="RH_C", lh="LH_C",
              chords=V4C, beat_tones=True, bass="block", chord_fingers=True, meter="4/4",
              rhythms=["half", "q_rich"], motion=STEPS_SKIPS, tempo=60, extend=1,
              rh_chords={"prob": 0.9, "min": 1}),
         dict(name="B", title="A march in 2/4", count=10, bars=8, mode="together", rh="RH_G", lh="LH_G",
              chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="2/4",
              rhythms=["basic24", "e24"], motion=STEPS_SKIPS, tempo=88, tonic=G4, dynamics=True, extend=1,
              repeat_prob=0.3, rh_chords={"prob": 0.8, "where": "strong", "min": 2}, **KEY_G),
         dict(name="C", title="Chorale: chords in both hands", count=8, bars=4, mode="together", rh="RH_F",
              lh="LH_F", chords=V4C, beat_tones=True, bass="block2", chord_fingers=True, meter="4/4",
              rhythms="half", motion=STEPS_SKIPS, tempo=60, tonic=F4, extend=1,
              rh_chords={"prob": 1.0, "min": 3}, **KEY_F),
         dict(name="D", title="A B-flat waltz with chords", count=8, bars=8, mode="together", rh="RH_Bb",
              lh="LH_Bb", chords=V4C, beat_tones=True, bass="waltz", bass_leap=6, chord_fingers=True,
              meter="3/4", rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=84, tonic=B4,
              dynamics=True, repeat_prob=0.3, extend=1, rh_chords={"prob": 0.8, "where": "strong", "min": 2},
              **KEY_BB),
     ]},
    {"id": 3, "title": "High Notes", "new": "Ledger lines above the treble staff, up to D6; the hand moves up an octave",
     "parts": [
         dict(name="A", title="High C position", count=10, bars=4, mode="RH", rh="RH_C5", meter="4/4",
              rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=C5),
         dict(name="B", title="Up and down an octave", count=8, bars=4, mode="RH", rh_positions=["RH_C", "RH_C5"],
              shift_prob=0.9, shift_every=1, shift_motion=OCTAVE_SHIFT, meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="High G position over broken chords", count=8, bars=8, mode="together", rh="RH_G5",
              lh="LH_G", chords=V4C, beat_tones=True, bass="broken", chord_fingers=True, meter="4/4",
              rhythms="q_rich", motion=STEPS_SKIPS, tempo=66, tonic=G4, dynamics=True, repeat_prob=0.3, **KEY_G),
         dict(name="D", title="D major in 2/4, high and low", count=8, bars=8, mode="together",
              rh_positions=["RH_D", "RH_D5"], shift_prob=0.8, shift_motion=OCTAVE_SHIFT, lh="LH_D", chords=V4C,
              beat_tones=True, bass="alberti", bass_leap=6, chord_fingers=True, meter="2/4",
              rhythms=["basic24", "e24"], motion=STEPS_SKIPS, tempo=80, tonic=D4, artic=ART_LIGHT, **KEY_D),
     ]},
    {"id": 4, "title": "Low Notes and the Middle", "new": "Ledger lines below the bass staff, down to C2; both hands near middle C",
     "parts": [
         dict(name="A", title="The left hand down low", count=10, bars=4, mode="LH", lh_positions=["LH_C2", "LH_F2"],
              shift_prob=0.7, meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="The tune in the bass, chords above", count=8, bars=8, mode="lhtune", lh="LH_F2",
              rh="RH_C", chords=V4C, beat_tones=True, accomp="afterbeat", meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=80, tonic=F4, dynamics=True, repeat_prob=0.3, **KEY_F),
         dict(name="C", title="The right hand below middle C", count=8, bars=4, mode="RH", rh="RH_A3",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60),
         dict(name="D", title="Both hands around middle C", count=8, bars=8, mode="alt", rh="RH_A3", lh="LH_C4",
              meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=66, repeat_prob=0.3),
     ]},
    {"id": 5, "title": "Syncopation", "new": "Notes that start between the beats: ties over the beat and the bar line, accents",
     "parts": [
         dict(name="A", title="Off the beat", count=10, bars=4, mode="RH", rh="RH_C", meter="4/4",
              rhythms=["synco", "quarter"], motion=STEPS_SKIPS, tempo=60, accents=True),
         dict(name="B", title="Ragtime in 2/4", count=8, bars=8, mode="together", rh="RH_C", lh="LH_C",
              chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="2/4",
              rhythms=["synco24", "basic24"], motion=STEPS_SKIPS, tempo=72, accents=True, repeat_prob=0.3),
         dict(name="C", title="Across the bar line", count=8, bars=8, mode="together", rh="RH_G", lh="LH_G",
              chords=V4C, beat_tones=True, bass="block2", chord_fingers=True, meter="4/4",
              rhythms="synco", motion=STEPS_SKIPS, tempo=66, tonic=G4, anticip_prob=0.9,
              accents=True, **KEY_G),
         dict(name="D", title="Syncopation in two voices", count=8, bars=8, mode="duet", rh="RH_F", lh="LH_F",
              meter="4/4", rhythms=["synco", "q_rich"], counter_rhythms="half", motion=STEPS_SKIPS, tempo=66,
              tonic=F4, accents=True, repeat_prob=0.3, **KEY_F),
     ]},
    {"id": 6, "title": "Sixteenth Notes", "new": "Four sixteenths, an eighth and two sixteenths, the dotted eighth and sixteenth",
     "parts": [
         dict(name="A", title="Sixteenths in the right hand", count=10, bars=4, mode="RH", rh="RH_C", meter="2/4",
              grid=2, rhythms="s24", fast_steps=True, motion=STEPS_SKIPS, tempo=60),
         dict(name="B", title="Sixteenths in the left hand", count=8, bars=4, mode="LH", lh="LH_C", meter="2/4",
              grid=2, rhythms="s24", fast_steps=True, motion=STEPS_SKIPS, tempo=60),
         dict(name="C", title="Sixteenths over block chords", count=8, bars=8, mode="together", rh="RH_G",
              lh="LH_G", chords=V4C, beat_tones=True, bass="block2", chord_fingers=True, meter="4/4", grid=2,
              rhythms="s44", fast_steps=True, motion=STEPS_SKIPS, tempo=60, tonic=G4, repeat_prob=0.3, **KEY_G),
         dict(name="D", title="Dotted eighth and sixteenth", count=8, bars=8, mode="together", rh="RH_F",
              lh="LH_F", chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="2/4", grid=2,
              rhythms=["dot24", "s24"], fast_steps=True, motion=STEPS_SKIPS, tempo=66, tonic=F4, dynamics=True,
              repeat_prob=0.3, **KEY_F),
     ]},
    {"id": 7, "title": "Three Sharps and Three Flats", "new": "A major, E-flat major, F-sharp minor and C minor",
     "parts": [
         dict(name="A", title="A major", count=8, bars=8, mode="together", rh="RH_AM", lh="LH_AM", chords=V4C,
              beat_tones=True, bass="alberti", bass_leap=6, chord_fingers=True, meter="4/4",
              rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=60, tonic=A4, dynamics=True,
              repeat_prob=0.3, **KEY_A),
         dict(name="B", title="E-flat major waltz", count=8, bars=8, mode="together", rh="RH_Eb", lh="LH_Eb",
              chords=V4C, beat_tones=True, bass="waltz", bass_leap=6, chord_fingers=True, meter="3/4",
              rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=80, tonic=E4, artic=ART_LIGHT,
              repeat_prob=0.3, **KEY_EB),
         dict(name="C", title="F-sharp minor: E-sharp", count=9, bars=8, mode="together", rh="RH_Fsm", extend=1,
              lh="LH_Fsm", chords=V4C, minor=True, beat_tones=True, lead_weight=20, bass="broken", bass_leap=6,
              chord_fingers=True, meter="4/4", rhythms="q_rich", motion=STEPS_SKIPS, tempo=60, tonic=F4,
              dynamics=True, repeat_prob=0.3, **KEY_FSM),
         dict(name="D", title="C minor: B-natural", count=9, bars=8, mode="together", rh="RH_Cm", extend=1,
              lh="LH_Cm", chords=V4C, minor=True, beat_tones=True, lead_weight=20, bass="oompah",
              chord_fingers=True, meter="4/4", rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=66,
              tonic=C4, dynamics=True, repeat_prob=0.3, **KEY_CM),
     ]},
    {"id": 8, "title": "Changing Key", "new": "A new key mid-piece, shown by a new key signature or by accidentals; review",
     "parts": [
         dict(name="A", title="C major to G major", count=8, bars=8, mode="together", rh="RH_C", lh="LH_C",
              chords=V4C, beat_tones=True, bass="broken", chord_fingers=True, meter="4/4", rhythms="q_rich",
              motion=STEPS_SKIPS, tempo=66,
              modulate={"home_bars": 4, "show": "signature",
                        "to": [dict(bars=4, rh="RH_G", lh="LH_G", tonic=G4, **KEY_G)]}),
         dict(name="B", title="F major to D minor, with accidentals", count=8, bars=8, mode="together", rh="RH_F",
              lh="LH_F", chords=V4C, beat_tones=True, bass="broken", chord_fingers=True, meter="3/4",
              rhythms=["basic", "dotted34"], motion=STEPS_SKIPS, tempo=72, tonic=F4, extend=1,
              modulate={"home_bars": 4, "show": "accidentals",
                        "to": [dict(bars=4, rh="RH_Dm", lh="LH_Dm", tonic=D4, minor=True, lead_weight=20,
                                    key_acc={"b": "es"})]}, **KEY_F),
         dict(name="C", title="Away and back: G, D, G", count=8, bars=8, mode="together", rh="RH_G", lh="LH_G",
              chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="4/4",
              rhythms=["q_rich", "dotted"], motion=STEPS_SKIPS, tempo=66, tonic=G4,
              modulate={"home_bars": 4, "show": "signature",
                        "to": [dict(bars=2, rh="RH_D", lh="LH_D", tonic=D4, **KEY_D),
                               dict(bars=2, rh="RH_G", lh="LH_G", tonic=G4, **KEY_G)]}, **KEY_G),
         dict(name="D", title="Review: E-flat major march", count=10, bars=8, mode="together", rh="RH_Eb",
              lh="LH_Eb", chords=V4C, beat_tones=True, bass="oompah", chord_fingers=True, meter="2/4",
              rhythms=["synco24", "basic24", "e24"], motion=STEPS_SKIPS, tempo=80, tonic=E4, accents=True,
              dynamics=True, repeat_prob=0.3, extend=1, rh_chords={"prob": 0.8, "where": "strong", "min": 2},
              **KEY_EB),
     ]},
]

# =========================================================================== Volume 5
# Level 5-6: repertoire reading. Hand positions give way to reading by key, chord and pattern.
# Volume 5 parts are generated by gen5.py (not generator.py). Keys are (LilyPond tonic, mode);
# "variants" cycles through overrides (usually keys) exercise by exercise.
def _keys(*ks):
    return [dict(key=k) for k in ks]


C_, G_, F_, D_, BB_ = ("c", "major"), ("g", "major"), ("f", "major"), ("d", "major"), ("bes", "major")
AM_, DM_, EM_ = ("a", "minor"), ("d", "minor"), ("e", "minor")
GM_ = ("g", "minor")
CIRCLE = [("c", "major"), ("g", "major"), ("d", "major"), ("a", "major"), ("e", "major"), ("b", "major"),
          ("fis", "major"), ("des", "major"), ("aes", "major"), ("ees", "major"), ("bes", "major"), ("f", "major")]

VOLUME5 = [
    {"id": 1, "title": "Two Voices in One Hand", "new": "A tune and a held voice in the same hand: stems up and stems down",
     "parts": [
         dict(name="A", title="A held voice under the tune", count=8, bars=8, meter="4/4", rhythms="basic",
              bass="block", rh2="held", rh_up=2, tempo=66, repeat_prob=0.3, variants=_keys(C_, G_)),
         dict(name="B", title="Held voices in 3/4", count=8, bars=8, meter="3/4", rhythms="basic",
              bass="waltz", rh2="held", rh_up=2, tempo=84, repeat_prob=0.3, variants=_keys(F_, D_)),
         dict(name="C", title="Two voices in the left hand", count=8, bars=8, meter="4/4", rhythms=["basic", "slow"],
              lh2="tenor", rh_up=3, tempo=60, repeat_prob=0.3, variants=_keys(G_, F_, BB_)),
     ]},
    {"id": 2, "title": "Chorales", "new": "Four voices on two staves; chords on every degree of the scale, and first inversions",
     "parts": [
         dict(name="A", title="Three voices in half notes", count=8, bars=8, meter="4/4", texture="chorale",
              voices=3, tempo=60, chords=["I", "IV", "V", "vi", "ii"], variants=_keys(C_, G_, F_)),
         dict(name="B", title="Four voices (SATB)", count=8, bars=8, meter="4/4", texture="chorale", voices=4,
              tempo=60, require_inversion=True, variants=_keys(C_, G_, F_, D_, BB_)),
         dict(name="C", title="Chorales in minor keys", count=8, bars=8, meter="4/4", texture="chorale", voices=4,
              tempo=60, variants=_keys(AM_, DM_, EM_)),
     ]},
    {"id": 3, "title": "Chromatic Notes", "new": "Chromatic passing and neighbour notes, V7 of V, the melodic minor",
     "parts": [
         dict(name="A", title="Chromatic passing and neighbour notes", count=8, bars=8, meter="4/4",
              rhythms="basic", bass="block", tempo=66, chromatic={"passing": 0.6, "neighbour": 0.6, "min": 2},
              variants=_keys(C_, G_, F_)),
         dict(name="B", title="V7 of V: the raised 4th", count=8, bars=8, meter="4/4", rhythms=["basic", "eighths"],
              bass="broken", tempo=72, chords=["I", "IV", "ii", "vi", "V", "V7", "V7/V"], require_chords=["V7/V"],
              variants=_keys(C_, G_, F_)),
         dict(name="C", title="The melodic minor", count=8, bars=8, meter="4/4", rhythms=["eighths", "basic"],
              bass="block", tempo=66, melodic_minor=True, rh_span=11, variants=_keys(AM_, DM_, EM_)),
     ]},
    {"id": 4, "title": "Triplets and New Time Signatures", "new": "Eighth-note triplets; 3/8, 9/8, 12/8 and 2/2 (alla breve)",
     "parts": [
         dict(name="A", title="Triplets", count=8, bars=8, tempo=66, rhythms=["trip", "basic"], repeat_prob=0.3,
              variants=[dict(key=C_, meter="4/4", bass="block2"), dict(key=G_, meter="3/4", bass="waltz"),
                        dict(key=F_, meter="4/4", bass="block2"), dict(key=AM_, meter="3/4", bass="waltz")]),
         dict(name="B", title="3/8 and 9/8", count=8, bars=8, tempo=60, tempo_unit="4.", rhythms="basic",
              variants=[dict(key=G_, meter="3/8", bass="waltz"), dict(key=D_, meter="9/8", bass="broken"),
                        dict(key=AM_, meter="3/8", bass="waltz"), dict(key=F_, meter="9/8", bass="broken")]),
         dict(name="C", title="2/2 and 12/8", count=8, bars=8, tempo=60, tempo_unit="2", rhythms="basic",
              variants=[dict(key=C_, meter="2/2", bass="oompah"),
                        dict(key=BB_, meter="12/8", bass="broken", tempo=50, tempo_unit="4."),
                        dict(key=G_, meter="2/2", bass="block2"),
                        dict(key=EM_, meter="12/8", bass="broken", tempo=50, tempo_unit="4.")]),
     ]},
    {"id": 5, "title": "Four Sharps and Four Flats", "new": "E major and A-flat major; C-sharp minor (B-sharp) and F minor (E-natural)",
     "parts": [
         dict(name="A", title="E major", count=8, bars=8, meter="4/4", rhythms=["basic", "eighths"], bass="alberti",
              tempo=66, repeat_prob=0.3, dynamics=True, variants=_keys(("e", "major"))),
         dict(name="B", title="A-flat major", count=8, bars=8, meter="3/4", rhythms="basic", bass="waltz",
              tempo=80, repeat_prob=0.3, dynamics=True, variants=_keys(("aes", "major"))),
         dict(name="C", title="C-sharp minor and F minor", count=8, bars=8, meter="4/4", rhythms="basic",
              bass="broken", tempo=66, repeat_prob=0.3, variants=_keys(("cis", "minor"), ("f", "minor"))),
     ]},
    {"id": 6, "title": "Every Key", "new": "Five, six and seven sharps or flats; enharmonic keys (F-sharp = G-flat)",
     "parts": [
         dict(name="A", title="B major and D-flat major", count=8, bars=8, meter="4/4", rhythms="basic",
              bass="block2", tempo=60, variants=_keys(("b", "major"), ("des", "major"))),
         dict(name="B", title="Twins, and two minor keys", count=8, bars=8,
              meter="3/4", rhythms="basic", bass="waltz", tempo=72,
              variants=[dict(key=("fis", "major"), twin=("ges", "major")), dict(key=("bes", "minor")),
                        dict(key=("fis", "major"), twin=("ges", "major")), dict(key=("gis", "minor"))]),
         dict(name="C", title="Round the circle of fifths", count=12, bars=4, meter="4/4", rhythms="basic",
              bass="block", tempo=60, variants=_keys(*CIRCLE)),
     ]},
    {"id": 7, "title": "Pedal, Clefs and the Whole Keyboard", "new": "The sustain pedal; the left hand in the treble clef and the right hand in the bass clef",
     "parts": [
         dict(name="A", title="Wide broken chords with pedal", count=8, bars=8, rhythms=["basic", "slow"], pedal=True,
              tempo=66, rh_up=2,
              variants=[dict(key=C_, meter="4/4", bass="wide"), dict(key=G_, meter="3/4", bass="wide"),
                        dict(key=D_, meter="4/4", bass="wide"), dict(key=F_, meter="3/4", bass="wide")]),
         dict(name="B", title="Low bass, chord in the middle", count=8, bars=8, meter="3/4", rhythms="slow",
              bass="leap", pedal=True, tempo=72, rh_up=3, variants=_keys(D_, G_, C_, EM_)),
         dict(name="C", title="Clef changes", count=8, bars=8, meter="4/4", rhythms="basic", texture="alt",
              tempo=66, variants=_keys(C_, G_, F_, D_)),
     ]},
    {"id": 8, "title": "Counterpoint, Ornaments and Review", "new": "Sequences and imitation; trills, mordents, turns and grace notes; review",
     "parts": [
         dict(name="A", title="Sequences: the left hand imitates", count=8, bars=8, texture="sequence", tempo=66,
              variants=[dict(key=C_, meter="4/4"), dict(key=G_, meter="3/4"), dict(key=F_, meter="4/4"),
                        dict(key=AM_, meter="3/4")]),
         dict(name="B", title="Ornaments", count=8, bars=8, meter="4/4", rhythms="basic", bass="broken", tempo=66,
              ornaments={"trill": 1.0, "mordent": 0.3, "grace": 0.3, "turn": 0.3, "min": 3},
              variants=_keys(G_, D_, BB_, ("a", "major"))),
         dict(name="C", title="Review: sixteen bars", count=8, bars=16, tempo=72, repeat_prob=0.5, rhythms="basic",
              variants=[dict(key=("e", "major"), meter="4/4", bass="alberti"),
                        dict(key=("aes", "major"), meter="3/4", bass="waltz", rh2="held", rh_up=2),
                        dict(key=("cis", "minor"), meter="4/4", bass="broken", chromatic={"passing": 0.4, "neighbour": 0.4, "min": 1}),
                        dict(key=("des", "major"), meter="4/4", bass="wide", pedal=True, rhythms=["basic", "slow"]),
                        dict(key=("b", "major"), meter="6/8", bass="broken"),
                        dict(key=("ees", "major"), meter="4/4", bass="block2", rhythms=["trip", "basic"]),
                        dict(key=("f", "minor"), meter="3/4", bass="leap", pedal=True, rhythms="slow", rh_up=3),
                        dict(key=("a", "major"), meter="4/4", bass="broken", ornaments={"trill": 1.0, "mordent": 0.2, "grace": 0.2, "min": 2})]),
     ]},
]

# =========================================================================== Volume 6
# Level 7-8: reading music written for anyone. Parts are generated by gen6.py (which builds on
# gen5.py); the full plan is in the README ("Volume 6 plan"). Each unit's parts are added when
# that unit is built - an empty "parts" list means the unit is not written yet.
VOLUME6 = [
    {"id": 1, "title": "Three Voices",
     "new": "Three independent voices on two staves; the middle voice passes between the hands; fugue entries",
     "parts": [
         dict(name="A", title="Three voices: two in the right hand", count=8, bars=4, meter="4/4", texture="trio",
              rhythms=["basic", "eighths"], tempo=60, variants=_keys(C_, G_, F_, DM_)),
         dict(name="B", title="The middle voice changes hands", count=8, bars=8, meter="4/4", texture="cross",
              rhythms=["basic", "eighths"], tempo=60, variants=_keys(D_, BB_, EM_, ("a", "major"))),
         dict(name="C", title="Fugue entries: subject, answer, countersubject", count=8, bars=8, meter="4/4",
              texture="fugue", tempo=56,
              variants=[dict(key=C_, subject_start=(0,), label_entries=True),
                        dict(key=AM_, subject_start=(0,), label_entries=True),
                        dict(key=G_, subject_start=(4,), label_entries=True),
                        dict(key=DM_, subject_start=(4,), label_entries=True),
                        dict(key=F_, subject_start=(0, 4)), dict(key=EM_, subject_start=(4,)),
                        dict(key=D_, subject_start=(0, 4)), dict(key=("g", "minor"), subject_start=(0, 4))]),
     ]},
    {"id": 2, "title": "Rhythm Against Rhythm",
     "new": "Two against three, three against four, duplets, quintuplets and septuplets, hemiola",
     "parts": [
         dict(name="A", title="Two against three", count=8, bars=8, meter="4/4", rhythms=["eighths"],
              bass="triplet", tempo=60,
              variants=[dict(key=C_), dict(key=G_, texture="swap"), dict(key=F_), dict(key=DM_, texture="swap"),
                        dict(key=D_), dict(key=BB_, texture="swap"), dict(key=EM_), dict(key=("a", "major"), texture="swap")]),
         dict(name="B", title="Duplets, and three against four", count=8, bars=8, meter="6/8", texture="rhythm",
              rhythms=["duplet"], bass="broken", tempo=56, tempo_unit="4.", require_tuplet=True,
              variants=[dict(key=D_), dict(key=F_, meter="2/4", rhythms=["trip"], bass="alberti16", tempo=56, tempo_unit="4"),
                        dict(key=G_), dict(key=("e", "major"), meter="2/4", rhythms=["trip"], bass="alberti16", tempo=56, tempo_unit="4"),
                        dict(key=AM_), dict(key=("ees", "major"), meter="2/4", rhythms=["trip"], bass="alberti16", tempo=56, tempo_unit="4"),
                        dict(key=("b", "minor")), dict(key=C_, meter="2/4", rhythms=["trip"], bass="alberti16", tempo=56, tempo_unit="4")]),
         dict(name="C", title="Runs of 5, 6 and 7 notes, and hemiolas", count=8, bars=8, meter="4/4", texture="runs",
              rhythms=["basic"], bass="block2", tempo=60, runs={"count": 2},
              variants=[dict(key=C_), dict(key=D_, meter="3/4", texture="hemiola", bass="waltz", tempo=96),
                        dict(key=AM_), dict(key=F_, meter="3/4", texture="hemiola", bass="waltz", tempo=96),
                        dict(key=("e", "major")), dict(key=GM_, meter="3/4", texture="hemiola", bass="waltz", tempo=96),
                        dict(key=("aes", "major")), dict(key=G_, meter="3/4", texture="hemiola", bass="waltz", tempo=96)]),
     ]},
    {"id": 3, "title": "Changing Meters, Modes and No Key",
     "new": "Changing time signatures; 5/4, 7/8 and 5/8; modes; pentatonic and whole-tone scales; no bar lines",
     "parts": [
         dict(name="A", title="Changing meters", count=8, bars=8, meter="5/4", texture="meters", meters=["5/4", "6/4"],
              tempo=88,
              variants=[dict(key=BB_), dict(key=EM_, meter="3/4", meters=["3/4", "3/4", "2/4"]),
                        dict(key=G_), dict(key=D_, meter="3/4", meters=["3/4", "2/4"]),
                        dict(key=DM_), dict(key=("a", "major"), meter="3/4", meters=["3/4", "3/4", "2/4"]),
                        dict(key=("ees", "major")), dict(key=("c", "minor"), meter="3/4", meters=["3/4", "2/4"])]),
         dict(name="B", title="7/8, 5/8 and the modes", count=8, bars=8, meter="7/8", texture="meters", tempo=160,
              tempo_unit="8",
              variants=[dict(key=D_), dict(key=("a", "dorian"), meter="4/4", no_signature=True, tempo=72, tempo_unit="4"),
                        dict(key=GM_, meter="5/8"), dict(key=("d", "mixolydian"), meter="3/4", no_signature=True, tempo=72, tempo_unit="4"),
                        dict(key=F_), dict(key=("e", "phrygian"), meter="4/4", no_signature=True, tempo=72, tempo_unit="4"),
                        dict(key=("a", "major"), meter="5/8"), dict(key=("f", "lydian"), meter="3/4", no_signature=True, tempo=72, tempo_unit="4")]),
         dict(name="C", title="Without bar lines: pentatonic and whole-tone tunes", count=8, bars=1, meter="4/4",
              texture="meters", unbarred=True, scale="pentatonic", tempo=72,
              variants=[dict(key=F_), dict(key=C_, scale="wholetone"), dict(key=G_), dict(key=F_, scale="wholetone"),
                        dict(key=D_), dict(key=BB_, scale="wholetone"), dict(key=("ees", "major")), dict(key=C_, scale="wholetone")]),
     ]},
    {"id": 4, "title": "Chromatic Harmony",
     "new": "Secondary dominants, diminished sevenths, Neapolitan and augmented sixths, enharmonic modulation",
     "parts": []},
    {"id": 5, "title": "Big Textures",
     "new": "Octaves, full chords, 8va and 8vb signs, three-staff piano music, crossed hands, simplifying",
     "parts": []},
    {"id": 6, "title": "Accompanying",
     "new": "Three staves: a singer's line above the piano; introductions and interludes; following the soloist",
     "parts": []},
    {"id": 7, "title": "Open Score, C Clefs and Transposing",
     "new": "Four staves (SATB), the vocal tenor clef, the alto and tenor clefs; transposing at sight",
     "parts": []},
    {"id": 8, "title": "Lead Sheets, Simplifying and Review",
     "new": "Chord symbols (C, Am7, G7/B, Fmaj7, Bdim, C/E); playing from a lead sheet; review",
     "parts": []},
]
