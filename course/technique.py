"""Build "Read at Sight - Technique": scales, arpeggios and chord work to practise alongside the course.

Six stages, one per volume (Stage 6 goes with Volumes 6 and 7). Everything is generated from the
fingering tables below; test_technique.py checks them against the published fourth-finger chart and
the thumb rules, so a wrong fingering cannot slip into the book.

Usage (from course/):  python3 technique.py
Output: ../build/Read at Sight - Technique.pdf
"""
import os
import re
import subprocess

import build
from build import s

OUT = os.path.join(build.BUILD, "Read at Sight - Technique")
LETTERS = "cdefgab"
NATURAL = [0, 2, 4, 5, 7, 9, 11]
MODES = {"major": [0, 2, 4, 5, 7, 9, 11], "harmonic": [0, 2, 3, 5, 7, 8, 11],
         "melodic": [0, 2, 3, 5, 7, 9, 11], "natural": [0, 2, 3, 5, 7, 8, 10]}

# ---------------------------------------------------------------- fingering tables
# Scales: for each hand, the finger on each scale degree (1-7) in the middle of a scale of several
# octaves ("cycle"), plus the finger on the first note (RH: always cycle[0]; LH: "lh_start") and on
# the last note (RH: "rh_end"; LH: always cycle[0]). Descending uses the same fingers in reverse.
C_RH, C_LH = [1, 2, 3, 1, 2, 3, 4], [1, 4, 3, 2, 1, 3, 2]          # thumbs on degrees 1 and 4 / 1 and 5
B_LH = [1, 3, 2, 1, 4, 3, 2]
F_RH = [1, 2, 3, 4, 1, 2, 3]
BLACK_LH = [3, 2, 1, 4, 3, 2, 1]


def fing(rh, rh_end, lh, lh_start):
    return {"rh": rh, "rh_end": rh_end, "lh": lh, "lh_start": lh_start}


C_TYPE = fing(C_RH, 5, C_LH, 5)
SCALE_FINGERS = {
    ("c", 0, "major"): C_TYPE, ("g", 0, "major"): C_TYPE, ("d", 0, "major"): C_TYPE,
    ("a", 0, "major"): C_TYPE, ("e", 0, "major"): C_TYPE,
    ("b", 0, "major"): fing(C_RH, 5, B_LH, 4),
    ("f", 0, "major"): fing(F_RH, 4, C_LH, 5),
    ("b", -1, "major"): fing([4, 1, 2, 3, 1, 2, 3], 4, BLACK_LH, 3),
    ("e", -1, "major"): fing([3, 1, 2, 3, 4, 1, 2], 3, BLACK_LH, 3),
    ("a", -1, "major"): fing([3, 4, 1, 2, 3, 1, 2], 3, BLACK_LH, 3),
    ("d", -1, "major"): fing([2, 3, 1, 2, 3, 4, 1], 2, BLACK_LH, 3),
    ("f", 1, "major"): fing([2, 3, 4, 1, 2, 3, 1], 2, [4, 3, 2, 1, 3, 2, 1], 4),
    ("a", 0, "minor"): C_TYPE, ("e", 0, "minor"): C_TYPE, ("d", 0, "minor"): C_TYPE,
    ("g", 0, "minor"): C_TYPE, ("c", 0, "minor"): C_TYPE,
    ("b", 0, "minor"): fing(C_RH, 5, B_LH, 4),
    ("f", 0, "minor"): fing(F_RH, 4, C_LH, 5),
    ("f", 1, "minor"): fing([3, 4, 1, 2, 3, 1, 2], 3, [4, 3, 2, 1, 3, 2, 1], 4),
    ("c", 1, "minor"): fing([3, 4, 1, 2, 3, 1, 2], 3, BLACK_LH, 3),
    ("g", 1, "minor"): fing([3, 4, 1, 2, 3, 1, 2], 3, BLACK_LH, 3),
    ("b", -1, "minor"): fing([4, 1, 2, 3, 1, 2, 3], 4, [2, 1, 3, 2, 1, 4, 3], 2),
    ("e", -1, "minor"): fing([3, 1, 2, 3, 4, 1, 2], 3, [2, 1, 4, 3, 2, 1, 3], 2),
}

# Arpeggios (root position, two octaves, 7 notes ascending): RH and LH fingers, bottom to top.
# Source: Prof. Escandon's chart (University of Miami), as published by B. Burt; white-key minor
# arpeggios also as in Baylor University's "Piano Basics" (open textbook). Black-key rows start
# with 2 in the right hand (the chart's alternative is 3).
A_ROW1 = ("1231235", "5421421")
ARP_FINGERS = {
    ("c", 0, "major"): A_ROW1, ("f", 0, "major"): A_ROW1, ("g", 0, "major"): A_ROW1,
    ("f", 1, "major"): A_ROW1,
    ("a", 0, "minor"): A_ROW1, ("d", 0, "minor"): A_ROW1, ("e", 0, "minor"): A_ROW1,
    ("b", 0, "minor"): A_ROW1, ("c", 0, "minor"): A_ROW1, ("f", 0, "minor"): A_ROW1,
    ("g", 0, "minor"): A_ROW1,
    ("e", -1, "minor"): A_ROW1,   # all three notes black, like F-sharp major
    ("a", 0, "major"): ("1231235", "5321321"), ("d", 0, "major"): ("1231235", "5321321"),
    ("e", 0, "major"): ("1231235", "5321321"), ("b", 0, "major"): ("1231235", "5321321"),
    ("a", -1, "major"): ("2124124", "2142142"), ("d", -1, "major"): ("2124124", "2142142"),
    ("e", -1, "major"): ("2124124", "2142142"),
    ("c", 1, "minor"): ("2124124", "2142142"), ("f", 1, "minor"): ("2124124", "2142142"),
    ("g", 1, "minor"): ("2124124", "2142142"),
    ("b", -1, "major"): ("2124124", "3213213"),
    ("b", -1, "minor"): ("2312312", "3213213"),
}
# First and second inversions, same chart (white-key keys of its first row).
ARP_INV = {1: ("1241245", "5421421"), 2: ("1241245", "5321321")}

FIVE = ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])


# ---------------------------------------------------------------- pitches
class Note:
    """A spelled pitch: diatonic step number (C4 = 28) and alteration."""
    def __init__(self, step, alt):
        self.step, self.alt = step, alt

    @property
    def midi(self):
        return 12 * (self.step // 7) + NATURAL[self.step % 7] + self.alt + 12

    def lily(self):
        name = LETTERS[self.step % 7] + ("is" * self.alt if self.alt > 0 else "es" * -self.alt)
        name = name.replace("ees", "es").replace("aes", "as")
        octv = self.step // 7 - 3
        return name + ("'" * octv if octv > 0 else "," * -octv)

    @property
    def black(self):
        return (self.midi % 12) in (1, 3, 6, 8, 10)


def key_name(tonic, alt, mode):
    n = tonic.upper() + {1: "-sharp", -1: "-flat", 0: ""}[alt]
    return f"{n} {'major' if mode == 'major' else 'minor'}"


def lily_key(tonic, alt, mode):
    return f"\\key {Note(LETTERS.index(tonic), alt).lily().rstrip(',')} \\{'major' if mode == 'major' else 'minor'}"


def scale_notes(tonic, alt, kind, base_step, n_degrees):
    """n_degrees notes of the scale upward from the tonic at diatonic step base_step."""
    t = LETTERS.index(tonic)
    tonic_pc = NATURAL[t] + alt
    out = []
    for i in range(n_degrees):
        step = base_step + i
        target = (tonic_pc + MODES[kind][i % 7]) % 12
        a = (target - NATURAL[step % 7]) % 12
        a = a - 12 if a > 6 else a
        out.append(Note(step, a))
    return out


def tonic_step(tonic, hand):
    """RH tonic between C4 and B4 (A and B a little lower); LH two octaves below."""
    t = LETTERS.index(tonic)
    step = 28 + t if t < 5 else 21 + t
    return step if hand == "rh" else step - 14


# ---------------------------------------------------------------- fingering
def scale_fingering(key, hand, octaves):
    f = SCALE_FINGERS[key]
    cyc = f[hand]
    n = 7 * octaves + 1
    up = [cyc[i % 7] for i in range(n)]
    if hand == "rh":
        up[-1] = f["rh_end"]
    else:
        up[0] = f["lh_start"]
    return up


def arp_fingering(key, hand, inversion=0):
    rh, lh = ARP_FINGERS[key] if inversion == 0 else ARP_INV[inversion]
    return [int(c) for c in (rh if hand == "rh" else lh)]


# ---------------------------------------------------------------- music strings
def seq(notes, fingers, durs, direction):
    out = []
    for n, f, d in zip(notes, fingers, durs):
        out.append(f"{n.lily()}{d}-{f}" if f else f"{n.lily()}{d}")
    return " ".join(out)


def up_down(notes, fingers):
    return notes + notes[-2::-1], fingers + fingers[-2::-1]


def sixteenth_run(notes, fingers):
    """Notes in sixteenths, the last one a quarter (completing 4/4 bars when len-1 is a multiple of 16)."""
    durs = ["16"] * (len(notes) - 1) + ["4"]
    return seq(notes, fingers, durs, None)


def score(rh, lh, key, title, time="4/4", extra=""):
    return rf"""
\score {{
  \header {{ piece = \markup \line {{ \exLabel {s(title)} }} }}
  \new PianoStaff <<
    \new Staff {{ \clef treble {key} \time {time} \override Fingering.direction = #UP {extra} {rh} \bar "|." }}
    \new Staff {{ \clef bass {key} \time {time} \override Fingering.direction = #DOWN {extra} {lh} \bar "|." }}
  >>
  \layout {{ \context {{ \Score \override BarNumber.break-visibility = ##(#f #f #f) }} }}
}}
"""


def scale_ex(tonic, alt, mode, kind=None, octaves=2):
    key = (tonic, alt, mode)
    kind = kind or ("major" if mode == "major" else "harmonic")
    parts = {}
    for hand in ("rh", "lh"):
        n = 7 * octaves + 1
        up = scale_notes(tonic, alt, kind, tonic_step(tonic, hand), n)
        fu = scale_fingering(key, hand, octaves)
        if kind == "melodic":   # down in the natural minor
            down = scale_notes(tonic, alt, "natural", tonic_step(tonic, hand), n)[::-1][1:]
            notes, fingers = up + down, fu + fu[::-1][1:]
        else:
            notes, fingers = up_down(up, fu)
        if octaves == 2:
            parts[hand] = sixteenth_run(notes, fingers)
        else:   # one octave: eighths, last note a quarter (15 notes = 7 beats + 1)
            parts[hand] = seq(notes, fingers, ["8"] * (len(notes) - 1) + ["4"], None)
    label = {"major": "", "harmonic": " (harmonic)", "melodic": " (melodic)"}[kind]
    title = f"{key_name(tonic, alt, mode)}{label}"
    return score(parts["rh"], parts["lh"], lily_key(tonic, alt, mode), title)


def arpeggio_ex(tonic, alt, mode, inversion=0):
    key = (tonic, alt, mode)
    kind = "major" if mode == "major" else "harmonic"
    parts = {}
    for hand in ("rh", "lh"):
        sc = scale_notes(tonic, alt, kind, tonic_step(tonic, hand), 22)
        chord = [sc[i] for i in range(22) if i % 7 in (0, 2, 4)]
        start = {0: 0, 1: 1, 2: 2}[inversion]
        up = chord[start:start + 7]
        notes, fingers = up_down(up, arp_fingering(key, hand, inversion))
        trip = " ".join(f"{n.lily()}8-{f}" for n, f in zip(notes[:12], fingers[:12]))
        last = f"{notes[12].lily()}2-{fingers[12]} r2"
        parts[hand] = f"\\tuplet 3/2 {{ {trip} }} | {last}"
    inv = {0: "", 1: ", first inversion", 2: ", second inversion"}[inversion]
    return score(parts["rh"], parts["lh"], lily_key(tonic, alt, mode), f"{key_name(tonic, alt, mode)}{inv}",
                 extra="\\tupletSpan 4 \\omit TupletNumber \\omit TupletBracket")


def five_finger_ex(tonic, alt, mode):
    kind = "major" if mode == "major" else "harmonic"
    parts = {}
    for hand, fingers in zip(("rh", "lh"), FIVE):
        sc = scale_notes(tonic, alt, kind, tonic_step(tonic, hand) + (7 if hand == "lh" else 0), 5)
        up = list(zip(sc, fingers))
        run = up + up[-2:0:-1]                   # 1 2 3 4 5 4 3 2
        triad = [up[0], up[2], up[4], up[2]]      # 1 3 5 3
        bar1 = " ".join(f"{n.lily()}8-{f}" for n, f in run)
        bar2 = " ".join(f"{n.lily()}8-{f}" for n, f in triad) + f" {up[0][0].lily()}2-{up[0][1]}"
        parts[hand] = f"{bar1} | {bar2}"
    return score(parts["rh"], parts["lh"], lily_key(tonic, alt, mode), key_name(tonic, alt, mode))


def broken_triad_ex(tonic, alt, mode):
    """One-octave arpeggio (1 3 5 8 5 3 1) with the first chart row's fingering."""
    key = (tonic, alt, mode)
    kind = "major" if mode == "major" else "harmonic"
    parts = {}
    for hand in ("rh", "lh"):
        sc = scale_notes(tonic, alt, kind, tonic_step(tonic, hand), 8)
        up = [sc[0], sc[2], sc[4], sc[7]]
        f = arp_fingering(key, hand)
        fu = [f[0], f[1], f[2], 5] if hand == "rh" else [f[0], f[1], f[2], f[3]]
        notes, fingers = up_down(up, fu)
        body = " ".join(f"{n.lily()}8-{x}" for n, x in zip(notes[:6], fingers[:6]))
        parts[hand] = f"{body} {notes[6].lily()}4-{fingers[6]}"
    return score(parts["rh"], parts["lh"], lily_key(tonic, alt, mode), key_name(tonic, alt, mode), time="2/4",
                 extra="")


def inversions_ex(tonic, alt, mode):
    """Tonic triad: root, first, second inversion, root an octave up, and back."""
    kind = "major" if mode == "major" else "harmonic"
    parts = {}
    for hand in ("rh", "lh"):
        sc = scale_notes(tonic, alt, kind, tonic_step(tonic, hand), 15)
        shapes = [(0, 2, 4), (2, 4, 7), (4, 7, 9), (7, 9, 11)]
        fing = {"rh": [(1, 3, 5), (1, 2, 5), (1, 3, 5), (1, 3, 5)],
                "lh": [(5, 3, 1), (5, 3, 1), (5, 2, 1), (5, 3, 1)]}[hand]
        order = [0, 1, 2, 3, 2, 1, 0]
        chords = []
        for k, i in enumerate(order):
            ns = [sc[d] for d in shapes[i]]
            body = " ".join(f"{n.lily()}-{f}" for n, f in zip(ns, fing[i]))
            chords.append(f"<{body}>{'4' if k < 6 else '2'}")
        parts[hand] = " ".join(chords[:4]) + " | " + " ".join(chords[4:]) + " r4"
    return score(parts["rh"], parts["lh"], lily_key(tonic, alt, mode), key_name(tonic, alt, mode),
                 extra="\\set fingeringOrientations = #'(left)")


def cadence_ex(tonic, alt, mode):
    """I - IV - I - V7 - I: right hand in close position (moving as little as possible), left hand roots."""
    kind = "major" if mode == "major" else "harmonic"
    rs = tonic_step(tonic, "rh")
    sc = scale_notes(tonic, alt, kind, rs - 7, 22)        # index 7 = RH tonic
    rh_ch = [(7, 9, 11), (7, 10, 12), (7, 9, 11), (6, 10, 11), (7, 9, 11)]
    rh = []
    for k, ch in enumerate(rh_ch):
        rh.append("<" + " ".join(sc[i].lily() for i in ch) + ">" + ("4" if k < 4 else "1"))
    ls = scale_notes(tonic, alt, kind, rs - 14 - 7, 15)    # index 7 = LH tonic
    lh_idx = [7, 3, 7, 4, 7]
    lh = [ls[i].lily() + ("4" if k < 4 else "1") for k, i in enumerate(lh_idx)]
    numerals = ("I IV I V7 I" if mode == "major" else "i iv i V7 i").split()
    rh_s = " ".join(rh[:4]) + " | " + rh[4]
    named = [f"{n}_\\markup {{ \\bold {s(r)} }}" for n, r in zip(lh, numerals)]
    lh_s = " ".join(named[:4]) + " | " + named[4]
    return score(rh_s, lh_s, lily_key(tonic, alt, mode), key_name(tonic, alt, mode))


CHROM_RH = {0: 2, 1: 3, 2: 1, 3: 3, 4: 1, 5: 2, 6: 3, 7: 1, 8: 3, 9: 1, 10: 3, 11: 1}
CHROM_LH = {0: 1, 1: 3, 2: 1, 3: 3, 4: 2, 5: 1, 6: 3, 7: 1, 8: 3, 9: 1, 10: 3, 11: 2}
SHARP_SPELL = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (5, 0), (5, 1), (6, 0)]
FLAT_SPELL = [(0, 0), (1, -1), (1, 0), (2, -1), (2, 0), (3, 0), (4, -1), (4, 0), (5, -1), (5, 0), (6, -1), (6, 0)]


def chromatic_notes(base_step, semis, spell):
    o = base_step // 7
    out = []
    for k in semis:
        letter, a = spell[k % 12]
        out.append(Note(7 * (o + k // 12) + letter, a))
    return out


def chromatic_ex():
    parts = {}
    for hand, table in (("rh", CHROM_RH), ("lh", CHROM_LH)):
        base = 28 if hand == "rh" else 14
        up = chromatic_notes(base, range(25), SHARP_SPELL)
        down = chromatic_notes(base, range(23, -1, -1), FLAT_SPELL)
        notes = up + down
        fingers = [table[n.midi % 12] for n in notes]
        fingers[0] = fingers[-1] = 1
        parts[hand] = sixteenth_run(notes, fingers)
    return score(parts["rh"], parts["lh"], "", "Chromatic scale from C, two octaves")


def contrary_ex(tonic, alt):
    """Contrary motion from the tonic (both hands on the same key), two octaves: each hand uses its own
    scale fingering (RH ascending, LH descending)."""
    key = (tonic, alt, "major")
    rs = tonic_step(tonic, "rh")
    rh_up = scale_notes(tonic, alt, "major", rs, 15)
    rf = scale_fingering(key, "rh", 2)
    lh_down = scale_notes(tonic, alt, "major", rs - 14, 15)[::-1]   # from the same key-note, as in exams
    lf = scale_fingering(key, "lh", 2)[::-1]
    rn, rfi = up_down(rh_up, rf)
    ln, lfi = up_down(lh_down, lf)
    return score(sixteenth_run(rn, rfi), sixteenth_run(ln, lfi), lily_key(tonic, alt, "major"),
                 f"{key_name(tonic, alt, 'major')}, contrary motion")


# ---------------------------------------------------------------- the stages
M, m = "major", "minor"
STAGES = [
    ("Stage 1", "With Volume 1", "Five-finger patterns",
     "Each pattern: up and down the five notes, then the broken chord (1-3-5-3-1). Hands separately first, "
     "then together. Keep every finger curved over its own key and play from the fingertip.",
     [("Five-finger patterns", [five_finger_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("d", 0, M), ("f", 0, M), ("a", 0, m), ("d", 0, m), ("e", 0, m)]])]),
    ("Stage 2", "With Volume 2", "One-octave scales and broken chords",
     "The thumb now passes under the hand (right hand going up, left hand going down) and the third or fourth "
     "finger crosses over it. Pass the thumb early and smoothly, without a bump; the wrist stays level and quiet.",
     [("One-octave scales", [scale_ex(*k, octaves=1) for k in
       [("c", 0, M), ("g", 0, M), ("f", 0, M), ("a", 0, m), ("e", 0, m), ("d", 0, m)]]),
      ("Broken chords", [broken_triad_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("f", 0, M), ("a", 0, m), ("e", 0, m), ("d", 0, m)]])]),
    ("Stage 3", "With Volume 3", "Two-octave scales, arpeggios and inversions",
     "Keys up to two sharps or two flats. Scales two octaves, hands together an octave apart (in sixteenths: "
     "four notes to each metronome beat). Arpeggios in triplets: three notes to a beat.",
     [("Scales", [scale_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("d", 0, M), ("f", 0, M), ("b", -1, M),
        ("a", 0, m), ("e", 0, m), ("b", 0, m), ("d", 0, m), ("g", 0, m)]] + [contrary_ex("c", 0)]),
      ("Arpeggios", [arpeggio_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("d", 0, M), ("f", 0, M), ("b", -1, M),
        ("a", 0, m), ("e", 0, m), ("b", 0, m), ("d", 0, m), ("g", 0, m)]]),
      ("Triads and their inversions", [inversions_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("d", 0, M), ("f", 0, M), ("a", 0, m), ("d", 0, m)]])]),
    ("Stage 4", "With Volume 4", "New keys, cadences, chromatic scale",
     "New keys up to three sharps or flats, the melodic minor (raised sixth and seventh going up, natural "
     "going down), the chromatic scale, and the cadence that ends most pieces: I - IV - I - V7 - I. In the "
     "cadences the right hand moves as little as possible; say the chord names as you play.",
     [("Scales", [scale_ex(*k) for k in
       [("a", 0, M), ("e", -1, M), ("f", 1, m), ("c", 0, m)]] +
       [scale_ex(t, 0, m, "melodic") for t in "aedgc"] + [chromatic_ex()]),
      ("Arpeggios", [arpeggio_ex(*k) for k in [("a", 0, M), ("e", -1, M), ("f", 1, m), ("c", 0, m)]]),
      ("Cadences", [cadence_ex(*k) for k in
       [("c", 0, M), ("g", 0, M), ("d", 0, M), ("a", 0, M), ("f", 0, M), ("b", -1, M), ("e", -1, M),
        ("a", 0, m), ("e", 0, m), ("b", 0, m), ("f", 1, m), ("d", 0, m), ("g", 0, m), ("c", 0, m)]])]),
    ("Stage 5", "With Volume 5", "Every key",
     "The remaining keys: four sharps and flats first (Volume 5, Unit 5), then the rest (Unit 6). With these, "
     "you have scales and arpeggios in all 24 keys; from now on, play the whole set round the circle of "
     "fifths, a few keys a day.",
     [("Scales", [scale_ex(*k) for k in
       [("e", 0, M), ("a", -1, M), ("b", 0, M), ("d", -1, M), ("f", 1, M),
        ("c", 1, m), ("f", 0, m), ("g", 1, m), ("b", -1, m), ("e", -1, m)]]),
      ("Arpeggios", [arpeggio_ex(*k) for k in
       [("e", 0, M), ("a", -1, M), ("b", 0, M), ("d", -1, M), ("f", 1, M),
        ("c", 1, m), ("f", 0, m), ("g", 1, m), ("b", -1, m), ("e", -1, m)]]),
      ("Cadences", [cadence_ex(*k) for k in
       [("e", 0, M), ("a", -1, M), ("b", 0, M), ("d", -1, M), ("f", 1, M),
        ("c", 1, m), ("f", 0, m), ("g", 1, m), ("b", -1, m), ("e", -1, m)]])]),
    ("Stage 6", "With Volumes 6 and 7", "Contrary motion and inverted arpeggios",
     "Scales in contrary motion (both hands start on the same key-note and move away from each other, each with its own "
     "fingering) and arpeggios starting on the third and fifth of the chord. Keep playing all 24 scales and "
     "arpeggios round the circle, and raise the speed slowly.",
     [("Contrary motion", [contrary_ex(*k) for k in
       [("g", 0), ("d", 0), ("a", 0), ("e", 0), ("b", 0), ("f", 1), ("d", -1), ("a", -1), ("e", -1),
        ("b", -1), ("f", 0)]]),
      ("Arpeggios in inversion", [arpeggio_ex(t, 0, mo, inv) for t, mo in
       [("c", M), ("g", M), ("f", M), ("a", m), ("d", m), ("e", m)] for inv in (1, 2)])]),
]

TEMPI = [("Stage 1", "♩ = 60, eighths"), ("Stage 2", "♩ = 60-72, eighths"), ("Stage 3", "♩ = 60, sixteenths"),
         ("Stage 4", "♩ = 72, sixteenths"), ("Stage 5", "♩ = 80, sixteenths"), ("Stage 6", "♩ = 96 and up")]

HOW = [
    ("Why technique", "Sight-reading trains your eyes; technique trains your hands to do what your eyes see. "
     "Scales, arpeggios and chords are the shapes most music is built from: once your hands know them, you "
     "recognise them on the page and play them without working them out."),
    ("How long", "About ten minutes a day, at the start of practice, before sight-reading. Work on the stage "
     "that goes with the volume you are reading; keep the earlier stages going, a few keys a day."),
    ("How to practise", "1. Hands separately until the fingering is automatic, then hands together. 2. Slowly, "
     "with the metronome, every note even in time and in loudness. 3. Use exactly the fingering printed: it is "
     "the standard one, chosen so the thumb lands on a white key and the hand never runs out of fingers. "
     "4. Raise the speed by 4-8 beats per minute only after two clean runs. 5. Stay relaxed: shoulders down, "
     "wrist level, no tension in the thumb as it passes under. Stop and shake out the hand if anything tightens."),
    ("Target speeds", "Speeds to aim for by the end of each stage (sixteenths: four notes to each beat; "
     "arpeggios in triplets at two-thirds of that): " + "; ".join(f"{a}: {b}" for a, b in TEMPI) + "."),
    ("Pieces above your reading level", "Keep learning pieces you love that are harder than you can sight-read: "
     "that is how most pianists work. Reading (the volumes) trains the eyes on lots of easy music played once; "
     "pieces (Volume 7, or any you choose) train the hands, memory and musicianship over weeks. A good rule: "
     "choose pieces about two levels above your sight-reading. Much higher, and you spend months decoding notes "
     "instead of making music. Learn them as Volume 7 describes: hard places first, in short sections, slowly."),
]


def stage_pages(stage):
    label, vol, title, intro, groups = stage
    out = [rf"""\markup \column {{
  \vspace #1
  \fontsize #2 \italic {s(label + '  -  ' + vol)}
  \fontsize #6 \bold {s(title)}
  \vspace #0.6
  {build.para(intro, 1)}
  \vspace #0.4
}}"""]
    for gname, scores in groups:
        out.append(f"\\markup \\column {{ \\vspace #0.8 \\fontsize #3 \\bold {s(gname)} \\vspace #0.2 }}")
        out.append("\\noPageBreak")
        out += scores
    out.append("\\pageBreak")
    return out


def document():
    build._layout_for(1)
    parts = [build.PREAMBLE.replace("@@HEADER@@", "Read at Sight  -  Technique").replace("@@STAFF_SIZE@@", "20"),
             "\\book {"]
    kb = build.keyboard_markup(21, 35, [], {28: "Middle C"})
    parts.append(rf"""\markup \column {{
  \vspace #10
  \fill-line {{ \fontsize #12 \bold "Read at Sight" }}
  \vspace #1
  \fill-line {{ \fontsize #4 \italic "A graded sight-reading course for piano" }}
  \vspace #2
  \fill-line {{ \fontsize #6 "Technique: Scales, Arpeggios and Chords" }}
  \vspace #6
  \fill-line {{ {kb} }}
  \vspace #12
  \fill-line {{ \override #'(line-width . 70) \fontsize #1 \center-column {{
    "Ten minutes a day alongside the volumes:"
    "six stages, one for each volume, with standard fingering throughout."
  }} }}
}}
\pageBreak""")
    parts.append("\\markup \\column { \\fontsize #6 \\bold \"How to use this book\" \\vspace #1 }")
    for head, body in HOW:
        parts.append(f"\\markup \\column {{ \\fontsize #2 \\bold {s(head)} \\vspace #0.3 {build.para(body, 1)} \\vspace #0.6 }}")
    rows = " ".join(f"\\vspace #0.5 \\line {{ \\bold {s(st[0])} \\hspace #1 {s(st[1] + ':  ' + st[2])} }}" for st in STAGES)
    parts.append(f"\\markup \\column {{ \\fontsize #2 \\bold \"The stages\" \\vspace #0.2 \\fontsize #1 \\column {{ {rows} }} }}")
    parts.append(f"\\markup \\column {{ \\vspace #0.8 {build.para('Fingering: 1 is the thumb, 5 the little finger, in both hands. Right-hand fingers are printed above the notes, left-hand fingers below. Scale fingerings follow the standard chart (the fourth finger falls once in each octave on a fixed note of the key); arpeggio fingerings follow the chart of Prof. Escandon (University of Miami), as published by B. Burt.', -1)} }}")
    parts.append("\\pageBreak")
    for st in STAGES:
        parts += stage_pages(st)
    parts.append("}")
    return "\n".join(parts)


def main():
    ly = OUT + ".ly"
    open(ly, "w").write(document())
    r = subprocess.run([build.lilypond_bin(), "-l", "WARNING", "-o", OUT, ly], capture_output=True, text=True)
    warns = [l for l in r.stderr.splitlines() if re.search(r"(warning|error):", l)
             and not any(b in l for b in ("compressed", "over-full"))]
    for w in warns:
        print("WARN:", w)
    if r.returncode != 0:
        raise SystemExit("LilyPond failed")
    os.remove(ly)
    print("built", OUT + ".pdf")


if __name__ == "__main__":
    main()
