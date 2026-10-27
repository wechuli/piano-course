"""Volume 5, Unit 3: Chromatic notes."""

KEYBOARDS = []

INTRO = [
    "A chromatic note is a note outside the key: a sharp, flat or natural that is not in the key signature. "
    "In this unit they come in three ways: as quick passing and neighbour notes in the tune, as the raised 4th "
    "of a chord that leads to V (V7 of V), and as the raised 6th and 7th of the melodic minor scale.",
]

NEW_IDEAS = [
    ("An accidental lasts to the bar line", "A sharp, flat or natural applies to every later note on the same "
                                            "line or space until the end of the bar. The next bar is back to "
                                            "the key signature. A reminder in the next bar (a 'courtesy' "
                                            "accidental) is only there to help you."),
    ("Chromatic passing notes", "Between two notes a whole step apart, the tune can slip through the half step "
                                "in between: C C-sharp D going up, E E-flat D going down. They are short and "
                                "fall between the beats."),
    ("Chromatic neighbours", "A note can dip to the half step below and come back: E D-sharp E."),
    ("V7 of V", "In C major the chord D F-sharp A C leads strongly to G (V). Its F-sharp is the raised 4th of the "
                "key; in G major it is C-sharp, in F major B-natural. After it, the natural sign cancels it again."),
    ("The melodic minor", "Going up to the tonic, minor tunes often raise the 6th and the 7th (in A minor F-sharp "
                          "and G-sharp); coming down they use the natural notes of the key signature (G and F)."),
]

EXAMPLES = [
    {"title": "Chromatic passing and neighbour notes",
     "text": "C C-sharp D (passing, going up), E E-flat D (passing, going down), E D-sharp E (neighbour). The sharp "
             "in bar 1 does not carry into bar 2.",
     "staff": "treble", "time": "4/4",
     "rh": "c''8 cis'' d''4 e''8 ees'' d''4 | e''8 dis'' e''4 c''2 \\bar \"||\""},
    {"title": "V7 of V in C major, then V and I",
     "text": "D F-sharp A C leads to G B D F, then to C. In V7 the natural sign cancels the F-sharp.",
     "time": "4/4",
     "rh": "<< { a''2 g'' | e''1 } \\\\ { c''2 b' | g'1 } >> \\bar \"||\"",
     "lh": "<d fis>2 <g, f> | <c e>1"},
    {"title": "A melodic minor, up and down",
     "text": "Up: F-sharp and G-sharp. Down: G and F, as in the key signature.",
     "staff": "treble", "time": "4/4",
     "rh": "a'8 b' c'' d'' e'' fis'' gis'' a'' | a'' g'' f'' e'' d'' c'' b' a' \\bar \"||\""},
]

TIPS = [
    "Scan for accidentals before you play, and decide which notes they change for the rest of the bar.",
    "A chromatic passing note always moves on in the same direction by a half step: let your finger slide.",
    "In minor keys, expect the raised 7th whenever the music leans towards the tonic.",
    "After a bar full of sharps, check the next bar: the key signature is back.",
]

PART_NOTES = {
    "A": "C, G and F major: chromatic passing notes (between two notes a whole step apart) and lower neighbours, "
         "always on the second half of a beat.",
    "B": "V7 of V comes before V: listen for F-sharp in C major, C-sharp in G major and B-natural in F major.",
    "C": "A, D and E minor with the melodic minor: raised 6th and 7th going up, natural notes coming down.",
}

PIECES = [
    {
        "title": "Chromatic Walk", "credit": "Original", "meter": "4/4", "tempo": 76,
        "note": "D-sharp and C-sharp are chromatic neighbour and passing notes. In bars 3 and 7, V7 of V brings "
                "F-sharp into both hands; the natural sign on F in bar 7 cancels it.",
        "rh": "e''4\\mp dis''8( e'') g''4 e'' | c''4 cis''8( d'') e''2 | fis''4 e''8( d'') c''4 a' | b'2 d'' | \\break "
              "e''4 dis''8( e'') g''4 e'' | f''4\\< a''8( g'') f''4 c'' | a''4\\mf fis''8( g'') f''4 d'' | e''2 c''",
        "lh": "c4 <e g> g, <e g> | c4 <e g> g, <e g> | d4 <fis c'> a, <fis c'> | g,4 <b d'> d <b d'> | "
              "c4 <e g> g, <e g> | f,4 <a c'> c <a c'> | d4 <fis c'> g, <f b> | <c e g>1",
    },
    {
        "title": "Up the Melodic Minor", "credit": "Original", "meter": "4/4", "tempo": 72, "key": "a \\minor",
        "note": "Going up (bars 2 and 6) the tune uses F-sharp and G-sharp; coming down (bar 3) it uses G and F "
                "from the key signature. The left hand's G-sharp belongs to the E major chord (V).",
        "rh": "a'4\\p c'' e''2 | e''8\\<( fis'' gis'' a'') b''2\\mf | a''8\\>( g'' f'' e'') d''4 c'' | b'2\\p e' | \\break "
              "a'4 c'' e''2 | e'8\\<( fis' gis' a') b'4\\! c'' | d''8( c'' b' a') gis'4 b' | a'1",
        "lh": "a,4 <c e> e, <c e> | a,4 <c e> e, <gis, b,> | a,4 <c e> d <f a> | e,4 <gis, b,> e, <gis, b,> | "
              "a,4 <c e> e, <c e> | a,4 <c e> e, <gis, b,> | d4 <f a> e, <gis, d> | <a, c e>1",
    },
    {
        "title": "First Loss", "credit": "Robert Schumann (1848), Album for the Young, Op. 68 No. 16 - first part",
        "meter": "2/4", "tempo": 66, "key": "e \\minor", "upbeat": "1/8", "allow": ["clef changes"], "allow_leap": 13,
        "note": "D-sharp is the raised 7th of E minor; the left hand climbs chromatically A, A-sharp, B in bars 6, 7 "
                "and 14-15. The left hand moves into the treble clef for its off-beat chords and back into the bass "
                "clef (watch the clef signs: Unit 7 is about them). Play the whole passage twice. Notes retyped from "
                "the Mutopia Project engraving no. 676 by Philippe Hezaine (CC BY-SA 2.5).",
        "rh": "\\repeat volta 2 { \\partial 8 g''8(\\fp | fis''8 e'' dis'' e'' | b'4.) e''8( | c''4.) e''8( | b'4.) b'8( | "
              "\\break c''8) c''( b' a' | g'8) g'( fis' e') | dis'4.( e'8 | <dis' fis'>4.) g''8(\\fp | \\break "
              "fis''8 e'' dis'' e'' | b'4.) e''8( | c''4.) e''8( | b'4.) b'8( | \\break c''8) c''( b' a' | g'8) g'( fis' e') | "
              "dis'4.( fis'8 | e'4) r8 }",
        "lh": "\\repeat volta 2 { \\partial 8 r8 | R2 | \\clef treble r8 g'8~ <e' g'>4 | r8 a'8~ <e' a'>4 | "
              "r8 g'8~ <e' g'>4 | r8 fis'8( dis' fis') | \\clef bass r8 e'8( a ais) | r8 ais8( b4~ | b8) b( b,) r8 | "
              "R2 | \\clef treble r8 g'8~ <e' g'>4 | r8 a'8~ <e' a'>4 | r8 g'8~ <e' g'>4 | r8 fis'8( dis' fis') | "
              "\\clef bass r8 e'8( a ais) | r8 ais8( b a | <e g>8) e( e,) }",
    },
    {
        "title": "Poor Orphan", "credit": "Robert Schumann (1848), Album for the Young, Op. 68 No. 6 - first part",
        "meter": "2/4", "tempo": 60, "key": "a \\minor", "upbeat": "1/8", "allow": ["clef changes"], "allow_32": True,
        "note": "Two voices in each hand. G-sharp, the raised 7th, is in the right hand; in bar 2 the left hand has "
                "G-natural (the natural minor). The tune in bars 3-4 and 7-8 is in the left hand, which moves into the "
                "treble clef. In bar 2 the F is a thirty-second note: very short, just before the beat. Play the "
                "passage twice. Notes retyped from the Mutopia Project engraving no. 687 by Philippe Hezaine "
                "(CC BY-SA 2.5).",
        "rh": "\\repeat volta 2 { \\partial 8 a'16\\p( b') | <a' c''>8-.( <gis' b'>-. a'-.) a'16( b') | "
              "<a' c''>8-.( <b' d''>-. <c'' e''>-.) e''16.( f''32 | <e'' g''>4 <d'' f''> | b'4.) a'16( b') | \\break "
              "<a' c''>8-.( <gis' b'>-. a'-.) a'16( b') | <a' c''>8-.( <b' d''>-. <c'' e''>-.) e''16.( f''32 | "
              "<e'' g''>4 <d'' f''>) | << { b'8.( c''16 a'8) } \\\\ { gis'4 a'8 } >> }",
        "lh": "\\repeat volta 2 { \\partial 8 r8 | <a e'>8-.( <e d'>-. <a c'>-.) r8 | <a e'>8-.( <g g'>-. <c' g'>-.) r8 | "
              "\\clef treble << { c''4( b'8. a'16 | gis'4.) } \\\\ { c'4 d' | e'4. } >> r8 | "
              "\\clef bass <a e'>8-.( <e d'>-. <a c'>-.) r8 | <a e'>8-.( <g g'>-. <c' g'>-.) r8 | "
              "\\clef treble << { c''4( b'8. a'16) | e'8.( d'16 c'8) } \\\\ { c'4 d' | e'4 a8 } >> }",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 4?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if every accidental is right, including notes later in the same bar, and the key signature returns "
    "in the next bar.",
    "Pass if you can play Chromatic Walk and Up the Melodic Minor at sight, and First Loss after a few days.",
    "When you pass, move on to Unit 4.",
]
