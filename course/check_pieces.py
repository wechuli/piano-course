"""Check hand-written pieces against what each unit has taught.

Checks, per piece and staff:
  - every bar adds up to the time signature
  - every note lies inside a hand position used in this unit (for that hand)
  - consecutive notes in one hand never leap further than the unit allows
    (exception from Unit 5: the left-hand bass may move between the position's
     lowest note and the note a 5th above, i.e. finger 5 <-> finger 1)
  - rhythms are not used before they are taught (dotted half: Unit 3; eighths: Unit 9)

Usage: python3 check_pieces.py [--vol N] [unit ids...]
"""
import importlib
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "content"))
from units import VOLUME1, VOLUME2, VOLUME3, VOLUME4, POSITIONS  # noqa: E402

VOLS = {1: (VOLUME1, "unit"), 2: (VOLUME2, "v2unit"), 3: (VOLUME3, "v3unit"), 4: (VOLUME4, "v4unit")}
# Largest leap allowed (in diatonic steps) by the end of each unit
MAX_LEAP = {1: {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2, 8: 4, 9: 4, 10: 4},
            2: {i: 4 for i in range(1, 11)},
            3: {1: 5, 2: 6, 3: 6, 4: 6, 5: 6, 6: 6, 7: 6, 8: 7, 9: 7, 10: 7},
            4: {i: 7 for i in range(1, 9)}}  # Vol 4: octave moves  # Vol 3: broken chords, Alberti; octaves from Unit 8
DOTTED_HALF_FROM = {1: 3, 2: 1, 3: 1, 4: 1}
EIGHTH_FROM = {1: 9, 2: 1, 3: 1, 4: 1}
SIXTEENTH_FROM = {1: 99, 2: 99, 3: 99, 4: 6}
DOTTED_QUARTER_FROM = {1: 99, 2: 3, 3: 1, 4: 1}
STRETCH_FROM = {1: 99, 2: 2, 3: 1, 4: 1}  # from this unit a hand may reach one key beyond its positions
BAR = {"4/4": 8, "3/4": 6, "6/8": 6, "2/4": 4}
TOKEN = re.compile(r"^(R|r|[a-g](?:is|es)?)([',]*)(\d+)?(\.?)(.*)$")
DUR8 = {"1": 8, "2": 4, "4": 2, "8": 1, "16": 0.5}


def parse(music):
    """Yield bars as lists of (step or None, eighths, raw)."""
    bars, cur, last = [], [], "4"
    music = re.sub(r'\\bar\s+"[^"]*"', " ", music)
    music = re.sub(r"\\key\s+\S+\s+\\\w+", " ", music)  # key changes inside a piece
    music = re.sub(r"\\time\s+\S+", " ", music)
    # a two-note chord <e' g'>4 becomes one token "e'+g'4"; its notes are checked one by one
    music = re.sub(r"(?<!\\)<([^<>\\]*)>", lambda m: "+".join(re.sub(r"-\d", "", m.group(1)).split()), music)
    for tok in music.replace("|", " | ").split():
        if tok == "|":
            bars.append(cur)
            cur = []
            continue
        if tok.startswith("\\") or tok.startswith('"'):
            continue
        others = []
        if "+" in tok:  # chord: check every note, follow the top note for leaps
            *low, tok = tok.split("+")
            low = [TOKEN.match(x).groups() for x in low]
            others = [(3 + mk.count("'") - mk.count(","), nm) for nm, mk, _, _, _ in low]
        m = TOKEN.match(tok)
        if not m:
            raise ValueError(f"cannot parse token {tok!r}")
        name, marks, dur, dot, _ = m.groups()
        if name == "R":
            # full-bar rest like R1 or R2.
            d = DUR8[dur] + (DUR8[dur] / 2 if dot else 0)
            cur.append((None, d, tok, True))
            continue
        if dur:
            last = dur + dot
        base = DUR8[last.rstrip(".")]
        d = base + (base / 2 if last.endswith(".") else 0)
        if name == "r":
            cur.append((None, d, tok, False))
            continue
        for octv, nm in others:
            cur.append((octv * 7 + "cdefgab".index(nm[0]), 0, tok, "chord"))
        octave = 3 + marks.count("'") - marks.count(",")
        step = octave * 7 + "cdefgab".index(name[0])
        cur.append((step, d, tok, False))
    if cur:
        bars.append(cur)
    return bars


def unit_ranges(unit, content, extra=(), stretch=0):
    keys = set(extra)
    for p in unit["parts"]:
        for k in ("rh", "lh"):
            if p.get(k):
                keys.add(p[k])
            keys.update(p.get(k + "_positions", []))
            for seg in p.get("modulate", {}).get("to", []):  # key changes bring their own positions
                if seg.get(k):
                    keys.add(seg[k])
    for group in getattr(content, "KEYBOARDS", []) or []:
        keys.update(group)
    ranges = {"RH": [], "LH": []}
    for k in keys:
        pos = POSITIONS[k]
        ranges[pos["hand"]].append((pos["low"] - stretch, pos["high"] + stretch))
    return ranges


def check_unit(unit, vol=1):
    content = importlib.import_module(f"{VOLS[vol][1]}{unit['id']:02d}")
    uid = unit["id"]
    stretch = 1 if uid >= STRETCH_FROM[vol] else 0
    problems = []
    for pc in content.PIECES:
        ranges = unit_ranges(unit, content, pc.get("positions", ()), stretch)
        base_ranges = unit_ranges(unit, content, pc.get("positions", ()), 0)
        L = BAR[pc["meter"]]
        for hand, staff in (("RH", "rh"), ("LH", "lh")):
            bars = parse(pc[staff])
            prev = None
            for b, bar in enumerate(bars, 1):
                total = sum(d for _, d, _, _ in bar)
                if total != L:
                    problems.append(f"{pc['title']} {staff} bar {b}: {total} eighths, expected {L}")
                for step, d, raw, full in bar:
                    if full == "chord":  # lower note of a two-note chord: range check only
                        if not pc.get("allow_range") and not any(lo <= step <= hi for lo, hi in ranges[hand]):
                            problems.append(f"{pc['title']} {staff} bar {b}: {raw} outside this unit's {hand} positions")
                        continue
                    if full:
                        prev = None  # hand re-enters later; no leap check across silence
                        continue
                    if d == 6 and uid < DOTTED_HALF_FROM[vol]:
                        problems.append(f"{pc['title']} {staff} bar {b}: dotted half not taught yet ({raw})")
                    if d == 1 and uid < EIGHTH_FROM[vol]:
                        problems.append(f"{pc['title']} {staff} bar {b}: eighth note not taught yet ({raw})")
                    if d < 1 and uid < SIXTEENTH_FROM[vol]:
                        problems.append(f"{pc['title']} {staff} bar {b}: sixteenth note not taught yet ({raw})")
                    if d == 3 and uid < DOTTED_QUARTER_FROM[vol]:
                        problems.append(f"{pc['title']} {staff} bar {b}: dotted quarter not taught yet ({raw})")
                    if step is None:
                        continue
                    if not pc.get("allow_range") and not any(lo <= step <= hi for lo, hi in ranges[hand]):
                        problems.append(f"{pc['title']} {staff} bar {b}: {raw} outside this unit's {hand} positions")
                    bass_5th = (hand == "LH" and (vol > 1 or uid >= 5) and abs(step - prev if prev is not None else 0) == 4
                                and any(min(step, prev) == lo for lo, hi in base_ranges["LH"]))
                    allowed = pc.get("allow_leap", 0)  # a documented exception, e.g. a folk tune's one skip
                    if (prev is not None and abs(step - prev) > max(MAX_LEAP[vol][uid], allowed)
                            and not bass_5th):
                        problems.append(f"{pc['title']} {staff} bar {b}: leap of {abs(step - prev)} steps ({raw})")
                    prev = step
    return problems


if __name__ == "__main__":
    args = sys.argv[1:]
    vol = 1
    if args and args[0] == "--vol":
        vol, args = int(args[1]), args[2:]
    units = VOLS[vol][0]
    ids = [int(x) for x in args] or [u["id"] for u in units]
    bad = 0
    for uid in ids:
        unit = next(u for u in units if u["id"] == uid)
        try:
            probs = check_unit(unit, vol)
        except ModuleNotFoundError:
            print(f"Unit {uid}: not written yet")
            continue
        print(f"Unit {uid}: {'OK' if not probs else str(len(probs)) + ' problem(s)'}")
        for p in probs:
            print("   ", p)
        bad += len(probs)
    sys.exit(1 if bad else 0)
