"""Volume 4, Unit 5: Syncopation."""

KEYBOARDS = []

INTRO = [
    "Most notes so far started on a beat. A syncopated note starts between two beats and holds through the next "
    "one, so the accent falls where you do not expect it. Syncopation gives ragtime, jazz and many dances their "
    "bounce. The secret is to keep the beat completely steady underneath: the syncopation only works against a "
    "beat that does not move.",
]

NEW_IDEAS = [
    ("Eighth, quarter, eighth", "Count 1-and-2-and: the quarter note starts on 'and' and lasts through beat 2. "
                                "Clap it first: short-LONG-short."),
    ("Accents", "The sign > over or under a note means: play it a little louder. In this unit it marks the "
                "syncopated notes."),
    ("Ties over the beat and the bar line", "A note tied over the bar line starts early, on the last 'and' of the "
                                            "bar, and is not played again on beat 1. This 'anticipation' is the "
                                            "sound of ragtime."),
]

TIPS = [
    "Count out loud, with the 'and's, the first few times: 1-and-2-and-3-and-4-and.",
    "Let the left hand play exactly on the beats; the right hand's accents fall between them.",
    "At a tie over the bar line, feel beat 1 in the left hand while the right hand holds.",
]

PART_NOTES = {
    "A": "Right hand alone in C position: syncopated rhythms with accents.",
    "B": "Ragtime in 2/4: a syncopated tune over an oom-pah bass.",
    "C": "G major: notes tied over the bar line, over block chords.",
    "D": "Two voices: a syncopated tune above a steady left hand in half notes.",
}

PIECES = [
    {
        "title": "The Entertainer", "credit": "Scott Joplin (1902), first strain - simplified, note values doubled",
        "meter": "4/4", "tempo": 72, "positions": ["LH_C4"],
        "note": "The most famous ragtime. Joplin wrote it in 2/4 with sixteenth notes; here every note lasts twice as "
                "long, so it reads in 4/4 with eighths. The tune is an octave lower than written and the bass is a "
                "simplified oom-pah. Watch the ties over the bar lines. Source: Mutopia Project no. 263.",
        "rh": "e'8^1\\p c''4->^5 e'8 c''4-> e'8 c''~ | c''2~ c''8 c'' d'' dis'' | e''8 c'' d'' e''~ e'' b' d''4 | "
              "c''2~ c''4 d'8^2 dis'^3 | \\break "
              "e'8^1 c''4->^5 e'8 c''4-> e'8 c''~ | c''2~ c''4 a'8 g' | fis'8 a' c'' e''~ e'' d'' c'' a' | "
              "d''2~ d''4 d'8 dis' | \\break "
              "e'8\\f c''4-> e'8 c''4-> e'8 c''~ | c''2~ c''8 c'' d'' dis'' | e''8 c'' d'' e''~ e'' b' d''4 | c''2~ c''4 r",
        "lh": "c4_5 <e-3 g-1> c <e g> | f <a c'> e <g c'> | g <c' e'> g <f b> | c <e g> c <e g> | "
              "c <e g> c <e g> | f <a c'> e ees | d <fis a c'> d <fis a c'> | <g b>4 g a b | "
              "c <e g> c <e g> | f <a c'> e <g c'> | g <c' e'> g <f b> | c <e g> c2",
    },
    {
        "title": "Ragtime Rabbit", "credit": "Original", "meter": "2/4", "tempo": 84,
        "note": "Eighth-quarter-eighth in nearly every bar, over an oom-pah bass in 2/4. In bar 5 the last note is "
                "tied over the bar line: it starts early and is not played again.",
        "rh": "e'8^3\\mf g'4-> e'8 | d'8 f'4-> d'8 | c'8 e' g' e' | d'2 | \\break "
              "e'8 g'4-> c''8~ | c''8 a'4-> g'8 | f'8 d'4-> b8^1 | c'2",
        "lh": "c4_5 <e-3 g-1> | b,_5 <f-2 g-1> | c_5 <e g> | b,_5 <f g> | c_5 <e g> | c_5 <f-2 a-1> | b,_5 <f g> | <c e g>2",
    },
    {
        "title": "Late for the Train", "credit": "Original", "meter": "4/4", "tempo": 76, "key": "g \\major",
        "note": "Syncopated in G major over steady block chords. Two notes are tied over the bar line (bars 2 and 5).",
        "rh": "b'8^3\\mf d''4-> b'8 g'2 | a'8 c''4-> a'8 fis'4^1 a'8 b'~ | b'4 g'8 d''4-> b'8 g'4 | a'2 a'4 r | \\break "
              "b'8^3 d''4-> b'8 g'4 b'8 c''~ | c''4 a'8 c''4-> a'8 g'4 | a'8\\< c''4-> a'8 fis'4 a' | g'1\\f",
        "lh": "<g,-5 b,-3 d-1>2 <g, b, d> | <fis,-5 c-2 d-1>2 <fis, c d> | <g, b, d>2 <g, b, d> | <fis, c d>2 <fis, c d> | "
              "<g, b, d>2 <g, b, d> | <g,-5 c-2 e-1>2 <g, c e> | <fis, c d>2 <fis, c d> | <g, b, d>1",
    },
]

CHECKPOINT = [
    "Play five new Part B to D exercises at the speeds shown: at most one stop each, 9 notes out of 10 right.",
    "The beat stays steady under every syncopation, and tied notes are not played again.",
    "When you pass, move on to Unit 6.",
]
