"""Volume 5, Unit 6: Every key."""
import re

KEYBOARDS = []
KEY_PICTURES = [
    ("B major: five sharps", "b", "major"),
    ("D-flat major: five flats", "des", "major"),
    ("F-sharp major: six sharps (E-sharp is the white key F)", "fis", "major"),
    ("G-flat major: six flats (C-flat is the white key B) - the same keys as F-sharp major", "ges", "major"),
]

_ENH = {"fis": "ges", "gis": "aes", "ais": "bes", "cis": "des", "dis": "ees", "eis": "f"}


def _to_gflat(music):
    """Respell F-sharp major music in G-flat major: the same keys, every note one letter higher
    (B becomes C-flat, one octave mark higher)."""
    def sub(m):
        name, marks = m.group(1), m.group(2)
        if name == "b":
            if marks.startswith(","):
                return "ces" + marks[1:]
            return "ces" + marks + "'"
        return _ENH[name] + marks
    return re.sub(r"(?<![a-z\\])(fis|gis|ais|cis|dis|eis|b)(?![a-z])([',]*)", sub, music)


_TWIN_RH = ("ais'4\\p cis'' fis''2 | dis''4 b' fis''2 | eis''4 cis'' gis' b' | ais'1 | \\break "
            "dis''4\\mf fis'' ais''2 | gis''4( fis'') dis''2 | eis''4\\> gis'' cis'' b' | ais'2 fis'\\p")
_TWIN_LH = ("<fis, ais, cis>1 | <b, dis fis>1 | <cis eis gis b>1 | <fis, ais, cis>1 | <dis fis ais>1 | "
            "<b, dis fis>1 | <cis eis gis b>1 | <fis, ais, cis>1")


INTRO = [
    "There are fifteen major keys and fifteen minor keys. You have met the keys with up to four sharps or "
    "flats; now come the rest: five, six and seven. Three pairs of them sound exactly the same and use the same "
    "keys on the piano, but are written differently: B major and C-flat major, F-sharp major and G-flat "
    "major, C-sharp major and D-flat major. Such keys are called enharmonic.",
    "Keys with many sharps or flats look frightening, but they lie well under the hand: most of their notes "
    "are black keys, and the long fingers fall on them naturally.",
]

NEW_IDEAS = [
    ("The circle of fifths", "Each sharp key is a fifth above the last: C, G, D, A, E, B, F-sharp, C-sharp "
                             "(0 to 7 sharps). Each flat key is a fifth below: C, F, B-flat, E-flat, A-flat, "
                             "D-flat, G-flat, C-flat (0 to 7 flats). Round the circle they meet: F-sharp is G-flat."),
    ("Order of sharps and flats", "Sharps: F C G D A E B. Flats: B E A D G C F, the same letters backwards."),
    ("Enharmonic notes", "One key on the piano can have two names: F-sharp is G-flat, E-sharp is F, C-flat is B. "
                         "In F-sharp major E-sharp is the 7th note; in G-flat major C-flat is the 4th."),
    ("Minor keys too", "B-flat minor (five flats) and G-sharp minor (five sharps): their raised 7ths are A-natural "
                       "and F-double-sharp (the white key G). A double sharp looks like a small x."),
]

EXAMPLES = [
    {"title": "The same keys, two names",
     "text": "F-sharp major and G-flat major: every note sounds the same and uses the same key on the piano.",
     "staff": "treble", "time": "4/4", "key": "fis \\major",
     "rh": "fis'4 ais' cis'' eis'' | fis''1 \\bar \"||\" \\set Staff.printKeyCancellation = ##f \\key ges \\major ges'4 bes' des'' f'' | ges''1 \\bar \"||\""},
]

TIPS = [
    "Count the sharps or flats, name the key, and say the black keys it uses before you play.",
    "In five-, six- and seven-sharp or flat keys, think of the white keys as the exceptions.",
    "E-sharp, B-sharp, C-flat and F-flat are white keys: read the name, find the key, and trust your hand.",
    "Round the circle of fifths, each new key changes only one note: find it.",
]

PART_NOTES = {
    "A": "B major and D-flat major, with chords in half notes.",
    "B": "Twins: each F-sharp major exercise is printed again in G-flat major (a and b): play both and hear that "
         "they are the same. Between them, B-flat minor and G-sharp minor waltzes.",
    "C": "Round the circle of fifths: each four-bar exercise is in a new key, sharps first, then flats.",
}

PIECES = [
    {
        "title": "Night Song in B", "credit": "Original", "meter": "3/4", "tempo": 84, "key": "b \\major",
        "note": "Five sharps: F, C, G, D and A. The left hand plays a waltz bass; the chords are B, E, F-sharp7 "
                "(with A-sharp) and G-sharp minor.",
        "rh": "b'4\\p dis'' fis'' | gis''2 e''4 | fis''4 e'' cis'' | dis''2. | \\break b'4\\< dis'' gis'' | "
              "gis''2\\mf e''4 | e''4\\> cis'' ais' | b'2.\\p",
        "lh": "b,4 <dis fis> <dis fis> | e4 <gis b> <gis b> | fis,4 <e ais> <e ais> | b,4 <dis fis> <dis fis> | "
              "gis,4 <dis b> <dis b> | e4 <gis b> <gis b> | fis,4 <e ais> <e ais> | <b, fis b>2.",
    },
    {
        "title": "Enharmonic Twins (1): F-sharp major", "credit": "Original", "meter": "4/4", "tempo": 72,
        "key": "fis \\major",
        "note": "Six sharps. E-sharp (the white key F) is in the C-sharp7 chord. Play this, then the next piece: "
                "it is the same music in G-flat major.",
        "rh": _TWIN_RH, "lh": _TWIN_LH,
    },
    {
        "title": "Enharmonic Twins (2): G-flat major", "credit": "Original", "meter": "4/4", "tempo": 72,
        "key": "ges \\major",
        "note": "Six flats: the same keys on the piano as the F-sharp major piece, every note with a new name. "
                "C-flat is the white key B; F is in the D-flat7 chord.",
        "rh": _to_gflat(_TWIN_RH), "lh": _to_gflat(_TWIN_LH),
    },
    {
        "title": "Raindrop Prelude", "credit": "Frederic Chopin (1839), Prelude in D-flat, Op. 28 No. 15 - bars 1-8, "
                                           "simplified",
        "meter": "4/4", "tempo": 60, "key": "des \\major",
        "note": "Five flats. The left hand's A-flats fall like raindrops all through the piece. Chopin's left hand "
                "has an inner voice and some notes for the right hand; here it plays the A-flats with its chords, "
                "and the ornamental run in bar 4 is left out. Chopin asks for the pedal: leave it until Unit 7. "
                "Source: Mutopia Project no. 471 (public domain).",
        "rh": "f''8.\\p( des''16 aes'2 bes'4 | c''2. des''4 | ees''8. f''16 ges''2 f''4 | f''4. ees''8 des''2) | \\break "
              "f''8.( des''16 aes'2 bes'4 | c''2. des''4 | ees''8. f''16 ges''2 f''4 | f''4.\\> ees''8 des''2\\!)",
        "lh": "des8 aes <des' f'> aes aes aes <des' f'> aes | <ees' ges'>8 aes aes aes bes aes <des' f'> aes | "
              "aes,8 aes <c' ges'> aes aes aes <c' ges'> aes | aes,8 aes <c' ges'> aes <des' f'> aes <des' f'> aes | "
              "des8 aes <des' f'> aes aes aes <des' f'> aes | <ees' ges'>8 aes aes aes bes aes <des' f'> aes | "
              "aes,8 aes <c' ges'> aes aes aes <c' ges'> aes | aes,8 aes <c' ges'> aes <des aes des'>2",
    },
    {
        "title": "Impromptu in G-flat", "credit": "Franz Schubert (1827), Impromptu, D. 899 No. 3 - the first "
                                               "sixteen bars, simplified",
        "meter": "2/2", "cut": True, "tempo": 50, "tempo_unit": "2", "key": "ges \\major", "allow_span": 14, "allow_leap": 14,
        "note": "Six flats. Schubert writes four half notes in a bar (4/2); here each of his bars is split into two "
                "bars of 2/2. The right hand plays the slow tune (stems up) and a flowing accompaniment of six notes "
                "to each half note (stems down): all its eighths are triplet eighths, three to a quarter beat, "
                "though the figures 6 and 3 are printed only at the start. Count two beats in a bar. In bar 15 the hand stretches a ninth, from G-flat to the tune's A-flat. The last bar's accompaniment is a G-flat "
                "chord, so that the excerpt ends at home. Source: Mutopia Project no. 1193 (public domain).",
        "rh": "<< { bes'1\\pp( | bes'2-. bes'-.) | bes'1( | ges'1) | \\break aes'1( | ges'4 f' ees' des') | ges'2 bes' | "
              "aes'2. a'4 | \\break bes'1( | bes'2 bes') | bes'1( | ges'2 f') | \\break ees'2( aes' | "
              "ges'4 f' ees' f') | aes'1( | ges'1) } \\\\ { \\override TupletBracket.bracket-visibility = ##f "
              "\\tuplet 6/4 { r8 bes des' ges' des' bes } \\tuplet 6/4 { des'8 bes des' ges' des' bes } | \\omit TupletNumber "
              "\\tuplet 6/4 { r8 bes des' ges' des' bes } \\tuplet 6/4 { r8 bes des' ges' des' bes } | "
              "\\tuplet 6/4 { r8 bes ees' ges' ees' bes } \\tuplet 6/4 { ees'8 bes ees' ges' ees' bes } | "
              "\\tuplet 6/4 { r8 ges bes ees' bes ges } \\tuplet 6/4 { bes8 ges bes ees' bes ges } | "
              "\\tuplet 6/4 { r8 aes ces' ees' ces' aes } \\tuplet 6/4 { ces'8 aes ces' ees' ces' aes } | "
              "\\tuplet 3/2 { r8 aes ces' } \\tuplet 3/2 { r8 aes ces' } \\tuplet 3/2 { r8 aes ces' } \\tuplet 3/2 { r8 f aes } | "
              "\\tuplet 6/4 { r8 ges bes des' bes ges } \\tuplet 6/4 { r8 c' ees' ges' ees' c' } | "
              "\\tuplet 6/4 { r8 aes des' f' des' aes } \\tuplet 6/4 { des'8 aes des' f' des' aes } | "
              "\\tuplet 6/4 { r8 bes des' ges' des' bes } \\tuplet 6/4 { des'8 bes des' ges' des' bes } | "
              "\\tuplet 6/4 { r8 bes des' ges' des' bes } \\tuplet 6/4 { r8 bes des' ges' des' bes } | "
              "\\tuplet 6/4 { r8 bes ees' ges' ees' bes } \\tuplet 6/4 { ees'8 bes ees' ges' ees' bes } | "
              "\\tuplet 6/4 { r8 ges bes ees' bes ges } \\tuplet 6/4 { r8 aes ces' ees' ces' aes } | "
              "\\tuplet 3/2 { r8 ces' aes } \\tuplet 3/2 { r8 ces' aes } \\tuplet 3/2 { r8 ces' aes } \\tuplet 3/2 { r8 ces' aes } | "
              "\\tuplet 6/4 { r8 ces' des' f' des' ces' } \\tuplet 6/4 { des'8 ces' des' f' des' ces' } | "
              "\\tuplet 6/4 { r8 ges bes des' bes ges } \\tuplet 6/4 { bes8 ges bes des' bes ges } | "
              "\\tuplet 6/4 { r8 ges bes des' bes ges } \\tuplet 6/4 { bes8 ges bes des' bes ges } } >>",
        "lh": "<ges, des>1 | <ges, des>2 <ges, des> | <ees, ees>1~ | <ees, ees>1 | <ces, ces>1 | <des, des>2. <ces des>4 | "
              "<bes, des>2 <ges, ees> | <des, des>1 | <ges, des>1 | <ges, des>2 <ges, des> | <ees, ees>1~ | "
              "<ees, ees>2 <bes,, bes,> | <ces, ces>2 <aes,, aes,> | <des, des>1 | <ges, des>1~ | <ges, des>1",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 7?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if you can name all fifteen major keys from their key signatures, round the circle of fifths.",
    "Pass if you can play both Enharmonic Twins at sight and hear that they are the same music.",
    "When you pass, move on to Unit 7.",
]
