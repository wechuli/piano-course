"""Volume 5 exercise generator: reading by key, chord and pattern (Levels 5-6).

Volume 5 leaves the five-finger positions behind, so it has its own generator. Volumes 1-4 keep
using generator.py, which is not touched (their output must stay byte-identical).

Pitches are (step, alt) pairs: the diatonic step (C4 = 28, as in units.py) and the note's actual
alteration in half steps (-1 flat, 0 natural, +1 sharp), independent of the key signature.
LilyPond prints accidentals against the key signature by itself. Durations are Fractions of a
whole note; a triplet eighth is 1/12.

Every exercise is built in layers: a chord plan (one chord per bar), a tune that puts chord tones on
the strong beats and moves by step through any other note, then the texture of the part (a held
second voice, a tenor line, a left-hand pattern, four-part harmony, ...). Each layer is checked, and
the whole exercise is validated before it is accepted.
"""
import random
from fractions import Fraction as Fr

LETTERS = "cdefgab"
NAT = [0, 2, 4, 5, 7, 9, 11]
ACC = {-2: "eses", -1: "es", 0: "", 1: "is", 2: "isis"}
SCALES = {"major": [0, 2, 4, 5, 7, 9, 11], "minor": [0, 2, 3, 5, 7, 8, 10]}
ACC_EN = {-2: "-double-flat", -1: "-flat", 0: "", 1: "-sharp", 2: "-double-sharp"}


def midi(n):
    return 12 + 12 * (n[0] // 7) + NAT[n[0] % 7] + n[1]


def lily(n):
    step, alt = n
    o = step // 7 - 3
    return LETTERS[step % 7] + ACC[alt] + ("'" * o if o > 0 else "," * (-o))


class Key:
    """A key: tonic letter and alteration, mode, and the key signature as {pitch class: alt}."""

    def __init__(self, name, mode="major"):
        self.name, self.mode = name, mode
        self.tpc = LETTERS.index(name[0])
        rest = name[1:]
        self.talt = rest.count("is") - rest.count("es")
        tsemi = NAT[self.tpc] + self.talt
        self.sig = {}
        for d, iv in enumerate(SCALES[mode]):
            p = (self.tpc + d) % 7
            a = (tsemi + iv - NAT[p]) % 12
            self.sig[p] = a - 12 if a > 6 else a
        self.lily = f"{name} \\{mode}"
        self.tonic = 28 + self.tpc  # the tonic in the octave above middle C

    def degree(self, step):
        return (step - self.tpc) % 7

    def note(self, step, extra=0):
        return (step, self.sig[step % 7] + extra)

    def accidentals(self):
        return sum(1 for a in self.sig.values() if a)

    def text(self):
        return LETTERS[self.tpc].upper() + ACC_EN[self.talt] + " " + self.mode


# ---------------------------------------------------------------- meters and rhythms
METERS = {  # bar length, strong beats, beat length, full-bar rest
    "4/4": (Fr(1), (Fr(0), Fr(1, 2)), Fr(1, 4), "R1"),
    "3/4": (Fr(3, 4), (Fr(0),), Fr(1, 4), "R2."),
    "2/4": (Fr(1, 2), (Fr(0),), Fr(1, 4), "R2"),
    "6/8": (Fr(3, 4), (Fr(0), Fr(3, 8)), Fr(3, 8), "R2."),
    "3/8": (Fr(3, 8), (Fr(0),), Fr(3, 8), "R4."),
    "9/8": (Fr(9, 8), (Fr(0), Fr(3, 8), Fr(3, 4)), Fr(3, 8), "R4.*3"),
    "12/8": (Fr(3, 2), (Fr(0), Fr(3, 4)), Fr(3, 8), "R1."),
    "2/2": (Fr(1), (Fr(0), Fr(1, 2)), Fr(1, 2), "R1"),
}
TOK = {"1.": Fr(3, 2), "1": Fr(1), "2..": Fr(7, 8), "2.": Fr(3, 4), "2": Fr(1, 2), "4.": Fr(3, 8),
       "4": Fr(1, 4), "8.": Fr(3, 16), "8": Fr(1, 8), "16": Fr(1, 16)}
PRINT = {v: k for k, v in TOK.items()}

# One entry = one bar. "t8" is a triplet eighth (three in a quarter), "t4" a triplet quarter;
# "b" is a note lasting the whole bar.
RHY = {
    "4/4": {
        "basic": ["4 4 4 4", "2 4 4", "4 4 2", "4. 8 4 4", "4 4 4. 8", "2 2", "4 8 8 4 4", "4 4 8 8 4"],
        "eighths": ["8 8 8 8 4 4", "4 4 8 8 8 8", "8 8 4 8 8 4", "4. 8 8 8 4", "4 8 8 2"],
        "trip": ["t8 t8 t8 4 4 4", "4 t8 t8 t8 4 4", "4 4 t8 t8 t8 4", "t8 t8 t8 t8 t8 t8 2",
                 "4 t4 t8 4 4", "2 t8 t8 t8 4", "t8 t8 t8 4 t8 t8 t8 4"],
        "slow": ["2 2", "2. 4", "1", "2 4 4", "4 4 2"],
        "motive": ["8 8 8 8 4 4", "8 8 4 8 8 4", "4 8 8 8 8 4", "8 8 8 8 8 8 4"],
        "cad": ["2 2", "4 4 2", "2. 4"], "fin": ["1"],
    },
    "3/4": {
        "basic": ["4 4 4", "2 4", "4 2", "4. 8 4", "4 4 4"],
        "eighths": ["8 8 4 4", "4 8 8 4", "4 4 8 8", "4. 8 8 8"],
        "trip": ["t8 t8 t8 4 4", "4 t8 t8 t8 4", "4 4 t8 t8 t8", "t8 t8 t8 2", "4 t4 t8 4"],
        "slow": ["2.", "2 4", "4 2", "2."],
        "motive": ["8 8 8 8 4", "4 8 8 8 8", "8 8 4 8 8"],
        "cad": ["2 4", "2."], "fin": ["2."],
    },
    "2/4": {
        "basic": ["4 4", "8 8 4", "4 8 8", "4. 8", "2", "8 8 8 8"],
        "cad": ["2", "4 4"], "fin": ["2"],
    },
    "6/8": {
        "basic": ["4. 4.", "4 8 4.", "4. 4 8", "8 8 8 4.", "4 8 4 8", "2."],
        "cad": ["4. 4.", "4 8 4."], "fin": ["2."],
    },
    "3/8": {
        "basic": ["4.", "4 8", "8 8 8", "8 4", "16 16 8 8", "8. 16 8", "8 16 16 8"],
        "cad": ["4.", "4 8"], "fin": ["4."],
    },
    "9/8": {
        "basic": ["4. 4. 4.", "4 8 4. 4.", "4. 4 8 4.", "8 8 8 4. 4.", "4. 4. 4 8", "4. 8 8 8 4."],
        "cad": ["2. 4.", "4. 4. 4."], "fin": ["b"],
    },
    "12/8": {
        "basic": ["4. 4. 4. 4.", "4 8 4. 4 8 4.", "8 8 8 4. 4. 4.", "2. 4. 4.", "4. 4. 2.", "4. 4 8 4. 4 8"],
        "cad": ["2. 2.", "4. 4. 2."], "fin": ["1."],
    },
    "2/2": {
        "basic": ["2 2", "4 4 2", "2 4 4", "4 4 4 4", "2. 4"],
        "cad": ["2 2", "1"], "fin": ["1"],
    },
}


def parse_rhythm(s, bar):
    out = []
    for t in s.split():
        if t == "b":
            out.append((bar, False))
        elif t.startswith("t"):
            out.append((TOK[t[1:]] * Fr(2, 3), True))
        else:
            out.append((TOK[t], False))
    assert sum(d for d, _ in out) == bar, s
    return out


# ---------------------------------------------------------------- chords
# root degree and chord degrees (0 = tonic), root first
CHORDS = {
    "I": (0, (0, 2, 4)), "ii": (1, (1, 3, 5)), "IV": (3, (3, 5, 0)), "V": (4, (4, 6, 1)),
    "V7": (4, (4, 6, 1, 3)), "vi": (5, (5, 0, 2)), "V7/V": (1, (1, 3, 5, 0)),
    "i": (0, (0, 2, 4)), "iv": (3, (3, 5, 0)), "VI": (5, (5, 0, 2)),
}
MOVES = {
    "major": {"I": {"I": 0.5, "IV": 2.0, "ii": 1.2, "vi": 1.2, "V": 1.5, "V7": 1.2, "V7/V": 0.8},
              "ii": {"V": 2.0, "V7": 2.0, "V7/V": 0.6},
              "IV": {"V": 2.0, "V7": 1.5, "I": 1.2, "ii": 1.0, "V7/V": 1.0},
              "V": {"I": 3.0, "vi": 0.8, "V7": 0.8},
              "V7": {"I": 3.0, "vi": 0.8},
              "vi": {"ii": 1.5, "IV": 1.5, "V": 0.5, "V7/V": 0.8},
              "V7/V": {"V": 2.0, "V7": 2.0}},
    "minor": {"i": {"i": 0.5, "iv": 2.0, "VI": 1.2, "V": 1.5, "V7": 1.2},
              "iv": {"V": 2.0, "V7": 1.5, "i": 1.2},
              "V": {"i": 3.0, "VI": 0.8, "V7": 0.8},
              "V7": {"i": 3.0, "VI": 0.8},
              "VI": {"iv": 1.5, "V": 0.8, "V7": 0.6}},
}


def tonic_chord(key):
    return "I" if key.mode == "major" else "i"


def chord_alts(key, name):
    """Accidentals a chord adds to the key: the raised 7th of V in minor, the raised 4th of V7/V."""
    alts = {}
    if key.mode == "minor" and name in ("V", "V7"):
        alts[6] = 1
    if name == "V7/V":
        alts[3] = 1
        if key.mode == "minor":
            alts[5] = 1
    return alts


def chord_degrees(name):
    return CHORDS[name][1]


def spell(key, step, chord=None, extra=0):
    alt = key.sig[step % 7]
    if chord:
        alt += chord_alts(key, chord).get(key.degree(step), 0)
    return (step, alt + extra)


def voicing(key, chord, root_step):
    """Close root-position chord on root_step: root, third, fifth (and seventh)."""
    n = len(chord_degrees(chord))
    return [spell(key, root_step + 2 * i, chord) for i in range(n)]


def nearest(key, degree, target, lo, hi):
    opts = [s for s in range(lo, hi + 1) if key.degree(s) == degree]
    return min(opts, key=lambda s: (abs(s - target), s))


# ---------------------------------------------------------------- events and LilyPond output
def ev(d, notes=(), tup=False, post=None, end=None, pre=None):
    return {"d": d, "n": list(notes), "t": tup, "post": list(post or []), "end": list(end or []),
            "pre": list(pre or [])}


SPLIT = {Fr(9, 8): ["2.", "4."], Fr(5, 8): ["2", "8"], Fr(5, 4): ["1", "4"]}


def dur_pieces(d):
    if d in PRINT:
        return [PRINT[d]]
    if d in SPLIT:
        return SPLIT[d]
    out = []
    for v in sorted(PRINT, reverse=True):
        while d >= v:
            out.append(PRINT[v])
            d -= v
    assert d == 0
    return out


def ev_str(e):
    if e.get("R"):
        return " ".join(e["pre"] + [e["R"]])
    pieces = [PRINT[e["d"] * Fr(3, 2)]] if e["t"] else dur_pieces(e["d"])
    if not e["n"]:
        toks = ["r" + p for p in pieces]
    else:
        ns = sorted(e["n"], key=midi)
        pitch = lily(ns[0]) if len(ns) == 1 else "<" + " ".join(lily(x) for x in ns) + ">"
        toks = [pitch + p for p in pieces]
        toks = [t + "~" for t in toks[:-1]] + toks[-1:]
    toks[0] += "".join(e["post"])
    toks[-1] += "".join(e["end"])
    return " ".join(e["pre"] + toks)


def voice_str(bars, breaks=()):
    out = []
    for b, bar in enumerate(bars):
        acc, open_ = Fr(0), False
        for e in bar:
            if e["t"] and not open_:
                out.append("\\tuplet 3/2 {")
                open_, acc = True, Fr(0)
            out.append(ev_str(e))
            if open_:
                acc += e["d"]
                if acc == Fr(1, 4):
                    out.append("}")
                    open_ = False
        assert not open_, "unfinished triplet"
        out.append("|")
        if b in breaks:
            out.append("\\break \\noPageBreak")
    return " ".join(out)


def staff_str(voices, breaks=()):
    if len(voices) == 1:
        return voice_str(voices[0], breaks)
    return ("<< { " + voice_str(voices[0], breaks) + " } \\\\ { " + voice_str(voices[1]) + " } >>")


def full_rest(meter):
    return {"R": METERS[meter][3], "pre": [], "d": METERS[meter][0], "n": [], "t": False}


# ---------------------------------------------------------------- plans
def phrase_marks(n):
    """Cadence bars: {bar index: kind}. 8 bars: a breath at bar 4; 16 bars: a half close at bar 8."""
    if n == 8:
        return {3: "phrase"}
    if n == 16:
        return {3: "phrase", 7: "half", 11: "phrase"}
    return {}


def repeat_map(part, n, rng):
    """{bar: earlier bar it copies}: bars 5-6 copy 1-2 (8 bars), bars 9-12 copy 1-4 (16 bars)."""
    if not rng_flag(part, "repeat_prob", rng):
        return {}
    if n == 8:
        return {4: 0, 5: 1}
    if n == 16:
        return {8: 0, 9: 1, 10: 2, 11: 3}
    return {}


def rng_flag(part, key, rng):
    p = part.get(key, 0)
    return bool(p) and rng.random() < p


def gen_rhythm(part, rng, n, rep):
    T = RHY[part["meter"]]
    bar = METERS[part["meter"]][0]
    names = part["rhythms"] if isinstance(part["rhythms"], list) else [part["rhythms"]]
    vocab = [r for k in names for r in T[k]]
    bars = [rng.choice(vocab) for _ in range(n)]
    for b in phrase_marks(n):
        bars[b] = rng.choice(T["cad"])
    bars[-1] = rng.choice(T["fin"])
    for dst, src in rep.items():
        bars[dst] = bars[src]
    return [parse_rhythm(r, bar) for r in bars]


def gen_chord_plan(part, key, n, rep, rng):
    allowed = part.get("chords") or (["I", "IV", "V", "V7", "ii", "vi"] if key.mode == "major"
                                     else ["i", "iv", "V", "V7", "VI"])
    moves = MOVES[key.mode]
    I = tonic_chord(key)
    dom = [c for c in ("V7", "V") if c in allowed]
    marks = phrase_marks(n)
    for _ in range(300):
        plan = [I]
        for b in range(1, n):
            if b in rep:
                opts = [plan[rep[b]]]
            elif b == n - 1:
                opts = [I]
            elif b == n - 2:
                opts = dom
            elif marks.get(b) == "half":
                opts = ["V"] if "V" in allowed else dom
            elif marks.get(b) == "phrase":
                opts = [I, "V"] if "V" in allowed else [I]
            else:
                opts = allowed
            opts = [c for c in opts if c in moves.get(plan[-1], {})]
            if not opts:
                break
            plan.append(rng.choices(opts, [moves[plan[-1]][c] for c in opts])[0])
        if len(plan) == n and all(c in plan for c in part.get("require_chords", ())):
            if len(set(plan)) >= min(3, len(allowed)):
                return plan
    raise RuntimeError(f"no chord plan for {part['name']}")


# ---------------------------------------------------------------- the tune
MOTION = {0: 1.0, 1: 5.0, 2: 2.5, 3: 1.0, 4: 0.8, 5: 0.3, 7: 0.3}


def rh_range(part, key):
    lo, span = part.get("rh_lo"), part.get("rh_span", 10)
    if lo is None:
        lo = max(28, key.tonic - 3) + part.get("rh_up", 0)
        lo = min(lo, 40 - span)  # never higher than A5
    return lo, lo + span


def gen_tune(part, key, rbars, plan, rng, lo, hi, bass=None, start=None, prev=None, end_degs=None,
             cad_degs=None, rep=None, strict_end=True):
    """Depth-first search for a tune over the chord plan.

    rbars: [[(dur, tuplet)]] per bar; plan: chord per bar; bass: midi of the bass at each bar's
    downbeat (for the parallel-octave check). Chord tones on accented notes (downbeats, strong beats,
    dotted quarters and longer); any other note is a passing or neighbour note, entered and left by
    step. A leap of a 4th or more is followed by a step back (or a smaller leap the other way).
    Returns [[step]] per bar, or None."""
    meter = part["meter"]
    strong = METERS[meter][1]
    motion = part.get("motion", MOTION)
    slots = []
    for b, r in enumerate(rbars):
        on = Fr(0)
        for i, (d, tup) in enumerate(r):
            slots.append({"b": b, "i": i, "d": d, "on": on, "t": tup,
                          "acc": i == 0 or on in strong or d >= Fr(3, 8)})
            on += d
    n = len(slots)
    first_of = {}
    for k, s in enumerate(slots):
        first_of.setdefault(s["b"], k)
    forced = {}
    for dst, src in (rep or {}).items():
        for i in range(len(rbars[dst])):
            forced[first_of[dst] + i] = first_of[src] + i
    marks = phrase_marks(len(rbars))
    cad_idx = {max(k for k, s in enumerate(slots) if s["b"] == b): kind for b, kind in marks.items()}
    tones = [set(chord_degrees(c)) for c in plan]
    I = tonic_chord(key)
    mel = [None] * n
    end_degs = end_degs if end_degs is not None else {0}

    def deg(s):
        return key.degree(s)

    def cands(k):
        if k in forced:
            v = mel[forced[k]]
            return [v] if lo <= v <= hi else []
        if k == 0 and prev is None:
            c = [s for s in range(lo, hi + 1) if deg(s) in (start or {0, 2, 4})]
            rng.shuffle(c)
            return c
        p = mel[k - 1] if k else prev
        direction = 0
        if k >= 2:
            direction = (mel[k - 1] > mel[k - 2]) - (mel[k - 1] < mel[k - 2])
        pool = []
        for s in range(lo, hi + 1):
            iv = abs(s - p)
            if iv not in motion:
                continue
            w = motion[iv]
            if direction and (s - p) * direction > 0:
                w *= 1.5
            pool.append((s, w))
        order = []
        while pool:
            tot = sum(w for _, w in pool)
            r, acc = rng.random() * tot, 0
            for j, (s, w) in enumerate(pool):
                acc += w
                if r <= acc:
                    order.append(s)
                    pool.pop(j)
                    break
        return order

    def ok(k, s):
        sl = slots[k]
        b = sl["b"]
        ct = deg(s) in tones[b]
        p = mel[k - 1] if k else prev
        if k >= 3 and mel[k - 1] == mel[k - 2] == mel[k - 3] == s:
            return False
        if k == 0 and start is not None and deg(s) not in start:
            return False
        if sl["acc"] and not ct:
            return False
        if not ct and (p is None or abs(s - p) != 1):
            return False  # a non-chord note is reached by step
        if k >= 1 and p is not None:
            pb = slots[k - 1]["b"] if k else None
            pdeg_ct = k >= 1 and deg(mel[k - 1]) in tones[slots[k - 1]["b"]]
            if k >= 1 and not pdeg_ct and abs(s - p) != 1:
                return False  # ... and left by step
            if k >= 2 and abs(mel[k - 1] - mel[k - 2]) >= 3:
                lp = mel[k - 1] - mel[k - 2]
                if (s - p) * lp > 0 or abs(s - p) >= abs(lp):
                    return False  # fill the gap after a leap
            # the leading note of V rises to the tonic over I
            pbar = slots[k - 1]["b"]
            if (pbar != b and plan[pbar] in ("V", "V7") and plan[b] == I and deg(p) == 6 and s != p + 1):
                return False
            if key.mode == "minor" and plan[pbar] in ("V", "V7") and deg(p) == 6 and s < p:
                return False  # the raised 7th does not fall
            if key.mode == "minor" and abs(s - p) == 1 and {deg(s), deg(p)} == {5, 6} \
                    and not part.get("melodic_minor"):
                return False  # no augmented second (F to G-sharp in A minor)
            if part.get("melodic_minor") and k >= 2 and deg(mel[k - 2]) == 5 and p == mel[k - 2] + 1 \
                    and s != p + 1:
                return False  # 6-7 going up continues to the tonic (both raised)
            if plan[b] == "V7" and p is not None and deg(p) == 3 and pbar == b and s > p and \
                    deg(p) in tones[b] and slots[k - 1]["acc"]:
                return False  # an accented 7th of V7 falls
        if k == n - 1 and strict_end and deg(s) not in end_degs:
            return False
        if k in cad_idx:
            kind = cad_idx[k]
            allowed = cad_degs.get(kind) if cad_degs else None
            if allowed is None:
                allowed = {1, 4, 6} if kind == "half" else (tones[b] if plan[b] != I else {0, 2, 4})
            if deg(s) not in allowed:
                return False
        if bass is not None and sl["i"] == 0 and b > 0:
            m1, b1 = midi(spell(key, mel[first_of[b - 1]], plan[b - 1])), bass[b - 1]
            m2, b2 = midi(spell(key, s, plan[b])), bass[b]
            if m1 != m2 and b1 != b2 and (m1 - b1) % 12 == (m2 - b2) % 12 and (m2 - b2) % 12 in (0, 7):
                return False  # parallel octaves or fifths with the bass
        return True

    budget = [30000]

    def dfs(k):
        budget[0] -= 1
        if budget[0] < 0:
            return False
        if k == n:
            return True
        for s in cands(k):
            if ok(k, s):
                mel[k] = s
                if dfs(k + 1):
                    return True
        mel[k] = None
        return False

    if not dfs(0):
        return None
    out, k = [], 0
    for r in rbars:
        out.append(mel[k:k + len(r)])
        k += len(r)
    return out


def tune_events(key, rbars, steps, plan, melodic=False):
    """Turn a tune into events with the right accidentals (raised 7th of minor, V7/V's raised 4th,
    and with melodic=True the raised 6th and 7th of the rising melodic minor)."""
    flat = [(b, i, s) for b, bar in enumerate(steps) for i, s in enumerate(bar)]
    alts = {}
    for k, (b, i, s) in enumerate(flat):
        n = spell(key, s, plan[b])
        d = key.degree(s)
        nxt = flat[k + 1][2] if k + 1 < len(flat) else None
        if key.mode == "minor":
            if d == 6 and nxt == s + 1:
                n = (s, key.sig[s % 7] + 1)  # leading note rising to the tonic
            if melodic and d == 5 and nxt == s + 1 and k + 2 < len(flat) and flat[k + 2][2] == s + 2:
                n = (s, key.sig[s % 7] + 1)  # raised 6th going up through 6-7-8
            if melodic and d == 6 and nxt == s + 1:
                n = (s, key.sig[s % 7] + 1)
        alts[(b, i)] = n
    out = []
    for b, bar in enumerate(rbars):
        out.append([ev(d, [alts[(b, i)]], tup) for i, (d, tup) in enumerate(bar)])
    return out


def check_line(events, max_leap=12):
    """No augmented seconds or leaps over an octave in a single line."""
    flat = [e["n"][0] for bar in events for e in bar if e["n"]]
    for a, c in zip(flat, flat[1:]):
        if abs(a[0] - c[0]) == 1 and abs(midi(a) - midi(c)) == 3:
            return False
        if abs(midi(a) - midi(c)) > max_leap:
            return False
    return True


# ---------------------------------------------------------------- left-hand patterns
# (duration, what): an index into the chord (0 root, 1 third, 2 fifth, 3 seventh), "c" the whole
# chord, "u" its upper notes, "w5"/"w10" the fifth and the tenth above the root (wide patterns),
# "hi" the chord an octave above the root (after a low root: the Gymnopedie pattern).
LH = {
    ("block", "4/4"): [("1", "c")], ("block", "3/4"): [("2.", "c")], ("block", "2/4"): [("2", "c")],
    ("block", "6/8"): [("2.", "c")], ("block", "3/8"): [("4.", "c")], ("block", "9/8"): [("b", "c")],
    ("block", "12/8"): [("1.", "c")], ("block", "2/2"): [("1", "c")],
    ("block2", "4/4"): [("2", "c"), ("2", "c")], ("block2", "2/2"): [("2", "c"), ("2", "c")],
    ("waltz", "3/4"): [("4", 0), ("4", "u"), ("4", "u")],
    ("waltz", "3/8"): [("8", 0), ("8", "u"), ("8", "u")],
    ("oompah", "4/4"): [("4", 0), ("4", "u"), ("4", 0), ("4", "u")],
    ("oompah", "2/2"): [("4", 0), ("4", "u"), ("4", 0), ("4", "u")],
    ("oompah", "2/4"): [("4", 0), ("4", "u")],
    ("broken", "4/4"): [("4", 0), ("4", 1), ("4", 2), ("4", 1)],
    ("broken", "3/4"): [("4", 0), ("4", 1), ("4", 2)],
    ("broken", "6/8"): [("8", 0), ("8", 1), ("8", 2), ("8", 1), ("8", 2), ("8", 1)],
    ("broken", "9/8"): [("8", 0), ("8", 1), ("8", 2)] * 3,
    ("broken", "12/8"): [("8", 0), ("8", 1), ("8", 2)] * 4,
    ("broken", "3/8"): [("8", 0), ("8", 1), ("8", 2)],
    ("broken", "2/2"): [("4", 0), ("4", 1), ("4", 2), ("4", 1)],
    ("alberti", "4/4"): [("8", 0), ("8", 2), ("8", 1), ("8", 2)] * 2,
    ("alberti", "3/4"): [("8", 0), ("8", 2), ("8", 1), ("8", 2), ("8", 1), ("8", 2)],
    ("triplet", "4/4"): [("t8", 0), ("t8", 1), ("t8", 2)] * 4,
    ("triplet", "3/4"): [("t8", 0), ("t8", 1), ("t8", 2)] * 3,
    ("triplet", "2/2"): [("t8", 0), ("t8", 1), ("t8", 2)] * 4,
    ("wide", "4/4"): [("4", 0), ("4", "w5"), ("4", "w10"), ("4", "w5")],
    ("wide", "3/4"): [("4", 0), ("4", "w5"), ("4", "w10")],
    ("wide", "6/8"): [("8", 0), ("8", "w5"), ("8", "w10"), ("8", "w5"), ("8", "w10"), ("8", "w5")],
    ("wide8", "4/4"): [("8", 0), ("8", "w5"), ("8", "w10"), ("8", "w5")] * 2,
    ("leap", "3/4"): [("4", 0), ("2", "hi")],
    ("leap", "4/4"): [("4", 0), ("4", "hi"), ("4", "w5"), ("4", "hi")],
}
LH_ROOTS = {"wide": (14, 20), "wide8": (14, 20), "leap": (15, 21)}  # roots lower for these patterns


def lh_note(key, chord, root, what):
    v = voicing(key, chord, root)
    if what == "c":
        return v
    if what == "u":
        return v[1:]
    if what == "w5":
        return [spell(key, root + 4, chord)]
    if what == "w10":
        return [spell(key, root + 9, chord)]
    if what == "hi":
        return [spell(key, root + 7 + 2 * i, chord) for i in range(3)]
    return [v[min(what, len(v) - 1)]]


def lh_roots(part, key, plan):
    lo, hi = part.get("lh_roots") or LH_ROOTS.get(part.get("bass"), (17, 23))
    roots, prev = [], key.tonic - 10
    for c in plan:
        r = nearest(key, CHORDS[c][0], prev, lo, hi)
        roots.append(r)
        prev = r
    return roots


def gen_lh(part, key, plan, roots):
    """Left-hand pattern bars from the chord plan. The last bar holds the tonic chord (or root)."""
    meter = part["meter"]
    bar = METERS[meter][0]
    pat = LH[(part["bass"], meter)]
    out = []
    n = len(plan)
    for b, (c, r) in enumerate(zip(plan, roots)):
        if b == n - 1:
            if part["bass"] in ("wide", "wide8", "leap"):
                out.append([ev(bar, [spell(key, r, c)])])
            else:
                out.append([ev(bar, voicing(key, c, r) if part["bass"] != "broken" else [spell(key, r, c)])])
            continue
        evs = []
        for dtok, what in pat:
            d = bar if dtok == "b" else (TOK[dtok[1:]] * Fr(2, 3) if dtok.startswith("t") else TOK[dtok])
            evs.append(ev(d, lh_note(key, c, r, what), dtok.startswith("t")))
        out.append(evs)
    return out


def add_pedal(lh, plan):
    """Sustain pedal (bracket style): down on the first note, changed (up and down again) at every
    chord change. The last pedal is held to the final bar line."""
    for b, bar in enumerate(lh):
        if b == 0:
            bar[0]["post"].append("\\sustainOn")
        elif plan[b] != plan[b - 1]:
            bar[0]["post"].append("\\sustainOff\\sustainOn")


# ---------------------------------------------------------------- second voices
def held_voice(part, key, rbars, mel_ev, plan, roots, rng):
    """Mode rh2='held': a lower voice in the right hand that holds a chord tone a 3rd or 6th below
    the tune for the whole bar. It stays below every tune note it sounds under (no unisons, no
    crossing) and within an octave of the highest one. Returns bars of events, or None."""
    bar = METERS[part["meter"]][0]
    out, prev = [], None
    n = len(plan)
    for b in range(n):
        notes = [e["n"][0] for e in mel_ev[b] if e["n"]]
        top = max(notes, key=midi)
        low = min(notes, key=midi)
        first = mel_ev[b][0]["n"][0]
        cands = []
        for iv in (2, 5):
            s = first[0] - iv
            if key.degree(s) not in chord_degrees(plan[b]):
                continue
            h = spell(key, s, plan[b])
            if midi(h) >= midi(low) or midi(top) - midi(h) > 12 or s < 25:
                continue
            if b == n - 1 and key.degree(s) not in (0, 2, 4):
                continue
            w = 2.0 if prev is None or abs(s - prev[0]) <= 2 else 0.6
            cands.append((h, w))
        if not cands:
            return None
        h = rng.choices([c for c, _ in cands], [w for _, w in cands])[0]
        out.append([ev(bar, [h])])
        prev = h
    return out


def tenor_voice(part, key, plan, roots, mel_ev, rng):
    """Mode lh2='tenor': the left hand holds the bass (the chord root) with stems down and plays a
    quarter-note tenor line above it with stems up: chord tones on the beats where the chord is
    struck, passing notes by step between them; within an octave of the bass and below the tune."""
    meter = part["meter"]
    bar = METERS[meter][0]
    n = len(plan)
    beats = int(bar / Fr(1, 4))
    rb = []
    for b in range(n):
        if b == n - 1:
            rb.append([bar])
        else:
            rb.append(rng.choice([[Fr(1, 4)] * beats, [Fr(1, 2)] + [Fr(1, 4)] * (beats - 2)]))
    slots = [(b, i, d, sum(rb[b][:i])) for b in range(n) for i, d in enumerate(rb[b])]

    def rh_low(b, on, d):
        lows = []
        t = Fr(0)
        for e in mel_ev[b]:
            if t < on + d and t + e["d"] > on and e["n"]:
                lows.append(midi(e["n"][0]))
            t += e["d"]
        return min(lows) if lows else 99

    line = [None] * len(slots)

    def ok(k, s):
        b, i, d, on = slots[k]
        r = roots[b]
        if not (r + 2 <= s <= r + 7):
            return False
        note = spell(key, s, plan[b])
        if midi(note) >= rh_low(b, on, d) - 2:
            return False
        ct = key.degree(s) in chord_degrees(plan[b])
        if (i == 0 or on in METERS[meter][1] or d >= Fr(1, 2)) and not ct:
            return False
        if k:
            p = line[k - 1]
            if abs(s - p) > 3:
                return False
            pct = key.degree(p) in chord_degrees(plan[slots[k - 1][0]])
            if (not ct or not pct) and abs(s - p) != 1:
                return False
            if k >= 2 and line[k - 1] == line[k - 2] == s:
                return False
            if i == 0:  # parallels with the bass at the bar line
                pb = slots[k - 1][0]
                t1, b1 = midi(spell(key, p, plan[pb])), midi(spell(key, roots[pb], plan[pb]))
                t2, b2 = midi(note), midi(spell(key, r, plan[b]))
                if t1 != t2 and b1 != b2 and (t1 - b1) % 12 == (t2 - b2) % 12 in (0, 7):
                    return False
        if k == len(slots) - 1 and key.degree(s) not in (2, 4):
            return False
        return True

    budget = [8000]

    def dfs(k):
        budget[0] -= 1
        if budget[0] < 0:
            return False
        if k == len(slots):
            return True
        b = slots[k][0]
        opts = list(range(roots[b] + 2, roots[b] + 8))
        rng.shuffle(opts)
        if k:
            opts.sort(key=lambda s: abs(s - line[k - 1]) + rng.random() * 1.5)
        for s in opts:
            if ok(k, s):
                line[k] = s
                if dfs(k + 1):
                    return True
        line[k] = None
        return False

    if not dfs(0):
        return None
    tenor, bass = [], []
    k = 0
    for b in range(n):
        tb = []
        for d in rb[b]:
            tb.append(ev(d, [spell(key, line[k], plan[b])]))
            k += 1
        tenor.append(tb)
        bass.append([ev(bar, [spell(key, roots[b], plan[b])])])
    if len({e["n"][0] for bar_ in tenor for e in bar_}) < 4:
        return None
    return tenor, bass


# ---------------------------------------------------------------- chromatic notes
def add_chromatic(key, mel, cfg, rng):
    """Chromatic passing notes (a quarter splits into two eighths: C C-sharp | D, or E E-flat | D) and
    chromatic lower neighbours (E D-sharp | E). Only on unaccented halves of the beat."""
    flat = [(b, i) for b, bar in enumerate(mel) for i in range(len(bar))]
    count = 0
    for k in range(len(flat) - 1, -1, -1):
        b, i = flat[k]
        e = mel[b][i]
        if k + 1 >= len(flat) or e["d"] != Fr(1, 4) or e["t"] or not e["n"]:
            continue
        nb, ni = flat[k + 1]
        nx = mel[nb][ni]
        if not nx["n"]:
            continue
        a, c = e["n"][0], nx["n"][0]
        new = None
        if abs(a[0] - c[0]) == 1 and abs(midi(a) - midi(c)) == 2 and rng.random() < cfg.get("passing", 0):
            new = (a[0], a[1] + (1 if c[0] > a[0] else -1))
        elif a == c and rng.random() < cfg.get("neighbour", 0):
            below = key.note(a[0] - 1)
            if midi(a) - midi(below) == 2:
                new = (below[0], below[1] + 1)
        if new and abs(new[1]) <= 2:
            mel[b][i:i + 1] = [ev(Fr(1, 8), [a], post=e["post"]), ev(Fr(1, 8), [new])]
            count += 1
    return count


# ---------------------------------------------------------------- chorales
CHORALE_RANGES = {"S": (28, 39), "A": (26, 35), "T": (21, 31), "B": (16, 28)}
INVERSIONS = {"I": 0.25, "ii": 0.6, "IV": 0.25, "V": 0.2, "vi": 0.1, "i": 0.25, "iv": 0.25, "VI": 0.0, "V7": 0.0}


def chorale_chords(key, n, allowed, ends, rng):
    """A chord for every note of a chorale: starts on I, changes chord on every note within a phrase,
    follows MOVES, ends each phrase with V-I (full close) or on V (half close). [(chord, bass degree)]."""
    moves = MOVES[key.mode]
    I = tonic_chord(key)
    dom = [c for c in ("V", "V7") if c in allowed]
    for _ in range(200):
        out = []
        for k in range(n):
            if k == 0:
                opts = [I]
            elif ends.get(k) == "auth":
                opts = [I]
            elif ends.get(k) == "half":
                opts = ["V"]
            elif ends.get(k + 1) == "auth":
                opts = dom
            elif ends.get(k + 1) == "half":
                opts = [c for c in allowed if "V" in moves.get(c, {}) and c not in ("V", "V7")]
            else:
                opts = allowed
            prev = out[-1][0] if out else None
            if prev and (k - 1) not in ends:
                opts = [c for c in opts if c in moves.get(prev, {}) and c != prev]
            if not opts:
                break
            w = [moves[prev][c] if prev and c in moves.get(prev, {}) else 1.0 for c in opts]
            c = rng.choices(opts, w)[0]
            degs = chord_degrees(c)
            inv = 0
            if k not in ends and (k + 1) not in ends and k > 0 and rng.random() < INVERSIONS.get(c, 0):
                inv = 1
            out.append((c, degs[inv]))
        if len(out) == n:
            return out
    return None


def chorale_soprano(key, harm, ends, lo, hi, rng):
    """A soprano of chord tones: mostly steps, the leading note rising, a 7th falling, phrase ends on
    1 or 3 (full close; the last note the tonic) or on a note of V (half close)."""
    n = len(harm)
    line = [None] * n
    I = tonic_chord(key)
    mot = {0: 0.5, 1: 6.0, 2: 2.5, 3: 0.6}

    def ok(k, s):
        c, bdeg = harm[k]
        d = key.degree(s)
        if d not in chord_degrees(c):
            return False
        if bdeg != CHORDS[c][0] and d == bdeg:
            return False  # don't double the bass of an inversion in the soprano
        if k in ends and ends[k] == "auth" and d not in ((0,) if k == n - 1 else (0, 2)):
            return False
        if k == 0:
            return d in (0, 2, 4)
        p = line[k - 1]
        pc_, pd = harm[k - 1][0], key.degree(p)
        if k >= 2 and abs(line[k - 1] - line[k - 2]) >= 2 and (s - p) * (line[k - 1] - line[k - 2]) > 0:
            return False
        if k >= 2 and line[k - 1] == line[k - 2] == s:
            return False
        if pc_ in ("V", "V7") and c in (I, "vi", "VI") and pd == 6 and s != p + 1:
            return False  # the leading note rises (also in V-vi)
        if pc_ == "V7" and pd == 3 and s != p - 1:
            return False
        if abs(s - p) == 1 and abs(midi(spell(key, s, c)) - midi(spell(key, p, pc_))) == 3:
            return False
        if k == n - 1 and abs(s - p) != 1:
            return False
        return True

    def dfs(k):
        if k == n:
            return True
        if k == 0:
            opts = list(range(lo, hi + 1))
            rng.shuffle(opts)
        else:
            pool = [(x, mot[abs(x - line[k - 1])]) for x in range(lo, hi + 1) if abs(x - line[k - 1]) in mot]
            opts = []
            while pool:
                tot = sum(w for _, w in pool)
                r, acc = rng.random() * tot, 0
                for j, (x, w) in enumerate(pool):
                    acc += w
                    if r <= acc:
                        opts.append(x)
                        pool.pop(j)
                        break
        for x in opts:
            if ok(k, x):
                line[k] = x
                if dfs(k + 1):
                    return True
        line[k] = None
        return False

    return line if dfs(0) else None


def chorale_voicing(key, sop, harm, voices, rng):
    """Alto, tenor and bass under a given soprano, by dynamic programming over the chords: ranges,
    spacing (each hand within an octave), no crossing, complete chords and sensible doubling, no
    parallel 5ths or octaves, the leading note rising and the 7th falling. Cheapest motion wins."""
    n = len(sop)
    I = tonic_chord(key)

    def states(k):
        c, bdeg = harm[k]
        degs = chord_degrees(c)
        s = spell(key, sop[k], c)
        lo, hi = CHORALE_RANGES["B"]
        basses = [spell(key, x, c) for x in range(lo, hi + 1) if key.degree(x) == bdeg]
        alts = [spell(key, x, c) for x in range(CHORALE_RANGES["A"][0], CHORALE_RANGES["A"][1] + 1)
                if key.degree(x) in degs]
        tens = [spell(key, x, c) for x in range(CHORALE_RANGES["T"][0], CHORALE_RANGES["T"][1] + 1)
                if key.degree(x) in degs] if voices == 4 else [None]
        out = []
        for b in basses:
            for t in tens:
                for a in alts:
                    v = [s, a] + ([t] if t else []) + [b]
                    m = [midi(x) for x in v]
                    if any(m[i] <= m[i + 1] for i in range(len(m) - 1)):
                        continue
                    if m[0] - m[1] > 12:
                        continue
                    if voices == 4 and (m[1] - m[2] > 12 or m[2] - m[3] > 12):
                        continue
                    if voices == 3 and m[1] - m[2] > 24:
                        continue
                    present = {key.degree(x[0]) for x in v}
                    need = set(degs) if c != "V7" else {degs[0], degs[1], degs[3]}
                    if voices == 3 and c != "V7":
                        need = {degs[0], degs[1]}
                    if not need <= present:
                        continue
                    lead = 6 if c in ("V", "V7") else None
                    cnt = {}
                    for x in v:
                        cnt[key.degree(x[0])] = cnt.get(key.degree(x[0]), 0) + 1
                    if lead is not None and cnt.get(lead, 0) > 1:
                        continue  # never double the leading note
                    if c == "V7" and cnt.get(3, 0) > 1:
                        continue
                    third = degs[1]
                    pen = 0.0
                    if cnt.get(third, 0) > 1:
                        if c in ("ii", "vi") or bdeg == third:
                            pen += 1.5
                        else:
                            continue
                    if bdeg == degs[0] and cnt.get(degs[0], 0) < 2 and voices == 4 and c != "V7":
                        pen += 2.0  # root position: double the root
                    out.append((tuple(v), pen))
        return out

    def trans_ok(k, v1, v2):
        m1, m2 = [midi(x) for x in v1], [midi(x) for x in v2]
        c1, c2 = harm[k - 1][0], harm[k][0]
        nv = len(v1)
        for i in range(nv):
            for j in range(i + 1, nv):
                i1, i2 = (m1[i] - m1[j]) % 12, (m2[i] - m2[j]) % 12
                if i1 == i2 and i1 in (0, 7) and m1[i] != m2[i] and m1[j] != m2[j]:
                    return False  # parallel octaves or fifths
        for i in range(1, nv):
            step = abs(v2[i][0] - v1[i][0])
            if i < nv - 1 and step > 4:
                return False  # inner voices move by at most a fifth
            if i == nv - 1 and step > 7:
                return False
            if abs(v2[i][0] - v1[i][0]) == 1 and abs(m2[i] - m1[i]) == 3:
                return False  # augmented second
            if i < nv - 1 and (m2[i] > m1[i - 1] or (i + 1 < nv and m2[i] < m1[i + 1])):
                return False  # overlapping voices
            d1 = key.degree(v1[i][0])
            if c1 in ("V", "V7") and c2 in (I, "vi", "VI") and d1 == 6:
                if i == nv - 1 and v2[i][0] != v1[i][0] + 1:
                    return False
                if i < nv - 1 and v2[i][0] not in (v1[i][0] + 1, v1[i][0] - 2):
                    return False
            if c1 == "V7" and d1 == 3 and v2[i][0] != v1[i][0] - 1:
                return False  # the 7th falls by step
        return True

    layers = [states(k) for k in range(n)]
    if any(not L for L in layers):
        return None
    best = [{v: (pen + rng.random() * 0.4, None) for v, pen in layers[0]}]
    for k in range(1, n):
        cur = {}
        for v2, pen in layers[k]:
            m2 = [midi(x) for x in v2]
            choice = None
            for v1, (cost, _) in best[-1].items():
                if not trans_ok(k, v1, v2):
                    continue
                m1 = [midi(x) for x in v1]
                move = sum(abs(a - b) for a, b in zip(m1[1:-1], m2[1:-1])) + 0.3 * abs(m1[-1] - m2[-1])
                cst = cost + move + pen + rng.random() * 0.4
                if choice is None or cst < choice[0]:
                    choice = (cst, v1)
            if choice:
                cur[v2] = choice
        if not cur:
            return None
        best.append(cur)
    end = min(best[-1].items(), key=lambda kv: kv[1][0])[0]
    path = [end]
    for k in range(n - 1, 0, -1):
        path.append(best[k][path[-1]][1])
    return path[::-1]


def make_chorale(part, key, rng):
    """Mode 'chorale': three voices (soprano and alto in the right hand, bass in the left) in half
    notes, or four voices (SATB) in quarter notes with fermatas at the phrase ends."""
    meter = part["meter"]
    bar = METERS[meter][0]
    n = part["bars"]
    voices = part.get("voices", 4)
    unit = Fr(1, 2) if voices == 3 else Fr(1, 4)
    per = int(bar / unit)
    # rhythm: every bar is even notes; the last note of every second bar is longer and has a fermata
    rb = []
    for b in range(n):
        if b % 2 == 1:
            rb.append([unit] * (per - 2) + [unit * 2] if voices == 4 else [unit] * (per - 1) + [unit])
        else:
            rb.append([unit] * per)
    rbars = [[(d, False) for d in r] for r in rb]
    allowed = part.get("chords") or (["I", "ii", "IV", "V", "V7", "vi"] if key.mode == "major"
                                     else ["i", "iv", "V", "V7", "VI"])
    ends = {}
    k = 0
    for b in range(n):
        k += len(rb[b])
        if b % 2 == 1:
            ends[k - 1] = "auth" if (b == n - 1 or (b // 2) % 2 == 1) else rng.choice(["half", "auth"])
    lo, hi = part.get("sop_range", (29, 37))
    nn = sum(len(r) for r in rb)
    for _ in range(60):
        harm = chorale_chords(key, nn, allowed, ends, rng)
        if harm is None:
            continue
        if part.get("require_inversion") and not any(bd != CHORDS[c][0] for c, bd in harm):
            continue
        sop = chorale_soprano(key, harm, ends, lo, hi, rng)
        if sop is None or len(set(sop)) < 5:
            continue
        path = chorale_voicing(key, sop, harm, voices, rng)
        if path is None:
            continue
        # events
        parts_ev = [[] for _ in range(voices)]
        k = 0
        for b in range(n):
            bars_v = [[] for _ in range(voices)]
            for d in rb[b]:
                for vi in range(voices):
                    post = ["\\fermata"] if (k in ends and vi in (0, voices - 1)) else []
                    bars_v[vi].append(ev(d, [path[k][vi]], post=post))
                k += 1
            for vi in range(voices):
                parts_ev[vi].append(bars_v[vi])
        rh = [parts_ev[0], parts_ev[1]]
        lh = [parts_ev[2], parts_ev[3]] if voices == 4 else [parts_ev[2]]
        return {"rh": rh, "lh": lh, "harm": harm}
    return None


# ---------------------------------------------------------------- hands taking turns, clef changes
CLEF_RANGES = {"RH": (29, 38), "RHlow": (21, 27), "LH": (17, 25), "LHhigh": (31, 38)}


def make_alt(part, key, rbars, rng):
    """Mode 'alt' with clef_switch: the hands take turns every two bars; some right-hand turns sit
    below middle C (bass clef) and some left-hand turns above it (treble clef)."""
    n = len(rbars)
    nseg = n // 2
    for _ in range(50):
        first = rng.choice(["RH", "LH"])
        hands = [first if s % 2 == 0 else ("LH" if first == "RH" else "RH") for s in range(nseg)]
        where = []
        for h in hands:
            if h == "RH":
                where.append("RHlow" if rng.random() < 0.5 else "RH")
            else:
                where.append("LHhigh" if rng.random() < 0.5 else "LH")
        if "RHlow" not in where or "LHhigh" not in where:
            continue
        # one tune across all segments; each segment in its own range
        steps = []
        okall = True
        for s in range(nseg):
            lo, hi = CLEF_RANGES[where[s]]
            seg = rbars[2 * s:2 * s + 2]
            last = s == nseg - 1
            got = free_tune(key, seg, rng, lo, hi, end_degs={0} if last else None)
            if not got:
                okall = False
                break
            steps += got
        if not okall:
            continue
        rh, lh = [], []
        clef_rh, clef_lh = "treble", "bass"
        for s in range(nseg):
            for j in range(2):
                b = 2 * s + j
                evs = [ev(d, [key.note(x)], t) for (d, t), x in zip(rbars[b], steps[b])]
                if hands[s] == "RH":
                    if j == 0:
                        want = "bass" if where[s] == "RHlow" else "treble"
                        if want != clef_rh:
                            evs[0]["pre"].append(f"\\clef {want}")
                            clef_rh = want
                    rh.append(evs)
                    lh.append([full_rest(part["meter"])])
                else:
                    if j == 0:
                        want = "treble" if where[s] == "LHhigh" else "bass"
                        if want != clef_lh:
                            evs[0]["pre"].append(f"\\clef {want}")
                            clef_lh = want
                    lh.append(evs)
                    rh.append([full_rest(part["meter"])])
        return {"rh": [rh], "lh": [lh], "where": where, "hands": hands}
    return None


def free_tune(key, rbars, rng, lo, hi, end_degs=None):
    """A tune with no chord plan (hands taking turns): steps and skips, start on 1, 3 or 5."""
    flat = [x for r in rbars for x in r]
    n = len(flat)
    line = [None] * n
    mot = {0: 1.0, 1: 5.0, 2: 2.5, 3: 0.8, 4: 0.6}

    def ok(k, s):
        if k == 0:
            return key.degree(s) in (0, 2, 4)
        if k >= 3 and line[k - 1] == line[k - 2] == line[k - 3] == s:
            return False
        if k >= 2 and abs(line[k - 1] - line[k - 2]) >= 3 and (s - line[k - 1]) * (line[k - 1] - line[k - 2]) > 0:
            return False
        if k == n - 1 and end_degs is not None and key.degree(s) not in end_degs:
            return False
        if k == n - 1 and end_degs is None and key.degree(s) not in (0, 2, 4, 1):
            return False
        if key.mode == "minor" and abs(s - line[k - 1]) == 1 and {key.degree(s), key.degree(line[k - 1])} == {5, 6}:
            return False
        return True

    def dfs(k):
        if k == n:
            return True
        if k == 0:
            opts = list(range(lo, hi + 1))
            rng.shuffle(opts)
        else:
            pool = [(s, mot[abs(s - line[k - 1])]) for s in range(lo, hi + 1) if abs(s - line[k - 1]) in mot]
            opts = []
            while pool:
                tot = sum(w for _, w in pool)
                r, acc = rng.random() * tot, 0
                for j, (s, w) in enumerate(pool):
                    acc += w
                    if r <= acc:
                        opts.append(s)
                        pool.pop(j)
                        break
        for s in opts:
            if ok(k, s):
                line[k] = s
                if dfs(k + 1):
                    return True
        line[k] = None
        return False

    if not dfs(0):
        return None
    out, k = [], 0
    for r in rbars:
        out.append(line[k:k + len(r)])
        k += len(r)
    return out


# ---------------------------------------------------------------- sequences (two-part counterpoint)
def consonant(a, b, strong):
    iv = abs(midi(a) - midi(b)) % 12
    if strong:
        return iv in (0, 3, 4, 7, 8, 9)
    return iv in (0, 3, 4, 7, 8, 9, 2, 5, 10, 1, 11, 6) and True


def make_sequence(part, key, rng):
    """Mode 'sequence' (8 bars): bar 1, the right hand plays a one-bar motive over a held tonic;
    bars 2-4, the left hand imitates the motive an octave or two lower while the right hand plays a
    counter-motive, the pair moving down a step each bar; bars 5-6, the right hand takes the motive
    again, two steps lower each time, over a left-hand counter-motive; bars 7-8 close V7-I."""
    meter = part["meter"]
    bar = METERS[meter][0]
    strong = METERS[meter][1]
    I = tonic_chord(key)
    T = RHY[meter]
    lo, hi = rh_range(part, key)
    for _ in range(200):
        r1 = parse_rhythm(rng.choice(T["motive"]), bar)
        # the motive: a one-bar line on the tonic chord
        m = gen_tune(dict(part, motion={0: 0.5, 1: 5.0, 2: 2.5, 3: 0.8}), key, [r1], [I], rng, lo + 2, hi,
                     start={0, 2, 4}, strict_end=False)
        if not m or len(set(m[0])) < 3:
            continue
        mot = m[0]
        if abs(mot[-1] - mot[0]) > 4:
            continue
        down = -14 if min(mot) - 14 >= 15 else -7
        lmot = [s + down for s in mot]
        # a counter-motive for the right hand above the left-hand motive, consonant in all three
        # transpositions (0, -1, -2) and able to connect bar to bar
        rc = parse_rhythm(rng.choice(T["slow"] if meter == "4/4" else T["basic"]), bar)
        cm = counter_line(key, rc, r1, lmot, [0, -1, -2], rng, lo, hi, above=True, strong=strong)
        if not cm:
            continue
        # bars 5-6: the right hand has the motive at -3 and -4 (from its bar-1 pitch), the left hand a
        # counter-motive below it
        rl = parse_rhythm(rng.choice(T["slow"] if meter == "4/4" else T["basic"]), bar)
        lcm = counter_line(key, rl, r1, mot, [-3, -4], rng, 15, 27, above=False, strong=strong)
        if not lcm:
            continue
        # joins between bars must be singable: the counter-motive bar to bar, and into bar 5
        if abs(cm[0] - 1 - cm[-1]) > 4 or abs(lcm[0] - 1 - lcm[-1]) > 4:
            continue
        if abs((mot[0] - 3) - (cm[-1] - 2)) > 5:
            continue
        rh, lh = [], []
        rh.append([ev(d, [key.note(s)], t) for (d, t), s in zip(r1, mot)])
        lh.append([ev(bar, [key.note(nearest(key, 0, mot[0] + down, 14, 27))])])
        for sh in (0, -1, -2):
            rh.append([ev(d, [key.note(s + sh)], t) for (d, t), s in zip(rc, cm)])
            lh.append([ev(d, [key.note(s + sh)], t) for (d, t), s in zip(r1, lmot)])
        for sh in (-3, -4):
            rh.append([ev(d, [key.note(s + sh)], t) for (d, t), s in zip(r1, mot)])
            lh.append([ev(d, [key.note(s + sh)], t) for (d, t), s in zip(rl, lcm)])
        # cadence: V7 - I
        rcad = [parse_rhythm(rng.choice(T["basic"]), bar), parse_rhythm(T["fin"][0], bar)]
        plan = ["V7", I]
        roots = [nearest(key, 4, mot[0] - 11, 15, 22), None]
        roots[1] = nearest(key, 0, roots[0], 14, 22)
        bass = [midi(spell(key, r, c)) for r, c in zip(roots, plan)]
        prev = mot[-1] - 4
        cad = gen_tune(part, key, rcad, plan, rng, lo, hi, bass=bass, prev=prev)
        if not cad:
            continue
        rh += tune_events(key, rcad, cad, plan)
        lh.append([ev(Fr(bar / 2), [spell(key, roots[0], "V7")]), ev(Fr(bar / 2), [spell(key, roots[0] - 7 if roots[0] - 7 >= 14 else roots[0], "V7")])]
                  if meter == "4/4" else [ev(bar, [spell(key, roots[0], "V7")])])
        lh.append([ev(bar, [spell(key, roots[1], I)])])
        if not check_line(rh) or not check_line(lh):
            continue
        return {"rh": [rh], "lh": [lh]}
    return None


def counter_line(key, rc, rm, motive, shifts, rng, lo, hi, above, strong):
    """A one-bar counter-line (rhythm rc) against `motive` (rhythm rm) that is consonant in every
    transposition in `shifts`: every note of the counter-line is a 3rd, 5th, 6th or octave against
    the motive note sounding with it, at least on strong beats; no parallels; no crossing."""
    ons_m, t = [], Fr(0)
    for d, _ in rm:
        ons_m.append(t)
        t += d
    ons_c, t = [], Fr(0)
    for d, _ in rc:
        ons_c.append(t)
        t += d

    def sounding(t):
        j = max(i for i, o in enumerate(ons_m) if o <= t)
        return j

    n = len(rc)
    line = [None] * n

    def ok(k, s):
        for sh in shifts:
            c = key.note(s + sh)
            # every motive note that starts while this note holds
            end = ons_c[k] + rc[k][0]
            for j, o in enumerate(ons_m):
                if (o <= ons_c[k] and (j + 1 == len(ons_m) or ons_m[j + 1] > ons_c[k])) or ons_c[k] < o < end:
                    mnote = key.note(motive[j] + sh)
                    if above and midi(c) <= midi(mnote):
                        return False
                    if not above and midi(c) >= midi(mnote):
                        return False
                    st = o in strong or o == ons_c[k]
                    iv = abs(midi(c) - midi(mnote)) % 12
                    if st and iv not in (0, 3, 4, 7, 8, 9):
                        return False
                    if not st and iv in (1, 11, 6):
                        return False
            if k:
                p = key.note(line[k - 1] + sh)
                j1, j2 = sounding(ons_c[k - 1]), sounding(ons_c[k])
                m1, m2 = key.note(motive[j1] + sh), key.note(motive[j2] + sh)
                i1, i2 = (midi(p) - midi(m1)) % 12, (midi(c) - midi(m2)) % 12
                if i1 == i2 and i1 in (0, 7) and p != c and m1 != m2:
                    return False
        if k and abs(s - line[k - 1]) > 4:
            return False
        if abs(min(motive) - s) > 16 or abs(max(motive) - s) > 16:
            return False
        return True

    def dfs(k):
        if k == n:
            return True
        opts = list(range(lo, hi + 1))
        rng.shuffle(opts)
        if k:
            opts.sort(key=lambda s: abs(s - line[k - 1]) + rng.random() * 2)
        for s in opts:
            if ok(k, s):
                line[k] = s
                if dfs(k + 1):
                    return True
        line[k] = None
        return False

    return line if dfs(0) else None


# ---------------------------------------------------------------- ornaments
def add_ornaments(key, mel, cfg, rng):
    """A trill on the note before the last (if it is a quarter or longer); mordents on some
    strong-beat quarters; grace notes a step above some downbeats; a turn on some half notes."""
    n = len(mel)
    count = 0
    flat = [(b, i) for b in range(n) for i in range(len(mel[b]))]
    pb, pi = flat[-2]
    pen = mel[pb][pi]
    if cfg.get("trill") and pen["d"] >= Fr(1, 4) and pen["n"] and rng.random() < cfg["trill"]:
        pen["post"].append("\\trill")
        count += 1
    for b in range(n - 1):
        for i, e in enumerate(mel[b]):
            if (b, i) == (pb, pi) or not e["n"] or e["t"] or e["post"]:
                continue
            if i == 0 and b and cfg.get("grace") and rng.random() < cfg["grace"]:
                s = e["n"][0]
                g = key.note(s[0] + 1)
                e["pre"].append(f"\\acciaccatura {lily(g)}8")
                count += 1
            elif e["d"] == Fr(1, 4) and cfg.get("mordent") and rng.random() < cfg["mordent"]:
                e["post"].append(rng.choice(["\\prall", "\\prall", "\\mordent"]))
                count += 1
            elif e["d"] >= Fr(1, 2) and cfg.get("turn") and rng.random() < cfg["turn"]:
                e["post"].append("\\turn")
                count += 1
    return count


# ---------------------------------------------------------------- one exercise
def bass_midis(key, plan, roots):
    return [midi(spell(key, r, c)) for r, c in zip(roots, plan)]


def make_exercise(part, rng):
    key = Key(*part["key"])
    n = part["bars"]
    meter = part["meter"]
    tex = part.get("texture", "chords")
    for _ in range(300):
        rep = repeat_map(part, n, rng)
        if tex == "chorale":
            got = make_chorale(part, key, rng)
            if got and finish(part, key, got):
                return got
            continue
        if tex == "sequence":
            got = make_sequence(part, key, rng)
            if got and finish(part, key, got):
                return got
            continue
        rbars = gen_rhythm(part, rng, n, rep)
        if tex == "alt":
            got = make_alt(part, key, rbars, rng)
            if got and finish(part, key, got):
                return got
            continue
        plan = gen_chord_plan(part, key, n, rep, rng)
        roots = lh_roots(part, key, plan)
        lo, hi = rh_range(part, key)
        cad = None
        if n == 16:
            cad = {"half": {1, 4, 6}}
        steps = gen_tune(part, key, rbars, plan, rng, lo, hi, bass=bass_midis(key, plan, roots),
                         rep=rep, cad_degs=cad)
        if steps is None:
            continue
        mel = tune_events(key, rbars, steps, plan, melodic=part.get("melodic_minor"))
        if not check_line(mel):
            continue
        if part.get("melodic_minor"):
            raised6 = [e for bar in mel for e in bar if e["n"] and key.degree(e["n"][0][0]) == 5
                       and e["n"][0][1] > key.sig[e["n"][0][0] % 7]]
            if not raised6:
                continue
            if any(e["n"] and key.degree(e["n"][0][0]) == 5 and e["n"][0][1] > key.sig[e["n"][0][0] % 7]
                   and 5 in chord_degrees(plan[b]) for b, bar in enumerate(mel) for e in bar):
                continue  # a raised 6th against a chord that has the natural 6th
        if part.get("chromatic"):
            if add_chromatic(key, mel, part["chromatic"], rng) < part["chromatic"].get("min", 1):
                continue
        if part.get("ornaments"):
            if add_ornaments(key, mel, part["ornaments"], rng) < part["ornaments"].get("min", 2):
                continue
        if part.get("require_degree"):
            pass
        got = {"rh": [mel], "plan": plan}
        if part.get("rh2") == "held":
            hv = held_voice(part, key, rbars, mel, plan, roots, rng)
            if hv is None:
                continue
            got["rh"] = [mel, hv]
        if part.get("lh2") == "tenor":
            tv = tenor_voice(part, key, plan, roots, mel, rng)
            if tv is None:
                continue
            got["lh"] = list(tv)
        else:
            got["lh"] = [gen_lh(part, key, plan, roots)]
            if part.get("pedal"):
                add_pedal(got["lh"][0], plan)
        if part.get("dynamics"):
            add_dynamics(got, n, rng)
        if finish(part, key, got):
            return got
    raise RuntimeError(f"could not generate exercise for part {part['name']}")


def add_dynamics(got, n, rng):
    first = got["rh"][0][0][0]
    lv = rng.choice(["p", "mp", "mf"])
    first["post"].append("\\" + lv)
    if n >= 8:
        e = got["rh"][0][4][0]
        other = rng.choice([x for x in ("p", "mf", "f") if x != lv])
        got["rh"][0][2][0]["post"].append("\\<" if ["p", "mp", "mf", "f"].index(other) > ["p", "mp", "mf", "f"].index(lv) else "\\>")
        e["post"].append("\\" + other)


STATS = {}


def finish(part, key, got):
    """Validate a candidate; None (and a note in STATS) if it breaks a rule."""
    got["key"] = key
    try:
        validate(part, key, got)
    except AssertionError as e:
        STATS[str(e)] = STATS.get(str(e), 0) + 1
        return None
    return got


# ---------------------------------------------------------------- validation
def timeline(voices):
    """[(onset, dur, notes)] of every sounding event in a staff, all voices."""
    out = []
    for v in voices:
        t = Fr(0)
        for bar in v:
            for e in bar:
                if e["n"]:
                    out.append((t, e["d"], e["n"]))
                t += e["d"]
    return out


def validate(part, key, ex):
    meter = part["meter"]
    bar = METERS[meter][0]
    n = part["bars"]
    for staff in ("rh", "lh"):
        for v in ex[staff]:
            assert len(v) == n, f"{staff} has {len(v)} bars"
            for b, bb in enumerate(v):
                assert sum(e["d"] for e in bb) == bar, f"bar {b + 1} of {staff} has the wrong length"
        tl = timeline(ex[staff])
        # one hand never spans more than an octave at any moment (two voices or a chord)
        for t, d, ns in tl:
            sounding = [m for (t2, d2, ns2) in tl if t2 <= t < t2 + d2 for m in map(midi, ns2)]
            assert max(sounding) - min(sounding) <= 12, f"{staff} spans more than an octave"
    if part.get("texture") != "alt":
        rt, lt = timeline(ex["rh"]), timeline(ex["lh"])
        for t, d, ns in rt:
            low = min(map(midi, ns))
            for t2, d2, ns2 in lt:
                if t2 < t + d and t < t2 + d2:
                    assert max(map(midi, ns2)) < low, "the hands cross"
    top = ex["rh"][0]
    if not any(e["n"] for e in top[-1]):
        top = ex["lh"][0]  # hands taking turns: the left hand may have the last bars
    last = [e for e in top[-1] if e["n"]][-1]["n"]
    assert key.degree(max(last, key=midi)[0]) == 0, "must end on the tonic"
    notes = {midi(x) for v in ex["rh"][:1] + ex["lh"][:1] for bar in v for e in bar for x in e["n"]}
    assert len(notes) >= 4, "too little variety"


def signature(ex):
    return tuple(voice_str(v) for v in ex["rh"] + ex["lh"])


def variants(part):
    vs = part.get("variants")
    if not vs:
        return [dict(part)]
    return [dict(part, **v) for v in vs]


def generate_part(part, rng, seen):
    out = []
    vs = variants(part)
    tries = 0
    while len(out) < part["count"]:
        tries += 1
        if tries > part["count"] * 40:
            raise RuntimeError("too many duplicates; widen the rules")
        sub = vs[len(out) % len(vs)]
        ex = make_exercise(sub, rng)
        sig = signature(ex)
        if sig in seen:
            continue
        seen.add(sig)
        ex["part"] = sub
        if sub.get("twin"):
            ex["twin"] = twin(ex, Key(*sub["twin"]))
        out.append(ex)
    return out


def twin(ex, key2):
    """The same exercise spelled in the enharmonic key (F-sharp major -> G-flat major): every note
    keeps its key on the keyboard and changes its name."""
    shift = key2.tpc - ex["key"].tpc
    if shift > 3:
        shift -= 7
    if shift < -3:
        shift += 7

    def conv(nt):
        s = nt[0] + shift
        a = midi(nt) - midi((s, 0))
        assert -2 <= a <= 2
        return (s, a)

    def conv_ev(e):
        e2 = dict(e)
        e2["n"] = [conv(x) for x in e["n"]]
        e2["post"], e2["end"], e2["pre"] = list(e["post"]), list(e["end"]), list(e["pre"])
        return e2

    return {"key": key2, "rh": [[[conv_ev(e) for e in bar] for bar in v] for v in ex["rh"]],
            "lh": [[[conv_ev(e) for e in bar] for bar in v] for v in ex["lh"]]}


def generate_unit(unit, seed=None):
    rng = random.Random(seed if seed is not None else 5000 + unit["id"])
    seen = set()
    return [(part, generate_part(part, rng, seen)) for part in unit["parts"]]


# ---------------------------------------------------------------- scores
def breaks_for(n):
    return {8: (3,), 16: (3, 7, 11), 12: (3, 7)}.get(n, ())


def tempo_markup(bpm, unit="4"):
    return (f"\\hspace #3 \\concat {{ \\general-align #Y #DOWN \\fontsize #-2 \\note {{{unit}}} #UP "
            f"\\fontsize #-1 \" = {bpm}\" }}")


def score(part, ex, label, own_tempo=""):
    meter = part["meter"]
    key = ex["key"]
    n = part["bars"]
    tsig = "\\once \\override Staff.TimeSignature.style = #'C " if meter == "2/2" else ""
    rh = staff_str(ex["rh"], breaks_for(n))
    lh = staff_str(ex["lh"])
    acc = "\\accidentalStyle modern "
    ped = "\\set Staff.pedalSustainStyle = #'bracket " if "sustainOn" in lh else ""
    return f"""
\\score {{
  \\header {{ piece = \\markup \\line {{ \\exLabel "{label}" {own_tempo} }} }}
  \\new PianoStaff <<
    \\new Staff = "up" {{ \\autoLineBreaksOff \\clef treble \\key {key.lily} {tsig}\\time {meter} {acc}{rh} \\bar "|." }}
    \\new Staff = "down" {{ \\clef bass \\key {key.lily} {tsig}\\time {meter} {acc}{ped}{lh} \\bar "|." }}
  >>
  \\layout {{ }}
}}
"""


def lily_exercise(part, ex, label):
    """LilyPond scores for one exercise (two when it has an enharmonic twin)."""
    p = ex.get("part", part)
    own = ""
    if (p.get("tempo"), p.get("tempo_unit", "4")) != (part.get("tempo"), part.get("tempo_unit", "4")):
        own = tempo_markup(p["tempo"], p.get("tempo_unit", "4"))  # this exercise has its own speed
    if ex.get("twin"):
        return [score(p, ex, label + "a", own), score(p, ex["twin"], label + "b", own)]
    return [score(p, ex, label, own)]
