"""Volume 6, Unit 3: Changing meters, modes and no key."""

KEYBOARDS = []

INTRO = [
    "So far every piece has kept one time signature from start to finish, and its key signature has told you "
    "the key. Many composers since 1870 do neither: the time signature changes every bar or two, bars of 5 or 7 "
    "beats appear, the music uses an old mode or a scale with no key at all, and sometimes there are no bar "
    "lines.",
    "Reading this music means trusting the page bar by bar: look at each new time signature as it comes, count "
    "the beat groups that the beams show, and read every accidental as written.",
]

NEW_IDEAS = [
    ("Changing time signatures", "A new time signature is printed only when the meter changes; it lasts until "
                                 "the next one. Keep the quarter (or eighth) the same speed: only the number of "
                                 "beats in the bar changes. 5/4 is usually 3 + 2 beats, 6/4 is 3 + 3."),
    ("7/8 and 5/8", "In 7/8 the eighth is the unit and the bar has three uneven beats, shown by the beams: "
                    "2 + 2 + 3 (count \"one-two, one-two, one-two-three\"). 5/8 is 3 + 2 or 2 + 3. The long beat "
                    "is the one with three eighths."),
    ("Modes", "A mode uses the notes of a major scale but makes a different note the home note. Dorian (D to D on "
              "the white keys) is a minor scale with a raised 6th; Mixolydian (G to G) a major scale with a "
              "lowered 7th; Phrygian (E to E) a minor scale with a lowered 2nd; Lydian (F to F) a major scale "
              "with a raised 4th. Modal music is often printed without a key signature: find the home note from "
              "the bass and the last note."),
    ("Whole-tone and pentatonic scales", "The pentatonic scale has five notes (C D E G A: no half steps); the "
                                         "whole-tone scale has six notes a whole step apart (C D E F-sharp "
                                         "G-sharp A-sharp). Both float without a strong pull home."),
    ("Music without bar lines", "With no time signature and no bar lines, read in phrases: dotted bar lines (or "
                                "none) mark where a phrase ends. Keep a steady quarter beat; an accidental lasts "
                                "until the next bar line, so in unbarred music it may last a long time."),
]

EXAMPLES = [
    {"title": "5/4 and 6/4",
     "text": "The quarter note stays the same speed; the bars alternate between five beats (3 + 2) and six (3 + 3).",
     "time": "5/4", "key": "bes \\major", "wide": True,
     "rh": "f'4 g' bes' a'2 | \\time 6/4 c''2. bes'2. | \\time 5/4 d''4 c'' bes' a'2 | \\time 6/4 bes'1.",
     "lh": "bes,2. <d f>2 | \\time 6/4 f,2. <bes, d>2. | \\time 5/4 bes,2. <c f>2 | \\time 6/4 <bes, d f>1."},
    {"title": "7/8 as 2 + 2 + 3",
     "text": "The beams show the beat groups: two short beats and a long one. Count \"one-two, one-two, one-two-three\".",
     "time": "2,2,3 7/8", "key": "a \\minor", "wide": True,
     "rh": "a'8 b' c'' d'' e''4. | d''8 c'' b' a' gis'4. | a'2..",
     "lh": "a,4 <c e> <c e>4. | e,4 <gis d'> <gis b>4. | <a, e>2.."},
    {"title": "D Dorian, without a key signature",
     "text": "The white keys from D to D. It sounds minor (F is a minor third above D), but B, the 6th, is raised. "
             "The bass and the final note tell you the home note is D.",
     "staff": "treble", "wide": True,
     "rh": "d'4 e' f' g' a' b' c'' d''2"},
    {"title": "Pentatonic and whole-tone scales",
     "text": "The pentatonic scale on C (five notes, no half steps), then the whole-tone scale on C (six notes, all a "
             "whole step apart), written without bar lines.",
     "staff": "treble", "wide": True,
     "rh": "\\cadenzaOn c'4 d' e' g' a' c''2 \\bar \"||\" c'4 d' e' fis' gis' ais' c''2 \\bar \"|.\""},
]

TIPS = [
    "Before you play, find every time signature in the exercise and say the beat groups aloud.",
    "Keep the short note value (quarter or eighth) at one speed through every change of meter.",
    "With no key signature, look at the bass and the last note to find the home note, then name the mode.",
    "In unbarred music, read in phrases and breathe at the dotted bar lines.",
    "An accidental lasts until the next bar line: in unbarred music, look back for the last one.",
]

PART_NOTES = {
    "A": "Changing meters: bars of 5/4 and 6/4 alternating (as in Mussorgsky's Promenade), alternating with "
         "exercises in which 3/4 and 2/4 bars mix. The left hand plays the beat groups: a bass note for the first "
         "group, the chord for the others.",
    "B": "7/8 (2 + 2 + 3) and 5/8 (3 + 2), alternating with tunes in the modes printed without a key signature: "
         "A Dorian, D Mixolydian, E Phrygian and F Lydian. Name the mode's home note before you play.",
    "C": "Without bar lines: pentatonic tunes over an open fifth, and whole-tone tunes over a major third. Dotted "
         "bar lines end the phrases.",
}

PIECES = [
    {
        "title": "Promenade", "credit": "Modest Mussorgsky (1874), Pictures at an Exhibition: Promenade - bars 1-6, "
                                        "with a closing chord",
        "meter": "5/4", "tempo": 92, "key": "bes \\major",
        "note": "The time signature changes every bar: 5/4, 6/4, 5/4 ... Keep the quarter note steady. The tune "
                "starts alone, like a soloist, and the whole group answers in chords (bars 3-4); then the solo "
                "and the answer come again. Mussorgsky's direction: \"in the Russian manner, not fast\". The left "
                "hand plays in octaves. In bars 3-4 a low C under the right hand's first quarter is left out (it is "
                "out of reach of one hand). Source: Mutopia Project no. 475 (public domain).",
        "rh": "g'4-- f'-- bes'-- c''8( f'' d''4) | \\time 6/4 c''8( f'' d''4) bes' c'' g' f' | "
              "\\time 5/4 <bes d' g'>4 <a c' f'> <bes d' bes'> << { c''8( f'' d''4) } \\\\ { a'4 <f' a'> } >> | "
              "\\break \\time 6/4 << { c''8( f'' d''4) } \\\\ { a'4 <f' bes'> } >> <d' g' bes'>4 <e' g' c''> <g c' g'> <a c' f'> | "
              "\\time 5/4 f'4-- g'-- d'-- f'8( g' c'4) | \\time 6/4 g'8( a' f'4) <f' f''>4 <f' d''> << { c''8( bes' f'4) } \\\\ { f'4 f' } >> | "
              "\\time 5/4 <bes d' f'>2. r2\\fermata",
        "lh": "R4*5 | \\time 6/4 R1. | \\time 5/4 <g, g>4 <a, f> <g, g> <f, f> <d, d> | "
              "\\time 6/4 <f, f>4 <bes, bes> <g, g> <c, c> <e, e> <f, f> | \\time 5/4 R4*5 | "
              "\\time 6/4 r4 r <f, f> <bes, bes> <g, g> <f, f> | \\time 5/4 <bes,, bes,>2. r2\\fermata",
    },
    {
        "title": "Dance in Seven", "credit": "Original, written for this book",
        "meter": "7/8", "tempo": 176, "tempo_unit": "8", "key": "a \\minor",
        "note": "A dance in 7/8, grouped 2 + 2 + 3 in every bar: the beams show the groups, and the left hand plays a "
                "bass note on the first group and chords on the other two. The long third beat gives the dance its "
                "limp. Count \"one-two, one-two, one-two-three\" before you start.",
        "rh": "\\time 2,2,3 7/8 a'8-> b' c'' d'' e''4. | d''8 c'' b' a' gis'4. | a'8-> c'' e'' a'' g''4. | "
              "f''8 e'' d'' c'' b'4. | \\break c''8-> d'' e'' c'' a'4. | d''8 e'' f'' d'' b'4. | "
              "c''8 b' a' b' gis'4. | a'2..",
        "lh": "\\time 2,2,3 7/8 a,4 <c e> <c e>4. | e,4 <gis d'> <gis b>4. | a,4 <c e> <c e>4. | "
              "d4 <f a> <e gis b>4. | a,4 <c e> <c e>4. | d4 <f a> <f a>4. | e,4 <gis d'> <gis b>4. | <a, e>2..",
    },
    {
        "title": "Gnossienne No. 1", "credit": "Erik Satie (1890), Gnossienne No. 1 - the first theme",
        "tempo": 60, "key": "c \\major",
        "note": "No time signature and no bar lines: read in phrases, keeping a slow, even quarter beat. Every phrase "
                "starts after a rest and the tune is full of grace notes (play them quickly, just before the beat). "
                "The left hand plays a low F and then a chord, again and again, with the pedal (it changes when the "
                "bass changes); count four slow beats for each bass note. An accidental lasts until the end of the "
                "line here: watch the B (natural) and the E (natural and flat). Notes retyped from the Mutopia "
                "Project engraving no. 2035 (Creative Commons Attribution-ShareAlike 4.0).",
        "rh": "\\cadenzaOn r4 c''8([ ees''] d''4 c'' \\grace c''8 b'2 \\grace c''8 b'2) "
              "r4 c''8([ ees''] d''4 c'' \\grace e''8 f''2 \\grace e''8 f''2) \\break "
              "r4 c''8([ ees''] d''4 c'' \\grace c''8 b'2 \\grace aes'8 g'2 "
              "\\grace f'8 g'4 \\grace f'8 g'2~ g'8) r \\break "
              "\\grace aes'8 g'4( \\grace g'8 f'4~ f'2~ f'1)\\fermata \\bar \"|.\"",
        "lh": "\\cadenzaOn << { r4 <aes c' f'>2 <aes c' f'>4 r4 <aes c' f'>2 <aes c' f'>4 r4 <aes c' f'>2 <aes c' f'>4 "
              "r4 <aes c' f'>2 <aes c' f'>4 r4 <aes c' f'>2 <aes c' f'>4 r4 <aes c' f'>2 <aes c' f'>4 "
              "r4 <ees g c'>2 <ees g c'>4 r4 <aes c' f'>2 <aes c' f'>4 r4 <aes c' f'>2 <aes c' f'>4\\fermata } \\\\ "
              "{ f,1\\sustainOn f,1 f,1 f,1 f,1 f,1 c1\\sustainOff\\sustainOn f,1\\sustainOff\\sustainOn f,1\\fermata } >> "
              "\\bar \"|.\"",
    },
    {
        "title": "Scarborough Fair", "credit": "Traditional English ballad, arranged for this book",
        "meter": "3/4", "tempo": 100, "key": "c \\major",
        "note": "A tune in D Dorian, printed without a key signature. It looks like C major, but D is the home note: "
                "the bass starts and ends on it. The Dorian sound comes from B natural, the raised 6th, in bar 7 "
                "(the tune) and in the G major chords. Sing the tune in your head as you play: it is a song.",
        "rh": "d'2\\mp d'4 | a'2 a'4 | e'4. f'8 e'4 | d'2. | r4 a' c'' | d''2 c''4 | a'4 b' g' | a'2. | \\break "
              "r4 r d''\\mf | d''2 d''4 | c''2 a'4 | a'4 g' f' | e'4 c'2 | d'2 a'4 | g'4 f' e' | d'2.\\fermata",
        "lh": "d4 <f a> <f a> | f4 <a c'> <a c'> | c4 <e g> <e g> | d4 <f a>2 | d4 <f a> <f a> | d4 <f a> <f a> | "
              "g,4 <b, d> <b, d> | a,4 <c e> <c e> | d4 <f a> <f a> | f4 <a c'> <a c'> | a,4 <c e> <c e> | "
              "g,4 <b, d> <b, d> | c4 <e g> <e g> | d4 <f a> <f a> | c4 <e g> <e g> | <d, a,>2.\\fermata",
    },
]

CHECKPOINT = [
    "Play two new exercises from each part at the speeds shown, with no more than one stop each.",
    "Pass if every change of meter is counted correctly (the quarter or eighth keeps its speed) and you name the "
    "mode of each Part B exercise before you play.",
    "Pass if you can play the Dance in Seven and Scarborough Fair at sight, and the Promenade after a few days.",
    "When you pass, move on to Unit 4.",
]
