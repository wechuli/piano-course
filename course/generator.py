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
from units import CHORDS, CHORD_ORDER, CHORD_MOVES, BASS_PATTERNS, CHORD_MAX_LEAP
from units import R68, CADENCE68, FINAL68
from units import R24, CADENCE24, FINAL24, R24_16, R44_16, CADENCE24_16, CADENCE44_16, FINAL24_16, FINAL44_16
from units import RH_PATTERNS

NAMES = "cdefgab"
BAR_LEN = {"4/4": 8, "3/4": 6, "6/8": 6, "2/4": 4}
DUR = {8: "1", 6: "2.", 4: "2", 3: "4.", 2: "4", 1: "8"}
DUR16 = {16: "1", 12: "2.", 8: "2", 6: "4.", 4: "4", 3: "8.", 2: "8", 1: "16"}  # grid 2: in sixteenths
FULL_REST = {"4/4": "R1", "3/4": "R2.", "6/8": "R2.", "2/4": "R2"}
RHYTHMS = {"4/4": (R44, CADENCE44, FINAL44), "3/4": (R34, CADENCE34, FINAL34), "6/8": (R68, CADENCE68, FINAL68),
           "2/4": (R24, CADENCE24, FINAL24)}
RHYTHMS16 = {"4/4": (R44_16, CADENCE44_16, FINAL44_16), "2/4": (R24_16, CADENCE24_16, FINAL24_16)}
STRONG = {"4/4": (0, 4), "3/4": (0,), "6/8": (0, 3), "2/4": (0,)}  # strong beats, in eighths from the bar line
CONSONANT = (0, 2, 4, 5)  # between two voices: octave/unison, third, fifth, sixth (diatonic steps mod 7)
COUNTER_MOTION = {0: 1.0, 1: 4.0, 2: 3.0, 3: 1.2, 4: 1.2}
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


# Volume 4: a part with grid=2 counts durations in sixteenths instead of eighths.
def grid(part):
    return part.get("grid", 1)


def bar_len(part):
    return BAR_LEN[part["meter"]] * grid(part)


def strong(part):
    return tuple(x * grid(part) for x in STRONG[part["meter"]])


def dur_str(part, d):
    return (DUR16 if grid(part) == 2 else DUR)[d]


def rhythm_tables(part):
    return (RHYTHMS16 if grid(part) == 2 else RHYTHMS)[part["meter"]]


def notes_of(x):
    """The notes of a cell: a single step, a chord (tuple of steps) or a rest (None)."""
    if x is None:
        return ()
    return x if isinstance(x, tuple) else (x,)


def bottom(x):
    return x[0] if isinstance(x, tuple) else x


def raised_pitch(step, key_acc=None):
    """The note one half step above its key-signature spelling (the raised 7th in a minor key)."""
    name = NAMES[step % 7]
    acc = (key_acc or {}).get(name, "")
    up = {"es": "", "": "is", "is": "isis"}[acc]
    n = step // 7 - 3
    return name + up + ("'" * n if n > 0 else "," * (-n))


def note_name(part, ex, b, step, key_acc):
    """LilyPond name of a note in bar b; in a minor key the leading note is raised in V7 bars."""
    if (part.get("minor") and ex.get("chords") and ex["chords"][b] == "V7"
            and pc(step) == (tonic_pc(part) + 6) % 7):
        return raised_pitch(step, key_acc)
    return lily_pitch(step, key_acc)


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
def rhythm_vocab(part, key="rhythms"):
    table = rhythm_tables(part)[0]
    keys = part[key] if isinstance(part[key], list) else [part[key]]
    return [bar for k in keys for bar in table[k]]


def gen_rhythm(part, rng):
    meter = part["meter"]
    vocab = rhythm_vocab(part)
    table, cad, fin = rhythm_tables(part)
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
    if mode == "duet":
        return [part.get("lead", "RH")] * n
    if mode == "lhtune":
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
def gen_melody(part, bars, hands, plan, repeat, rng, chords=None, end_ok=None):
    """Depth-first search for a melody that satisfies all constraints.
    With a chord plan, the first note of each bar and every long note belong to the bar's chord.
    end_ok: pitch classes the last note may have (default: the tonic only)."""
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
    if chords:
        lead = (t + 6) % 7
        tones = [{(t + x) % 7 for x in CHORDS[c]["tones"]} for c in chords]
        bar_start = [k for k, (b, i) in enumerate(slots) if i == 0]
        bass = [chord_notes(part, c)[0] for c in chords]
        onset = [sum(bars[b][:i]) for b, i in slots]
    g = grid(part)

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
            if chords and part.get("lead_weight") and chords[slots[k][0]] == "V7" and pc(s) == lead:
                w *= part["lead_weight"]  # favour the (raised) leading note in V7 bars
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
        if part.get("fast_steps") and k > 0 and hands[slots[k][0]] == hands[slots[k - 1][0]]:
            short = bars[slots[k][0]][slots[k][1]] == 1 or bars[slots[k - 1][0]][slots[k - 1][1]] == 1
            if short and abs(s - mel[k - 1]) > 1:
                return False  # sixteenths move by step (or repeat)
        if k == last_idx and pc(s) not in (end_ok or {t}):
            return False
        if k == cad_idx and pc(s) not in cad_ok:
            return False
        if chords:
            b, i = slots[k]
            if (i == 0 or bars[b][i] >= 4 * g) and pc(s) not in tones[b]:
                return False
            if part.get("beat_tones") and onset[k] in strong(part) and pc(s) not in tones[b]:
                return False  # chord tones on every strong beat (beats 1 and 3, or both beats of 6/8)
            if i == 0 and chords[b] == "V7" and pc(s) == lead:
                return False  # the bass already has the leading note
            if i == 0 and b > 0:
                m1, b1 = mel[bar_start[b - 1]], bass[b - 1]
                if m1 != s and b1 != bass[b] and (m1 - b1) % 7 == (s - bass[b]) % 7 in (0, 4):
                    return False  # parallel octaves or fifths
            if part.get("minor") and chords[b] == "V7" and i > 0 and abs(s - mel[k - 1]) == 1:
                if {pc(s), pc(mel[k - 1])} == {(t + 5) % 7, lead}:
                    return False  # no augmented second (F to G-sharp in A minor)
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


# ---------------------------------------------------------------- chord bass (Volume 3)
def chord_notes(part, name):
    """The three notes of a chord shape, low to high, built on the LH position's lowest note."""
    root = POSITIONS[part["lh"]]["low"]
    return [root + x for x in CHORDS[name]["voicing"]]


def chord_fingers(notes):
    """LH fingers for a three-note shape: 5 on the bottom, 1 on top, 3 or 2 in the middle."""
    return [5, 3 if notes[1] - notes[0] == 2 else 2, 1]


def pattern_note(notes, i):
    """A bass-pattern entry: an index into the shape, "c" (the whole chord) or "u" (its upper two notes)."""
    if i == "c":
        return tuple(notes)
    if i == "u":
        return tuple(notes[1:])
    return notes[i]


def chord_leap_ok(part, a, b):
    """Can the hand get from the end of chord a's pattern to the start of chord b's?"""
    if not part.get("bass"):
        return True  # no left-hand chord pattern (mode "lhtune")
    _, idx = BASS_PATTERNS[(part["bass"], part["meter"])]
    first = bottom(pattern_note(chord_notes(part, b), idx[0]))
    last = bottom(pattern_note(chord_notes(part, a), idx[-1]))
    return abs(first - last) <= part.get("bass_leap", CHORD_MAX_LEAP)


def gen_chord_plan(part, n, repeat, rng):
    """One chord per bar, chosen before the melody. Starts on I, ends V7-I; in 8 bars,
    bar 4 is a half close (V7) or a full close (I). Only called for parts with 'chords'."""
    allowed = [c for c in CHORD_ORDER if c in part["chords"]]
    for _ in range(100):
        plan = ["I"]
        for b in range(1, n):
            if b == n - 1:
                opts = ["I"]
            elif b == n - 2:
                opts = ["V7"]
            elif n == 8 and b == 3:
                opts = ["V7", "I"]
            elif repeat and b in (4, 5):
                opts = [plan[b - 4]]
            else:
                opts = allowed
            opts = [c for c in opts if c in CHORD_MOVES[plan[-1]] and chord_leap_ok(part, plan[-1], c)]
            if not opts:
                break
            w = [CHORD_MOVES[plan[-1]][c] for c in opts]
            plan.append(rng.choices(opts, w)[0])
        if len(plan) == n and all(c in plan for c in part.get("require_chords", ())):
            return plan
    raise RuntimeError(f"no chord plan for part {part['name']}")


def gen_chord_bass(part, bars, chords):
    """Left-hand broken or block chords. Returns (bars of (dur, step or chord), {(bar, note): finger(s)}).
    Patterns with whole chords ("c"/"u") end on the full I chord; broken patterns end on its root."""
    L = bar_len(part)
    durs, idx = BASS_PATTERNS[(part["bass"], part["meter"])]
    durs = [d * grid(part) for d in durs]
    blocks = any(not isinstance(i, int) for i in idx)
    out, fingers = [], {}
    n = len(bars)
    for b, name in enumerate(chords):
        notes = chord_notes(part, name)
        fing = chord_fingers(notes)
        if b == n - 1:
            out.append([(L, tuple(notes) if blocks else notes[0])])
        else:
            out.append([(d, pattern_note(notes, i)) for d, i in zip(durs, idx)])
        if b == 0 or (part.get("chord_fingers") and name != chords[b - 1]):
            first = "c" if (b == n - 1 and blocks) else (0 if b == n - 1 else idx[0])
            fingers[(b, 0)] = fing if first == "c" else (fing[1:] if first == "u" else fing[first])
    return out, fingers


def validate_chords(part, ex, min_used=2):
    """Extra rules for a broken-chord bass under the melody."""
    t = tonic_pc(part)
    chords, mel, lh = ex["chords"], ex["melody"], ex["lh_bars"]
    n = len(chords)
    lead = (t + 6) % 7
    flat = [bottom(s) for bar in lh for _, s in bar]
    for a, c in zip(flat, flat[1:]):
        assert abs(a - c) <= part.get("bass_leap", CHORD_MAX_LEAP), "bass leap too large"
    tops = []
    for b in range(n):
        notes = chord_notes(part, chords[b])
        assert all(x in notes for _, s in lh[b] for x in notes_of(s)), "bass note outside its chord"
        top = mel[b][0]
        tones = {(t + x) % 7 for x in CHORDS[chords[b]]["tones"]}
        assert top is None or pc(top) in tones, "beat 1 of the melody must belong to the chord"
        if chords[b] == "V7":
            assert top is None or pc(top) != lead, "leading note doubled"
        tops.append((top, bottom(lh[b][0][1])))
    for (m1, b1), (m2, b2) in zip(tops, tops[1:]):
        if None in (m1, m2) or m1 == m2 or b1 == b2:
            continue
        i1, i2 = (m1 - b1) % 7, (m2 - b2) % 7
        assert not (i1 == i2 and i1 in (0, 4)), "parallel octaves or fifths between the hands"
    used = set(chords[:-1])
    assert len(used) >= min_used, "too few chords"
    for c in part.get("require_chords", ()):
        assert c in used, f"chord {c} missing"


def add_dyads(part, bars, mel, hands, plan, chords, ties, repeat, rng):
    """Right-hand two-note chords: a third (or sixth) below some melody notes.
    Returns {(bar, note index): lower step}. Only called for parts with 'dyads'."""
    cfg = part["dyads"]
    t = tonic_pc(part)
    out = {}
    tied = {(b, len(bars[b]) - 1) for b in ties} | {(b + 1, 0) for b in ties}
    for b, bar in enumerate(bars):
        if hands[b] != "RH":
            continue
        if repeat and b in (4, 5):
            out.update({(b, i): lo for (bb, i), lo in out.items() if bb == b - 4})
            continue
        lo_pos, _ = pos_range(part, plan["RH"][b])
        for i, d in enumerate(bar):
            s = mel[b][i]
            if s is None or d < cfg.get("min_dur", 2) or (b, i) in tied or rng.random() >= cfg["prob"]:
                continue
            opts = []
            for iv in cfg.get("intervals", (2,)):
                low = s - iv
                if low < lo_pos:
                    continue
                if chords:
                    tones = {(t + x) % 7 for x in CHORDS[chords[b]]["tones"]}
                    if pc(low) not in tones or pc(s) not in tones:
                        continue
                    if chords[b] == "V7" and pc(low) == (t + 6) % 7:
                        continue  # the bass has the leading note
                opts.append(low)
            if opts:
                w = [cfg.get("weights", {}).get(s - low, 1.0) for low in opts]
                out[(b, i)] = rng.choices(opts, w)[0]
    return out


def add_rh_chords(part, bars, mel, hands, plan, chords, ties, repeat, rng):
    """Right-hand three-note chords: the chord tones just below a melody note, inside the hand position.
    Returns {(bar, note index): (lower notes)}. Only called for parts with 'rh_chords' (and 'chords')."""
    cfg = part["rh_chords"]
    t = tonic_pc(part)
    g = grid(part)
    out = {}
    tied = {(b, len(bars[b]) - 1) for b in ties} | {(b + 1, 0) for b in ties}
    for b, bar in enumerate(bars):
        if hands[b] != "RH":
            continue
        if repeat and b in (4, 5):
            out.update({(b, i): lo for (bb, i), lo in out.items() if bb == b - 4})
            continue
        lo_pos, _ = pos_range(part, plan["RH"][b])
        tones = {(t + x) % 7 for x in CHORDS[chords[b]]["tones"]}
        if chords[b] == "V7":
            tones.discard((t + 6) % 7)  # the bass has the leading note
        pos = 0
        for i, d in enumerate(bar):
            s, start = mel[b][i], pos
            pos += d
            where = d >= cfg.get("min_dur", 4) * g or (cfg.get("where") == "strong" and start in strong(part))
            if s is None or not where or (b, i) in tied or pc(s) not in tones or rng.random() >= cfg["prob"]:
                continue
            below = [x for x in range(s - 1, max(lo_pos, s - 5) - 1, -1) if pc(x) in tones]
            if below:
                out[(b, i)] = tuple(sorted(below[:cfg.get("size", 3) - 1]))
    return out


def rh_shape(part, chord, pkey, size=3):
    """Right-hand chord for an accompaniment: the lowest chord tones inside the position, a close shape."""
    t = tonic_pc(part)
    tones = {(t + x) % 7 for x in CHORDS[chord]["tones"]}
    lo, hi = pos_range(part, pkey)
    cand = [x for x in range(lo, hi + 1) if pc(x) in tones]
    if chord == "V7" and len(cand) > size:
        cand = [x for x in cand if pc(x) != (t + 6) % 7]
    return tuple(cand[:size])


def gen_rh_accomp(part, bars, chords, plan):
    """Mode 'lhtune': the right hand plays off-beat chords (pattern from RH_PATTERNS) above a left-hand tune."""
    L = bar_len(part)
    durs, kinds = RH_PATTERNS[(part["accomp"], part["meter"])]
    out = []
    for b, name in enumerate(chords):
        shape = rh_shape(part, name, plan["RH"][b], part.get("accomp_size", 2))
        if b == len(chords) - 1:
            out.append([(L, rh_shape(part, name, plan["RH"][b], 3))])
        else:
            out.append([(d * grid(part), shape if k else None) for d, k in zip(durs, kinds)])
    return out


def counter_rhythm(part, n, repeat, rng):
    """Rhythm for the second voice: from part['counter_rhythms'], cadence in bar 4 of 8, long last bar."""
    vocab = rhythm_vocab(part, "counter_rhythms")
    table, cad, fin = rhythm_tables(part)
    bars = [list(rng.choice(vocab)) for _ in range(n)]
    if n == 8:
        bars[3] = list(rng.choice(cad))
    bars[-1] = list(rng.choice(fin))
    if repeat:
        bars[4], bars[5] = list(bars[0]), list(bars[1])
    return bars


def timed(bars, notes, start=0):
    """[(start, duration, step)] in eighths for a run of bars."""
    out, pos = [], start
    for r, m in zip(bars, notes):
        for d, x in zip(r, m):
            out.append((pos, d, x))
            pos += d
    return out


def gen_counter(part, hand, main, rbars, positions, rng, prev=None, start_pcs=None, end_pcs=None,
                copy=None):
    """A second voice for `hand` against a fixed line `main` ([(start, dur, step)], eighths from the
    first counter bar). Every attack is consonant with the other voice (3rds, 6ths, 5ths, 8ves);
    a note the other voice moves to while this one holds may be a passing note on a weak beat.
    No parallel 5ths or 8ves; contrary motion is preferred. Returns notes per bar, or None."""
    L = BAR_LEN[part["meter"]]
    strong = STRONG[part["meter"]]
    upper = hand == "RH"
    motion = part.get("counter_motion", COUNTER_MOTION)
    slots = []
    for b, r in enumerate(rbars):
        pos = b * L
        for i, d in enumerate(r):
            slots.append((b, i, pos, d))
            pos += d
    n = len(slots)
    idx_of = {(b, i): k for k, (b, i, _, _) in enumerate(slots)}
    forced = {}
    for dst, src in (copy or {}).items():
        for i in range(len(rbars[dst])):
            forced[idx_of[(dst, i)]] = idx_of[(src, i)]
    mains = [x for _, _, x in main]

    def main_at(t0):
        for j, (a, d, x) in enumerate(main):
            if a <= t0 < a + d:
                return j, x
        return None, None

    def interval_ok(c, m):
        if m is None:
            return True
        if (upper and c <= m) or (not upper and c >= m):
            return False  # the voices never cross or meet
        return abs(c - m) % 7 in CONSONANT

    def passing(j):
        return 0 < j < len(mains) - 1 and abs(mains[j] - mains[j - 1]) == 1 and abs(mains[j + 1] - mains[j]) == 1

    cnt = [None] * n
    budget = [6000]

    def ok(k, c):
        b, i, a, d = slots[k]
        j, m = main_at(a)
        if not interval_ok(c, m):
            return False
        for jj, (a2, d2, m2) in enumerate(main):  # the other voice moves while this note holds
            if a < a2 < a + d and not interval_ok(c, m2):
                if (a2 % L) in strong or not passing(jj):
                    return False
        if k == 0 and start_pcs is not None and pc(c) not in start_pcs:
            return False
        if k == n - 1 and end_pcs is not None and pc(c) not in end_pcs:
            return False
        if k >= 2 and cnt[k - 1] == cnt[k - 2] == c:
            return False
        if k >= 1 and m is not None:
            pa = slots[k - 1][2]
            _, pm = main_at(pa)
            pc_ = cnt[k - 1]
            if pm is not None and pc_ != c and pm != m and abs(c - m) % 7 == abs(pc_ - pm) % 7 in (0, 4):
                return False  # parallel octaves or fifths
        return True

    def candidates(k):
        b, i, a, d = slots[k]
        lo, hi = pos_range(part, positions[b])
        if k in forced:
            v = cnt[forced[k]]
            return [v] if lo <= v <= hi else []
        last = cnt[k - 1] if k else prev
        _, m = main_at(a)
        weighted = []
        for c in range(lo, hi + 1):
            w = 1.0
            if last is not None:
                iv = abs(c - last)
                if iv not in motion:
                    continue
                w = motion[iv]
                if k:
                    _, pm = main_at(slots[k - 1][2])
                    if m is not None and pm is not None:
                        dm, dc = (m > pm) - (m < pm), (c > last) - (c < last)
                        w *= 2.0 if dm * dc < 0 else (1.2 if dm * dc == 0 else 1.0)
            if m is not None and abs(c - m) % 7 in (2, 5):
                w *= 1.5  # thirds and sixths sound fullest
            weighted.append((c, w))
        order = []
        while weighted:
            tot = sum(w for _, w in weighted)
            r, acc = rng.random() * tot, 0
            for j, (c, w) in enumerate(weighted):
                acc += w
                if r <= acc:
                    order.append(c)
                    weighted.pop(j)
                    break
        return order

    def dfs(k):
        budget[0] -= 1
        if budget[0] < 0:
            return False
        if k == n:
            return True
        for c in candidates(k):
            if ok(k, c):
                cnt[k] = c
                if dfs(k + 1):
                    return True
        cnt[k] = None
        return False

    if not dfs(0):
        return None
    out, k = [], 0
    for r in rbars:
        out.append(cnt[k:k + len(r)])
        k += len(r)
    return out


def make_duet(part, bars, mel, plan, repeat, rng):
    """Mode 'duet': the lead hand plays the melody, the other hand a counter-melody."""
    t = tonic_pc(part)
    lead = part.get("lead", "RH")
    other = "LH" if lead == "RH" else "RH"
    n = len(bars)
    rbars = counter_rhythm(part, n, repeat, rng)
    starts = {t} if other == "LH" else {t, (t + 2) % 7, (t + 4) % 7}
    cnt = gen_counter(part, other, timed(bars, mel), rbars, plan[other], rng, start_pcs=starts,
                      end_pcs={t}, copy={4: 0, 5: 1} if repeat else None)
    if cnt is None:
        return None
    lead_bars = [list(zip(r, m)) for r, m in zip(bars, mel)]
    other_bars = [list(zip(r, m)) for r, m in zip(rbars, cnt)]
    return (lead_bars, other_bars) if lead == "RH" else (other_bars, lead_bars)


def transpose_into(notes, lo, hi):
    """Move a line by whole octaves so it fits lo..hi, or None."""
    flat = [x for bar in notes for x in bar]
    for k in range(-3, 4):
        if all(lo <= x + 7 * k <= hi for x in flat):
            return [[x + 7 * k for x in bar] for bar in notes]
    return None


def make_imitation(part, rng):
    """Mode 'imitate': the right hand plays a two-bar tune, then the left hand plays it an octave
    (or two) lower while the right hand adds a counter-melody. Eight bars do this twice, with the
    left hand's counter-melody under the second tune. Returns (rh_bars, lh_bars, melody) or None."""
    t = tonic_pc(part)
    n = part["bars"]
    vocab = rhythm_vocab(part)
    _, cad, fin = RHYTHMS[part["meter"]]
    rh, lh = part["rh"], part["lh"]
    sub = dict(part, bars=2)
    one = {"RH": [rh, rh], "LH": [lh, lh]}
    llo, lhi = pos_range(part, lh)
    L = BAR_LEN[part["meter"]]

    def tune(last_bar, end_ok):
        r = [list(rng.choice(vocab)), list(rng.choice(last_bar))]
        m = gen_melody(sub, r, ["RH", "RH"], one, False, rng, end_ok=end_ok)
        if m is None or len({x for bar in m for x in bar}) < 3:
            return None, None, None
        low = transpose_into(m, llo, lhi)
        return (r, m, low) if low else (None, None, None)

    def counter(hand, r_main, m_main, prev, end_pcs, last_fin):
        rb = [list(rng.choice(rhythm_vocab(part, "counter_rhythms"))), list(rng.choice(last_fin))]
        c = gen_counter(part, hand, timed(r_main, m_main), rb, [part["rh" if hand == "RH" else "lh"]] * 2,
                        rng, prev=prev, end_pcs=end_pcs)
        flat = [x for bar in c or [] for x in bar]
        if not c or len(set(flat)) < min(3, len(flat)):
            return None, None  # a counter-melody that only repeats one note is no melody
        return rb, c

    if n == 4:
        ra, ma, la = tune(cad, {t})
        if ma is None:
            return None
        rc, mc = counter("RH", ra, la, ma[-1][-1], {t}, cad)
        if mc is None:
            return None
        rh_bars = [list(zip(r, m)) for r, m in zip(ra + rc, ma + mc)]
        lh_bars = [None, None] + [list(zip(r, m)) for r, m in zip(ra, la)]
        return rh_bars, lh_bars, ma + mc
    ra, ma, la = tune(cad, {t, (t + 2) % 7, (t + 4) % 7})
    if ma is None:
        return None
    rc, mc = counter("RH", ra, la, ma[-1][-1], {(t + 1) % 7, (t + 2) % 7, (t + 4) % 7}, cad)
    if mc is None:
        return None
    rb_, mb, lb = tune(cad, {t})
    if mb is None or abs(mb[0][0] - mc[-1][-1]) > 4:
        return None
    rd, md = counter("LH", rb_, mb, la[-1][-1], None, cad)
    if md is None:
        return None
    re_, me = counter("RH", rb_, lb, mb[-1][-1], {t}, fin)
    if me is None:
        return None
    rh_r, rh_m = ra + rc + rb_ + re_, ma + mc + mb + me
    lh_r, lh_m = ra + rd + rb_, la + md + lb
    rh_bars = [list(zip(r, m)) for r, m in zip(rh_r, rh_m)]
    lh_bars = [None, None] + [list(zip(r, m)) for r, m in zip(lh_r, lh_m)]
    return rh_bars, lh_bars, rh_m


def segment_parts(part):
    """Mode option 'modulate': the exercise in segments, each a sub-part with its own key, tonic and
    positions. The first segment is the home key; later ones start on V7 of their key."""
    segs, home = [], dict(part)
    home.pop("modulate", None)
    first = part["modulate"]["home_bars"]
    segs.append(dict(home, bars=first))
    for seg in part["modulate"]["to"]:
        sub = dict(home)
        sub.pop("rh_positions", None)
        sub.pop("lh_positions", None)
        sub.update(seg)
        segs.append(sub)
    return segs


def make_modulation(part, bars, rng):
    """Build an exercise that changes key. Each segment gets its own chord plan and melody;
    the melody moves smoothly from one segment to the next."""
    rh_bars, lh_bars, mel_all, chords_all, fingers_all, plan_all, bar_parts = [], [], [], [], {}, {"RH": [], "LH": []}, []
    start = 0
    segs = segment_parts(part)
    for si, sub in enumerate(segs):
        n = sub["bars"]
        r = bars[start:start + n]
        t = tonic_pc(sub)
        if si == 0:
            ch = gen_chord_plan(sub, n, False, rng)
        else:
            if n >= 4:  # V7 I ... V7 I: the new key is confirmed at once and again at the end
                middle = [rng.choice(["I", "IV"]) if "IV" in sub["chords"] else "I" for _ in range(n - 4)]
                ch = ["V7", "I"] + middle + ["V7", "I"]
            else:
                ch = ["V7", "I", "I"][:n]
        plan = {"RH": [sub["rh"]] * n, "LH": [sub["lh"]] * n}
        last = si == len(segs) - 1
        end = {t} if last else {t, (t + 2) % 7, (t + 4) % 7}
        m = gen_melody(sub, r, ["RH"] * n, plan, False, rng, ch, end_ok=end)
        if m is None:
            return None
        if mel_all and abs(m[0][0] - mel_all[-1][-1]) > 4:
            return None  # the tune must flow into the new key
        lb, fg = gen_chord_bass(sub, r, ch)
        for (b, j), f in fg.items():
            fingers_all[(b + start, j)] = f
        rh_bars += [list(zip(rr, mm)) for rr, mm in zip(r, m)]
        lh_bars += lb
        mel_all += m
        chords_all += ch
        plan_all["RH"] += plan["RH"]
        plan_all["LH"] += plan["LH"]
        bar_parts += [sub] * n
        start += n
    return rh_bars, lh_bars, mel_all, chords_all, fingers_all, plan_all, bar_parts


def validate_segments(part, ex):
    """Each key segment follows the chord rules of its own key; the piece ends on the last key's tonic,
    and the new key's leading note appears after each change."""
    start = 0
    for si, sub in enumerate(segment_parts(part)):
        n = sub["bars"]
        sl = slice(start, start + n)
        sub_ex = {"chords": ex["chords"][sl], "melody": ex["melody"][sl], "lh_bars": ex["lh_bars"][sl]}
        validate_chords(sub, sub_ex, min_used=2 if si == 0 else 1)
        if si > 0:
            lead = (tonic_pc(sub) + 6) % 7
            heard = [x for bar in ex["lh_bars"][sl] for _, c in bar for x in notes_of(c)]
            heard += [x for bar in ex["melody"][sl] for x in bar if x is not None]
            assert any(pc(x) == lead for x in heard), "the new key's leading note must appear"
        start += n
    last = segment_parts(part)[-1]
    assert pc(ex["melody"][-1][-1]) == tonic_pc(last), "must end on the tonic"
    notes = [x for bar in ex["melody"] for x in bar if x is not None]
    assert len(set(notes)) >= 4, "too little variety"


def validate_voices(part, ex):
    """Duet and imitation: both hands end on the tonic, enough variety, consonant last chord."""
    t = tonic_pc(part)
    for staff in ("rh_bars", "lh_bars"):
        notes = [x for bar in ex[staff] if bar for _, x in bar]
        assert pc(notes[-1]) == t, "each hand must end on the tonic"
        assert len(set(notes)) >= 3, "too little variety"
    assert ex["rh_bars"][-1][-1][1] > ex["lh_bars"][-1][-1][1], "hands cross"


# ---------------------------------------------------------------- validation
def validate(part, ex):
    meter = part["meter"]
    L = bar_len(part)
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
            if hand == "LH" and part.get("chords"):
                continue  # broken-chord bass: checked by validate_chords
            pkey = part["lh"] if (hand == "LH" and part["mode"] == "together") else plan[hand][b]
            lo, hi = pos_range(part, pkey)
            for _, s in bar:
                for x in notes_of(s):
                    assert lo <= x <= hi, f"{hand} note out of position: {x}"
    if part.get("modulate"):
        validate_segments(part, ex)
        return
    if part["mode"] in ("duet", "imitate"):
        validate_voices(part, ex)
        if part["mode"] == "imitate":
            return
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
    if part.get("chords") and part["mode"] == "together":
        validate_chords(part, ex)
    if part.get("rh_chords"):
        assert len(ex["dyads"]) >= part["rh_chords"].get("min", 2), "too few right-hand chords"
    if part.get("dyads"):
        assert len(ex["dyads"]) >= part["dyads"].get("min", 2), "too few two-note chords"


def add_ties(part, mel, hands, plan, repeat, rng, bars=None):
    """Tie the last note of a bar to an equal first note of the next bar (same hand).
    anticip_prob (Volume 4): the same, but only when the bar ends with a short note (an anticipation)."""
    ties = set()
    p = part.get("tie_prob", 0) or part.get("anticip_prob", 0)
    if not p:
        return ties
    n = len(mel)
    for b in range(n - 1):
        if hands[b] != hands[b + 1] or plan[hands[b]][b] != plan[hands[b]][b + 1]:
            continue
        if repeat and (b + 1) in (1, 4, 5):
            continue
        if part.get("anticip_prob") and bars[b][-1] > grid(part):
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
        chords = gen_chord_plan(part, len(bars), repeat, rng) if part.get("chords") else None
        if part["mode"] == "imitate":
            plan = position_plan(part, False, rng)
            got = make_imitation(part, rng)
            if got is None:
                continue
            rh_bars, lh_bars, mel = got
            ex = {"rh_bars": rh_bars, "lh_bars": lh_bars, "melody": mel, "hands": ["RH"] * len(rh_bars),
                  "plan": plan, "repeat": False, "ties": set(), "artic": {},
                  "dyn": add_dynamics(part, len(rh_bars), rng)}
            try:
                validate(part, ex)
            except AssertionError:
                continue
            return ex
        if part.get("modulate"):
            got = make_modulation(part, bars, rng)
            if got is None:
                continue
            rh_bars, lh_bars, mel, chords, fingers, plan, bar_parts = got
            ex = {"rh_bars": rh_bars, "lh_bars": lh_bars, "melody": mel, "hands": ["RH"] * len(bars),
                  "plan": plan, "repeat": False, "ties": set(), "artic": add_articulation(part, len(bars), rng),
                  "dyn": add_dynamics(part, len(bars), rng), "chords": chords, "lh_fingers": fingers,
                  "bar_parts": bar_parts}
            try:
                validate(part, ex)
            except AssertionError:
                continue
            return ex
        mel = gen_melody(part, bars, hands, plan, repeat, rng, chords)
        if mel is None:
            continue
        ties = add_ties(part, mel, hands, plan, repeat, rng, bars=bars)
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
        extra = {}
        if part["mode"] == "together" and part.get("chords"):
            lh_bars, extra["lh_fingers"] = gen_chord_bass(part, bars, chords)
            extra["chords"] = chords
        elif part["mode"] == "together":
            lh_bars = gen_bass(part, bars, mel)
        elif part["mode"] == "duet":
            got = make_duet(part, bars, mel, plan, repeat, rng)
            if got is None:
                continue
            rh_bars, lh_bars = got
        elif part["mode"] == "lhtune":
            rh_bars = gen_rh_accomp(part, bars, chords, plan)
            extra["chords"] = chords
        if part.get("dyads"):
            extra["dyads"] = add_dyads(part, bars, mel, hands, plan, chords, ties, repeat, rng)
        if part.get("rh_chords"):
            extra["dyads"] = add_rh_chords(part, bars, mel, hands, plan, chords, ties, repeat, rng)
        ex = {"rh_bars": rh_bars, "lh_bars": lh_bars, "melody": mel, "hands": hands,
              "plan": plan, "repeat": repeat, "ties": ties, "artic": artic, "dyn": dyn, **extra}
        try:
            validate(part, ex)
        except AssertionError:
            continue
        return ex
    raise RuntimeError(f"could not generate exercise for part {part['name']}")


def signature(ex):
    def key(bars):
        return tuple(tuple(b) if b else None for b in bars)
    if ex.get("dyads"):
        return (key(ex["rh_bars"]), key(ex["lh_bars"]), tuple(sorted(ex["dyads"].items())))
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
    fingers = ex.get("lh_fingers") if together_bass else None  # chord bass: fingers chosen per shape
    dyads = ex.get("dyads", {}) if melody_hand else {}
    n = len(bars)
    inner = {}  # (bar, note): finger list printed inside a chord, <c-5 e-3 g-1>
    accents = part.get("accents") and melody_hand

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
            if fingers is not None:
                if (b, j) in fingers:
                    if isinstance(fingers[(b, j)], list):
                        inner[(b, j)] = fingers[(b, j)]
                    else:
                        suf.insert(0, "_" + str(fingers[(b, j)]))
            elif isinstance(s, tuple) and not marked and (prev_none or new_pos):
                inner[(b, j)] = [finger_for(part, pkey, x) for x in s]
                marked = True
            elif s is not None and not marked and (prev_none or new_pos):
                suf.insert(0, ("^" if hand == "RH" else "_") + str(finger_for(part, pkey, s)))
                marked = True
            if accents and s is not None and sum(dd for dd, _ in bar[:j]) % (2 * grid(part)) and d > grid(part):
                suf.append("->")  # a syncopated note: it starts between the beats
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
                if s is not None and d <= 2 * grid(part) and not tied_from and not tied_to:
                    suf.append("-.")

    def spell(cb, x):
        if "bar_parts" in ex:  # key changes: spell each bar in its own key
            bp = ex["bar_parts"][cb]
            return note_name(bp, ex, cb, x, bp.get("key_acc"))
        return note_name(part, ex, cb, x, key_acc)

    keys = ex.get("key_marks", {})
    toks = []
    for b in range(n):
        if b in keys:
            toks.append(keys[b])
        for (cb, j, d, s, suf) in [c for c in cells if c[0] == b]:
            if j is None:
                toks.append(FULL_REST[meter])
            elif s is None:
                toks.append("r" + dur_str(part, d) + "".join(suf))
            elif isinstance(s, tuple):
                fl = inner.get((cb, j))
                names = [spell(cb, x) + (f"-{fl[i]}" if fl else "") for i, x in enumerate(s)]
                toks.append("<" + " ".join(names) + ">" + dur_str(part, d) + "".join(suf))
            elif (cb, j) in dyads:
                low = dyads[(cb, j)]
                fl = inner.get((cb, j))
                pair = " ".join(spell(cb, x) for x in notes_of(low)) + " " + spell(cb, s)
                toks.append("<" + pair + ">" + dur_str(part, d) + "".join(suf))
            elif "bar_parts" in ex:
                toks.append(spell(cb, s) + dur_str(part, d) + "".join(suf))
            elif part.get("minor"):
                toks.append(note_name(part, ex, cb, s, key_acc) + dur_str(part, d) + "".join(suf))
            else:
                toks.append(lily_pitch(s, key_acc) + dur_str(part, d) + "".join(suf))
        toks.append("|")
        if part["bars"] == 8 and b == 3 and hand == "RH":
            toks.append("\\break \\noPageBreak")
    return " ".join(toks)


def lily_exercise(part, ex, label):
    meter = part["meter"]
    key = part.get("key", "c \\major")
    key_acc = part.get("key_acc")
    rh_mel, lh_mel = True, part["mode"] != "together"
    if part["mode"] == "duet":
        rh_mel = part.get("lead", "RH") == "RH"
        lh_mel = not rh_mel
    elif part["mode"] == "imitate":
        lh_mel = False
    elif part["mode"] == "lhtune":
        rh_mel = False
    if part.get("modulate"):
        ex["key_marks"] = key_marks(part)
    rh = staff_music(part, ex, "RH", key_acc, melody_hand=rh_mel)
    lh = staff_music(part, ex, "LH", key_acc, melody_hand=lh_mel)
    acc = "\\accidentalStyle modern " if part.get("minor") else ""  # a natural sign after a raised 7th

    def has_chords(bars):
        return any(isinstance(x, tuple) for bar in bars if bar for _, x in bar)
    left = "\\set fingeringOrientations = #'(left) "  # finger numbers beside a chord, not above and below
    rpre = left if has_chords(ex["rh_bars"]) or part.get("rh_chords") else ""
    lpre = left if has_chords(ex["lh_bars"]) else ""
    return f"""
\\score {{
  \\header {{ piece = \\markup \\exLabel "{label}" }}
  \\new PianoStaff <<
    \\new Staff = "up" {{ \\autoLineBreaksOff \\clef treble \\key {key} \\time {meter} {acc}{rpre}{rh} \\bar "|." }}
    \\new Staff = "down" {{ \\clef bass \\key {key} \\time {meter} {acc}{lpre}{lh} \\bar "|." }}
  >>
  \\layout {{ }}
}}
"""


def key_marks(part):
    """LilyPond key changes at the start of each new key segment (when the part shows them)."""
    if part["modulate"].get("show") != "signature":
        return {}
    out, start = {}, 0
    segs = segment_parts(part)
    for sub, nxt in zip(segs, segs[1:]):
        start += sub["bars"]
        out[start] = f'\\bar "||" \\key {nxt.get("key", "c \\major")}'
    return out


def generate_unit(unit, seed=None):
    rng = random.Random(seed if seed is not None else 1000 + unit["id"])
    seen = set()
    result = []
    for part in unit["parts"]:
        result.append((part, generate_part(part, rng, seen)))
    return result
