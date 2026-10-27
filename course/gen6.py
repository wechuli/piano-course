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


# ---------------------------------------------------------------- one exercise
def make_exercise(part, rng):
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
        sig = gen5.signature(ex)
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
def staff_code(st, key, meter, tsig, first=False, n=None, transpose=None):
    """One staff of a multi-staff score. The first printed staff carries the line breaks."""
    clef = CLEF[st.get("clef", "treble")]
    inner = ""
    if st.get("instrument"):
        inner += f'\\set Staff.instrumentName = "{st["instrument"]} " '
    music = gen5.staff_str(st["voices"], gen5.breaks_for(n) if first else ())
    body = f"\\key {key.lily} {tsig}\\time {meter} \\accidentalStyle modern {inner}{music} \\bar \"|.\""
    if transpose:
        body = f"\\transpose {transpose[0]} {transpose[1]} {{ {body} }}"
    auto = "\\autoLineBreaksOff " if first else ""
    out = f'\\new Staff = "{st["name"]}" {{ {auto}\\clef {clef} {body} }}'
    if st.get("lyrics"):
        out += f' \\addlyrics {{ {st["lyrics"]} }}'
    return out


def score6(part, ex, label, own_tempo="", transpose=None):
    """A multi-staff score: solo staves above a PianoStaff, ChoirStaff or StaffGroup."""
    meter = part["meter"]
    key = ex["key"]
    n = part["bars"]
    tsig = "\\once \\override Staff.TimeSignature.style = #'C " if meter == "2/2" else ""
    staves, group = as_staves(ex)
    solo = [st for st in staves if st.get("solo")]
    grouped = [st for st in staves if not st.get("solo")]
    codes, first = [], True
    for st in solo:
        codes.append(staff_code(st, key, meter, tsig, first, n, transpose))
        first = False
    inner = []
    for st in grouped:
        inner.append(staff_code(st, key, meter, tsig, first, n, transpose))
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
    if not ex.get("staves"):
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
