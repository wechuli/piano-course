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
from units import VOLUME1, VOLUME2, VOLUME3, VOLUME4, VOLUME5, POSITIONS  # noqa: E402

VOLS = {1: (VOLUME1, "unit"), 2: (VOLUME2, "v2unit"), 3: (VOLUME3, "v3unit"), 4: (VOLUME4, "v4unit"),
        5: (VOLUME5, "v5unit")}
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


# ---------------------------------------------------------------- Volume 5
# Volume 5 has no hand positions, so its pieces are checked for what has been taught instead: keys,
# time signatures, triplets, pedal, clef changes and ornaments, and (from LilyPond's own reading of the
# music) bar lengths, each hand's span at any moment and its largest leap.
V5_MAX_ACC = {1: 3, 2: 3, 3: 3, 4: 3, 5: 4, 6: 7, 7: 7, 8: 7}       # sharps or flats in the key signature
V5_METERS = {"4/4", "3/4", "2/4", "6/8"}
V5_METERS_U4 = V5_METERS | {"3/8", "9/8", "12/8", "2/2"}            # new time signatures from Unit 4
V5_FEATURES = [  # (pattern, first unit, name)
    (r"\\tuplet|\\times", 4, "triplets"),
    (r"\\sustainOn|\\sustainOff", 7, "pedal marks"),
    (r"\\clef", 7, "clef changes"),
    (r"\\trill|\\prall|\\mordent|\\turn|\\acciaccatura|\\appoggiatura|\\grace", 8, "ornaments"),
]
VERBOSE = "--verbose" in sys.argv
V5_MAX_LEAP = {u: (12 if u < 7 else 24) for u in range(1, 9)}     # semitones (left hand: a tenth); two octaves with the pedal

LISTENER = r"""
#(define (v5-listener context)
  (let ((id (ly:context-id context)))
    (make-engraver
      (listeners
        ((note-event engraver event)
          (let* ((m (ly:context-current-moment (ly:translator-context engraver)))
                 (p (ly:event-property event 'pitch))
                 (d (ly:event-property event 'duration)))
            (if (and (ly:pitch? p) (ly:duration? d))
              (format #t "EV ~a ~a ~a ~a ~a\n" id (ly:moment-main m)
                      (if (zero? (ly:moment-grace m)) 0 1)
                      (+ 60 (ly:pitch-semitones p)) (ly:moment-main (ly:duration-length d))))))))))
\layout { \context { \Staff \consists #v5-listener } }
"""


def v5_events(pieces):
    """Compile the pieces (without output) and collect every note LilyPond reads, per staff, plus
    LilyPond's warnings (a bar check that fails means a bar of the wrong length)."""
    import subprocess
    import tempfile
    from fractions import Fraction
    import build
    parts = ['\\version "2.24.0"', LISTENER]
    for i, pc in enumerate(pieces):
        pre = "\\once \\override Staff.TimeSignature.style = #'C " if pc.get("cut") else ""
        parts.append(f"""\\score {{ \\new PianoStaff <<
  \\new Staff = "p{i}rh" {{ \\clef treble \\key {pc.get('key', 'c \\major')} {pre}\\time {pc['meter']} {pc['rh']} }}
  \\new Staff = "p{i}lh" {{ \\clef bass \\key {pc.get('key', 'c \\major')} {pre}\\time {pc['meter']} {pc['lh']} }}
>> \\layout {{ }} }}""")
    with tempfile.TemporaryDirectory() as d:
        ly = os.path.join(d, "check.ly")
        open(ly, "w").write("\n".join(parts))
        r = subprocess.run([build.lilypond_bin(), "-dno-print-pages", "-o", os.path.join(d, "out"), ly],
                           capture_output=True, text=True, cwd=d)
    if r.returncode != 0:
        raise SystemExit(r.stderr[-3000:])
    ev = {}
    for line in r.stdout.splitlines():
        if line.startswith("EV "):
            _, sid, mom, grace, pitch, dur = line.split()
            ev.setdefault(sid, []).append((Fraction(mom), grace == "1", int(pitch), Fraction(dur)))
    warns = [w for w in r.stderr.splitlines() if "warning" in w.lower()]
    return ev, warns


def check_unit_v5(unit, content):
    import gen5
    uid = unit["id"]
    problems = []
    pieces = content.PIECES
    ev, warns = v5_events(pieces)
    for w in warns:
        problems.append("LilyPond: " + w.split("warning:")[-1].strip())
    for i, pc in enumerate(pieces):
        t = pc["title"]
        music = pc["rh"] + " " + pc["lh"]
        keys = [pc.get("key", "c \\major")] + re.findall(r"\\key\s+(\S+\s+\\\w+)", music)
        for k in keys:
            name, mode = k.split()
            n = gen5.Key(name, mode.lstrip("\\")).accidentals()
            if n > V5_MAX_ACC[uid] and not pc.get("allow_key"):
                problems.append(f"{t}: key {k} has {n} sharps or flats (Unit {uid} allows {V5_MAX_ACC[uid]})")
        meters = [pc["meter"]] + re.findall(r"\\time\s+(\d+/\d+)", music)
        for m in meters:
            if m not in (V5_METERS_U4 if uid >= 4 else V5_METERS):
                problems.append(f"{t}: time signature {m} not taught yet")
        for pat, first, what in V5_FEATURES:
            if uid < first and re.search(pat, music) and what not in pc.get("allow", ()):
                problems.append(f"{t}: {what} not taught yet")
        for hand in ("rh", "lh"):
            notes = [x for x in ev.get(f"p{i}{hand}", []) if not x[1]]
            if not notes:
                continue
            span_max = pc.get("allow_span", 12)
            bar_len = Fraction_(*map(int, pc["meter"].split("/")))
            up = Fraction_(*map(int, pc["upbeat"].split("/"))) if pc.get("upbeat") else 0
            for m, _, p, d in notes:
                sounding = [p2 for m2, _, p2, d2 in notes if m2 <= m < m2 + d2]
                if max(sounding) - min(sounding) > span_max:
                    where = (m - up) / bar_len
                    problems.append(f"{t} {hand}: span of {max(sounding) - min(sounding)} semitones in bar "
                                    f"{int(where) + 1} (beat {float((where - int(where)) * bar_len * 4) + 1:g})")
                    if not VERBOSE:
                        break
            onsets = sorted({m for m, _, _, _ in notes})
            # how far the hand must jump: from what sounds just before each new note (or chord) to its
            # nearest note (so an oom-pah bass or a held voice is not counted as a leap)
            leap = 0
            for a, b in zip(onsets, onsets[1:]):
                before = [(p, m2 + d2) for m2, _, p, d2 in notes if m2 <= a < m2 + d2]
                if max(e for _, e in before) < b:
                    continue  # a rest in between: the hand has time to move
                new = [p for m2, _, p, _ in notes if m2 == b]
                leap = max(leap, min(abs(x - y) for x, _ in before for y in new))
            limit = V5_MAX_LEAP[uid] + (4 if hand == "lh" and uid < 7 else 0)  # oom-pah: bass to chord, a tenth
            if leap > pc.get("allow_leap", limit):
                problems.append(f"{t} {hand}: leap of {leap} semitones")
            short = min(d for _, _, _, d in notes)
            if short < Fraction_(1, 16) and not pc.get("allow_32"):
                problems.append(f"{t} {hand}: notes shorter than a sixteenth")
    return problems


def Fraction_(a, b):
    from fractions import Fraction
    return Fraction(a, b)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--verbose"]
    vol = 1
    if args and args[0] == "--vol":
        vol, args = int(args[1]), args[2:]
    units = VOLS[vol][0]
    ids = [int(x) for x in args] or [u["id"] for u in units]
    bad = 0
    for uid in ids:
        unit = next(u for u in units if u["id"] == uid)
        try:
            if vol >= 5:
                probs = check_unit_v5(unit, importlib.import_module(f"{VOLS[vol][1]}{uid:02d}"))
            else:
                probs = check_unit(unit, vol)
        except ModuleNotFoundError:
            print(f"Unit {uid}: not written yet")
            continue
        print(f"Unit {uid}: {'OK' if not probs else str(len(probs)) + ' problem(s)'}")
        for p in probs:
            print("   ", p)
        bad += len(probs)
    sys.exit(1 if bad else 0)
