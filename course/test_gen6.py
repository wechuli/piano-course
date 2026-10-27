"""Tests for the Volume 6 groundwork: gen6 multi-staff scores (plan feature 1) and the
Volume 6 checker and build changes (plan feature 10). No book units are built here.

Run from course/:   python3 test_gen6.py     (must print OK)
Then run            python3 check_identical.py   (Volumes 1-5 must stay identical).

It checks that
  - gen6 produces byte-identical exercises to gen5 when no Volume 6 option is on
  - `texture: "chorale", staves: 4` lays the gen5 chorale out on four open-score staves
  - score6 prints every group (PianoStaff, ChoirStaff, StaffGroup), a solo staff with
    lyrics above the piano, every clef, and the \\transpose wrapper for the Answers pages
  - the test book (exercises and pieces, staff size 20) compiles with no LilyPond warnings
  - check_pieces gates Volume 6 features by unit and checks spans on piano hands only
  - the three-voice textures of Unit 1 (plan feature 2): trio, the middle voice changing hands,
    and fugue expositions (real and tonal answers) keep the counterpoint rules between every
    pair of voices
"""
import os
import random
import re
import subprocess
import sys
import tempfile
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402
import check_pieces  # noqa: E402
import gen5  # noqa: E402
import gen6  # noqa: E402

PLAIN = dict(name="A", title="gen5 passthrough", count=2, bars=8, meter="4/4", rhythms="basic",
             bass="block", tempo=66, key=("c", "major"))
CHORALE4 = dict(name="B", title="Open score", count=2, bars=8, meter="4/4", texture="chorale",
                voices=4, staves=4, tempo=60, key=("g", "major"))
TRANSPOSE = dict(name="C", title="Transpose a tone up", count=1, bars=4, meter="4/4", rhythms="basic",
                 bass="block", tempo=60, key=("f", "major"), transpose={"by": "M2", "dir": "up"})
TEST_UNIT = {"id": 99, "title": "Groundwork test", "new": "multi-staff scores",
             "parts": [PLAIN, CHORALE4, TRANSPOSE]}

SATB_PIECE = {
    "title": "Test chorale (open score)", "credit": "Original", "tempo": 60, "meter": "4/4",
    "key": "c \\major", "note": "Four voices on four staves; the tenor reads the treble-8 clef.",
    "group": "choir", "staves": [
        {"name": "soprano", "clef": "treble", "instrument": "Soprano",
         "music": "e'4 f' g' e' | d'2 c'2"},
        {"name": "alto", "clef": "treble", "instrument": "Alto", "music": "c'4 c' d' c' | b2 c'2"},
        {"name": "tenor", "clef": "treble_8", "instrument": "Tenor", "music": "g4 a4 g g | g2 e2"},
        {"name": "bass", "clef": "bass", "instrument": "Bass", "music": "c4 f e c | g,2 c2"},
    ]}
SONG_PIECE = {
    "title": "Test song (voice and piano)", "credit": "Original", "tempo": 72, "meter": "3/4",
    "key": "g \\major", "note": "A singer's line above the piano.",
    "staves": [
        {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
         "music": "d'4 e' fis' | g'2 d'4 | e'4 d' b | g2.", "lyrics": "la la la la la la la la"},
        {"name": "up", "clef": "treble", "hand": "rh",
         "music": "<b d'>2. | <b d'>2. | <g b>2. | <g b>2."},
        {"name": "down", "clef": "bass", "hand": "lh", "music": "g,4 d g | b, d g | c e g | g,2."},
    ]}
TRIO = dict(name="A", title="Trio", count=2, bars=4, meter="4/4", texture="trio",
            rhythms=["basic", "eighths"], tempo=60, key=("d", "minor"))
CROSS = dict(name="B", title="Cross", count=2, bars=8, meter="4/4", texture="cross",
             rhythms=["basic", "eighths"], tempo=60, key=("bes", "major"))
FUGUE = dict(name="C", title="Fugue", count=2, bars=8, meter="4/4", texture="fugue", tempo=56,
             variants=[dict(key=("c", "minor"), subject_start=(4,), label_entries=True),
                       dict(key=("a", "major"), subject_start=(0,))])

PIANO_PIECE = {
    "title": "Test piano piece", "credit": "Original", "tempo": 66, "meter": "4/4",
    "key": "c \\major", "note": "",
    "rh": "e'4 f' g' a' | g'2 c'2", "lh": "c2 e2 | g,2 c2"}


def test_passthrough():
    a = gen5.generate_part(dict(PLAIN), random.Random(123), set())
    b = gen6.generate_part(dict(PLAIN), random.Random(123), set())
    assert [gen5.signature(x) for x in a] == [gen5.signature(x) for x in b], \
        "gen6 must not change gen5's output when no Volume 6 option is on"
    assert not any(x.get("staves") for x in b), "a plain part must stay on two piano staves"
    assert gen6.lily_exercise(PLAIN, b[0], "99.1") == gen5.lily_exercise(PLAIN, a[0], "99.1")
    print("passthrough: gen6 == gen5                 OK")


def test_open_score():
    exs = gen6.generate_part(dict(CHORALE4), random.Random(7), set())
    scores = []
    for k, ex in enumerate(exs):
        assert ex["group"] == "choir" and len(ex["staves"]) == 4
        assert [st["clef"] for st in ex["staves"]] == ["treble", "treble", "treble_8", "bass"]
        assert all(len(st["voices"]) == 1 for st in ex["staves"]), "one voice per open-score staff"
        scores += gen6.lily_exercise(CHORALE4, ex, f"99.{k + 1}")
    assert "ChoirStaff" in scores[0] and '"treble_8"' in scores[0] and "Tenor" in scores[0]
    print("open-score chorale (4 staves, ChoirStaff)  OK")
    return exs, scores


def quartet_score(ex):
    """The same chorale as a string quartet: StaffGroup, viola in the alto clef."""
    ex2 = dict(ex, group="quartet", staves=[
        dict(st, clef=cl, instrument=ins, name=nm) for st, cl, ins, nm in zip(
            ex["staves"], ("treble", "treble", "alto", "bass"),
            ("Violin 1", "Violin 2", "Viola", "Cello"), ("v1", "v2", "va", "vc"))])
    sc = gen6.score6(CHORALE4, ex2, "99.Q")
    assert "StaffGroup" in sc and "\\clef alto" in sc and "Viola" in sc
    return sc


def solo_score(ex):
    """A plain exercise with its tune doubled on a solo staff above the piano, with lyrics."""
    ex2 = dict(ex, group="piano", staves=[
        {"name": "voice", "clef": "treble", "solo": True, "instrument": "Voice",
         "voices": ex["rh"][:1], "lyrics": "la la la la la la la la"},
        {"name": "up", "clef": "treble", "hand": "rh", "voices": ex["rh"]},
        {"name": "down", "clef": "bass", "hand": "lh", "voices": ex["lh"]}])
    sc = gen6.score6(PLAIN, ex2, "99.S")
    assert "PianoStaff" in sc and "\\addlyrics" in sc
    assert sc.index('"voice"') < sc.index("PianoStaff"), "the solo staff sits above the group"
    return sc


def test_answers():
    scores = gen6.answer_scores(TEST_UNIT, seed=6099)
    assert len(scores) == 1, "one transposing exercise, one answer"
    assert "\\transpose c d" in scores[0] and "99.5" in scores[0], \
        "the answer is transposed up a tone and keeps the exercise's number"
    assert gen6.answer_scores({"id": 98, "title": "x", "new": "x", "parts": [PLAIN]}, seed=6098) == []
    print("Answers appendix (\\transpose, numbering)  OK")
    return scores


def test_build_compiles(scores):
    """The test book: generated scores and v6 pieces at staff size 20, like the real volume."""
    pre = build.PREAMBLE.replace("@@HEADER@@", "test").replace("@@STAFF_SIZE@@", "20")
    pieces = [build.piece_score_v6(pc) for pc in (SATB_PIECE, SONG_PIECE, PIANO_PIECE)]
    with tempfile.TemporaryDirectory() as d:
        ly = os.path.join(d, "test.ly")
        open(ly, "w").write("\n".join([pre, "\\book {"] + scores + pieces + ["}"]))
        r = subprocess.run([build.lilypond_bin(), "-l", "WARNING", "--pdf", "-o",
                            os.path.join(d, "test"), ly], capture_output=True, text=True)
        assert r.returncode == 0, r.stderr[-3000:]
    benign = ("has been compressed", "page must be compressed", "compressing over-full page")
    warns = [w for w in r.stderr.splitlines() if "warning" in w.lower()
             and not any(b in w for b in benign)]
    assert not warns, "LilyPond warnings:\n" + "\n".join(warns)
    print("test book compiles with no warnings       OK")


def test_checker():
    content = types.SimpleNamespace(PIECES=[SATB_PIECE, SONG_PIECE, PIANO_PIECE])
    probs = check_pieces.check_unit_v6({"id": 7}, content)
    assert not probs, "at Unit 7 everything is taught:\n" + "\n".join(probs)
    probs = check_pieces.check_unit_v6({"id": 1}, content)
    text = "\n".join(probs)
    for want in ("four staves", "tenor", "solo or vocal staff", "lyrics"):
        assert want in text, f"Unit 1 must flag {want!r}:\n{text}"
    assert "Test piano piece" not in text, "a plain piano piece passes at Unit 1"
    wide = dict(PIANO_PIECE, title="Too wide", rh="<c' e' g' c'' f''>1 | c''1")
    probs = check_pieces.check_unit_v6({"id": 1}, types.SimpleNamespace(PIECES=[wide]))
    assert any("span" in p for p in probs), "a span past an octave is flagged"
    nohand = dict(SATB_PIECE, staves=[dict(st) for st in SATB_PIECE["staves"]])
    nohand["staves"][0]["music"] = "<e' e''>4 f' g' e' | d'2 c'2"  # a tenth, but not a hand
    probs = check_pieces.check_unit_v6({"id": 7}, types.SimpleNamespace(PIECES=[nohand]))
    assert not any("span" in p for p in probs), "spans are checked on piano hands only"
    print("checker gates and spans (Units 1 and 7)   OK")


def pitches(voice):
    return [gen5.midi(e["n"][0]) for bar in voice for e in bar if e["n"]]


def test_three_voices():
    key = gen5.Key("c")
    ctx = [(key, "I"), (key, "V")]
    upper = [[gen5.ev(gen5.Fr(1), [(40, 0)])], [gen5.ev(gen5.Fr(1), [(41, 0)])]]  # a'' then b''
    lower = [[gen5.ev(gen5.Fr(1), [(35, 0)])], [gen5.ev(gen5.Fr(1), [(36, 0)])]]  # c'' then d''
    assert gen6.voices_ok("4/4", ctx, [upper, lower]), "parallel sixths are fine"
    assert not gen6.voices_ok("4/4", ctx, [lower, upper]), "crossed voices are caught"
    fifths = [[gen5.ev(gen5.Fr(1), [(32, 0)])], [gen5.ev(gen5.Fr(1), [(33, 0)])]]  # g' then a'
    low = [[gen5.ev(gen5.Fr(1), [(28, 0)])], [gen5.ev(gen5.Fr(1), [(29, 0)])]]  # c' then d'
    assert not gen6.voices_ok("4/4", ctx, [fifths, low]), "parallel fifths are caught"
    scores = []
    for part in (TRIO, CROSS):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6001), set())):
            key = ex["key"]
            ctx = [(key, c) for c in ex["plan"]]
            mid = ex.get("middle", ex["rh"][-1])
            assert gen6.voices_ok("4/4", ctx, [ex["rh"][0], mid, ex["lh"][-1]]), "three-voice rules"
            if part is CROSS:
                for b in range(part["bars"]):
                    on = [bool([e for e in v[b] if e["n"]]) for v in (ex["rh"][1], ex["lh"][0])]
                    assert on.count(True) == 1, "the middle voice is on one staff in each bar"
                assert "R" in ex["hands"] and "L" in ex["hands"], "the middle voice changes hands"
            scores += gen6.lily_exercise(part, ex, f"99.{part['name']}{k + 1}")
    exs = gen6.generate_part(dict(FUGUE), random.Random(6001), set())
    for k, ex in enumerate(exs):
        sop, alto = ex["rh"]
        bass = ex["lh"][0]
        assert gen6.voices_ok("4/4", ex["ctx"], [sop, alto, bass]), "three-voice rules"
        subj = pitches(ex["subject"])
        assert pitches(sop[:2]) == subj, "the subject opens in the soprano"
        ans = pitches(alto[2:4])
        assert [a - s for a, s in zip(ans[1:], subj[1:])] == [-5] * (len(subj) - 1), \
            "the answer is the subject a 4th lower, in the dominant key"
        assert ans[0] - subj[0] == (-7 if ex["tonal"] else -5), "tonal answer: the 5th answered by the tonic"
        assert pitches(bass[5:7]) == [m - 24 for m in subj], "the third entry: the subject in the bass"
        assert ex["tonal"] == (k == 0)
        scores += gen6.lily_exercise(ex["part"], ex, f"99.C{k + 1}")
    assert "\\markup \\small \\italic \"answer\"" in scores[-2], "entries are labelled"
    assert "answer" not in scores[-1]
    print("three voices: trio, cross-staff, fugue     OK")
    return scores


def test_rhythms():
    """Unit 2 (plan feature 3): cross-rhythms, duplets, runs and hemiolas."""
    Fr = gen5.Fr
    scores = []
    swap = dict(name="A", title="Swap", count=2, bars=8, meter="4/4", texture="swap", rhythms=["eighths"],
                tempo=60, key=("g", "major"))
    duplet = dict(name="B", title="Duplets", count=2, bars=8, meter="6/8", texture="rhythm", rhythms=["duplet"],
                  bass="broken", tempo=56, tempo_unit="4.", require_tuplet=True, key=("d", "major"))
    three4 = dict(duplet, meter="2/4", rhythms=["trip"], bass="alberti16", tempo_unit="4", key=("f", "major"))
    runs = dict(name="C", title="Runs", count=2, bars=8, meter="4/4", texture="runs", rhythms=["basic"],
                bass="block2", tempo=60, runs={"count": 2}, key=("a", "minor"))
    hemi = dict(name="D", title="Hemiola", count=2, bars=8, meter="3/4", texture="hemiola", rhythms=["basic"],
                bass="waltz", tempo=96, key=("g", "minor"))
    for part in (swap, duplet, three4, runs, hemi):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6002), set())):
            code = gen6.lily_exercise(part, ex, f"99.R{k}")[0]
            if part is swap:
                assert all(e["t"] for bar in ex["rh"][0][:-1] for e in bar), "right-hand triplets"
                assert max(gen5.midi(n) for bar in ex["lh"][0] for e in bar for n in e["n"]) < \
                    min(gen5.midi(n) for bar in ex["rh"][0] for e in bar for n in e["n"]), "the tune is below"
            if part is duplet:
                assert "\\tuplet 2/3 {" in code, "duplets"
            if part is three4:
                assert "\\tuplet 3/2 {" in code and "16" in code, "triplets against sixteenths"
            if part is runs:
                groups = re.findall(r"\\tuplet (\d)/4 \{([^}]*)\}", code)
                assert len(groups) == 2 and all(int(n) == len(g.split()) for n, g in groups), "two runs"
                for bar in ex["rh"][0]:
                    run = [e["n"][0][0] for e in bar if isinstance(e.get("t"), tuple)]
                    assert all(abs(a - b) == 1 for a, b in zip(run, run[1:])), "runs move by step"
            if part is hemi:
                r = [[e["d"] for e in bar] for bar in ex["rh"][0][5:7]]
                assert r == [[Fr(1, 2), Fr(1, 4)], [Fr(1, 4), Fr(1, 2)]], "three half notes over two bars"
                assert ex["rh"][0][5][1]["n"] == ex["rh"][0][6][0]["n"] and "~" in ex["rh"][0][5][1]["end"]
            scores.append(code)
    print("rhythm against rhythm: 2:3, duplets, 3:4, runs, hemiola     OK")
    return scores


def test_meters():
    """Unit 3 (plan feature 4): changing meters, beat groups, modes without a key signature, and
    unbarred pentatonic and whole-tone tunes."""
    scores = []
    mix = dict(name="A", title="5/4 and 6/4", count=2, bars=8, meter="5/4", texture="meters", meters=["5/4", "6/4"],
               tempo=88, key=("bes", "major"))
    seven = dict(name="B", title="7/8", count=2, bars=8, meter="7/8", texture="meters", tempo=160, tempo_unit="8",
                 key=("d", "major"))
    dorian = dict(name="C", title="Dorian", count=2, bars=8, meter="4/4", texture="meters", tempo=72,
                  key=("a", "dorian"), no_signature=True)
    pent = dict(name="D", title="Pentatonic", count=2, bars=1, meter="4/4", texture="meters", unbarred=True,
                scale="pentatonic", tempo=72, key=("f", "major"))
    whole = dict(pent, scale="wholetone", key=("c", "major"))
    for part in (mix, seven, dorian, pent, whole):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6003), set())):
            code = gen6.lily_exercise(part, ex, f"99.M{k}")[0]
            if part is mix:
                assert code.count("\\time 6/4") == 2 * 4 and ex["meters"][:2] == ["5/4", "6/4"], "the meter alternates"
            if part is seven:
                assert "\\time 2,2,3 7/8" in code, "beat groups"
            if part is dorian:
                assert "\\key c \\major" in code, "no key signature"
                assert any(n[1] == 1 for v in ex["rh"] for bar in v for e in bar for n in e["n"]), "F-sharp written out"
                assert ex["key"].degree([e for e in ex["rh"][0][-1] if e["n"]][-1]["n"][0][0]) == 0, "ends on A"
            if part in (pent, whole):
                assert "\\cadenzaOn" in code and "|" not in code.replace('"|."', ""), "no bar checks"
                semis = {gen5.midi(e["n"][0]) % 12 for e in ex["rh"][0][0]}
                tonic = gen5.midi(ex["key"].note(ex["key"].tonic)) % 12
                allowed = {(tonic + i) % 12 for i in (gen6.PENTATONIC if part is pent else gen6.WHOLE_TONE)}
                assert semis <= allowed, "only the scale's notes"
                assert code.count('\\bar ";"') == 2 * 3, "dotted bar lines between the four phrases"
            scores.append(code)
    print("changing meters, 7/8, modes, unbarred scales     OK")
    return scores


def test_harmony():
    """Unit 4 (plan feature 5): chromatic chords in four parts, voice leading, modulation."""
    scores = []
    sec = dict(name="A", title="Secondary", count=3, bars=8, meter="4/4", texture="harmony", harmony="secondary",
               tempo=56, key=("e", "major"), labels=True)
    pre = dict(sec, harmony="predominant", key=("f", "minor"))
    piv = dict(sec, harmony="pivot", key=("d", "major"))
    dim = dict(sec, harmony="dim7", key=("bes", "major"))
    c = gen6.chord6(gen5.Key("c"), "V7/V")
    assert sorted(gen5.LETTERS[l] + str(pc) for l, pc in c["tones"].values()) == ["a9", "c0", "d2", "f6"], "D7 in C"
    e = gen6.chord6(gen5.Key("e"), "vii7/vi")
    assert ("b", 0) in [(gen5.LETTERS[l], pc) for l, pc in e["tones"].values()], "B-sharp in E major (a double sharp's cousin)"
    a6 = gen6.chord6(gen5.Key("a", "minor"), "Ger6")
    assert {gen5.LETTERS[l] for l, _ in a6["tones"].values()} == {"f", "a", "c", "d"}, "German sixth F A C D-sharp"
    for part in (sec, pre, piv, dim):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6004), set())):
            voices = []
            for b in range(8):
                for re_, le in zip(ex["rh"][0][b], ex["lh"][0][b]):
                    voices.append([gen5.midi(le["n"][0])] + sorted(gen5.midi(n) for n in re_["n"]))
            for v1, v2 in zip(voices, voices[1:]):
                for i in range(4):
                    for j in range(i + 1, 4):
                        moved = v1[i] != v2[i] or v1[j] != v2[j]
                        same = (v1[j] - v1[i]) % 12 == (v2[j] - v2[i]) % 12 in (0, 7)
                        assert not (moved and same and v1[i] != v2[i]), "parallel fifths or octaves"
            names = ex["plan"]
            for n1, n2, v1, v2 in zip(names, names[1:], voices, voices[1:]):
                if n1.startswith(("V7/", "vii7/")) and n2 == n1.split("/")[1]:
                    assert any(b - a == 1 for a, b in zip(v1, v2)), "the leading note rises"
            code = gen6.lily_exercise(part, ex, f"99.H{k}")[0]
            if part in (piv, dim):
                assert code.count(f"\\key {ex['end_key'].lily}") >= 2 and ex["end_key"].lily != ex["key"].lily, \
                    "the new key signature"
            scores.append(code)
    print("chromatic harmony: secondary, N6/aug6, pivot, dim7     OK")
    return scores


def test_big():
    """Unit 5 (plan feature 6): octaves with 8va/8vb, full chords over arpeggios, crossed hands, and
    dense textures with a printed reduction."""
    scores = []
    octs = dict(name="A", title="Octaves", count=2, bars=8, meter="4/4", texture="big", big="octaves",
                rhythms=["basic"], tempo=72, key=("f", "major"), register="high")
    low = dict(octs, register="low", key=("g", "minor"), meter="3/4")
    chords = dict(octs, big="chords", rhythms=["slow"], register=None, key=("ees", "major"))
    cross = dict(octs, big="cross", rhythms=["slow"], register=None, meter="3/4", key=("c", "major"))
    dense = dict(octs, big="dense", rhythms=["slow"], register=None, key=("a", "minor"))
    for part in (octs, low, chords, cross, dense):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6005), set())):
            code = gen6.lily_exercise(part, ex, f"99.B{k}")[0]
            if part is octs:
                assert all(len(e["n"]) == 2 and e["n"][1][0] - e["n"][0][0] == 7 for bar in ex["rh"][0] for e in bar)
                assert "\\ottava #1" in code and "\\ottava #0" in code, "8va"
            if part is low:
                assert "\\ottava #-1" in code, "8vb"
            if part is chords:
                assert max(len(e["n"]) for bar in ex["rh"][0] for e in bar) >= 4, "full chords"
                assert "\\sustainOn" in code, "pedalled arpeggios"
            if part is cross:
                assert code.count("l.h.") == 7 and '\\change Staff = "up"' in code, "the left hand crosses"
            if part is dense:
                assert ex.get("reduction") and code.count("\\magnifyStaff #2/3") == 2, "the reduction staff"
            scores.append(code)
    print("big textures: octaves, 8va/8vb, chords, crossing, reduction     OK")
    return scores


def test_songs():
    """Unit 6 (plan feature 7): a singer's line above the piano, intro, interlude, doubling."""
    scores = []
    block = dict(name="A", title="Block", count=2, bars=8, meter="4/4", texture="song", accomp="block",
                 rhythms=["basic"], tempo=72, key=("f", "major"))
    intro = dict(block, bars=11, meter="3/4", accomp="afterbeat", intro=2, interlude=1, key=("d", "major"))
    arp = dict(intro, meter="4/4", accomp="arpeggio", key=("g", "minor"))
    dbl = dict(block, bars=9, interlude=1, double_tune=True, key=("e", "minor"))
    for part in (block, intro, arp, dbl):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6006), set())):
            code = gen6.lily_exercise(part, ex, f"99.S{k}")[0]
            voice = ex["voice"]
            notes = [e for bar in voice for e in bar if e["n"]]
            assert code.count(" la") == len(notes), "one neutral syllable per sung note"
            sung = [gen5.midi(e["n"][0]) for e in notes]
            assert max(sung) - min(sung) <= 14, "a singable range"
            assert len(voice) == part["bars"] and len(ex["rh"][0]) == part["bars"]
            if part.get("intro"):
                assert not any(e["n"] for bar in voice[:2] for e in bar), "the piano introduction"
            if part is dbl:
                tops = {gen5.midi(max(e["n"], key=gen5.midi)) for bar in ex["rh"][0] for e in bar if e["n"]}
                assert sum(m in tops for m in sung) >= 4, "the piano doubles the tune"
            assert "\\addlyrics" in code and "Voice" in code
            scores.append(code)
    print("songs: block, after-beat, arpeggio, intro, interlude, doubling     OK")
    return scores


def test_clefs_transposing():
    """Unit 7 (plan feature 8): quartet and C-clef layouts of the chorale, and transposing parts."""
    scores = []
    quartet = dict(name="B", title="Quartet", count=2, bars=8, meter="4/4", texture="chorale", voices=4, staves=4,
                   clefs="quartet", tempo=60, key=("d", "major"))
    cclefs = dict(quartet, clefs="c_clefs", key=("f", "major"))
    trans = dict(name="C", title="Transpose", count=2, bars=8, meter="4/4", rhythms="basic", bass="block", tempo=60,
                 key=("f", "major"), transpose={"by": "M2", "dir": "up"})
    for part in (quartet, cclefs, trans):
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6007), set())):
            code = gen6.lily_exercise(part, ex, f"99.Q{k}")[0]
            if part is quartet:
                assert "StaffGroup" in code and "\\clef alto" in code and "Violin 1" in code and "Cello" in code
            if part is cclefs:
                assert "\\clef alto" in code and "\\clef tenor" in code and "ChoirStaff" in code
            if part is trans:
                assert "Play it a tone higher: in G major" in code
            scores.append(code)
    assert gen6.transposed_key(gen5.Key("bes"), {"by": "M2", "dir": "down"}).text() == "A-flat major"
    assert gen6.transposed_key(gen5.Key("c"), {"by": "m3", "dir": "up"}).text() == "E-flat major"
    unit = {"id": 98, "parts": [dict(trans, count=2)]}
    ans = gen6.answer_scores(unit, 1)
    assert len(ans) == 2 and all("\\transpose c d" in a for a in ans), "the answers, a tone up"
    print("open score layouts, C clefs, transposing     OK")
    return scores + ans


def test_leadsheet():
    """Unit 8 (plan feature 9): a tune with chord symbols, triads and sevenths/slash chords."""
    scores = []
    base = dict(name="A", title="Lead", count=4, bars=8, meter="4/4", texture="leadsheet", rhythms=["basic"],
                tempo=72, chords=["I", "IV", "V", "V7", "ii", "vi"], key=("g", "major"))
    for kind in ("triads", "sevenths"):
        part = dict(base, symbols=kind)
        for k, ex in enumerate(gen6.generate_part(dict(part), random.Random(6008), set())):
            assert ex["group"] == "lead" and ex["staves"][0]["clef"] == "chords"
            syms = ex["staves"][0]["chords"].split()
            assert len(syms) == part["bars"], "one symbol per bar"
            if kind == "triads":
                assert not any("/" in s or "maj7" in s or "m7" in s for s in syms)
            code = gen6.lily_exercise(part, ex, f"99.L{k}")[0]
            assert "ChordNames" in code and "chordmode" in code and "PianoStaff" not in code
            scores.append(code)
    assert gen6.lily_name((4, 0)) == "g" and gen6.lily_name((3, 1)) == "fis"
    print("lead sheets                                  OK")
    return scores


if __name__ == "__main__":
    test_passthrough()
    exs, scores = test_open_score()
    scores.append(quartet_score(exs[0]))
    plain = gen6.generate_part(dict(PLAIN), random.Random(123), set())
    scores.append(solo_score(plain[0]))
    scores += test_answers()
    scores += test_three_voices()
    scores += test_rhythms()
    scores += test_meters()
    scores += test_harmony()
    scores += test_big()
    scores += test_songs()
    scores += test_leadsheet()
    scores += test_clefs_transposing()
    test_build_compiles(scores)
    test_checker()
    print("OK")
