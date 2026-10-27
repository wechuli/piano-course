"""Volume 6 exercise generator: reading music written for anyone (Levels 7-8).

gen6 imports and extends gen5.py; gen5 itself is never edited, and Volumes 1-5 must stay
byte-identical (run check_identical.py after every change here). No Volume 6 option draws
random numbers unless a part switches it on.

Feature 1 (the groundwork Units 5-8 depend on): an exercise is no longer only "rh"/"lh".
It may carry

  ex["staves"]  a list of staves, each {"name", "clef", "voices", "instrument"?, "hand"?,
                "solo"?, "lyrics"?}; "voices" is a list of gen5 voices (bars of events)
  ex["group"]   "piano" (PianoStaff), "choir" (ChoirStaff, open score) or
                "quartet" (StaffGroup)

Clefs: treble, bass, treble_8 (a vocal tenor: treble with an 8 below), alto, tenor.
A staff with "solo": True is printed above the group (a singer or violin over the piano);
"hand": "rh"/"lh" marks a piano staff (the checker tests spans and leaps only on hands).
Clef changes inside a staff travel in an event's "pre" list, exactly as in gen5's "alt"
texture, so staff_str prints them unchanged.

The first user is the open-score chorale (`texture: "chorale", staves: 4`): gen5 generates
and validates the SATB chorale on two staves, and only the layout changes, so no randomness
is consumed differently from gen5.
"""
import random

import gen5

CLEF = {"treble": "treble", "bass": "bass", "treble_8": '"treble_8"', "alto": "alto", "tenor": "tenor"}
GROUP = {"piano": "PianoStaff", "choir": "ChoirStaff", "quartet": "StaffGroup"}

# A tone, a third ... as LilyPond \transpose targets, measured up from c
INTERVALS = {"m2": "des", "M2": "d", "m3": "ees", "M3": "e", "P4": "f", "P5": "g"}


# ---------------------------------------------------------------- layouts
def open_score(ex):
    """Lay a gen5 chorale (SATB on two piano staves) out on four open-score staves."""
    voices = ex["rh"] + ex["lh"]
    assert len(voices) == 4, "open score needs a four-voice chorale"
    names = ("soprano", "alto", "tenor", "bass")
    instruments = ("Soprano", "Alto", "Tenor", "Bass")
    clefs = ("treble", "treble", "treble_8", "bass")
    ex["staves"] = [{"name": nm, "clef": cl, "instrument": ins, "voices": [v]}
                    for nm, cl, ins, v in zip(names, clefs, instruments, voices)]
    ex["group"] = "choir"
    return ex


def as_staves(ex):
    """Every exercise as (staves, group): rh/lh become the usual two piano staves."""
    if ex.get("staves"):
        return ex["staves"], ex.get("group", "piano")
    return ([{"name": "up", "clef": "treble", "voices": ex["rh"], "hand": "rh"},
             {"name": "down", "clef": "bass", "voices": ex["lh"], "hand": "lh"}], "piano")


def layout(part, ex):
    """Apply the part's score layout to a finished (validated) gen5 exercise."""
    if part.get("staves") == 4 and part.get("texture") == "chorale":
        open_score(ex)
    return ex


# ---------------------------------------------------------------- three voices (Unit 1)
# Feature 2. A voice is a list of bars of gen5 events. Every bar has a context (key, chord): in a
# fugue the answer's bars are in the dominant key. A new voice is searched note by note against
# any number of fixed voices:
#   - chord tones on accented notes (strong beats, and quarters or longer on a beat); any other
#     note is a passing or neighbour note, entered and left by step
#   - a dissonance (2nd, 7th, tritone; a 4th above the lowest voice on a strong beat) only
#     between a chord tone and a passing note, or between two notes of a seventh chord
#   - no unisons, no crossing, no parallel 5ths or octaves with any voice
#   - one hand never stretches more than an octave (the voice it shares a hand with)
Fr = gen5.Fr
DISSONANT = {1, 2, 6, 10, 11}
COUNTER_RHY = {
    "4/4": {"slow": ["2 2", "2. 4", "2 4 4", "4 4 2"],
            "mid": ["4 4 4 4", "4 8 8 4 4", "4 4 8 8 4", "4. 8 4 4", "2 8 8 4", "4 4 4 8 8"],
            "busy": ["8 8 8 8 4 4", "4 8 8 8 8 4", "8 8 4 8 8 4", "8 8 8 8 8 8 4"]},
    "3/4": {"slow": ["2.", "2 4", "4 2"],
            "mid": ["4 4 4", "4 8 8 4", "4. 8 4", "4 4 8 8"],
            "busy": ["8 8 8 8 4", "8 8 4 8 8", "4 8 8 8 8"]},
}
BASS_RHY = {"4/4": ["2 2", "4 4 2", "2 4 4", "4 4 4 4", "2. 4"], "3/4": ["2 4", "4 4 4", "2."]}
SUBJECT_RHY = {"4/4": (["8 8 8 8 4 4", "4 8 8 8 8 4", "8 8 4 8 8 4", "4. 8 8 8 4", "4 4 8 8 8 8"],
                       ["8 8 4 2", "4 8 8 2", "4 4 2", "8 8 8 8 2", "4. 8 2", "8 8 4 4 4"])}
LINE_MOTION = {0: 0.2, 1: 5.0, 2: 2.5, 3: 1.0, 4: 0.6, 5: 0.3, 7: 0.3}
TUNE_MOTION = {0: 0.4, 1: 5.0, 2: 2.5, 3: 1.0, 4: 0.6, 5: 0.2}
# middle voice: which hand plays it, bar by bar (Part B); the last bar follows the one before
HAND_PATTERNS = ["RRLLRRL", "LLRRLLR", "RRRLLRR", "RLLRRLL", "LLLRRRL", "RRLLLRR"]


def rhythm(s, meter):
    return [d for d, _ in gen5.parse_rhythm(s, gen5.METERS[meter][0])]


def spacer(meter):
    """An invisible whole-bar rest: the bars a voice spends on the other staff."""
    e = gen5.full_rest(meter)
    e["R"] = "s" + e["R"][1:]
    return e


def is_ct(key, chord, note):
    return key.degree(note[0]) in gen5.chord_degrees(chord)


def timeline(ctx, voice, bar):
    """[(on, end, midi, chord tone?, step)] of a fixed voice's notes."""
    out, t = [], Fr(0)
    for b, evs in enumerate(voice):
        key, ch = ctx[b]
        for e in evs:
            if e["n"]:
                n = e["n"][0]
                out.append((t, t + e["d"], gen5.midi(n), e.get("ct", is_ct(key, ch, n)), n[0]))
            t += e["d"]
    return out


def sounding(tl, t):
    for x in tl:
        if x[0] <= t < x[1]:
            return x
    return None


def before(tl, t):
    for x in tl:
        if x[0] < t <= x[1]:
            return x
    return None


def strong_at(meter, t):
    bar = gen5.METERS[meter][0]
    return (t % bar) in gen5.METERS[meter][1]


def clash(meter, ctx, tls, t, e, m, ct, chord):
    """Does a note (midi m, chord tone ct) sounding over [t, e) clash with the fixed voices?"""
    for tl in tls:
        for on, end, fm, fct, _ in tl:
            if end <= t or on >= e:
                continue
            if fm == m:
                return True  # voices never meet on one key
            tau = max(t, on)
            iv = abs(m - fm) % 12
            diss = iv in DISSONANT
            if iv == 5 and strong_at(meter, tau):
                low = min([x[2] for x in (sounding(tl2, tau) for tl2 in tls) if x] + [m])
                diss = min(m, fm) == low  # a 4th above the lowest voice
            if diss and ct == fct and not (ct and len(gen5.chord_degrees(chord)) == 4):
                return True
    return False


def parallel(tls, t, p, m):
    """Parallel 5ths or octaves between the new voice (p -> m at time t) and any fixed voice."""
    if p is None or p == m:
        return False
    for tl in tls:
        a, b = before(tl, t), sounding(tl, t)
        if a and b and a[2] != b[2] and (p - a[2]) % 12 == (m - b[2]) % 12 in (0, 7):
            return True
    return False


def line_search(meter, ctx, rbars, fixed, lo, hi, rng, b0=0, above=(), below=(), reach=None,
                prev=None, first_degs=None, bar_degs=None, end_degs=None, nxt=None, max_leap=4,
                bar_range=None, budget=6000):
    """Search a voice (rhythm rbars, one list of durations per bar from bar b0) against the fixed
    voices. above/below: indexes of fixed voices it stays above/below; reach(b) -> [(index, semis)]:
    the fixed voices it shares a hand with in bar b. bar_degs(b) -> degrees allowed on the bar's
    first note (a bass on the chord root); bar_range(b) -> (lo, hi) narrows the range bar by bar.
    Returns the steps per bar, or None."""
    bar = gen5.METERS[meter][0]
    beat = gen5.METERS[meter][2]
    tls = [timeline(ctx, v, bar) for v in fixed]
    slots = []
    for j, r in enumerate(rbars):
        b, on = b0 + j, Fr(0)
        for i, d in enumerate(r):
            t = b * bar + on
            acc = on in gen5.METERS[meter][1] or (on % beat == 0 and d >= beat)
            slots.append((b, i, d, t, acc))
            on += d
    n = len(slots)
    line = [None] * n
    info = [None] * n  # (midi, chord tone?)

    def ok(k, s):
        b, i, d, t, acc = slots[k]
        key, ch = ctx[b]
        note = gen5.spell(key, s, ch)
        m = gen5.midi(note)
        ct = is_ct(key, ch, note)
        if acc and not ct:
            return False
        p = line[k - 1] if k else prev
        pm = info[k - 1][0] if k else (gen5.midi(prev_note) if prev is not None else None)
        if p is None:
            if first_degs is not None and key.degree(s) not in first_degs:
                return False
        else:
            if abs(s - p) > max_leap:
                return False
            if abs(s - p) == 1 and abs(m - pm) == 3:
                return False  # augmented second
            if abs(m - pm) > 12:
                return False
            if not ct and abs(s - p) != 1:
                return False
            pct = info[k - 1][1] if k else True
            if not pct and abs(s - p) != 1:
                return False  # a passing note is left by step
            pp = line[k - 2] if k >= 2 else (prev if k == 1 else None)
            if pp is not None and abs(p - pp) >= 3 and ((s - p) * (p - pp) > 0 or abs(s - p) >= abs(p - pp)):
                return False  # a leap is followed by a step back
            if k >= 2 and line[k - 1] == line[k - 2] == s:
                return False
            pb = slots[k - 1][0] if k else b - 1
            if pb != b and pb >= 0:
                pkey, pch = ctx[pb]
                pd = pkey.degree(p)
                if pch == "V7" and pd == 3 and s != p - 1:
                    return False  # the 7th of V7 falls
                if pch in ("V", "V7") and pd == 6 and ch in ("I", "i") and s not in (p + 1, p - 2):
                    return False  # the leading note rises (or an inner voice falls to the 5th)
        if bar_range is not None and not bar_range(b)[0] <= s <= bar_range(b)[1]:
            return False
        if i == 0 and bar_degs is not None and key.degree(s) not in bar_degs(b):
            return False
        if k == n - 1:
            if end_degs is not None and key.degree(s) not in end_degs:
                return False
            if nxt is not None and abs(s - nxt) > max_leap:
                return False
        e = t + d
        for idx in above:
            if any(x[2] >= m for x in tls[idx] if x[0] < e and x[1] > t):
                return False
        for idx in below:
            if any(x[2] <= m for x in tls[idx] if x[0] < e and x[1] > t):
                return False
        for idx, lim in (reach(b) if reach else ()):
            if any(abs(x[2] - m) > lim for x in tls[idx] if x[0] < e and x[1] > t):
                return False
        if clash(meter, ctx, tls, t, e, m, ct, ch):
            return False
        if parallel(tls, t, pm, m):
            return False
        info[k] = (m, ct)
        return True

    prev_note = None
    if prev is not None:
        pk, pc = ctx[max(b0 - 1, 0)]
        prev_note = gen5.spell(pk, prev, pc)
    left = [budget]

    def order(k):
        p = line[k - 1] if k else prev
        if p is None:
            c = list(range(lo, hi + 1))
            rng.shuffle(c)
            return c
        pool = [(s, LINE_MOTION[abs(s - p)]) for s in range(lo, hi + 1) if abs(s - p) in LINE_MOTION]
        out = []
        while pool:
            tot = sum(w for _, w in pool)
            r, acc = rng.random() * tot, 0
            for j, (s, w) in enumerate(pool):
                acc += w
                if r <= acc:
                    out.append(s)
                    pool.pop(j)
                    break
        return out

    def dfs(k):
        left[0] -= 1
        if left[0] < 0:
            return False
        if k == n:
            return True
        for s in order(k):
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


def line_events(ctx, rbars, steps, b0=0):
    return [[gen5.ev(d, [gen5.spell(ctx[b0 + j][0], s, ctx[b0 + j][1])]) for d, s in zip(r, st)]
            for j, (r, st) in enumerate(zip(rbars, steps))]


def voices_ok(meter, ctx, voices):
    """Every pair of voices: no clashes, no crossing, no parallel 5ths or octaves (a final check
    of the finished texture; voices are listed from the top down)."""
    bar = gen5.METERS[meter][0]
    tls = [timeline(ctx, v, bar) for v in voices]
    for i, tl in enumerate(tls):
        others = tls[:i] + tls[i + 1:]
        prev = None
        for on, end, m, ct, s in tl:
            b = int(on // bar)
            ch = ctx[b][1]
            if clash(meter, ctx, others, on, end, m, ct, ch):
                return False
            if prev is not None and prev[1] == on and parallel(others, on, prev[2], m):
                return False
            for j, tl2 in enumerate(tls):
                for on2, end2, m2, _, _ in tl2:
                    if on2 < end and on < end2 and ((j > i and m2 >= m) or (j < i and m2 <= m)):
                        return False  # voices cross
            prev = (on, end, m)
    return True


def counter_rhythm(meter, against, rng):
    """A bar of the new voice that moves when the other voice holds, and holds when it moves."""
    T = COUNTER_RHY[meter]
    if len(against) >= 5:
        pool = T["slow"]
    elif len(against) <= 2:
        pool = T["busy"] + T["mid"]
    else:
        pool = T["mid"] + T["slow"]
    return rhythm(rng.choice(pool), meter)


def bar_rhythms(voice):
    return [[e["d"] for e in bar] for bar in voice]


# registers as steps (C4 = 28): the tune G4-A5, a middle voice in the right hand B3-D5 (in the
# left hand A3-E4 when it changes hands), the bass F2-A3
TRIO_RANGE = {"tune": (31, 40), "mid": (27, 36), "mid_R": (27, 36), "mid_L": (23, 30),
              "bass": (17, 26), "cross_bass": (15, 24)}
FUGUE_RANGE = {"subject": (32, 40), "sop": (31, 40), "alto": (26, 35), "bass": (14, 24)}


def make_trio(part, key, rng):
    """texture 'trio' (and 'cross'): a bass line from the chord plan, a tune by gen5.gen_tune, and a
    middle voice searched against both. In 'trio' the middle voice shares the right hand with the
    tune; in 'cross' it changes hands bar by bar (written on whichever staff that hand reads)."""
    meter, n = part["meter"], part["bars"]
    bar = gen5.METERS[meter][0]
    cross = part.get("texture") == "cross"
    plan = gen5.gen_chord_plan(part, key, n, {}, rng)
    ctx = [(key, c) for c in plan]
    # bass: the chord root on every downbeat, chord tones and passing notes between
    brb = [rhythm(rng.choice(BASS_RHY[meter]), meter) for _ in range(n - 1)] + [[bar]]
    blo, bhi = TRIO_RANGE["cross_bass" if cross else "bass"]
    bass_s = line_search(meter, ctx, brb, [], blo, bhi, rng, first_degs={0}, end_degs={0},
                         bar_degs=lambda b: {gen5.CHORDS[plan[b]][0]}, max_leap=5)
    if not bass_s:
        return None
    bass = line_events(ctx, brb, bass_s)
    if not gen5.check_line(bass):
        return None
    # tune
    rbars = gen5.gen_rhythm(part, rng, n, {})
    lo, hi = TRIO_RANGE["tune"]
    downs = [gen5.midi(bar_[0]["n"][0]) for bar_ in bass]
    steps = gen5.gen_tune(dict(part, motion=TUNE_MOTION), key, rbars, plan, rng, lo, hi, bass=downs)
    if steps is None:
        return None
    tune = gen5.tune_events(key, rbars, steps, plan)
    if not gen5.check_line(tune) or not voices_ok(meter, ctx, [tune, bass]):
        return None
    # middle voice
    mrb = [counter_rhythm(meter, rbars[b], rng) for b in range(n - 1)] + [[bar]]
    if cross:
        pat = rng.choice(HAND_PATTERNS)[:n - 1]
        hands = pat + pat[-1]

        def reach(b):
            return [(0, 12)] if hands[b] == "R" else [(1, 12)]

        def bar_range(b):
            return TRIO_RANGE["mid_" + hands[b]]
    else:
        def reach(b):
            return [(0, 12)]

        def bar_range(b):
            return TRIO_RANGE["mid"]
    mid_s = line_search(meter, ctx, mrb, [tune, bass], 21, 38, rng, above=[1], below=[0], reach=reach,
                        first_degs={0, 2, 4}, end_degs={0, 2, 4}, bar_range=bar_range)
    if not mid_s:
        return None
    mid = line_events(ctx, mrb, mid_s)
    if not gen5.check_line(mid) or not voices_ok(meter, ctx, [tune, mid, bass]):
        return None
    if not cross:
        return {"rh": [tune, mid], "lh": [bass], "plan": plan}
    up = [mid[b] if hands[b] == "R" else [spacer(meter)] for b in range(n)]
    down = [mid[b] if hands[b] == "L" else [spacer(meter)] for b in range(n)]
    return {"rh": [tune, up], "lh": [down, bass], "plan": plan, "hands": hands, "middle": mid}


def dominant_key(key):
    d = key.note(key.tonic + 4)
    return gen5.Key(gen5.LETTERS[d[0] % 7] + gen5.ACC[d[1]], key.mode)


def move(events, k1, k2, shift, tonal=False):
    """A line moved by `shift` steps from key k1 into key k2, keeping each note's alteration
    against the key signature (C minor's B-natural becomes G minor's F-sharp). tonal: the first
    note, if it is the 5th of k1, is answered by k1's tonic (the tonal answer)."""
    out, first = [], True
    for bar_ in events:
        nb = []
        for e in bar_:
            e2 = dict(e, n=list(e["n"]), post=list(e["post"]), end=list(e["end"]), pre=list(e["pre"]))
            e2.pop("ct", None)
            if e["n"]:
                s, a = e["n"][0]
                rel = a - k1.sig[s % 7]
                s2 = s + shift
                if first and tonal and k1.degree(s) == 4:
                    s2 -= 1
                    e2["ct"] = True  # the tonic, heard as a chord tone
                e2["n"] = [(s2, k2.sig[s2 % 7] + rel)]
                first = False
            nb.append(e2)
        out.append(nb)
    return out


def label(events, text, below=False):
    events[0][0]["post"].append(f'{"_" if below else "^"}\\markup \\small \\italic "{text}"')


def make_fugue(part, key, rng):
    """texture 'fugue' (8 bars of 4/4): a fugue exposition in three voices.
    Bars 1-2 the subject (soprano, I-V); bars 3-4 the answer a 4th lower in the dominant key
    (alto; tonal when the subject starts on the 5th), with the countersubject above it; bar 5 a
    codetta on V7; bars 6-7 the subject in the bass, the countersubject in the alto and a free
    soprano; bar 8 the tonic chord."""
    meter = part["meter"]
    bar = gen5.METERS[meter][0]
    I = gen5.tonic_chord(key)
    K2 = dominant_key(key)
    I2 = gen5.tonic_chord(K2)
    lo, hi = FUGUE_RANGE["subject"]
    slo, shi = FUGUE_RANGE["sop"]
    alo, ahi = FUGUE_RANGE["alto"]
    r1, r2 = SUBJECT_RHY[meter]
    srb = [rhythm(rng.choice(r1), meter), rhythm(rng.choice(r2), meter)]
    sp = dict(part, motion=TUNE_MOTION)
    steps = gen5.gen_tune(sp, key, [[(d, False) for d in r] for r in srb], [I, "V"], rng, lo, hi,
                          start=set(part.get("subject_start", (0, 4))), end_degs={4})
    if steps is None or len(set(steps[0] + steps[1])) < 5:
        return None
    subject = gen5.tune_events(key, [[(d, False) for d in r] for r in srb], steps, [I, "V"])
    tonal = key.degree(steps[0][0]) == 4
    answer = move(subject, key, K2, -3, tonal)
    ctx = [(key, I), (key, "V"), (K2, I2), (K2, "V"), (key, "V7"), (key, I), (key, "V"), (key, I)]
    rest = [gen5.full_rest(meter)]
    alto = [rest, rest] + answer
    # countersubject above the answer
    crb = [counter_rhythm(meter, bar_rhythms(answer)[j], rng) for j in range(2)]
    cs = line_search(meter, ctx, crb, [alto], slo, shi, rng, b0=2, above=[0], reach=lambda b: [(0, 12)],
                     prev=steps[1][-1])
    if not cs:
        return None
    cs_ev = line_events(ctx, crb, cs, b0=2)
    sop = subject + cs_ev
    # the third entry: the subject two octaves (or one) lower, with the countersubject in the alto
    bass_sub = move(subject, key, key, -14)
    alto_cs = move(cs_ev, K2, key, -4)
    first_cs = alto_cs[0][0]["n"][0][0]
    # codetta: alto, then soprano, over V7
    rb5 = [counter_rhythm(meter, [1, 1, 1, 1], rng)]
    a5 = line_search(meter, ctx, rb5, [], alo, ahi, rng, b0=4, prev=alto[3][-1]["n"][0][0], nxt=first_cs)
    if not a5:
        return None
    alto = alto + line_events(ctx, rb5, a5, b0=4)
    rb5s = [counter_rhythm(meter, rb5[0], rng)]
    s5 = line_search(meter, ctx, rb5s, [alto], slo, shi, rng, b0=4, above=[0], reach=lambda b: [(0, 12)],
                     prev=cs[-1][-1])
    if not s5:
        return None
    sop = sop + line_events(ctx, rb5s, s5, b0=4)
    alto = alto + alto_cs
    bass = [rest] * 5 + bass_sub
    if not voices_ok(meter, ctx[:7], [alto[:7], bass[:7]]):
        if not tonal:
            return None
        # the countersubject was written against the tonal answer's first note: against the
        # subject itself its first note is changed (as Bach often does)
        e0 = alto[5][0]
        one = line_search(meter, ctx, [[e0["d"]]], [bass], alo, ahi, rng, b0=5, prev=a5[0][-1],
                          nxt=alto[5][1]["n"][0][0] if len(alto[5]) > 1 else alto[6][0]["n"][0][0])
        if not one:
            return None
        alto[5] = line_events(ctx, [[e0["d"]]], one, b0=5)[0] + alto[5][1:]
        if not voices_ok(meter, ctx[:7], [alto[:7], bass[:7]]):
            return None
    # free soprano over the third entry
    frb = [counter_rhythm(meter, bar_rhythms(bass_sub)[j], rng) for j in range(2)]
    fs = line_search(meter, ctx, frb, [alto, bass], slo, shi, rng, b0=5, above=[0, 1],
                     reach=lambda b: [(0, 12)], prev=s5[0][-1])
    if not fs:
        return None
    sop = sop + line_events(ctx, frb, fs, b0=5)
    # the final chord
    whole = [[bar]]
    b8 = line_search(meter, ctx, whole, [], *FUGUE_RANGE["bass"], rng, b0=7, prev=bass[6][-1]["n"][0][0],
                     end_degs={0}, max_leap=4)
    if not b8:
        return None
    bass = bass + line_events(ctx, whole, b8, b0=7)
    s8 = line_search(meter, ctx, whole, [bass], slo, shi, rng, b0=7, above=[0], prev=fs[-1][-1],
                     end_degs={0}, max_leap=2)
    if not s8:
        return None
    sop = sop + line_events(ctx, whole, s8, b0=7)
    a8 = line_search(meter, ctx, whole, [sop, bass], alo, ahi, rng, b0=7, above=[1], below=[0],
                     reach=lambda b: [(0, 12)], prev=alto[6][-1]["n"][0][0], end_degs={2, 4, 0})
    if not a8:
        return None
    alto = alto + line_events(ctx, whole, a8, b0=7)
    if not all(gen5.check_line(v) for v in (sop, alto, bass)) or not voices_ok(meter, ctx, [sop, alto, bass]):
        return None
    if part.get("label_entries"):
        label(sop[0:1], "subject")
        label(alto[2:3], "answer", below=True)
        label(sop[2:3], "countersubject")
        label(bass[5:6], "subject", below=True)
    return {"rh": [sop, alto], "lh": [bass], "subject": subject, "answer": answer, "tonal": tonal,
            "ctx": ctx}


THREE_VOICES = {"trio": make_trio, "cross": make_trio, "fugue": make_fugue}


def make_three(part, rng):
    key = gen5.Key(*part["key"])
    for _ in range(400):
        got = THREE_VOICES[part["texture"]](part, key, rng)
        if got and gen5.finish(part, key, got):
            return got
    raise RuntimeError(f"could not generate exercise for part {part['name']}")



# ---------------------------------------------------------------- rhythm against rhythm (Unit 2)
# Feature 3. Besides gen5's triplets (an event with "t": True), an event may carry a general
# tuplet: "t": (n, m, span) means n notes in the time of m, the group lasting `span` (a whole
# number of beats): a duplet in 6/8 is (2, 3, 3/8), five sixteenths in a quarter (5, 4, 1/4).
# The printed value is d * n / m. gen6's voice_str prints both kinds and is identical to gen5's
# for every exercise without a general tuplet.
# Textures:
#   "swap"      the tune in the left hand (eighths), triplet broken chords in the right hand
#   rhythms "duplet" (6/8) and "trip16" (2/4) for the right hand, with the left hand's eighths
#               or sixteenths: 2 against 3 and 3 against 4
#   "runs"      a tune whose quarters (one or two) become runs of 5, 6 or 7 notes ({"runs": ...})
#   "hemiola"   a 3/4 waltz whose bars 6-7 become three half notes (both hands, accented)
DUPLET = (2, 3, Fr(3, 8))
NEW_RHY = {
    ("6/8", "duplet"): ["d8 d8 4.", "4. d8 d8", "d8 d8 d8 d8", "4. 4 8", "d8 d8 8 8 8", "8 8 8 d8 d8"],
    ("2/4", "trip"): ["t8 t8 t8 t8 t8 t8", "t8 t8 t8 4", "4 t8 t8 t8", "t8 t8 t8 8 8", "8 8 t8 t8 t8"],
}
NEW_LH = {
    ("alberti16", "2/4"): [("16", 0), ("16", 2), ("16", 1), ("16", 2)] * 2,
    ("alberti16", "4/4"): [("16", 0), ("16", 2), ("16", 1), ("16", 2)] * 4,
}


def install_tables():
    """Add Volume 6 rhythm and left-hand tables to gen5's dictionaries. Only new keys are added:
    gen5 never looks these up, so Volumes 1-5 are unchanged."""
    for (meter, name), pats in NEW_RHY.items():
        gen5.RHY[meter].setdefault(name, pats)
    for k, v in NEW_LH.items():
        gen5.LH.setdefault(k, v)


install_tables()


def parse_rhythm6(s, bar):
    """gen5.parse_rhythm plus "d8": a duplet eighth (two in a dotted quarter)."""
    out = []
    for t in s.split():
        if t == "b":
            out.append((bar, False))
        elif t.startswith("t"):
            out.append((gen5.TOK[t[1:]] * Fr(2, 3), True))
        elif t.startswith("d"):
            out.append((gen5.TOK[t[1:]] * Fr(3, 2), DUPLET))
        else:
            out.append((gen5.TOK[t], False))
    assert sum(d for d, _ in out) == bar, s
    return out


def gen_rhythm6(part, rng, n, rep):
    """gen5.gen_rhythm, reading duplets too (same random draws)."""
    T = gen5.RHY[part["meter"]]
    bar = gen5.METERS[part["meter"]][0]
    names = part["rhythms"] if isinstance(part["rhythms"], list) else [part["rhythms"]]
    vocab = [r for k in names for r in T[k]]
    bars = [rng.choice(vocab) for _ in range(n)]
    for b in gen5.phrase_marks(n):
        bars[b] = rng.choice(T["cad"])
    bars[-1] = rng.choice(T["fin"])
    for dst, src in rep.items():
        bars[dst] = bars[src]
    return [parse_rhythm6(r, bar) for r in bars]


def ev_str6(e):
    t = e.get("t")
    if isinstance(t, tuple):
        e2 = dict(e, t=False, d=e["d"] * t[0] / t[1])
        return gen5.ev_str(e2)
    return gen5.ev_str(e)


def voice_str(bars, breaks=(), checks=True):
    out = []
    for b, bar in enumerate(bars):
        acc, open_ = Fr(0), None
        for e in bar:
            t = e.get("t")
            if t and open_ is None:
                if isinstance(t, tuple):
                    out.append(f"\\tuplet {t[0]}/{t[1]} {{")
                    open_ = t[2]
                else:
                    out.append("\\tuplet 3/2 {")
                    open_ = Fr(1, 4)
                acc = Fr(0)
            out.append(ev_str6(e))
            if open_ is not None:
                acc += e["d"]
                if acc == open_:
                    out.append("}")
                    open_ = None
        assert open_ is None, "unfinished tuplet"
        if checks:
            out.append("|")
        if b in breaks:
            out.append("\\break \\noPageBreak")
    return " ".join(out)


def staff_str(voices, breaks=(), checks=True):
    if len(voices) == 1:
        return voice_str(voices[0], breaks, checks)
    return ("<< { " + voice_str(voices[0], breaks, checks) + " } \\\\ { " + voice_str(voices[1], (), checks) + " } >>")


def signature(ex):
    return tuple(voice_str(v) for v in ex["rh"] + ex["lh"])


def tonic_top_chord(key, lo=33):
    """The tonic chord with the tonic on top (third, fifth, tonic), its top note at or above lo."""
    t = next(s for s in range(lo, lo + 7) if key.degree(s) == 0)
    return [key.note(t - 5), key.note(t - 3), key.note(t)]


def make_swap(part, key, rng):
    """The tune in the left hand (rhythms from the part, eighths), the right hand playing the
    chords as triplet broken chords: 3 in the right hand against 2 in the left."""
    n = part["bars"]
    rep = gen5.repeat_map(part, n, rng)
    rbars = gen_rhythm6(part, rng, n, rep)
    plan = gen5.gen_chord_plan(part, key, n, rep, rng)
    steps = gen5.gen_tune(part, key, rbars, plan, rng, 17, 26, rep=rep)
    if steps is None:
        return None
    tune = gen5.tune_events(key, rbars, steps, plan)
    if not gen5.check_line(tune):
        return None
    roots = [gen5.nearest(key, gen5.CHORDS[c][0], 31, 29, 35) for c in plan]
    rh = gen5.gen_lh(dict(part, bass=part.get("rh_pattern", "triplet")), key, plan, roots)
    rh[-1] = [gen5.ev(gen5.METERS[part["meter"]][0], tonic_top_chord(key))]
    return {"rh": [rh], "lh": [tune], "plan": plan}


def run_notes(a, b, n):
    """A run of n notes (diatonic steps) starting on a and leading by step into b: straight when
    the distance allows, otherwise turning once (going past and coming back). None if no run fits."""
    for last in (b - 1, b + 1):
        dist = last - a
        free = n - 1 - abs(dist)
        if free < 0 or free % 2:
            continue
        d = 1 if dist > 0 else -1 if dist < 0 else (1 if b > a else -1)
        k = free // 2
        out = [a]
        for _ in range(k):
            out.append(out[-1] - d)  # first away from the goal ...
        while len(out) < n:
            out.append(out[-1] + d)  # ... then towards it
        if out[-1] == last and len(set(out[:3])) == len(out[:3]):
            return out
    return None


def add_runs(part, key, mel, plan, rng):
    """Turn one or two quarter notes of the tune into runs of 5, 6 or 7 sixteenth-sized notes
    (a tuplet filling the beat) that lead by step into the next note."""
    cfg = part["runs"]
    want = cfg.get("count", 1)
    spots = []
    flat = [(b, i) for b, bar in enumerate(mel) for i in range(len(bar))]
    for k, (b, i) in enumerate(flat[:-1]):
        e = mel[b][i]
        if e["d"] != Fr(1, 4) or b >= len(mel) - 2 or e.get("t") or not e["n"]:
            continue
        nb, ni = flat[k + 1]
        spots.append((b, i, mel[nb][ni]["n"][0][0]))
    rng.shuffle(spots)
    done, used = 0, set()
    for b, i, target in spots:
        if done == want or b in used:
            continue
        n = rng.choice(cfg.get("notes", (5, 6, 7)))
        a = mel[b][i]["n"][0][0]
        steps = run_notes(a, target, n)
        if steps is None:
            continue
        mel[b][i:i + 1] = [gen5.ev(Fr(1, 4 * n), [gen5.spell(key, s, plan[b])], (n, 4, Fr(1, 4))) for s in steps]
        used.add(b)
        done += 1
    return done


HEMIOLA_PRE = {"major": ("ii", "IV"), "minor": ("iv",)}


def make_hemiola(part, key, rng):
    """A 3/4 waltz (8 bars) whose bars 6-7 are a hemiola: three half notes across the two bars
    (the middle one tied over the bar line), accented, in both hands; then the final tonic."""
    n = part["bars"]
    assert part["meter"] == "3/4" and n == 8
    rbars = gen_rhythm6(part, rng, n, {})
    plan = gen5.gen_chord_plan(dict(part, chords=part.get("chords")), key, n, {}, rng)
    if plan[5] not in HEMIOLA_PRE[key.mode]:
        return None
    rbars[5] = gen5.parse_rhythm("2 4", Fr(3, 4))
    rbars[6] = gen5.parse_rhythm("4 2", Fr(3, 4))
    roots = gen5.lh_roots(part, key, plan)
    lo, hi = gen5.rh_range(part, key)
    steps = gen5.gen_tune(part, key, rbars, plan, rng, lo, hi, bass=gen5.bass_midis(key, plan, roots))
    if steps is None:
        return None
    harm = [plan[5], "V", "V7"]
    tones = [set(gen5.chord_degrees(c)) for c in harm]
    p, f = steps[4][-1], steps[7][0]
    cands = []
    for m1 in range(lo, hi + 1):
        for m2 in range(m1 - 2, m1 + 3):
            for m3 in range(m2 - 2, m2 + 3):
                ds = [key.degree(x) for x in (m1, m2, m3)]
                if all(d in t for d, t in zip(ds, tones)) and abs(m1 - p) <= 3 and abs(m3 - f) <= 1 \
                        and m1 != m2 and lo <= m3 <= hi and len({m1, m2, m3}) == 3:
                    cands.append((m1, m2, m3))
    if not cands:
        return None
    m1, m2, m3 = rng.choice(cands)
    steps[5], steps[6] = [m1, m2], [m2, m3]
    tune = gen5.tune_events(key, rbars, steps, plan)
    tune[5][0]["n"] = [gen5.spell(key, m1, harm[0])]
    tune[5][1]["n"] = [gen5.spell(key, m2, "V")]
    tune[6][0]["n"] = [gen5.spell(key, m2, "V")]
    tune[6][1]["n"] = [gen5.spell(key, m3, "V7")]
    tune[5][0]["post"].append("->")
    tune[5][1]["post"].append("->")
    tune[5][1]["end"].append("~")
    tune[6][1]["post"].append("->")
    if not gen5.check_line(tune):
        return None
    lh = gen5.gen_lh(part, key, plan, roots)
    r5 = roots[5]
    rv = roots[6]
    c1, c2, c3 = (gen5.voicing(key, harm[0], r5), gen5.voicing(key, "V", rv), gen5.voicing(key, "V7", rv))
    lh[5] = [gen5.ev(Fr(1, 2), c1), gen5.ev(Fr(1, 4), c2, end=["~"])]
    lh[6] = [gen5.ev(Fr(1, 4), c2), gen5.ev(Fr(1, 2), c3)]
    plan = plan[:6] + ["V7"] + plan[7:]
    return {"rh": [tune], "lh": [lh], "plan": plan}


def make_runs(part, key, rng):
    """A gen5 tune and left-hand pattern, with one or two quarters turned into runs."""
    got = gen5.make_exercise(dict(part, texture="chords"), rng)
    mel = got["rh"][0]
    if add_runs(part, key, mel, got["plan"], rng) < part["runs"].get("count", 1):
        return None
    return got


def make_rhythm(part, key, rng):
    """Duplets (6/8) and triplets over sixteenths (2/4): gen5's tune and left hand, but the tune's
    rhythm read with duplets."""
    n = part["bars"]
    rep = gen5.repeat_map(part, n, rng)
    rbars = gen_rhythm6(part, rng, n, rep)
    plan = gen5.gen_chord_plan(part, key, n, rep, rng)
    roots = gen5.lh_roots(part, key, plan)
    lo, hi = gen5.rh_range(part, key)
    steps = gen5.gen_tune(part, key, rbars, plan, rng, lo, hi, bass=gen5.bass_midis(key, plan, roots), rep=rep)
    if steps is None:
        return None
    mel = gen5.tune_events(key, rbars, steps, plan)
    if not gen5.check_line(mel):
        return None
    if part.get("require_tuplet") and not any(e.get("t") for bar in mel for e in bar):
        return None
    return {"rh": [mel], "lh": [gen5.gen_lh(part, key, plan, roots)], "plan": plan}


RHYTHM_TEXTURES = {"swap": make_swap, "hemiola": make_hemiola, "runs": make_runs, "rhythm": make_rhythm}


def make_v6(part, rng):
    key = gen5.Key(*part["key"])
    for _ in range(400):
        got = RHYTHM_TEXTURES[part["texture"]](part, key, rng)
        if got and gen5.finish(part, key, got):
            got["v6"] = True
            return got
    raise RuntimeError(f"could not generate exercise for part {part['name']}")



# ---------------------------------------------------------------- changing meters, modes, no key (Unit 3)
# Feature 4. `meters: ["5/4", "6/4"]` cycles time signatures bar by bar (printed only when they
# change); 7/8 and 5/8 carry beat groups (`\time 2,2,3 7/8`). Modes are gen5 keys with new scales
# (Key("d", "dorian")); `no_signature: True` prints the C major signature and every accidental.
# `unbarred: True` writes a pentatonic or whole-tone tune without bar lines (\cadenzaOn, dotted
# bar lines at the ends of phrases) over an open fifth.
MODES = {"dorian": [0, 2, 3, 5, 7, 9, 10], "phrygian": [0, 1, 3, 5, 7, 8, 10], "lydian": [0, 2, 4, 6, 7, 9, 11],
         "mixolydian": [0, 2, 4, 5, 7, 9, 10], "aeolian": [0, 2, 3, 5, 7, 8, 10]}
# beat groups (in the meter's note value) and rhythms per meter; "b" = the whole bar
GROUPS = {"5/4": (3, 2), "6/4": (3, 3), "3/4": (1, 2), "2/4": (1, 1), "4/4": (2, 2), "7/8": (2, 2, 3),
          "5/8": (3, 2), "3/2": (2, 2, 2)}
BEAT_TIME = {"7/8": "\\time 2,2,3 7/8", "5/8": "\\time 3,2 5/8"}
METER_RHY = {
    "5/4": {"basic": ["2. 2", "4 4 4 2", "2. 4 4", "4 8 8 4 2", "2 4 4 4", "4 4 4 4 4", "4. 8 4 2"],
            "cad": ["2. 2"], "fin": ["b"]},
    "6/4": {"basic": ["2. 2.", "4 4 4 2.", "2. 4 4 4", "2 4 2 4", "4 4 4 4 4 4", "4 8 8 4 2."],
            "cad": ["2. 2.", "2 4 2."], "fin": ["b"]},
    "7/8": {"basic": ["4 4 4.", "8 8 4 4.", "4 8 8 4.", "4 4 8 8 8", "8 8 8 8 4.", "4 8 8 8 8 8"],
            "cad": ["4 4 4.", "2.."], "fin": ["b"]},
    "5/8": {"basic": ["4. 4", "8 8 8 4", "4. 8 8", "4 8 4", "8 8 8 8 8"], "cad": ["4. 4"], "fin": ["b"]},
    "3/4": {"basic": ["4 4 4", "2 4", "4 2", "4. 8 4", "8 8 4 4", "4 8 8 4"], "cad": ["2 4", "2."], "fin": ["b"]},
    "2/4": {"basic": ["4 4", "8 8 4", "4 8 8", "4. 8", "2"], "cad": ["2", "4 4"], "fin": ["b"]},
    "4/4": {"basic": ["4 4 4 4", "2 4 4", "4 4 2", "4. 8 4 4", "2 2", "4 8 8 4 4", "4 4 8 8 4"],
            "cad": ["2 2", "4 4 2"], "fin": ["b"]},
}
NEW_METERS = {"5/4": (Fr(5, 4), (Fr(0),), Fr(1, 4), "R4*5"), "6/4": (Fr(3, 2), (Fr(0), Fr(3, 4)), Fr(1, 4), "R1."),
              "7/8": (Fr(7, 8), (Fr(0),), Fr(1, 8), "R8*7"), "5/8": (Fr(5, 8), (Fr(0),), Fr(1, 8), "R8*5"),
              "mix": (None, (Fr(0),), Fr(1, 4), None)}
MODE_PLANS = {"dorian": "IV", "mixolydian": "VII", "aeolian": "VII", "phrygian": "ii", "lydian": "ii"}


def install_meters():
    """Volume 6 scales, chords and meters, added to gen5's tables under new keys only."""
    for m, sc in MODES.items():
        gen5.SCALES.setdefault(m, sc)
    gen5.CHORDS.setdefault("VII", (6, (6, 1, 3)))
    for k, v in NEW_METERS.items():
        gen5.METERS.setdefault(k, v)


install_meters()


def bar_len(meter):
    a, b = meter.split("/")
    return Fr(int(a), int(b))


def unit_of(meter):
    return Fr(1, int(meter.split("/")[1]))


def mode_plan(key, n, rng):
    """A modal chord plan: the tonic, with the mode's colour chord (Dorian IV, Mixolydian and
    Aeolian VII, Phrygian bII, Lydian II), ending colour-tonic."""
    col = MODE_PLANS[key.mode]
    plan = []
    for b in range(n):
        if b == 0 or b == n - 1:
            plan.append("I")
        elif b == n - 2:
            plan.append(col)
        else:
            plan.append(rng.choice(["I", col, col]) if plan[-1] == "I" else "I")
    return plan


def group_lh(key, chord, root, meter, last=False, fifth_only=False):
    """One bar of left hand by beat groups: the root for the first group, the chord's upper notes
    for the others (an oom-pah that shows the beat groups). The last bar holds the chord."""
    bar = bar_len(meter)
    v = gen5.voicing(key, chord, root)
    if fifth_only:
        v = [v[0], v[2]]
    if last:
        return [gen5.ev(bar, v if not fifth_only else v)]
    u = unit_of(meter)
    out = []
    for i, g in enumerate(GROUPS[meter]):
        out.append(gen5.ev(u * g, [v[0]] if i == 0 else v[1:]))
    return out


def make_meters(part, key, rng):
    """Changing meters (Part A), 7/8 and 5/8 with beat groups, and modes (Part B)."""
    n = part["bars"]
    meters = part.get("meters", [part["meter"]])
    bm = [meters[b % len(meters)] for b in range(n)]
    rbars = []
    marks = gen5.phrase_marks(n)
    for b, m in enumerate(bm):
        T = METER_RHY[m]
        pool = T["fin"] if b == n - 1 else T["cad"] if b in marks else T["basic"]
        rbars.append(gen5.parse_rhythm(rng.choice(pool), bar_len(m)))
    if key.mode in MODES:
        plan = mode_plan(key, n, rng)
    else:
        plan = gen5.gen_chord_plan(part, key, n, {}, rng)
    roots = gen5.lh_roots(part, key, plan)
    lo, hi = gen5.rh_range(part, key)
    steps = gen5.gen_tune(dict(part, meter="mix"), key, rbars, plan, rng, lo, hi,
                          bass=gen5.bass_midis(key, plan, roots))
    if steps is None:
        return None
    mel = gen5.tune_events(key, rbars, steps, plan)
    if not gen5.check_line(mel):
        return None
    lh = [group_lh(key, c, r, m, b == n - 1) for b, (c, r, m) in enumerate(zip(plan, roots, bm))]
    for b, m in enumerate(bm):
        if b == 0 or m != bm[b - 1] or m in BEAT_TIME and b == 0:
            t = BEAT_TIME.get(m, f"\\time {m}")
            if b > 0 or m in BEAT_TIME:
                mel[b][0]["pre"].insert(0, t)
                lh[b][0]["pre"].insert(0, t)
    if key.mode in MODES and len(MODES) and part.get("require_colour", True):
        col = MODE_PLANS[key.mode]
        cdeg = {"IV": 3, "VII": 6, "ii": 1}[col]
        # the mode's characteristic note (Dorian raised 6th, Mixolydian lowered 7th ...) must be heard
        char = {"dorian": 5, "mixolydian": 6, "aeolian": 5, "phrygian": 1, "lydian": 3}[key.mode]
        if not any(key.degree(e["n"][0][0]) == char for bar in mel for e in bar):
            return None
    return {"rh": [mel], "lh": [lh], "plan": plan, "meters": bm}


WHOLE_TONE = (0, 2, 4, 6, 8, 10)
PENTATONIC = (0, 2, 4, 7, 9)
PHRASE_RHY = {8: ["4 4 4 4 2 2", "4 8 8 4 4 2 2", "2 4 4 4 4 2", "4 4 8 8 4 2 2", "4. 8 4 4 4 4 2"],
              6: ["4 4 4 4 2", "4 8 8 4 4 2", "2 4 4 2", "4 4 8 8 4 2"]}


def scale_notes(key, kind, lo=28, hi=42):
    """(step, alt) of a pentatonic or whole-tone scale on the key's tonic, from step lo to hi."""
    semis = PENTATONIC if kind == "pentatonic" else WHOLE_TONE
    out = []
    base = gen5.midi(key.note(key.tonic)) - 12
    for octv in range(3):
        for i, iv in enumerate(semis):
            m = base + 12 * octv + iv
            if kind == "pentatonic":
                step = key.tonic - 7 + 7 * octv + (0, 1, 2, 4, 5)[i]
            else:
                step = key.tonic - 7 + 7 * octv + i
            alt = m - gen5.midi((step, 0))
            if -2 <= alt <= 2 and lo <= step <= hi:
                out.append((step, alt))
    return out


def make_unbarred(part, key, rng):
    """An unbarred tune (4 phrases, dotted bar lines between them) on a pentatonic or whole-tone
    scale, over an open fifth (pentatonic) or a major third (whole-tone) in half notes."""
    kind = part["scale"]
    sc = scale_notes(key, kind)
    tonics = [i for i, n in enumerate(sc) if gen5.midi(n) % 12 == gen5.midi(key.note(key.tonic)) % 12]
    lengths = [rng.choice([6, 8]) for _ in range(4)]
    idx = rng.choice(tonics[:2])
    rh, lh = [], []
    for ph, L in enumerate(lengths):
        rhy = [d for d, _ in gen5.parse_rhythm(rng.choice(PHRASE_RHY[L]), Fr(L, 4))]
        notes = []
        for k, d in enumerate(rhy):
            if k == len(rhy) - 1:
                target = tonics if ph == 3 else [i for i in range(len(sc)) if i not in tonics]
                cands = [i for i in target if abs(i - idx) <= 2 and i != idx] or [min(target, key=lambda i: abs(i - idx))]
                idx = rng.choice(cands)
            elif k:
                moves = [-2, -1, -1, 1, 1, 2]
                cands = [idx + mv for mv in moves if 0 <= idx + mv < len(sc)]
                idx = rng.choice(cands)
            notes.append(gen5.ev(d, [sc[idx]]))
        for k in range(len(notes) - 1):  # beam pairs of eighths by hand (no automatic beams in a cadenza)
            if notes[k]["d"] == notes[k + 1]["d"] == Fr(1, 8) and not notes[k]["post"] and \
                    (k == 0 or notes[k - 1]["d"] != Fr(1, 8) or "]" in notes[k - 1]["end"]):
                notes[k]["post"].append("[")
                notes[k + 1]["end"].append("]")
        notes[-1]["end"].append(' \\bar ";"' if ph < 3 else "")
        if ph == 1:
            notes[-1]["end"].append(" \\break \\noPageBreak")
        rh += notes
        r = key.tonic - 14 if key.tonic - 14 >= 16 else key.tonic - 7
        low = [key.note(r), key.note(r + 4 if kind == "pentatonic" else r + 2)]
        lh += [gen5.ev(Fr(1, 2), low) for _ in range(L // 2)] + ([gen5.ev(Fr(1, 4), low)] if L % 2 else [])
        if ph < 3:
            lh[-1]["end"].append(' \\bar ";"')
    if len({gen5.midi(e["n"][0]) for e in rh}) < 5:
        return None
    if not gen5.check_line([rh]):
        return None
    rh[0]["pre"].append("\\cadenzaOn")
    lh[0]["pre"].append("\\cadenzaOn")
    return {"rh": [[rh]], "lh": [[lh]], "plan": ["I"], "unbarred": True}


def validate6(part, key, ex):
    """gen5's rules for exercises whose bars change length: each bar has its meter's length (one
    bar for unbarred music), each hand spans an octave at most, the hands do not cross, the tune
    ends on the tonic."""
    if ex.get("unbarred"):
        lens = [sum(e["d"] for e in ex["rh"][0][0])]
    else:
        lens = [bar_len(m) for m in ex["meters"]]
    for staff in ("rh", "lh"):
        for v in ex[staff]:
            assert len(v) == len(lens), "bars"
            for b, bb in enumerate(v):
                assert sum(e["d"] for e in bb) == lens[b], f"bar {b + 1} of {staff} has the wrong length"
        tl = gen5.timeline(ex[staff])
        for t, d, ns in tl:
            snd = [m for (t2, d2, ns2) in tl if t2 <= t < t2 + d2 for m in map(gen5.midi, ns2)]
            assert max(snd) - min(snd) <= 12, f"{staff} spans more than an octave"
    rt, lt = gen5.timeline(ex["rh"]), gen5.timeline(ex["lh"])
    for t, d, ns in rt:
        low = min(map(gen5.midi, ns))
        for t2, d2, ns2 in lt:
            if t2 < t + d and t < t2 + d2:
                assert max(map(gen5.midi, ns2)) < low, "the hands cross"
    last = [e for e in ex["rh"][0][-1] if e["n"]][-1]["n"]
    assert key.degree(max(last, key=gen5.midi)[0]) == 0, "must end on the tonic"


def make_unit3(part, rng):
    key = gen5.Key(*part["key"])
    for _ in range(400):
        got = (make_unbarred if part.get("unbarred") else make_meters)(part, key, rng)
        if not got:
            continue
        got["key"] = key
        try:
            validate6(part, key, got)
        except AssertionError as e:
            gen5.STATS[str(e)] = gen5.STATS.get(str(e), 0) + 1
            continue
        got["v6"] = True
        return got
    raise RuntimeError(f"could not generate exercise for part {part['name']}")


# ---------------------------------------------------------------- one exercise
def make_exercise(part, rng):
    if part.get("texture") in THREE_VOICES:
        return make_three(part, rng)
    if part.get("texture") in RHYTHM_TEXTURES:
        return make_v6(part, rng)
    if part.get("texture") == "meters":
        return make_unit3(part, rng)
    return layout(part, gen5.make_exercise(part, rng))


def generate_part(part, rng, seen):
    """gen5.generate_part, but exercises come from gen6.make_exercise (same rules, new layouts)."""
    out = []
    vs = gen5.variants(part)
    tries = 0
    while len(out) < part["count"]:
        tries += 1
        if tries > part["count"] * 40:
            raise RuntimeError("too many duplicates; widen the rules")
        sub = vs[len(out) % len(vs)]
        ex = make_exercise(sub, rng)
        sig = signature(ex) if ex.get("v6") else gen5.signature(ex)
        if sig in seen:
            continue
        seen.add(sig)
        ex["part"] = sub
        if sub.get("twin"):
            ex["twin"] = gen5.twin(ex, gen5.Key(*sub["twin"]))
        out.append(ex)
    return out


def generate_unit(unit, seed=None):
    rng = random.Random(seed if seed is not None else 6000 + unit["id"])
    seen = set()
    return [(part, generate_part(part, rng, seen)) for part in unit["parts"]]


# ---------------------------------------------------------------- scores
def staff_code(st, key, meter, tsig, first=False, n=None, transpose=None, checks=True, keystr=None):
    """One staff of a multi-staff score. The first printed staff carries the line breaks."""
    clef = CLEF[st.get("clef", "treble")]
    inner = ""
    if st.get("instrument"):
        inner += f'\\set Staff.instrumentName = "{st["instrument"]} " '
    music = staff_str(st["voices"], gen5.breaks_for(n) if first else (), checks)
    if st.get("hand") and "sustainOn" in music:
        inner += "\\set Staff.pedalSustainStyle = #'bracket "
    body = f"\\key {keystr or key.lily} {tsig}\\time {meter} \\accidentalStyle modern {inner}{music} \\bar \"|.\""
    if transpose:
        body = f"\\transpose {transpose[0]} {transpose[1]} {{ {body} }}"
    auto = "\\autoLineBreaksOff " if first else ""
    out = f'\\new Staff = "{st["name"]}" {{ {auto}\\clef {clef} {body} }}'
    if st.get("lyrics"):
        out += f' \\addlyrics {{ {st["lyrics"]} }}'
    return out


def score6(part, ex, label, own_tempo="", transpose=None):
    """A multi-staff score: solo staves above a PianoStaff, ChoirStaff or StaffGroup."""
    meter = ex["meters"][0] if ex.get("meters") else part["meter"]
    key = ex["key"]
    n = part["bars"]
    tsig = "\\once \\override Staff.TimeSignature.style = #'C " if meter == "2/2" else ""
    checks = not ex.get("unbarred")
    if not checks:
        tsig += "\\omit Staff.TimeSignature "
    keystr = "c \\major" if part.get("no_signature") else None
    staves, group = as_staves(ex)
    solo = [st for st in staves if st.get("solo")]
    grouped = [st for st in staves if not st.get("solo")]
    codes, first = [], True
    for st in solo:
        codes.append(staff_code(st, key, meter, tsig, first, n, transpose, checks, keystr))
        first = False
    inner = []
    for st in grouped:
        inner.append(staff_code(st, key, meter, tsig, first, n, transpose, checks, keystr))
        first = False
    body = f"\\new {GROUP[group]} <<\n    " + "\n    ".join(inner) + "\n  >>"
    if codes:
        body = "<<\n  " + "\n  ".join(codes) + "\n  " + body + "\n  >>"
    return f"""
\\score {{
  \\header {{ piece = \\markup \\line {{ \\exLabel "{label}" {own_tempo} }} }}
  {body}
  \\layout {{ }}
}}
"""


def lily_exercise(part, ex, label):
    """LilyPond scores for one exercise: gen5's own for plain rh/lh, score6 for staves."""
    if not ex.get("staves") and not ex.get("v6"):
        return gen5.lily_exercise(part, ex, label)
    p = ex.get("part", part)
    own = ""
    if (p.get("tempo"), p.get("tempo_unit", "4")) != (part.get("tempo"), part.get("tempo_unit", "4")):
        own = gen5.tempo_markup(p["tempo"], p.get("tempo_unit", "4"))
    return [score6(p, ex, label, own)]


# ---------------------------------------------------------------- the Answers appendix
def transpose_pair(spec):
    """{"by": "M2", "dir": "up"} -> the (from, to) pair for LilyPond's \\transpose."""
    to = INTERVALS[spec["by"]]
    return ("c", to) if spec.get("dir", "up") == "up" else (to, "c")


def answer_scores(unit, seed):
    """Every 'transpose' exercise of the unit, printed in its target key for the Answers
    appendix at the back of the book. The unit is regenerated (generation is deterministic),
    so the labels match the exercise numbers in the unit. Empty if nothing transposes."""
    if not any(p.get("transpose") or any(v.get("transpose") for v in p.get("variants", []))
               for p in unit["parts"]):
        return []
    out, n = [], 0
    for part, exercises in generate_unit(unit, seed):
        for ex in exercises:
            n += 1
            p = ex.get("part", part)
            if not p.get("transpose"):
                continue
            out.append(score6(p, ex, f"{unit['id']}.{n}", transpose=transpose_pair(p["transpose"])))
    return out
