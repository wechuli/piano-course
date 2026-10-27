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


if __name__ == "__main__":
    test_passthrough()
    exs, scores = test_open_score()
    scores.append(quartet_score(exs[0]))
    plain = gen6.generate_part(dict(PLAIN), random.Random(123), set())
    scores.append(solo_score(plain[0]))
    scores += test_answers()
    test_build_compiles(scores)
    test_checker()
    print("OK")
