"""Volume 5, Unit 5: Four sharps and four flats."""

KEYBOARDS = []
KEY_PICTURES = [
    ("E major: four sharps (F, C, G, D)", "e", "major"),
    ("A-flat major: four flats (B, E, A, D)", "aes", "major"),
    ("C-sharp minor: E major's relative minor; the raised 7th is B-sharp", "cis", "minor"),
    ("F minor: A-flat major's relative minor; the raised 7th is E-natural", "f", "minor"),
]


def _t(a, b, c, n=1):
    return " ".join([f"\\tuplet 3/2 {{ {a}8 {b} {c} }}"] * n)


INTRO = [
    "Each new key adds one sharp or one flat to the last. E major has four sharps: F, C, G and D. A-flat major "
    "has four flats: B, E, A and D. Their relative minors share the key signatures: C-sharp minor (with "
    "B-sharp as its raised 7th) and F minor (with E-natural). The keyboard pictures show which keys each scale "
    "uses: in four-sharp and four-flat keys most of the black keys are in play.",
]

NEW_IDEAS = [
    ("Four sharps", "F-sharp, C-sharp, G-sharp, D-sharp: E major and C-sharp minor. The last sharp (D-sharp) "
                    "is the 7th note of E major."),
    ("Four flats", "B-flat, E-flat, A-flat, D-flat: A-flat major and F minor. The second-last flat (A-flat) "
                   "names the major key."),
    ("B-sharp and E-natural", "The raised 7th of C-sharp minor is B-sharp (the white key C); the raised 7th of "
                              "F minor is E-natural. Both appear in every V chord."),
    ("Think in shapes", "In these keys the hand sits on the black keys. Learn the I, IV and V chord shapes of each "
                        "key: most passages are made of them."),
]

TIPS = [
    "Name the key, then play the scale and the I, IV and V chords once before you read.",
    "Watch for B-sharp and E-natural in the minor keys: they look strange but are the leading notes.",
    "Remember the key signature in every octave and in both clefs.",
    "If a passage is mostly on black keys, use your longer fingers (2, 3, 4) for them and thumbs on the white keys.",
]

PART_NOTES = {
    "A": "E major over an Alberti bass, with dynamics.",
    "B": "A-flat major waltzes, with dynamics.",
    "C": "C-sharp minor (B-sharp in the V chords) and F minor (E-natural), alternating.",
}

PIECES = [
    {
        "title": "E Major Morning", "credit": "Original", "meter": "4/4", "tempo": 76, "key": "e \\major",
        "note": "Four sharps. The left hand's Alberti bass uses the shapes of E (E G-sharp B), A (A C-sharp E) and "
                "B7 (B D-sharp F-sharp A).",
        "rh": "gis'4\\mp b' e'' dis'' | cis''4 a' fis' a' | gis'4 e' b'2 | dis''2 fis''4 dis'' | \\break "
              "gis''4\\mf e'' b''4. gis''8 | a''4 gis''8( fis'') e''4 cis'' | dis''4\\> fis''8( e'') dis''4 a' | gis'2\\p e'",
        "lh": "e8 b gis b e b gis b | a, e cis e b, a dis a | e8 b gis b e b gis b | b,8 fis dis fis b, fis dis fis | "
              "e8 b gis b e b gis b | a,8 e cis e a, e cis e | b,8 a dis a b, a dis a | <e gis b>1",
    },
    {
        "title": "Moment musical No. 3", "credit": "Franz Schubert (1823), Moments musicaux, D. 780 No. 3 - the "
                                                 "opening, grace notes left out",
        "meter": "2/4", "tempo": 80, "key": "f \\minor", "allow_leap": 17,
        "note": "F minor (four flats). The left hand plays an oom-pah of a bass note and a chord; E-natural, the raised "
                "7th, is in its C major chords. A-natural in bar 7 is chromatic; in bar 8 the left hand drops from its chord to a low F. The tune is staccato; the original's "
                "grace notes are left out (they come in Unit 8). Play bars 3-10 twice. Source: Mutopia Project no. "
                "1023 (public domain).",
        "rh": "R2 | R2 | \\repeat volta 2 { aes'8-.\\p aes'16( bes') aes'8-. g'-. | <aes' c''>4-> <aes' c''>-> | "
              "aes'8-. aes'16( bes') aes'8-. <g' c''>-. | <aes' f''>4-> <aes' f''>-> | \\break "
              "<< { f''8 f''16( ges'' f''8) f'' | f''8( bes''16) } \\\\ { aes'8 aes' a' a' | bes'8. } >> r16 <aes' f''>4 | "
              "<aes' c''>16( <g' bes'> <f' aes'> <g' bes'>) << { c''16( des'') c''( e'') } \\\\ { aes'8 <g' bes'> } >> | "
              "<aes' c'' f''>4 <aes' c'' f''> }",
        "lh": "f8-. <c' f'>-. f-. <c' f'>-. | f8-. <c' f'>-. f-. <c' f'>-. | \\repeat volta 2 { f8 <c' f'> f <c' e'> | "
              "f8 <c' f'> f <c' f'> | f8 <c' f'> f <c' e'> | f8 <c' f'> f <c' f'> | des8 <des' f'> c <c' ees' f'> | "
              "bes,8 <bes des' f'> f, <c f> | c,8 <c f> c, <c e> | f,8 <c f> f, <c f> }",
    },
    {
        "title": "Impromptu in A-flat", "credit": "Franz Schubert (1827), Impromptu, D. 935 No. 2 - the first eight "
                                                "bars, the last chord lengthened",
        "meter": "3/4", "tempo": 72, "key": "aes \\major", "upbeat": "1/4",
        "note": "Four flats. A slow sarabande: the stress is often on the second beat (the dotted quarters). The "
                "right hand plays a tune over two held notes, then three-note chords; the left hand repeats E-flat "
                "(stems up) above a slow bass (stems down). Source: Mutopia Project no. 1195 (public domain).",
        "rh": "\\partial 4 ees'4\\p | << { aes'4 aes'4.( bes'8) | aes'4 g'4.( bes'8) | bes'4( aes' bes') | c''2 } \\\\ "
              "{ <c' ees'>4 <c' ees'>2 | <des' ees'>4 <des' ees'>2 | r4 ees' <des' ees'> | <c' ees'>2 } >> ees'4 | \\break "
              "<c' ees' c''>4 <c' ees' c''>4.( <des' ees' des''>8) | <c' ees' c''>4 <bes ees' bes'>4.( <c' ees' c''>8) | "
              "<bes ees' bes'>4 << { <aes ees' aes'>4 ees''8. des''16 | c''2. } \\\\ { s4 <ees' bes'>4 | <ees' aes'>2. } >>",
        "lh": "\\partial 4 ees4 | << { ees4 ees2 | ees4 ees2 | ees4 ees ees | ees2 ees4 | ees4 ees2 | ees4 ees2 | "
              "ees4 ees ees | ees2. } \\\\ { aes,2. | bes,2. | c2 g,4 | aes,2 s4 | aes,2. | des2. | c2 g,4 | aes,2. } >>",
    },
    {
        "title": "Moonlight Sonata", "credit": "Ludwig van Beethoven (1801), Sonata Op. 27 No. 2, first movement - "
                                             "bars 1-9, simplified",
        "meter": "2/2", "cut": True, "tempo": 54, "key": "cis \\minor", "allow_span": 14,
        "note": "C-sharp minor, four sharps; B-sharp in bars 4 and 6 is the raised 7th. The right hand plays "
                "triplets all through (stems down) and, from bar 5, the tune above them (stems up): the tune's "
                "sixteenth comes after the third note of the triplet. The figure 3 is printed only in the first bar: all the eighths are triplets. The time signature is alla breve, but at this "
                "slow speed count four quarter beats. The left hand plays octaves. In bar 8 the right hand stretches a ninth, from the A of the triplet to the B of the tune. Beethoven asks for the pedal "
                "throughout; play without it until Unit 7, holding the bass octaves for their full length. The "
                "first triplet of bar 5, which Beethoven gives to the left hand, is in the right hand here. Notes "
                "retyped from the Mutopia Project engraving no. 276 (CC BY-SA 2.5).",
        "rh": "<< { s1 | s1 | s1 | \\break s1 | r2 r4 gis'8.\\pp gis'16 | gis'2. gis'8. gis'16 | \\break gis'2( a' | "
              "gis'2 fis'4 b') | e'4 r r2 } \\\\ { \\override TupletBracket.bracket-visibility = ##f "
              + _t("gis", "cis'", "e'", 4) + " | \\omit TupletNumber " + _t("gis", "cis'", "e'", 4) + " | "
              + _t("a", "cis'", "e'", 2) + " " + _t("a", "d'", "fis'", 2) + " | "
              + _t("gis", "bis", "fis'") + " " + _t("gis", "cis'", "e'") + " " + _t("gis", "cis'", "dis'") + " "
              + _t("fis", "bis", "dis'") + " | "
              + _t("e", "gis", "cis'") + " " + _t("gis", "cis'", "e'", 3) + " | " + _t("gis", "dis'", "fis'", 4) + " | "
              + _t("gis", "cis'", "e'", 2) + " " + _t("a", "cis'", "fis'", 2) + " | "
              + _t("gis", "b", "e'", 2) + " " + _t("a", "b", "dis'", 2) + " | " + _t("gis", "b", "e'", 4) + " } >>",
        "lh": "<cis, cis>1 | <b,, b,>1 | <a,, a,>2 <fis,, fis,> | <gis,, gis,>2 <gis,, gis,> | <cis, gis, cis>1 | "
              "<bis,, gis, bis,>1 | <cis, cis>2 <fis,, fis,> | <b,, b,>2 <b,, b,> | <e, e>1",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 6?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if you name the key of each exercise before you start, and play every B-sharp and E-natural.",
    "Pass if you can play E Major Morning at sight, and the opening of the Moonlight Sonata after a few days.",
    "When you pass, move on to Unit 6.",
]
