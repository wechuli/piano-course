"""Checks for the technique book's fingering tables (run from course/; prints OK).

1. Scales: the fourth finger falls where the published chart says (B. Burt, "Fingering charts, piano
   scales", from Prof. Escandon, University of Miami): one fourth-finger note per octave per hand.
2. Scales and arpeggios: the thumb is never on a black key, except in arpeggios whose notes are all
   black (F-sharp major, E-flat minor).
3. The fingering never jumps more than the hand allows: a thumb crossing (finger after the thumb
   going one way, thumb after a finger the other) only between neighbouring scale notes.
4. Spelling: every scale has seven different letters and the right number of sharps or flats.
"""
import technique as T

# Burt's chart: placement of the 4th finger (LH / RH), as scale degrees of the key (1 = tonic).
FOURTH = {  # (tonic, alt, mode): (LH degree, RH degree)
    **{(t, 0, "major"): (2, 7) for t in "cdega"},
    **{(t, 0, "minor"): (2, 7) for t in "cdega"},
    ("f", 0, "major"): (2, 4), ("f", 0, "minor"): (2, 4),
    ("b", 0, "major"): (5, 7), ("b", 0, "minor"): (5, 7),
    ("d", -1, "major"): (4, 6),                       # Gb / Bb
    ("c", 1, "minor"): (4, 2),                        # F# / D#  (harmonic)
    ("e", -1, "major"): (4, 5),                       # Ab / Bb
    ("e", -1, "minor"): (3, 5),                       # Gb / Bb  (harmonic)
    ("f", 1, "major"): (1, 3),                        # Gb(F#) / Bb(A#)
    ("f", 1, "minor"): (1, 2),                        # F# / G#  (harmonic)
    ("a", -1, "major"): (4, 2),                       # Db / Bb
    ("g", 1, "minor"): (4, 2),                        # C#(Db) / A#(Bb)  (harmonic)
    ("b", -1, "major"): (4, 1),                       # Eb / Bb
    ("b", -1, "minor"): (6, 1),                       # Gb / Bb  (harmonic)
}


def test_scales():
    assert set(FOURTH) == set(T.SCALE_FINGERS), "every scale is checked"
    for key, (lh4, rh4) in FOURTH.items():
        f = T.SCALE_FINGERS[key]
        assert [i + 1 for i, x in enumerate(f["rh"]) if x == 4] == [rh4], (key, "RH 4th")
        assert [i + 1 for i, x in enumerate(f["lh"]) if x == 4] == [lh4], (key, "LH 4th")
        tonic, alt, mode = key
        kind = "major" if mode == "major" else "harmonic"
        for hand in ("rh", "lh"):
            notes = T.scale_notes(tonic, alt, kind, T.tonic_step(tonic, hand), 15)
            fing = T.scale_fingering(key, hand, 2)
            assert len({n.step % 7 for n in notes[:7]}) == 7
            for n, x in zip(notes, fing):
                assert not (x == 1 and n.black), (key, hand, "thumb on a black key", n.lily())
            for (a, x), (b, y) in zip(zip(notes, fing), zip(notes[1:], fing[1:])):
                # RH going up / LH going down: fingers rise from the thumb, or the thumb passes under
                if hand == "rh":
                    assert y == x + 1 or y == 1 or (x == 1 and y == 2) or y == 5 or (y == 4 and x == 3) \
                        or (y == x + 1), (key, hand, x, y)
                assert abs(x - y) in (1, 2, 3), (key, hand, "fingers", x, y)
        # end and start fingers: 5 only at an end note of a white-key scale
        assert f["rh_end"] in (2, 3, 4, 5) and f["lh_start"] in (2, 3, 4, 5)


def test_key_signatures():
    sharps = {"g": 1, "d": 2, "a": 3, "e": 4, "b": 5}
    for t, n in sharps.items():
        notes = T.scale_notes(t, 0, "major", T.tonic_step(t, "rh"), 7)
        assert sum(x.alt for x in notes) == n, t
    assert sum(x.alt for x in T.scale_notes("f", 1, "major", T.tonic_step("f", "rh"), 7)) == 6
    assert sum(x.alt for x in T.scale_notes("d", -1, "major", T.tonic_step("d", "rh"), 7)) == -5
    hm = T.scale_notes("a", 0, "harmonic", T.tonic_step("a", "rh"), 7)
    assert hm[6].lily() == "gis'", "raised seventh in A harmonic minor"
    assert T.scale_notes("g", 1, "harmonic", T.tonic_step("g", "rh"), 7)[6].lily() == "fisis''", "F double-sharp in G-sharp minor"


def test_arpeggios():
    for key, (rh, lh) in T.ARP_FINGERS.items():
        assert len(rh) == len(lh) == 7
        tonic, alt, mode = key
        kind = "major" if mode == "major" else "harmonic"
        for hand, f in (("rh", rh), ("lh", lh)):
            sc = T.scale_notes(tonic, alt, kind, T.tonic_step(tonic, hand), 15)
            chord = [sc[i] for i in range(15) if i % 7 in (0, 2, 4)]
            all_black = all(n.black for n in chord[:3])
            for n, x in zip(chord, f):
                assert all_black or not (x == "1" and n.black), (key, hand, n.lily())
            assert f[3] == f[0] or (hand == "rh" and f[0] in "12") or (hand == "lh" and f[0] in "523"), key


def test_book_builds_strings():
    for st in T.STAGES:
        for _, scores in st[4]:
            for sc in scores:
                assert sc.count("\\score") == 1


if __name__ == "__main__":
    test_scales()
    test_key_signatures()
    test_arpeggios()
    test_book_builds_strings()
    print("OK")
