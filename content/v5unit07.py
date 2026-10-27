"""Volume 5, Unit 7: Pedal, clefs and the whole keyboard."""

KEYBOARDS = []


def _q(chord, n, first="", last=""):
    """A chord repeated in eighths: the first with `first` marks, the last with `last`."""
    notes = [chord + "8" + first] + ["q"] * (n - 1)
    if last:
        notes[-1] += last
    return " ".join(notes)


INTRO = [
    "The right pedal (the sustain pedal) keeps every note sounding after the fingers let go. With it the left "
    "hand can play a low bass note and then leap to a chord far above, and the bass still rings. In this volume "
    "the pedal is shown with a bracket under the bass staff: the pedal goes down where the bracket starts, up "
    "where it ends, and a notch in the bracket means 'up and straight down again' at a change of harmony.",
    "With the whole keyboard in use, the hands also borrow each other's clefs: the left hand reads in the "
    "treble clef when it plays above middle C, and the right hand in the bass clef when it goes low.",
]

NEW_IDEAS = [
    ("Pedal brackets", "Down at the start of the bracket, up at its end. At a notch, lift and press again just after "
                       "the new chord sounds, so that the old harmony is cleared without a gap."),
    ("Ped. and *", "Older editions write 'Ped.' for down and an asterisk for up. They mean the same."),
    ("Clef changes", "A small clef in the middle of a line changes the reading for that staff until the next clef. "
                     "Check the clef at the start of every line, too."),
    ("Leaps", "A low bass note followed by a chord in the middle of the keyboard is a leap of an octave or more. "
              "Look ahead, move the hand early, and let the pedal hold the bass."),
    ("Rolled chords", "A wavy line before a chord means: spread it from the bottom up, quickly, like a harp."),
]

EXAMPLES = [
    {"title": "Pedal changes with the harmony",
     "text": "Down on beat 1; at each new bar the bracket has a notch: up and down again.",
     "time": "3/4",
     "rh": "a'2. | b'2. | a'2. \\bar \"||\"",
     "lh": "d,4\\sustainOn a, fis | g,4\\sustainOff\\sustainOn d b | d,4\\sustainOff\\sustainOn a, fis\\sustainOff"},
    {"title": "The left hand in the treble clef",
     "text": "Both hands read the treble clef while the left hand plays above middle C; the clef sign changes it back.",
     "time": "4/4",
     "rh": "e''4 f'' g'' a'' | g''1 \\bar \"||\"",
     "lh": "\\clef treble c'8 g' d' g' e' g' f' g' | \\clef bass c4 g, c2"},
]

TIPS = [
    "Before you play, find every clef sign in the music, not only at the start of the lines.",
    "Pedal with the harmony: change it when the bass note changes, just after the new note sounds.",
    "For a leap, look at the landing chord before you leave the bass note.",
    "Keep the pedal foot's heel on the floor and use the ball of the foot.",
]

PART_NOTES = {
    "A": "Wide broken chords in the left hand (root, fifth, tenth): the pedal holds them. Change the pedal with "
         "each new chord.",
    "B": "Low bass note, then a chord in the middle of the keyboard (the Gymnopedie pattern), with the pedal.",
    "C": "The hands take turns; the left hand sometimes reads the treble clef and the right hand the bass clef. "
         "Watch the clef signs.",
}

PIECES = [
    {
        "title": "Pedal Song", "credit": "Original", "meter": "3/4", "tempo": 66, "key": "d \\major",
        "note": "The left hand spreads each chord over a tenth (bass, fifth, third an octave higher); the pedal "
                "holds it. Change the pedal at the start of every bar.",
        "rh": "a'2\\p d''4 | b'2 d''4 | cis''2 e''4 | d''2. | \\break fis''2\\< d''4 | g''4\\mf d'' b' | "
              "cis''4\\> e'' g'' | fis''2.\\p",
        "lh": "d,4\\sustainOn a, fis | g,4\\sustainOff\\sustainOn d b | a,4\\sustainOff\\sustainOn e cis' | "
              "d,4\\sustainOff\\sustainOn a, fis | b,,4\\sustainOff\\sustainOn fis, d | g,4\\sustainOff\\sustainOn d b | "
              "a,4\\sustainOff\\sustainOn e g | <d, a, d>2.\\sustainOff\\sustainOn",
    },
    {
        "title": "Little Piece", "credit": "Robert Schumann (1848), Album for the Young, Op. 68 No. 5 - complete",
        "meter": "4/4", "tempo": 80,
        "note": "The left hand plays above middle C all through, so it is written in the treble clef. Its eighths are "
                "two voices: a moving line and a repeated G. Both halves are repeated; each starts with a half-bar "
                "upbeat. Notes retyped from the Mutopia Project engraving no. 653 by Philippe Hezaine (CC BY-SA 2.5).",
        "rh": "\\repeat volta 2 { \\partial 2 e''4\\p( f'' | g''4 a'' d'' e'' | f''2) c''4( d'' | e''4 e'' d'' a' | "
              "c''4 b') e''( f'' | \\break g''4 a'' d'' e'' | f''2) c''4( d'' | e''4 e'' d'' b' | d''4 c'') } "
              "\\repeat volta 2 { b'4( c'' | \\break d''4 e'' c'' d'' | e''2) c''4( d'' | e''4 f'' d'' e'' | "
              "f''4 d'') e''( f'' | \\break g''4 a'' d'' e'' | f''2) c''4( d'' | e''4 e'' d'' b' | d''4 c'') }",
        "lh": "\\clef treble \\repeat volta 2 { \\partial 2 c'8( g' d' g' | e'8 g' f' g' b g' c' g' | d'8 g' d' g') a( g' b g' | "
              "c'8 g' c' g' d' fis' d' fis' | g8 g' g g') c'( g' d' g' | e'8 g' f' g' b g' c' g' | "
              "d'8 g' d' g') a( g' b g' | c'8 g' e' g' f f' g d') | << { f'4( e') } \\\\ { c'2 } >> } "
              "\\repeat volta 2 { g8( g' a g' | b8 g' c' g' a g' b g' | c'8 g' c' g') a( g' b g' | "
              "c'8 g' d' g' b g' c' g' | d'8 g' b g') c'( g' d' g' | e'8 g' f' g' b g' cis' g' | "
              "d'8 g' d' g') a( g' b g' | c'8 g' e' g' f f' g d') | << { f'4( e') } \\\\ { c'2 } >> }",
    },
    {
        "title": "Prelude in A", "credit": "Frederic Chopin (1839), Prelude, Op. 28 No. 7 - complete, one grace note "
                                     "left out",
        "meter": "3/4", "tempo": 60, "key": "a \\major", "upbeat": "1/4", "allow_span": 15,
        "note": "Chopin's own pedal marks: the pedal holds each two-bar phrase. The left hand leaps from a low bass note "
                "to chords in the middle; the right hand plays two-note and three-note chords, and in bar 12 a wide "
                "rolled chord (the wavy line). B-sharp is chromatic. Source: Mutopia Project no. 470 (public domain).",
        "rh": "\\partial 4 e'4( | cis''8. d''16 <d' gis' b'>4 <d' gis' b'> | <d' gis' b'>2) <d'' fis''>4( | "
              "<bis' dis''>8. <cis'' e''>16 <cis'' a''>4 <cis'' a''> | <cis'' a''>2) "
              "<< { <e' cis''>4( | s4 <fis' d''> <fis' d''> | <fis' d''>2) } \\\\ { s4 | <cis' ais'>8. <d' b'>16~ d'2~ | d'2 } >> "
              "<d' gis'>4( | \\break <d' gis'>8. <cis' a'>16 <cis' cis''>4 <cis' cis''> | <cis' cis''>2) "
              "<< { s4 | cis''8. d''16 s4 s | s2 } \\\\ { e'4(~ | <e' gis'>4 <d' gis' b'> <d' gis' b'> | <d' gis' b'>2) } >> "
              "<< { <d'' fis''>4( | \\break s4 <a'' cis'''> <a'' cis'''> | <ais' cis''>2)\\arpeggio } \\\\ "
              "{ s4 | <bis' dis''>8. <cis'' e''>16~ <cis'' e''>2 | <e'' ais'' cis'''>2\\arpeggio } >> <ais' cis''>4( | "
              "<ais' cis''>8. <b' d''>16 <b' fis''>4 <a' fis''> | <gis' fis''>2) "
              "<< { <d' gis'>4( | <d' b'>8. <cis' a'>16 <cis'' a''>4 <cis'' a''> | <cis'' a''>2) } \\\\ "
              "{ s4 | s4 a'2~ | a'2 } >> r4",
        "lh": "\\partial 4 r4\\p | e,4\\sustainOn <e e'> <e e'> | <e e'>2 r4\\sustainOff | a,4\\sustainOn <a e'> <a e'> | "
              "<a e'>2 r4\\sustainOff | e,4\\sustainOn <e b> <e b> | <e b>2 r4\\sustainOff | "
              "a,,4\\sustainOn <e a e'> <e a e'> | <e a e'>2 r4\\sustainOff | e,4\\sustainOn <e e'> <e e'> | "
              "<e e'>2 r4\\sustainOff | a,4\\sustainOn\\< <a e' a'> <a e' a'>\\sustainOff | "
              "<fis cis' e' fis'>2\\sustainOn\\! r4\\sustainOff | b,,4\\sustainOn <fis d'> <fis b d'>\\sustainOff | "
              "<e b d'>2\\sustainOn r4\\sustainOff | a,,4\\sustainOn <e a e'> <a e'> | <a e'>2 r4\\sustainOff",
    },
    {
        "title": "Prelude in E minor", "credit": "Frederic Chopin (1839), Prelude, Op. 28 No. 4 - first half, with a "
                                          "closing chord added",
        "meter": "2/2", "cut": True, "tempo": 60, "key": "e \\minor", "upbeat": "1/4", "allow_leap": 14,
        "note": "The right hand sings a long, slow tune; the left hand repeats soft chords whose notes slide down one "
                "half step at a time. Chopin's pedal marks show where to hold and change. Alla breve, but at this "
                "slow speed count four quarter beats. The grace note in bar 11 is left out, and a final E minor chord "
                "is added. Source: Mutopia Project no. 468 (public domain).",
        "rh": "\\partial 4 b8.\\p( b'16 | b'2. c''4 | b'2. c''4 | b'2. c''4 | b'2. bes'4 | \\break a'2. b'4 | a'2. b'4 | "
              "a'2. b'8. a'16 | a'2.) gis'4->(~ | \\break gis'4 a'8 b' d''\\> c'' e' a'\\! | fis'2.) a'4( | fis'2.) a'4( | "
              "g'8 fis' c' b dis' fis' \\tuplet 3/2 { d''8 c'' b' } | b'1)",
        "lh": "\\partial 4 r4 | " + " | ".join([
            _q("<g b e'>", 7, "\\sustainOn", "\\sustainOff") + " q",
            _q("<fis a e'>", 4, "\\sustainOn", "\\sustainOff") + " " + _q("<fis a dis'>", 4, "\\sustainOn", "\\sustainOff"),
            _q("<f a dis'>", 4, "\\sustainOn", "\\sustainOff") + " <f a d'>8 q <f gis d'> q",
            _q("<e gis d'>", 4, "\\sustainOn", "\\sustainOff") + " <e g d'>8 q <e g cis'> q",
            _q("<e g c'>", 4, "\\sustainOn", "\\sustainOff") + " " + _q("<e fis c'>", 4),
            _q("<e fis c'>", 4, "\\sustainOn", "\\sustainOff") + " " + _q("<dis fis c'>", 4, "\\sustainOn", "\\sustainOff"),
            _q("<d fis c'>", 7, "\\sustainOn", "\\sustainOff") + " q",
            _q("<d f c'>", 4, "\\sustainOn", "\\sustainOff") + " " + _q("<d f b>", 4),
            "<c e b>8 q <c e a> q q q q q",
            "<b, e a>8 q <b, dis a> q " + _q("<c e a>", 4, "\\sustainOn", "\\sustainOff"),
            _q("<b, dis a>", 4, "\\sustainOn", "\\sustainOff") + " " + _q("<c e a>", 4, "\\sustainOn", "\\sustainOff"),
            "<b, dis a>4 r4 r2", "<g b e'>1"]),
    },
    {
        "title": "Gymnopedie No. 1", "credit": "Erik Satie (1888), Trois Gymnopedies No. 1 - first half",
        "meter": "3/4", "tempo": 66, "key": "d \\major", "long": True, "allow_span": 14,
        "note": "Slow and sad. In every bar the left hand plays a low bass note on beat 1 and leaps to a chord in the "
                "middle of the keyboard on beat 2; the pedal (changed every bar; Satie left this to the player) "
                "holds the bass. A few four-note chords stretch a ninth: roll them quickly if your hand is small. The key signature has two sharps, but the music hovers between G major, D major and "
                "B minor, with C-natural and F-natural in the second half. Source: Mutopia Project no. 37 (public domain).",
        "rh": "R2. | R2. | R2. | R2. | \\break r4 fis''(\\pp a'' | g''4 fis'' cis'' | b'4 cis'' d'' | a'2. | fis'2.~ | "
              "fis'2.~ | \\break fis'2.~ | fis'2.) | r4 fis''( a'' | g''4 fis'' cis'' | b'4 cis'' d'' | a'2. | \\break "
              "cis''2. | fis''2. | e'2.~ | e'2.~ | e'2.) | a'4( b' c'' | \\break e''4 d'' b' | d''4 c'' b' | d''2.~ | "
              "d''2) d''4( | e''4 f'' g'' | a''4 c'' d'' | \\break e''4 d'' b' | d''2.~ | d''2) d''4 | g''2.( | fis''2. | "
              "b'4 a' b' | \\break cis''4 d'' e'' | cis''4 d'' e'' | fis'2. | <c' e' a' c''>2. | <d' fis' a' d''>2.)",
        "lh": " | ".join(
            [f"<< {{ r4 {c}2 }} \\\\ {{ {b}2.{p} }} >>" for b, c, p in [
                ("g,", "<b d' fis'>", "\\sustainOn"), ("d,", "<a cis' fis'>", "\\sustainOff\\sustainOn"),
                ("g,", "<b d' fis'>", "\\sustainOff\\sustainOn"), ("d,", "<a cis' fis'>", "\\sustainOff\\sustainOn")] * 4
             + [(b, c, "\\sustainOff\\sustainOn") for b, c in [
                ("fis,", "<a cis' fis'>"), ("b,,", "<b d' fis'>"), ("e,", "<g b>"), ("e,", "<b d' g'>"), ("d,", "<f a d'>"),
                ("a,,", "<a c' e'>"), ("d,", "<g b e'>"), ("d,", "<d g b e'>"), ("d,", "<c e a d'>"), ("d,", "<c fis a d'>"),
                ("d,", "<a c' f'>"), ("d,", "<a c' e'>"), ("d,", "<d g b e'>"), ("d,", "<c e a d'>"), ("d,", "<c fis a d'>"),
                ("e,", "<b e' g'>"), ("fis,", "<a cis' fis'>"), ("b,,", "<b d' fis'>"), ("e,", "<cis' e' a'>"),
                ("e,", "<a cis' fis' a'>")]]])
              + " | << { r4 <a d'>4 <b d' g'> } \\\\ { e,2.\\sustainOff\\sustainOn } >> | "
                "<a, g>2.\\sustainOff\\sustainOn | <d, a, d>2.\\sustainOff\\sustainOn",
    },
]

CHECKPOINT_TITLE = "Checkpoint: ready for Unit 8?"
CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if the pedal changes cleanly with the harmony (no blur, no gap) and every clef change is read in time.",
    "Pass if you can play Pedal Song at sight and the first page of the Gymnopedie after a few days.",
    "When you pass, move on to Unit 8, the last unit.",
]
