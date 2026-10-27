"""Exercise generator for the sight-reading course.

Produces graded, playable, deduplicated exercises from the part specs in units.py
and emits LilyPond code. Every exercise is validated before it is accepted.

Determinism: optional features (shifts, stretches, ties, rests, articulation,
dynamics) only draw random numbers when a part switches them on, so exercises of
parts that don't use them are byte-identical to earlier builds.
"""
import math
import random

from units import POSITIONS, R44, R34, CADENCE44, CADENCE34, FINAL44, FINAL34

NAMES = "cdefgab"
BAR_LEN = {"4/4": 8, "3/4": 6}
DUR = {8: "1", 6: "2.", 4: "2", 3: "4.", 2: "4", 1: "8"}
FULL_REST = {"4/4": "R1", "3/4": "R2."}
DEFAULT_SHIFT_MOTION = {0: 1.0, 1: 3.0, 2: 3.0, 3: 2.0, 4: 1.5}
DYN_LEVELS = ["p", "mp", "mf", "f"]


def lily_pitch(step, key_acc=None):
    name = NAMES[step % 7]
    if key_acc and name in key_acc:
        name += key_acc[name]
    octave = step // 7
    n = octave - 3
    return name + ("'" * n if n > 0 else "," * (-n))


def pc(step):
    """Pitch class index 0..6 (C..B)."""
    return step % 7


def tonic_pc(part):
    return pc(part.get("tonic", 28))


# ---------------------------------------------------------------- positions
def pos_range(part, pos_key):
    """(low, high) of a position, widened by the part's stretch ('extend')."""
    pos = POSITIONS[pos_key]
    e = part.get("extend", 0)
    return pos["low"] - e, pos["high"] + e


def finger_for(part, pos_key, step):
    pos = POSITIONS[pos_key]
    if pos["hand"] == "RH":
        f = step - pos["low"] + 1
    else:
        f = 5 - (step - pos["low"])
    return max(1, min(5, f))  # a stretch note uses the end finger (1 or 5)


def hand_options(part, hand):
    key = "rh" if hand == "RH" else "lh"
    opts = part.get(key + "_positions")
    if opts:
        return list(opts)
    return [part[key]] if part.get(key) else []


# ---------------------------------------------------------------- rhythm
def gen_rhythm(part, rng):
    meter = part["meter"]
    table = R44 if meter == "4/4" else R34
    keys = part["rhythms"] if isinstance(part["rhythms"], list) else [part["rhythms"]]
    vocab = [bar for k in keys for bar in table[k]]
    cad = CADENCE44 if meter == "4/4" else CADENCE34
    fin = FINAL44 if meter == "4/4" else FINAL34
    n = part["bars"]
    bars = [list(rng.choice(vocab)) for _ in range(n)]
    if n == 8:
        bars[3] = list(rng.choice(cad))
    bars[-1] = list(rng.choice(fin))
    repeat = n == 8 and rng.random() < part.get("repeat_prob", 0)
    if repeat:
        bars[4], bars[5] = list(bars[0]), list(bars[1])
    return bars, repeat


# ---------------------------------------------------------------- hands per bar
def hand_plan(part, rng):
    """Which hand plays the melody in each bar."""
    n, mode = part["bars"], part["mode"]
    if mode in ("RH", "together"):
        return ["RH"] * n
    if mode == "LH":
        return ["LH"] * n
    # alt: two-bar segments, alternating, random starting hand
    first = rng.choice(["RH", "LH"])
    other = "LH" if first == "RH" else "RH"
    return [first if (b // 2) % 2 == 0 else other for b in range(n)]


def position_plan(part, repeat, rng):
    """Hand position for every bar, per hand. Shifts happen at segment boundaries."""
    n = part["bars"]
    every = part.get("shift_every", 2)
    t = tonic_pc(part)
    plan = {}
    for hand in ("RH", "LH"):
        opts = hand_options(part, hand)
        if not opts:
            plan[hand] = [None] * n
            continue
        nseg = math.ceil(n / every)
        segs = [opts[0]]
        for _ in range(1, nseg):
            cur = segs[-1]
            if len(opts) > 1 and rng.random() < part.get("shift_prob", 0.7):
                cur = rng.choice([o for o in opts if o != cur])
            segs.append(cur)
        if repeat and every == 2 and nseg >= 3:
            segs[2] = segs[0]
        lo, hi = pos_range(part, segs[-1])
        if not any(pc(s) == t for s in range(lo, hi + 1)):
            segs[-1] = opts[0]  # must be able to end on the tonic
        plan[hand] = [segs[b // every] for b in range(n)]
    return plan


def shift_into(prev, lo, hi):
    """Move prev by octaves so it is as close as possible to the range lo..hi."""
    best, bestd = prev, 99
    for k in range(-3, 4):
        s = prev + 7 * k
        d = 0 if lo <= s <= hi else min(abs(s - lo), abs(s - hi))
        if d < bestd:
            best, bestd = s, d
    return best


# ---------------------------------------------------------------- melody
def gen_melody(part, bars, hands, plan, repeat, rng):
    """Depth-first search for a melody that satisfies all constraints."""
    motion = part["motion"]
    shift_motion = part.get("shift_motion", DEFAULT_SHIFT_MOTION)
    t = tonic_pc(part)
    slots = [(b, i) for b, bar in enumerate(bars) for i in range(len(bar))]
    n = len(slots)
    forced = {}
    if repeat:
        idx_of = {s: k for k, s in enumerate(slots)}
        for b_src, b_dst in ((0, 4), (1, 5)):
            for i in range(len(bars[b_src])):
                forced[idx_of[(b_dst, i)]] = idx_of[(b_src, i)]
    last_idx = n - 1
    cad_idx = None
    if len(bars) == 8:
        cad_idx = max(k for k, (b, i) in enumerate(slots) if b == 3)
    starts_ok = {t, (t + 2) % 7, (t + 4) % 7}
    cad_ok = {(t + 1) % 7, (t + 2) % 7, (t + 4) % 7}

    mel = [None] * n

    def where(k):
        b = slots[k][0]
        hand = hands[b]
        return hand, plan[hand][b]

    def candidates(k):
        hand, pkey = where(k)
        lo, hi = pos_range(part, pkey)
        rng_notes = list(range(lo, hi + 1))
        if k in forced:
            v = mel[forced[k]]
            return [v] if lo <= v <= hi else []
        if k == 0:
            c = [s for s in rng_notes if pc(s) in starts_ok]
            rng.shuffle(c)
            return c
        prev = mel[k - 1]
        phand, ppos = where(k - 1)
        table = motion
        if phand != hand:
            prev = shift_into(prev, lo, hi)
        elif ppos != pkey:
            table = shift_motion  # the hand moves to a new position here
        direction = 0
        if k >= 2 and hands[slots[k - 2][0]] == phand == hand:
            direction = (mel[k - 1] > mel[k - 2]) - (mel[k - 1] < mel[k - 2])
        weighted = []
        for s in rng_notes:
            iv = abs(s - prev)
            if iv not in table:
                continue
            w = table[iv]
            if direction and (s - prev) * direction > 0:
                w *= 1.6  # keep going the same way: produces scale fragments
            weighted.append((s, w))
        order = []
        pool = weighted[:]
        while pool:
            tot = sum(w for _, w in pool)
            r = rng.random() * tot
            acc = 0
            for j, (s, w) in enumerate(pool):
                acc += w
                if r <= acc:
                    order.append(s)
                    pool.pop(j)
                    break
        return order

    def ok(k, s):
        if k >= 3 and mel[k - 1] == mel[k - 2] == mel[k - 3] == s:
            return False
        if k == last_idx and pc(s) != t:
            return False
        if k == cad_idx and pc(s) not in cad_ok:
            return False
        return True

    budget = [20000]

    def dfs(k):
        budget[0] -= 1
        if budget[0] < 0:
            return False
        if k == n:
            return True
        for s in candidates(k):
            if ok(k, s):
                mel[k] = s
                if dfs(k + 1):
                    return True
        mel[k] = None
        return False

    if not dfs(0):
        return None
    out, k = [], 0
    for bar in bars:
        out.append(mel[k:k + len(bar)])
        k += len(bar)
    return out


# ---------------------------------------------------------------- bass for 'together'
def gen_bass(part, bars, melody):
    meter = part["meter"]
    L = BAR_LEN[meter]
    t = tonic_pc(part)
    lpos = POSITIONS[part["lh"]]
    tonic_note = lpos["low"]           # five-finger position starts on the tonic
    dom_note = lpos["low"] + 4         # and the dominant is the top note
    out = []
    n = len(bars)
    for b, (r, m) in enumerate(zip(bars, melody)):
        if part.get("bass", "whole") == "half" and meter == "4/4":
            spans = [(0, 4), (4, 8)]
        else:
            spans = [(0, L)]
        bar_notes = []
        pos = 0
        timed = []
        for d, s in zip(r, m):
            timed.append((pos, d, s))
            pos += d
        for (a, z) in spans:
            inside = [s for (p, d, s) in timed if p < z and p + d > a and s is not None]
            rel = [(pc(s) - t) % 7 for s in inside]
            i_score = sum(1 for x in rel if x in (0, 2))
            v_score = sum(1 for x in rel if x in (1, 3, 6))
            chord = "V" if v_score > i_score else "I"
            if b == n - 1:
                chord = "I"
            bar_notes.append((z - a, dom_note if chord == "V" else tonic_note))
        if len(bar_notes) == 2 and bar_notes[0][1] == bar_notes[1][1]:
            bar_notes = [(L, bar_notes[0][1])]
        out.append(bar_notes)
    return out


# ---------------------------------------------------------------- validation
def validate(part, ex):
    meter = part["meter"]
    L = BAR_LEN[meter]
    plan = ex["plan"]
    for staff in ("rh_bars", "lh_bars"):
        for bar in ex[staff]:
            if bar is None:
                continue
            assert sum(d for d, _ in bar) == L, f"bar length wrong in {staff}: {bar}"
    for hand, staff in (("RH", "rh_bars"), ("LH", "lh_bars")):
        for b, bar in enumerate(ex[staff]):
            if bar is None:
                continue
            pkey = part["lh"] if (hand == "LH" and part["mode"] == "together") else plan[hand][b]
            lo, hi = pos_range(part, pkey)
            for _, s in bar:
                if s is None:
                    continue
                assert lo <= s <= hi, f"{hand} note out of position: {s}"
    flat = [(s, ex["hands"][b], plan[ex["hands"][b]][b]) for b, bar in enumerate(ex["melody"]) for s in bar]
    shift_motion = part.get("shift_motion", DEFAULT_SHIFT_MOTION)
    for (a, ha, pa), (c, hc, pc_) in zip(flat, flat[1:]):
        if ha == hc and a is not None and c is not None:
            table = part["motion"] if pa == pc_ else shift_motion
            assert abs(a - c) in table, f"interval {abs(a - c)} not allowed"
    melody_notes = [s for s, _, _ in flat]
    assert melody_notes[-1] is not None and pc(melody_notes[-1]) == tonic_pc(part), "must end on tonic"
    sounding = [s for s in melody_notes if s is not None]
    assert len(set(sounding)) >= (4 if part["bars"] == 8 else 3), "too little variety"
    for b in ex.get("ties", ()):
        assert ex["melody"][b][-1] == ex["melody"][b + 1][0] is not None, "tie must join equal pitches"


def add_ties(part, mel, hands, plan, repeat, rng):
    """Tie the last note of a bar to an equal first note of the next bar (same hand)."""
    ties = set()
    p = part.get("tie_prob", 0)
    if not p:
        return ties
    n = len(mel)
    for b in range(n - 1):
        if hands[b] != hands[b + 1] or plan[hands[b]][b] != plan[hands[b]][b + 1]:
            continue
        if repeat and (b + 1) in (1, 4, 5):
            continue
        if rng.random() >= p:
            continue
        new = mel[b][-1]
        nxt = mel[b + 1][1] if len(mel[b + 1]) > 1 else (mel[b + 2][0] if b + 2 < n else None)
        if b + 1 == n - 1 and pc(new) != tonic_pc(part):
            continue
        if nxt is not None and abs(nxt - new) not in part["motion"]:
            continue
        mel[b + 1][0] = new
        ties.add(b)
    return ties


def entry_bars(hands, plan):
    """Bars whose first note starts a hand entry or a new hand position."""
    out = set()
    for b in range(len(hands)):
        h = hands[b]
        if b == 0 or hands[b - 1] != h or plan[h][b] != plan[h][b - 1]:
            out.add(b)
    return out


def add_rests(part, bars, mel, hands, plan, repeat, ties, rng):
    """Replace a few notes with rests of the same length (never first/last/cadence/tied notes)."""
    p = part.get("rest_prob", 0)
    if not p:
        return
    n = len(bars)
    protected = set()
    for b in ties:
        protected.add((b, len(bars[b]) - 1))
        protected.add((b + 1, 0))
    for b in entry_bars(hands, plan):
        protected.add((b, 0))  # carries the finger number
    if n == 8:
        protected.add((3, len(bars[3]) - 1))
    for b in range(n - 1):
        if repeat and b in (4, 5):
            for i in range(len(bars[b])):
                mel[b][i] = mel[b - 4][i]
            continue
        prev_rest = False
        pos_in_bar = 0
        for i, d in enumerate(bars[b]):
            start, pos_in_bar = pos_in_bar, pos_in_bar + d
            # half rests only on beats 1 and 3 (standard notation); never dotted-half or whole rests
            if (b, i) in protected or d >= 6 or prev_rest or (d == 4 and start % 4 != 0):
                prev_rest = False
                continue
            if rng.random() < p:
                mel[b][i] = None
                prev_rest = True
            else:
                prev_rest = False


def add_articulation(part, n, rng):
    """Per two-bar segment: 'slur' (legato), 'stacc' (staccato) or None."""
    a = part.get("artic")
    if not a:
        return {}
    out = {}
    for seg in range(math.ceil(n / 2)):
        r = rng.random()
        if r < a.get("slur", 0):
            out[seg] = "slur"
        elif r < a.get("slur", 0) + a.get("stacc", 0):
            out[seg] = "stacc"
    return out


def add_dynamics(part, n, rng):
    """Dynamic marks attached to the first note (or rest) of the melody in some bars."""
    if not part.get("dynamics"):
        return {}
    levels = part.get("dyn_levels", DYN_LEVELS)
    first = rng.choice(levels)
    marks = {0: "\\" + first}
    if n == 8:
        second = rng.choice([x for x in levels if x != first])
        louder = levels.index(second) > levels.index(first)
        marks[2] = "\\<" if louder else "\\>"
        marks[4] = "\\" + second
    elif rng.random() < 0.5:
        other = rng.choice([x for x in levels if x != first])
        louder = levels.index(other) > levels.index(first)
        marks[1] = "\\<" if louder else "\\>"
        marks[n - 1] = "\\" + other
    return marks


# ---------------------------------------------------------------- one exercise
def make_exercise(part, rng):
    for _ in range(200):
        bars, repeat = gen_rhythm(part, rng)
        hands = hand_plan(part, rng)
        plan = position_plan(part, repeat, rng)
        mel = gen_melody(part, bars, hands, plan, repeat, rng)
        if mel is None:
            continue
        ties = add_ties(part, mel, hands, plan, repeat, rng)
        add_rests(part, bars, mel, hands, plan, repeat, ties, rng)
        artic = add_articulation(part, len(bars), rng)
        dyn = add_dynamics(part, len(bars), rng)
        rh_bars, lh_bars = [], []
        for b, (r, m) in enumerate(zip(bars, mel)):
            notes = list(zip(r, m))
            if hands[b] == "RH":
                rh_bars.append(notes)
                lh_bars.append(None)
            else:
                lh_bars.append(notes)
                rh_bars.append(None)
        if part["mode"] == "together":
            lh_bars = gen_bass(part, bars, mel)
        ex = {"rh_bars": rh_bars, "lh_bars": lh_bars, "melody": mel, "hands": hands,
              "plan": plan, "repeat": repeat, "ties": ties, "artic": artic, "dyn": dyn}
        try:
            validate(part, ex)
        except AssertionError:
            continue
        return ex
    raise RuntimeError(f"could not generate exercise for part {part['name']}")


def signature(ex):
    def key(bars):
        return tuple(tuple(b) if b else None for b in bars)
    return (key(ex["rh_bars"]), key(ex["lh_bars"]))


def generate_part(part, rng, seen):
    out = []
    tries = 0
    while len(out) < part["count"]:
        tries += 1
        if tries > part["count"] * 50:
            raise RuntimeError("too many duplicates; widen the rules")
        ex = make_exercise(part, rng)
        sig = signature(ex)
        if sig in seen:
            continue
        seen.add(sig)
        out.append(ex)
    return out


# ---------------------------------------------------------------- LilyPond output
def staff_music(part, ex, hand, key_acc, melody_hand=True):
    meter = part["meter"]
    bars = ex["rh_bars"] if hand == "RH" else ex["lh_bars"]
    ties = ex.get("ties", ())
    plan = ex.get("plan") or {hand: [part.get("rh" if hand == "RH" else "lh")] * len(bars)}
    together_bass = hand == "LH" and part["mode"] == "together"
    artic = ex.get("artic", {}) if melody_hand else {}
    dyn = ex.get("dyn", {}) if melody_hand else {}
    n = len(bars)

    # Build per-note tokens first, then add slurs/staccato by two-bar segment.
    cells = []  # (bar, j, d, s, [suffixes])
    prev_none = True
    prev_pos = None
    for b, bar in enumerate(bars):
        if bar is None:
            cells.append((b, None, None, None, []))
            prev_none = True
            continue
        pkey = part["lh"] if together_bass else plan[hand][b]
        new_pos = pkey != prev_pos
        prev_pos = pkey
        marked = False
        for j, (d, s) in enumerate(bar):
            suf = []
            if j == 0 and b in dyn:
                suf.append(dyn[b])
            if s is not None and not marked and (prev_none or new_pos):
                suf.insert(0, ("^" if hand == "RH" else "_") + str(finger_for(part, pkey, s)))
                marked = True
            if s is not None and b in ties and j == len(bar) - 1 and melody_hand:
                suf.append("~")
            cells.append((b, j, d, s, suf))
        prev_none = False

    for seg, kind in artic.items():
        seg_cells = [c for c in cells if c[1] is not None and seg * 2 <= c[0] < seg * 2 + 2]
        if not seg_cells:
            continue
        if kind == "slur":
            sounding = [c for c in seg_cells if c[3] is not None]
            if len(sounding) >= 2 and all(c[3] is not None for c in seg_cells):
                sounding[0][4].append("(")
                sounding[-1][4].append(")")
        elif kind == "stacc":
            for c in seg_cells:
                b, j, d, s, suf = c
                tied_from = "~" in suf
                tied_to = (b - 1) in ties and j == 0
                if s is not None and d <= 2 and not tied_from and not tied_to:
                    suf.append("-.")

    toks = []
    for b in range(n):
        for (cb, j, d, s, suf) in [c for c in cells if c[0] == b]:
            if j is None:
                toks.append(FULL_REST[meter])
            elif s is None:
                toks.append("r" + DUR[d] + "".join(suf))
            else:
                toks.append(lily_pitch(s, key_acc) + DUR[d] + "".join(suf))
        toks.append("|")
        if part["bars"] == 8 and b == 3 and hand == "RH":
            toks.append("\\break \\noPageBreak")
    return " ".join(toks)


def lily_exercise(part, ex, label):
    meter = part["meter"]
    key = part.get("key", "c \\major")
    key_acc = part.get("key_acc")
    rh = staff_music(part, ex, "RH", key_acc)
    lh = staff_music(part, ex, "LH", key_acc, melody_hand=part["mode"] != "together")
    return f"""
\\score {{
  \\header {{ piece = \\markup \\exLabel "{label}" }}
  \\new PianoStaff <<
    \\new Staff = "up" {{ \\autoLineBreaksOff \\clef treble \\key {key} \\time {meter} {rh} \\bar "|." }}
    \\new Staff = "down" {{ \\clef bass \\key {key} \\time {meter} {lh} \\bar "|." }}
  >>
  \\layout {{ }}
}}
"""


def generate_unit(unit, seed=None):
    rng = random.Random(seed if seed is not None else 1000 + unit["id"])
    seen = set()
    result = []
    for part in unit["parts"]:
        result.append((part, generate_part(part, rng, seen)))
    return result
