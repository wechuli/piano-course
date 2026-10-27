"""Volume 6, Unit 1: Three voices."""

KEYBOARDS = []

INTRO = [
    "Volumes 1-5 taught you to read piano music. This volume teaches you to read music written for anyone: "
    "for three or four independent voices, for a singer and a pianist, for a string quartet, for a band "
    "reading from chord symbols. It starts with the hardest kind of piano music to read at sight: three "
    "voices at once, as in a Bach sinfonia or fugue.",
    "In three-voice music the right hand usually plays two voices on the upper staff and the left hand plays "
    "the bass. But the middle voice goes where it likes: when it comes down, the left hand takes it, and when "
    "it goes up, the right hand takes it back. Read each voice as a line, not as a pile of chords.",
]

NEW_IDEAS = [
    ("Three voices", "Two voices share the upper staff: the top one has stems up, the middle one stems down. The "
                     "bass is alone on the lower staff. Follow each line by its stems and beams; a note held in "
                     "one voice goes on while another voice moves."),
    ("The middle voice changes hands", "When the middle voice comes down near the bass, it is printed on the "
                                       "lower staff (stems up) and the left hand plays it. Look for a run of notes "
                                       "that moves from one staff to the other: it is one line."),
    ("Subject, answer, countersubject", "A fugue starts with one voice alone playing a short tune: the subject. "
                                        "Then a second voice plays it a fifth higher (or a fourth lower): the "
                                        "answer, while the first voice goes on with a counter-tune, the "
                                        "countersubject. Then the third voice plays the subject again. Once you "
                                        "know the subject, you can read every entry at a glance."),
]

EXAMPLES = [
    {"title": "Three voices on two staves",
     "text": "Top voice: stems up. Middle voice: stems down on the same staff. Bass: the lower staff. The top "
             "voice moves while the middle one holds, and the other way round.",
     "time": "4/4",
     "rh": "<< { e''4 d''8 c'' d''4 g'' | f''4 e''2. } \\\\ { c''4 b' a' b' | b'4 c''2. } >>",
     "lh": "c4 g f g | g,4 c2."},
    {"title": "The middle voice changes hands",
     "text": "The middle voice runs down from the right hand into the left hand (stems up on the lower staff) "
             "and comes back up in bar 2. It is one line: play it smoothly across the hands.",
     "time": "4/4",
     "rh": "<< { e''2 d''2 | c''1 } \\\\ { c''8 b' a' g' s2 | s2 g'2 } >>",
     "lh": "<< { s2 f'8 e' d' c' | e'2 s2 } \\\\ { c'2 b2 | c'1 } >>"},
    {"title": "A subject and its answer",
     "text": "The subject of the Fugue in G (the last piece in this unit), then the answer a fourth lower. A real answer "
             "moves every note by the same distance. This one is a tonal answer: the subject's first note, D "
             "(the fifth of G), is answered by G (the tonic), not by A; after that the answer is exact.",
     "staff": "treble", "key": "g \\major", "time": "4/4", "wide": True,
     "rh": "d''4^\\markup \\small \\italic subject g'8 a' b' c'' d'' b' | e''8 d'' c'' b' a'4 d'' \\bar \"||\" "
           "g'4^\\markup \\small \\italic answer d'8 e' fis' g' a' fis' | b'8 a' g' fis' e'4 a' \\bar \"||\""},
]

TIPS = [
    "Before you play, follow each voice through the first two bars with your eyes: top, middle, bass.",
    "Stems tell you the voice: on the upper staff, stems up are the top voice and stems down the middle voice.",
    "When notes jump from one staff to the other in a beamed group, it is the middle voice changing hands.",
    "In a fugue, learn the subject by heart before you start: every new entry is the same tune.",
    "Keep held notes held. If a held note is hard, shorten it rather than stop the beat.",
]

PART_NOTES = {
    "A": "Three voices: the right hand plays a tune and a middle voice on the upper staff, the left hand a bass. "
         "Four bars. C, G, F major and D minor.",
    "B": "The middle voice changes hands: in some bars it is on the upper staff (right hand), in others on the "
         "lower staff (left hand). Eight bars.",
    "C": "Fugue entries: the subject in the top voice (bars 1-2), the answer in the middle voice (bars 3-4) with "
         "the countersubject above it, a one-bar link, then the subject in the bass (bars 6-7) and the closing "
         "chord. The first four exercises label each entry; find them yourself in the others.",
}

PIECES = [
    {
        "title": "Sinfonia No. 1", "credit": "J. S. Bach, Sinfonia No. 1 in C, BWV 787 - bars 1-6, with a closing chord",
        "meter": "4/4", "tempo": 60, "allow_32": True,
        "note": "The top voice opens with a rising scale; in bar 2 the middle voice imitates it, starting in the "
                "left hand (stems up on the lower staff) and moving up into the right hand. In bar 6 the middle "
                "voice runs down into the left hand again and stays there. The bass imitates the scale in bars "
                "3-5. The excerpt ends with a C major chord in place of Bach's bar 7. Source: Mutopia Project "
                "no. 142 (public domain).",
        "rh": "<< { r16 g' a' b' c'' d'' e'' f'' g'' f'' g'' a'' f'' a'' g'' f'' | e''2~ e''4 fis'' | "
              "g''8 f''! e''4 d''8 e''16 f'' d''4~ | \\break d''8 g''16 f'' e''4~ e''8 e'' d''4~ | "
              "d''4. c''8~ c'' b'16\\prall a' b' c'' d'' b' | g'4~ g'16 c'' d'' e'' a' b' a' b' b'8.\\prall a'32 b' | "
              "c''1\\fermata } \\\\ "
              "{ r1 | r16 \\change Staff = \"down\" \\stemUp c' d' e' \\change Staff = \"up\" \\stemDown f' g' a' b' "
              "c'' b' c'' d'' c'' e'' d'' c'' | b'8 d''~ d'' c''~ c''4 b'~ | b'4 r16 d'' c'' b' a'4. a'8 | "
              "g'8 f' e'4 d'2~ | d'16 f' e' d' \\change Staff = \"down\" \\stemUp c' b a g f g f e f d e f | "
              "e1 } >>",
        "lh": "c4 r8 c' b g a b | \\stemDown c'4 \\stemNeutral r8 b a g a d | "
              "g,16 g a b c' d' e' f' g' f' g' a' f' a' g' f' | e'16 f' e' d' c' b a g f g f e f d e f | "
              "e16 g, a, b, c d e f g f g a f a g f | \\stemDown e2~ e4 d | c1\\fermata",
    },
    {
        "title": "Sinfonia No. 11", "credit": "J. S. Bach, Sinfonia No. 11 in G minor, BWV 797 - bars 1-16",
        "meter": "3/8", "tempo": 50, "tempo_unit": "4.", "key": "g \\minor", "allow_32": True,
        "note": "Three voices in 3/8, one beat in a bar. The top voice starts with a broken G minor chord; one bar "
                "later the middle voice copies it a fourth lower, and in bar 8 the bass, two octaves lower. Each time the broken "
                "chord runs down, its lowest note may be printed on the lower staff: the left hand takes it. In "
                "bar 12 that note is the C the left hand is already holding. Bar 9 has a short trill on B "
                "(the zig-zag sign: alternate B and C quickly), finished by two thirty-second notes. The excerpt ends in B-flat major, where "
                "Bach's first phrase closes. Source: Mutopia Project no. 200 (public domain).",
        "rh": "<< { r16 d'' bes' g' g''8 | f''4. | ees''4. | d''4. | \\break c''4 d''8 | bes'8. bes'16 ees''8 | "
              "a'8. bes'16 c''8 | bes'4. | \\break b'4\\prallprall~ b'16 a'32 b' | c''8. d''16 ees''8~ | "
              "ees''16 d'' b' g' f''8 | ees''4.~ | \\break ees''8. d''16 c''8~ | c''16 f'' d'' bes' bes''8 | "
              "d''8. ees''16 c''8 | bes'4.\\fermata } \\\\ "
              "{ r4. | r16 a' f' \\change Staff = \"down\" \\stemUp d' \\change Staff = \"up\" \\stemDown d''8~ | "
              "d''8. bes'16 c''8~ | c''8. a'16 bes'8 | a'4.~ | a'16 fis' g'4~ | g'4 fis'8 | g'4. | "
              "r16 d' b \\change Staff = \"down\" \\stemUp g \\change Staff = \"up\" \\stemDown g'8~ | g'4. | "
              "f'4 \\change Staff = \"down\" \\stemUp d'8 \\change Staff = \"up\" \\stemDown | "
              "r16 g' ees' \\change Staff = \"down\" \\stemUp c' \\change Staff = \"up\" \\stemDown bes'!8 | "
              "a'4. | f'8. bes'8.~ | bes'4 a'8 | bes'4. } >>",
        "lh": "\\stemDown g4 ees8 | d4 bes8 | g4 a8 | bes16 d' bes g g'8~ | g'8. e'16 fis'8 | g'4 c'8 | d'4 d8 | "
              "g16 d bes, g, g8 | f!4. | ees16 g ees c c'8~ | c'4 b8 | c'4.~ | c'16 c' a f ees'8 | d'8. g'16 ees'8 | "
              "f'4 f8 | bes16 f d bes,8.\\fermata",
    },
    {
        "title": "Fugue in C minor", "credit": "J. S. Bach, The Well-Tempered Clavier I, Fugue in C minor, BWV 847 - "
                                         "bars 1-8, with a closing chord",
        "meter": "4/4", "tempo": 60, "key": "c \\minor",
        "note": "The exposition of a famous fugue. The alto plays the subject alone (bars 1-2); the soprano answers "
                "it a fifth higher (bars 3-4), a tonal answer: the subject's leap down to G becomes a leap down to C, while the alto plays the countersubject in the left hand, in the "
                "treble clef. Bars 5-6 are an episode built from the subject's first notes. In bar 7 the bass "
                "enters with the subject and the alto comes back to the right hand. The closing chord (with the "
                "bass falling from E-flat to C) is added here; Bach's fugue goes on. Source: Mutopia Project no. "
                "1941 (Creative Commons Attribution-ShareAlike 4.0, typeset by Urs Metzger).",
        "rh": "<< { R1 | R1 | r8 g''16 fis'' g''8 c'' ees'' g''16 fis'' g''8 a'' | \\break "
              "d''8 g''16 fis'' g''8 a'' c''16 d'' ees''4 d''16 c'' | bes'8 ees''16 d'' ees''8 g' aes' f''16 ees'' f''8 a' | "
              "\\break bes'8 g''16 f'' g''8 b' c'' d''16 ees'' f''4~ | f''8 ees''16 d'' c'' bes' aes' g' f'8 aes'' g'' f'' | "
              "\\break ees''8 d'' ees'' f'' b' c'' d'' b' | c''1\\fermata } \\\\ "
              "{ r8 c''16 b' c''8 g' aes' c''16 b' c''8 d'' | g'8 c''16 b' c''8 d'' f'16 g' aes'4 g'16 f' | s1*4 | "
              "c''4 r r8 f'' ees'' d'' | r8 aes' g' f' g' f'16 ees' f'8 d' | g'4 ees'2. } >>",
        "lh": "R1 | R1 | \\clef treble ees'16 c'' b' a' g' f' ees' d' c'8 ees'' d'' c'' | "
              "bes'8 a' bes' c'' fis' g' a' fis' | g'4 r16 c' d' ees' f' g' aes'8~ aes'16 d' ees' f' | "
              "g'16 a' bes'8~ bes'16 ees' f' g' aes' g' f' ees' d'8 c''16 b' | "
              "\\clef bass r8 c'16 b c'8 g aes c'16 b c'8 d' | g8 c'16 b c'8 d' f16 g aes4 g16 f | ees4 c2.\\fermata",
    },
    {
        "title": "Fugue in G", "credit": "Original, written for this book",
        "meter": "4/4", "tempo": 60, "key": "g \\major",
        "note": "A small fugue made with the rules of Part C. The soprano plays the subject (bars 1-2); the alto "
                "answers it a fourth lower with a tonal answer: the subject's first note, D, is answered by G "
                "(see the example in this unit), while the soprano plays the countersubject. Bar 5 is a short "
                "episode in D major. In bar 6 the bass plays the subject two octaves lower, and bars 8-9 close "
                "in G.",
        "rh": "<< { d''4 g'8 a' b' c'' d'' b' | e''8 d'' c'' b' a'4 d'' | b'2 a'4 d'' | \\break "
              "g''8 fis'' e'' d'' cis'' d'' e'' cis'' | fis''8 e''16 d'' e''8 a' d'' c''16 b' c''8 a' | "
              "b'8 a'16 g' a'8 b' g'4 d'' | \\break e''4. c''8 fis'' e'' d'' b' | c''8 e'' g'' e'' a''4 fis'' | "
              "g''1\\fermata } \\\\ "
              "{ r1 | r1 | g'4 d'8 e' fis' g' a' fis' | b'8 a' g' fis' e'4 a' | a'4 fis'8 g' a'4 fis' | "
              "d'4. c'8 d'4 g' | c''8 b' a' g' fis' g' a'4 | g'4 c'' a' c'' | b'1 } >>",
        "lh": "R1 | R1 | R1 | R1 | R1 | d4 g,8 a, b, c d b, | e8 d c b, a,4 d | e8 d c e d c b, a, | g,1\\fermata",
    },
]

CHECKPOINT_TITLE = "Checkpoint"
CHECKPOINT = [
    "Play two exercises from Part C a day for a week: name each entry (subject, answer, subject in the bass) "
    "before you play, then play without stopping.",
    "Pass if you can play the Fugue in G and Part B's exercises at sight, steadily, with every held note held, "
    "and Sinfonia No. 1 after a few days.",
]
