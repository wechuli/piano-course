# Read at Sight — piano sight-reading course (build system)

A print-ready A4 course book, typeset with LilyPond.

## Status (2026-10-27)

| Volume | Status | Book | Contents |
| --- | --- | --- | --- |
| 1 · First Steps | complete | `build/Read at Sight - Volume 1.pdf` (130 pp.) | 10 units, 322 exercises, 39 pieces |
| 2 · Moving Hands | complete | `build/Read at Sight - Volume 2.pdf` (133 pp.) | 10 units, 306 exercises, 35 pieces |
| 3 · Two Voices | complete | `build/Read at Sight - Volume 3.pdf` (159 pp.) | 10 units, 342 exercises, 32 pieces |
| 4 · Patterns and Keys | complete | `build/Read at Sight - Volume 4.pdf` (129 pp.) | 8 units, 272 exercises, 24 pieces |
| 5 · Repertoire Reading | complete | `build/Read at Sight - Volume 5.pdf` (133 pp.) | 8 units, 196 exercises, 35 pieces |

Single units are in `build/units/` (`Read at Sight - VolN - Unit M.pdf`).

**The five-volume course is complete. Next: Volume 6** (Levels 7-8, an extension beyond the
original plan): the full plan is in "Volume 6 plan" below. All five volumes are protected by
`course/check_identical.py` (see "Build"). Volume 5 is described in "Volume 5 (done)" below; the
original plan follows it for reference.

Note: the Volume 1 PDFs were built before two small layout tweaks (the "What is new" heading
now stays with its first item, and keyboards widen to fit every key). Rebuilding Volume 1
would only change the page layout; exercises are identical.

## Five-volume plan

| Volume | Levels | Main new skills | Units |
| --- | --- | --- | --- |
| 1 · First Steps (done) | 0–1 | Both clefs, C/G/middle-C positions, hands together, rests and ties, eighths, D and F positions | 10 |
| 2 · Moving Hands (done) | 2 | Leaving five-finger positions, hand shifts and extensions, 1 sharp or flat keys and their relative minors, dotted quarters, slurs, simple dynamics | 10 |
| 3 · Two Voices (done) | 3 | Real left-hand independence, Alberti and broken-chord basses, 6/8, keys up to 2 sharps or flats, simple counterpoint | 8–10 |
| 4 · Patterns and Keys (done) | 4 | Chords in both hands, syncopation, sixteenths, ledger lines, changing key mid-piece | 8 |
| 5 · Repertoire Reading (done) | 5–6 | 3–4 voices, chromatic notes, all keys, chorales | 8 |
| 6 · Reading Like a Professional (planned) | 7–8 | Three-voice counterpoint, cross-rhythms, changing meters, chromatic harmony, big textures, accompanying, open score and C clefs, lead sheets | 8 |

Volumes 1–2 are mostly generated exercises. Volumes 3–4 are about half generated, half
re-engraved public-domain pieces. Volume 5 is mostly re-engraved repertoire.

## Volume 3 (done)

| Unit | Title | Keys and time | Generator features |
| --- | --- | --- | --- |
| 1 | Broken Chords | C, G, F; 4/4, 3/4 | `chords`, `bass: "broken"`, `chord_fingers`, `require_chords` |
| 2 | The Alberti Bass | C, G, F; 4/4, 3/4 | `bass: "alberti"`, `bass_leap` |
| 3 | Six-Eight Time | C, G, F; 6/8 | meter `"6/8"`, `R68`, `bass: "lilt"` and 6/8 `"broken"`, `tempo_unit` |
| 4 | D Major | D; 4/4, 3/4, 6/8 | RH shifts D/A position, thumb stretch to C-sharp |
| 5 | B-flat Major | B-flat; 4/4, 3/4 | positions `RH_Bb`, `LH_Bb`, `KEY_BB` |
| 6 | Accidentals | A, E, B, G minor | `minor`, `beat_tones`, `lead_weight`; positions `RH_Bm`, `LH_Bm`, `RH_Gm`, `LH_Gm` |
| 7 | Two Notes at Once | C, F, D | `dyads` (RH thirds and sixths) |
| 8 | Two Independent Voices | C, G, F | mode `"duet"`, `lead`, `counter_rhythms`, `counter_motion` |
| 9 | Imitation | C, G, F, D | mode `"imitate"` |
| 10 | Review | D, B-flat, B minor, G, B-flat | all of the above |

Pieces: 11 of the 32 are public-domain tunes (Ode to Joy, Jingle Bells, Twinkle Twinkle, Row Row
Row Your Boat, Silent Night, Lightly Row, Au clair de la lune, Greensleeves, London Bridge, Frère
Jacques, plus Ode to Joy in two voices); the rest are originals. Only melodies whose notes are
certain were used, so Volume 4 should lean more on transcriptions from verified sources such as
Mutopia.

Sixths: in a five-finger position (even with a one-key stretch) a sixth fits only over IV, because
the other places would double the bass's leading note. Generated exercises therefore have mostly
thirds; the Unit 7 pieces practise sixths.

## Volume 4 (done)

Level 4: chords in both hands, accompaniment patterns, ledger lines, syncopation, sixteenths,
keys with three sharps or flats, and changing key. 2/4 time is new (from Unit 2). Seeds 4001-4008.
Unit 8 doubles as the review of the volume.

| Unit | Title | Keys and time | Generator features |
| --- | --- | --- | --- |
| 1 | Block Chords | C, G, F, D; 4/4, 3/4 | `bass: "block"`, `"oompah"`, `"waltz"` (LH three-note chords) |
| 2 | Chords in Both Hands | C, G, F, B-flat; 4/4, 2/4, 3/4 | `rh_chords`, `bass: "block2"` (chorale), meter `"2/4"` with `R24` |
| 3 | High Notes | C, G, D; 4/4, 2/4 | positions `RH_C5`, `RH_G5`, `RH_D5`; octave moves; 2/4 `broken` and `alberti` |
| 4 | Low Notes and the Middle | C, F; 4/4 | positions `LH_C2`, `LH_F2`, `RH_A3`, `LH_C4`; mode `"lhtune"` with `accomp: "afterbeat"` |
| 5 | Syncopation | C, G, F; 4/4, 2/4 | `R44["synco"]`, `R24["synco24"]`, `anticip_prob`, `accents` |
| 6 | Sixteenth Notes | C, G, F; 2/4, 4/4 | `grid: 2`, `R24_16`, `R44_16`, `fast_steps` |
| 7 | Three Sharps and Three Flats | A, E-flat, F-sharp minor, C minor | `KEY_A`, `KEY_EB`, `KEY_FSM`, `KEY_CM` and their positions |
| 8 | Changing Key | C to G, F to D minor, G to D to G; review in E-flat 2/4 | `modulate` |

Pieces: 11 of the 24 are public-domain music transcribed from Mutopia engravings (each `.ly`
downloaded and rendered to check the notes); the rest are originals. Where an engraving is
CC BY-SA, only the notes were retyped and the source is named in the piece's note.

| Unit | Piece | Mutopia id | Changes |
| --- | --- | --- | --- |
| 1 | Burgmüller, La Candeur, Op. 100 No. 1 (opening) | 202 | RH an octave lower, last two bars simplified |
| 2 | Tchaikovsky, Morning Prayer, Op. 39 No. 1 (opening and close) | 2032 | LH an octave higher; bars 5-8 shorten the rest of the piece |
| 3 | Schumann, Humming Song, Op. 68 No. 3 (first section) | 651 | LH an octave lower |
| 3 | Mozart, Sonata K. 545, first movement (opening) | 998 | LH an octave lower, quick notes of bars 2 and 4 simplified |
| 4 | Schumann, The Happy Farmer, Op. 68 No. 10 (first part) | 659 | upbeat left out, bars 3 and 7 share a chord |
| 5 | Joplin, The Entertainer (first strain) | 263 | note values doubled (4/4), RH an octave lower, oom-pah bass |
| 6 | Bach notebook, Musette in D, BWV Anh. 126 (first part) | 79 | none |
| 6 | Schumann, Soldiers' March, Op. 68 No. 2 (first part) | 650 | bars 7-8 taken from the end of the second phrase |
| 7 | Bach notebook, Minuet in C minor, BWV Anh. 121 (first part) | 1613 | trill left out |
| 8 | Petzold (attr.), Minuet in G minor, BWV Anh. 115 (first part) | 76 | ornaments left out |
| 8 | Tchaikovsky, Old French Song, Op. 39 No. 16 (opening) | 2080 | inner voices left out, bar 8 rhythm simplified |

Changes from the plan: Soldiers' March moved from Unit 2 to Unit 6 (its dotted rhythms are
sixteenths); Clementi Op. 36 No. 1, Mozart K. 331 and the Minuet in G (Anh. 116) were dropped
were not used; Unit 3 reaches D6 (the plan said C6). Unit 8 has three
pieces, so the volume has 24 pieces rather than about 28.

## Volume 5 (done)

Level 5-6: reading by key, chord and pattern. Seeds 5001-5008. Volume 5 has its **own generator,
`course/gen5.py`** (the plan put the features into `generator.py`; a separate module guarantees that
Volumes 1-4 cannot change). `build.py` uses it for `--vol 5` only.

| Unit | Title | Parts |
| --- | --- | --- |
| 1 | Two Voices in One Hand | A: held RH voice, C/G, block chords. B: the same in 3/4, F/D, waltz. C: LH bass + tenor line, G/F/B-flat |
| 2 | Chorales | A: three voices in half notes. B: SATB with fermatas, inversions, ii and vi. C: SATB in A, D, E minor |
| 3 | Chromatic Notes | A: chromatic passing and neighbour notes. B: V7 of V. C: melodic minor |
| 4 | Triplets and New Time Signatures | A: triplets in 4/4 and 3/4. B: 3/8 and 9/8. C: 2/2 and 12/8 |
| 5 | Four Sharps and Four Flats | A: E major, Alberti. B: A-flat major waltzes. C: C-sharp minor and F minor |
| 6 | Every Key | A: B and D-flat major. B: F-sharp/G-flat twins, B-flat minor, G-sharp minor. C: 12 keys round the circle (4 bars) |
| 7 | Pedal, Clefs and the Whole Keyboard | A: wide LH broken chords with pedal. B: Gymnopedie pattern (low bass, chord), pedal. C: hands take turns with clef changes |
| 8 | Counterpoint, Ornaments and Review | A: two-part sequences with LH imitation. B: ornaments. C: 16-bar review in many keys and textures |

### gen5.py

Pitches are `(step, alteration)`; durations are Fractions (a triplet eighth is 1/12). Each exercise
is built in layers and validated (bar lengths, a hand never spans more than an octave at one moment,
the hands never cross, tonic ending, variety); failures retry. Part options (in `units.py`, `VOLUME5`):

| Key | Meaning |
| --- | --- |
| `key` | `(tonic, mode)`, e.g. `("fis", "major")`; any of the 30 keys (`gen5.Key` builds the signature) |
| `variants` | List of overrides cycled exercise by exercise (keys, meters, textures, tempo) |
| `meter`, `rhythms` | `4/4 3/4 2/4 6/8 3/8 9/8 12/8 2/2`; rhythm tables `RHY` (`basic`, `eighths`, `trip`, `slow`, `motive`); `t8` = triplet eighth |
| `chords`, `require_chords` | Chord vocabulary (`I ii IV V V7 vi V7/V`; minor `i iv V V7 VI`), moves in `MOVES` |
| `bass` | LH pattern from `LH`: `block block2 waltz oompah broken alberti triplet wide wide8 leap` |
| `rh2: "held"` | A held lower voice in the RH (a 3rd or 6th below the tune) |
| `lh2: "tenor"` | LH bass (stems down) and a quarter-note tenor line (stems up) |
| `texture` | `chords` (default), `chorale` (`voices` 3 or 4, `require_inversion`), `alt` (clef changes), `sequence` |
| `chromatic` | `{"passing": p, "neighbour": p, "min": n}` |
| `melodic_minor` | Raised 6th and 7th going up, natural going down |
| `pedal` | Bracket pedal marks, changed with the harmony |
| `ornaments` | `{"trill", "mordent", "grace", "turn": p, "min": n}` |
| `twin` | Print the exercise again in the enharmonic key (labels `a`/`b`) |
| `bars` | 4, 8 or 16 (16: a half close at bar 8, bars 9-12 may repeat 1-4) |
| `rh_up`, `rh_span`, `rh_lo` | Range of the tune (by default from the tonic, never above A5) |

Chorales: chords are chosen first (functional moves, cadences at the fermatas), then a soprano of
chord tones (leading note rising, 7ths falling), then alto, tenor and bass by dynamic programming over
voicings (ranges, spacing, complete chords, doubling, no parallel 5ths/8ves, no augmented seconds,
least motion).

### Pieces (35: 25 from Mutopia, 10 originals)

| Unit | Pieces (Mutopia id; CC = CC BY-SA engraving, notes retyped) |
| --- | --- |
| 1 | Schumann Melody Op. 68/1 (647 CC); Burgmuller Consolation, introduction (224); originals Evening Bells, Hymn with a Moving Tenor |
| 2 | Bach BWV 269 (378), O Haupt voll Blut (107), BWV 347 (379); Schumann Chorale Op. 68/4 (782 CC) |
| 3 | Schumann First Loss (676 CC), Poor Orphan (687 CC), first parts; originals Chromatic Walk, Up the Melodic Minor |
| 4 | Beethoven Fur Elise, theme (931); Schumann Of Foreign Lands (354, cross-staff triplets); Burgmuller Ballade, first part (227); original Rowing Song (12/8) |
| 5 | Schubert Moment musical 3, opening (1023); Impromptu D. 935/2, bars 1-8 (1195); Beethoven Moonlight bars 1-9 (276 CC); original E Major Morning |
| 6 | Chopin Raindrop bars 1-8, simplified (471); Schubert Impromptu D. 899/3, 16 bars in 2/2 (1193); originals Night Song in B, Enharmonic Twins (F-sharp, and G-flat respelled by code) |
| 7 | Satie Gymnopedie 1, first half (37); Chopin Preludes 7 complete (470) and 4 first half (468); Schumann Little Piece 68/5 (653 CC); original Pedal Song |
| 8 | Bach Invention 8, bars 1-12 (61); Polonaise Anh. 128 (1615); Burgmuller Pastorale (218); Bach Prelude in C bars 1-19 (5); Chopin Prelude 20 (472) |

Changes from the plan: Traumerei replaced by Chopin's Prelude No. 4 (Traumerei's voices cross the
staves too often for a clean two-staff text); BWV 928 left out (Unit 8 already had five pieces);
10 originals instead of 9 (the enharmonic twins are two pieces). Pedal marks, ornaments and clef
changes before their units are left out or flagged with a piece's `allow` list and explained in its
note; Melody, First Loss and Poor Orphan read the left hand in the treble clef before Unit 7.

### Checker and build (Volume 5)

`check_pieces.py --vol 5` compiles the pieces with an event listener and checks LilyPond warnings
(bar checks), keys (up to 3 accidentals in Units 1-4, 4 in Unit 5, any from Unit 6), time signatures
(new ones from Unit 4), triplets (4), pedal and clef changes (7), ornaments (8), each hand's span at one
moment (an octave; with the pedal only notes struck together count) and leaps (the jump to the nearest
new note, an octave in the RH and a tenth in the LH, two octaves from Unit 7; none across rests).
Piece options: `allow` (feature names), `allow_span`, `allow_leap` (semitones), `allow_32`,
`allow_key`, `upbeat` ("1/4", for bar numbers in reports), `long` (may break across pages), `cut`
(alla breve sign). `--verbose` lists every problem. Content files may also define `EXAMPLES`
(small scores with captions) and `KEY_PICTURES` (scale degrees on a keyboard). Piece staves are named
`up`/`down` for cross-staff notes. Tool used for transcription: LilyPond's `\displayLilyMusic` turns a
Mutopia source (after `convert-ly`) into absolute pitches.

The build now reports LilyPond warnings (it used `-s`, which hid them); only page-compression notices
are filtered.

## Volume 6 plan (Reading Like a Professional, Levels 7-8)

**Goal.** A Level 8 reader can sight-read what a working pianist is handed: a Bach sinfonia or fugue
exposition, Romantic and Impressionist pieces with cross-rhythms, changing meters and chromatic
harmony, a song accompaniment on three staves, a hymn or string quartet in open score (alto and
tenor clefs), and a lead sheet. Volume 6 also teaches the professional's two survival skills:
*simplifying at sight* (dropping notes without losing the music) and *transposing at sight*.

**Who it is for.** Readers who passed the Volume 5 checkpoint. Start-of-book text: "Volumes 1-5
taught you to read piano music. This volume teaches you to read music written for anyone."

**Size.** 8 units, 3 parts of 8 exercises each (192 exercises), 4 pieces per unit (32: 24 from
Mutopia, 8 originals or traditional tunes). About 150 pages. Seeds 6001-6008.

### Units

| Unit | Title | New ("New:" line) | Parts (8 exercises each) |
| --- | --- | --- | --- |
| 1 | Three Voices | Three independent voices on two staves; the middle voice passes between the hands; fugue entries | A: three-voice counterpoint, RH two voices over a LH bass, 4 bars, C/G/F/D minor. B: the middle voice changes hands (cross-staff notes), 8 bars. C: fugue expositions: subject, answer at the fifth, countersubject, third entry in the bass |
| 2 | Rhythm Against Rhythm | Two against three, three against four, duplets, quintuplets and septuplets, hemiola | A: RH triplets over LH eighths (2:3), then swapped. B: duplets in 6/8 and 3:4 (RH sixteenth-triplets over LH sixteenths). C: free runs (5, 6, 7 notes in a beat) and hemiola in 3/4 waltzes (two bars felt as one bar of 3/2, with accents) |
| 3 | Changing Meters, Modes and No Key | Time signatures that change every bar or two; 5/4, 7/8 (2+2+3), 5/8; modes, whole-tone and pentatonic scales; music without bar lines | A: alternating 5/4 and 6/4 (Promenade style), and 3/4 + 2/4. B: 7/8 and 5/8 with the beat groups shown (beam structure), modes (Dorian, Mixolydian, Phrygian, Lydian) without key signatures. C: unbarred music (dotted bar lines, no meter), whole-tone and pentatonic tunes over open fifths |
| 4 | Chromatic Harmony | Diminished sevenths, secondary dominants of every degree, the Neapolitan sixth, augmented sixths, enharmonic modulation; double sharps and flats | A: V7 of ii, iii, IV, V, vi (and vii°7 of each) in four-part piano texture. B: Neapolitan sixth and augmented sixths (Italian, German, French) leading to V, in minor keys. C: modulation by a pivot chord and by an enharmonic diminished seventh, to distant keys |
| 5 | Big Textures | Octaves in both hands, full chords with the tune on top, 8va / 8vb / 15ma signs, three-staff piano writing, hand crossing; reading the outline | A: RH octave melodies and LH octave basses, 8va and 8vb signs. B: chordal textures (four to six notes) and arpeggios over the whole keyboard, crossed hands (LH over RH). C: dense textures to *simplify at sight*: each exercise is printed with a suggested reduction underneath on a small staff |
| 6 | Accompanying | Three staves: a voice (or violin) line above the piano; introductions and interludes; following the soloist | A: a singer's line above a block-chord accompaniment, with "la" syllables (read the soloist's line while playing). B: the same with arpeggiated and after-beat accompaniments, a two-bar introduction and an interlude. C: the piano doubles the tune in some bars and not in others; rests in the voice part to count through |
| 7 | Open Score, C Clefs and Transposing | Four staves (SATB), the treble clef with an 8 below, the alto clef (viola) and the tenor clef (cello, bassoon); transposing at sight | A: four-part chorales on four staves (soprano, alto, tenor in treble-8, bass), played on the piano. B: string quartet textures: violin 1, violin 2, viola (alto clef), cello (bass and tenor clef). C: transposing at sight: a hymn tune or folk song printed in one key, to be played a tone higher or lower (answers at the back of the book) |
| 8 | Lead Sheets, Simplifying and Review | Chord symbols (C, Am7, G7/B, Fmaj7, Bdim, C/E); realising a lead sheet; review of the whole course | A: lead sheets: a tune with chord symbols, the left hand plays root-position chords, then broken chords. B: lead sheets with sevenths and slash chords, the left hand plays an accompaniment pattern of the reader's choice. C: review: 24-bar exercises in any key, meter and texture from Volume 6 |

### Generator features (`course/gen6.py`, building on gen5; Volumes 1-5 must stay identical)

`gen6.py` imports and extends `gen5.py` (it must not change gen5's output: run `check_identical.py`).

1. **Any number of staves (Units 5-8).** An exercise becomes a list of staves, each with a name,
   clef (`treble`, `bass`, `treble_8`, `alto`, `tenor`), optional instrument name and voices; the
   score is a `PianoStaff` (two or three staves), a `ChoirStaff` (open score) or a `StaffGroup`
   (quartet) plus an optional solo staff above. Clef changes inside a staff as in gen5's `alt`.
2. **Three-voice counterpoint (Unit 1).** Generalise `counter_line` to search a voice against any
   number of fixed voices (consonance on strong beats with every voice, passing dissonance on weak
   beats, no parallels between any pair, no crossing). `texture: "trio"`: bass line from the chord
   plan, tune by `gen_tune`, middle voice by the search. Cross-staff: the middle voice is assigned to
   the hand whose range it is in, bar by bar, written with `\change Staff`. `texture: "fugue"`: a
   1-2 bar subject (`gen_tune` on I-V), real or tonal answer at the fifth (tonal: the subject's 5th
   answered by the tonic), countersubject searched against the answer, entries soprano-alto-bass.
3. **Cross-rhythms (Unit 2).** Rhythm cells for different tuplets per hand: `rh_tuplet` / `lh_tuplet`
   (3 against 2, 4 against 3, duplets `\tuplet 2/3` in compound time); runs `run: {"notes": 5|6|7}`
   filling one beat by step to the next chord tone (`\tuplet 5/4` etc.); `hemiola: True` rewrites
   bars 7-8 of a 3/4 phrase as three half notes with accents. The bar validator works in exact
   fractions already (gen5), so only the emitter needs the new tuplet ratios.
4. **Changing meters, modes, no key (Unit 3).** `meters: ["5/4", "6/4"]` cycles meters bar by bar
   (rhythm tables per meter; `\time` printed when it changes); `beat_groups` for 7/8 and 5/8
   (`\time 2,2,3 7/8`). `Key` gains modes (`dorian`, `phrygian`, `lydian`, `mixolydian`, `aeolian`)
   and scales (`wholetone`, `pentatonic`); `no_signature: True` prints C major and every accidental.
   `unbarred: True` uses `\cadenzaOn` with dotted bar lines at phrase ends.
5. **Chromatic harmony (Unit 4).** Chord vocabulary grows: `V7/ii ... V7/vi`, `vii°7` and `vii°7/x`,
   `N6` (bII in first inversion), `It6`, `Ger6`, `Fr6` (each resolving to V or I6/4-V), with their
   alterations in `chord_alts` (double sharps and flats spelled correctly). The chorale voicing search
   (gen5) is reused for four-part piano texture, with extra rules: augmented sixths resolve outward to
   the octave, the Neapolitan's root falls. `modulate: {"to": key, "pivot": "chord"|"dim7"}`: a pivot
   chord common to both keys, or a diminished seventh respelled enharmonically.
6. **Big textures (Unit 5).** `rh_octaves`, `lh_octaves`, `rh_full: n` (melody on top of an n-note
   chord inside an octave span), `arpeggio_bass` over two or three octaves (pedal), `cross_hands`
   (LH crosses over for one note per bar: notated on the treble staff with a "l.h." mark).
   `\ottava` is inserted automatically when a passage stays above C6 or below C2 for a bar or more
   (8va, 8vb, 15ma). `reduction: True` prints a suggested reduction (outer voices plus the bass of
   each chord) on a small staff (`\magnifyStaff #2/3`) under the exercise.
7. **Accompanying (Unit 6).** `texture: "song"`: a singable line (range a ninth, mostly steps, rests
   at phrase ends) on a third staff above the piano, with `\addlyrics` "la" or vowel syllables;
   accompaniment from gen5's `LH` patterns split between the hands (`accomp: "block" | "arpeggio" |
   "afterbeat"`), `intro: 2` and `interlude: 1` bars built from the chord plan, `double_tune` (the
   piano's top note doubles the voice in the bars listed).
8. **Open score and transposing (Unit 7).** `texture: "chorale"` with `staves: 4` writes the gen5
   chorale on four staves (soprano, alto, tenor `treble_8`, bass); `clefs: "quartet"` prints violin 1,
   violin 2, viola (alto clef), cello (bass, switching to tenor clef above A3). `transpose:
   {"by": "M2", "dir": "up"}` prints the exercise in its own key with the instruction; an "Answers"
   appendix at the end of the book prints every transposition (LilyPond `\transpose`).
9. **Lead sheets (Unit 8).** `texture: "leadsheet"`: melody with `\new ChordNames` above the staff
   and an empty (rests) or slash-notated left hand; chord-symbol vocabulary `symbols: ["triads",
   "sevenths", "slash"]` derived from the chord plan (`G7/B` for V7 in first inversion). Example
   realisations in the unit's EXAMPLES.
10. **Checker and build.** `check_pieces.py --vol 6`: pieces may define `staves` (list of
    `{name, clef, music}`) instead of `rh`/`lh`; the event listener already reads every staff. New
    feature gates by unit: tuplets other than 3 (Unit 2), `\time` changes and `\cadenzaOn` (3),
    `\ottava` and three-staff piano (5), solo staff and lyrics (6), alto/tenor clefs and four staves
    (7), `ChordNames` (8). Spans: per hand on piano staves only (solo and vocal staves are not
    checked). `build.py`: `VOLUMES[6]` with its front matter, the "Answers" appendix, and piece
    `staves`. Build in A4 portrait at staff size 20 for four-staff systems (option `staff_size`).

### Pieces

All checked in the Mutopia archive (ids and licences read from the source files; PD = public domain;
CC = Creative Commons, so the notes are retyped and the source credited, as in Volumes 4-5).
"Excerpt" bars are decided when transcribing; each is shortened to a musical close.

| Unit | Piece | Mutopia id | Licence | Key, time | Why |
| --- | --- | --- | --- | --- | --- |
| 1 | Bach, Sinfonia No. 1 in C, BWV 787 (opening) | 142 | PD | C, 4/4 | three voices, the middle one shared |
| 1 | Bach, Sinfonia No. 11 in G minor, BWV 797 (opening) | 200 | PD | G minor, 3/8 | three voices in 3/8 |
| 1 | Bach, Fugue in C minor, WTC I, BWV 847 (exposition, bars 1-8) | 550 | PD | C minor, 4/4 | subject, answer, countersubject |
| 1 | Original: a short three-voice fugue in G | - | - | G, 4/4 | built from Part C's rules |
| 2 | Debussy, Arabesque No. 1 (opening) | 1777 | PD | E, 4/4 (2/4 in source) | triplets against eighths |
| 2 | Brahms, Waltz Op. 39 No. 15 | 794 | PD | A-flat, 3/4 | hemiola, two voices |
| 2 | Chopin, Nocturne Op. 9 No. 2 (first section, the long run simplified) | 1590 | CC BY-SA 3.0 | E-flat, 12/8 | grace groups and free runs |
| 2 | Joplin, Solace (first strain) | 482 | PD | C, 2/4 | habanera bass against straight eighths |
| 3 | Mussorgsky, Pictures at an Exhibition: Promenade 1 | 475 | PD | B-flat, 5/4-6/4 | changing meters |
| 3 | Satie, Gnossienne No. 1 (first page) | 2035 | CC BY-SA 4.0 | F minor, unbarred | no bar lines, no meter |
| 3 | Debussy, Prelude Book I No. 4 (opening) | 2002 | CC BY-SA 4.0 | A-flat, 5/4 / 3/4 | changing meters, chromatic chords |
| 3 | Traditional: Scarborough Fair (Dorian), harmonised | - | - | D Dorian, 3/4 | a modal tune without key signature |
| 4 | Beethoven, Sonata Pathetique Op. 13, Grave introduction | 299 | PD | C minor, 4/4 | diminished sevenths, Neapolitan, runs |
| 4 | Liszt, Consolation No. 3 (opening) | 1647 | CC BY 3.0 | D-flat, 4/4 | chromatic harmony, wide arpeggios |
| 4 | Grieg, Album Leaf Op. 12 No. 7 | 2194 | CC BY-SA 4.0 | E minor, 2/4 | chromatic voice leading |
| 4 | Original: a pivot-chord and enharmonic modulation study | - | - | C to E-flat | Part C's rules |
| 5 | Rachmaninoff, Prelude in C-sharp minor Op. 3 No. 2 (opening and the chordal close) | 2033 | CC BY-SA 4.0 | C-sharp minor, 4/4 | three staves, huge chords (public domain: published 1893, composer d. 1943) |
| 5 | Grieg, March of the Trolls Op. 54 No. 3 (opening) | 2014 | PD | D minor, 2/4 | octaves, staccato chords |
| 5 | Tchaikovsky, March of the Wooden Soldiers Op. 39 No. 5 | 1806 | PD | D, 2/4 | chords in both hands |
| 5 | Grieg, Wedding Day at Troldhaugen Op. 65 No. 6 (opening) | 781 | PD | D, 4/4 | octaves, 8va |
| 6 | Schubert, Heidenroslein D. 257 | 1555 | PD | G, 2/4 | voice and piano, three staves |
| 6 | Schubert, An die Musik D. 547 | 1001 | PD | D, 2/2 | a singing line over repeated chords |
| 6 | Grieg, Ich liebe dich Op. 5 No. 3 | 586 | PD | B-flat (source), 3/4 | romantic accompaniment, rubato |
| 6 | Schubert, Erlkonig D. 328 (first verse; repeated-octave triplets reduced at sight) | 1030 | PD | G minor, 4/4 | the classic accompanist's challenge |
| 7 | Tallis, If Ye Love Me (open score) | 412 | PD | F, 4/4 | four staves, treble-8 tenor |
| 7 | Tallis, O nata lux de lumine | 949 | PD | G minor, 3/2 | open score in 3/2 |
| 7 | Victoria, O magnum mysterium (first section) | 244 | CC BY-SA 3.0 | F minor (source), 4/4 | four-voice polyphony in open score |
| 7 | Haydn, String Quartet Op. 76 No. 3 ("Emperor"), II: the theme | 385 (Op. 76 set) | PD | G, 2/2 | viola in the alto clef, cello |
| 8 | Debussy, Clair de lune (opening) | 1778 | PD | D-flat, 9/8 | the last piece: 9/8, triplets against duplets, pedal |
| 8 | Joplin, Bethena (first strain) | 463 | PD | G, 3/4 | a concert waltz; chord-symbol analysis |
| 8 | Traditional: Shenandoah and Londonderry Air as lead sheets | - | - | various | realise the chord symbols |
| 8 | Traditional: Old Hundredth (Genevan Psalter, 1551) for transposing | - | - | G | transpose to F and A |

Spares: Bach Sinfonias BWV 788-801 (all on Mutopia); Brahms Waltzes Op. 39 Nos. 3, 9, 10 (264, 265,
2164, PD); Chopin Nocturne Op. 9 No. 1 (582, CC) and No. 3 (1955, CC); Debussy Arabesque No. 2 (1994,
CC); Mussorgsky's other Promenades (475, CC); Grieg Mountaineer's Song Op. 73 No. 7 (1628, PD) and
Homecoming Op. 62 No. 6 (1896, CC); Liszt Consolations Nos. 1 and 4 (1654, 1650, CC BY); Rachmaninoff
Preludes Op. 23 (all CC); Tallis's Canon (Ordinal, 2237, CC). The Fantaisie-Impromptu (Chopin Op. 66)
is a possible "four against three" challenge if a simplified version reads well.

### Build order

1. Feature 1 (multi-staff scores) and feature 10 (checker and build) first, with a test unit, because
   Units 5-8 depend on them; run `check_identical.py` after every change.
2. Then unit by unit, as in Volume 5: generator features, transcriptions (extract with LilyPond's
   `\displayLilyMusic` after `convert-ly`), `content/v6unitNN.py`, `check_pieces.py --vol 6 N`, build,
   look at every page, commit and push.
3. The fugue generator (feature 2) and the chromatic chord voicing (feature 5) are the largest pieces of
   new code; build them with small test scripts that print each rule check before they go into a book.
4. Last: the Answers appendix, the book PDF, README and fingerprints (`check_identical.py --add 6`).

**Risks.** Four-staff systems need a smaller staff size to fit A4 (try 18-20). Lyrics in generated
songs must be neutral syllables (no invented words). Unbarred and changing-meter music needs the bar
checks in the checker to be skipped inside `\cadenzaOn`. Erlkonig and the Rachmaninoff Prelude are
hard: present them explicitly as "simplify at sight" challenges, with a printed reduction.

## Volume 5 plan (as written before it was built)

**Goal.** A Level 6 reader can sight-read real piano music of the standard of Schumann's Album
for the Young, the easier Chopin Preludes and Bach's chorales: two voices in one hand, four-part
harmony, chromatic notes, triplets, every key, pedal marks, clef changes and ornaments. This is
the last volume, so the hand positions of Volumes 1-4 give way to reading by key, chord shape and
pattern, as in real music.

**Size.** 8 units. Each unit has 3 generated parts of 8 exercises (24 per unit, 192 in all; about a
third fewer than Volume 4) and 4-6 pieces (35 in all, 26 of them from Mutopia), so roughly 130
pages. The pieces are longer than before (12-24 bars) and are the heart of each unit;
the exercises prepare the one new skill each piece needs.

**Seeds** stay `volume * 1000 + unit id` (5001-5008).

### Units

| Unit | Title | New ("New:" line) | Parts (count) |
| --- | --- | --- | --- |
| 1 | Two Voices in One Hand | A tune and a held voice in the same hand: stems up and stems down | A: RH tune over a held lower voice in the same hand (half and whole notes a 3rd or 6th below), LH block chords; C, G; 4/4 (8). B: the same in 3/4, F and D, LH waltz (8). C: LH two voices (held bass, moving tenor in quarters) under a RH tune; G, F, B-flat (8) |
| 2 | Chorales | Four voices on two staves; chords on every scale degree and in first inversion | A: three voices (two in the RH, bass in the LH), half notes; C, G, F (8). B: four voices (SATB), quarter notes, fermatas at phrase ends, I ii IV V V7 vi and first inversions; keys up to 2 sharps or flats (8). C: four voices in minor keys (A, D, E minor) with the raised leading note (8) |
| 3 | Chromatic Notes | Chromatic passing and neighbour notes, V7 of V, melodic minor; accidentals last to the bar line | A: RH chromatic passing and neighbour notes over block chords; C, G, F (8). B: V7 of V (F-sharp in C, C-sharp in G, B-natural in F) with cancelling naturals (8). C: melodic minor, raised 6th and 7th going up, natural going down; A, D, E minor (8) |
| 4 | Triplets and New Time Signatures | Eighth-note triplets; 3/8, 9/8, 12/8 and 2/2 (alla breve) | A: RH triplets over block and waltz basses in 4/4 and 3/4 (8). B: 3/8 (one beat in a bar) and 9/8 (8). C: 2/2 counted in two, and 12/8 (8) |
| 5 | Four Sharps and Four Flats | E major, A-flat major, C-sharp minor (B-sharp) and F minor (E-natural) | A: E major (8). B: A-flat major (8). C: C-sharp minor and F minor, alternating (8) |
| 6 | Every Key | Five, six and seven sharps or flats; enharmonic keys (F-sharp = G-flat) | A: B major and D-flat major (8). B: F-sharp and G-flat major as twins (the same exercise in both spellings), B-flat minor and G-sharp minor (8). C: round the circle of fifths: each exercise in a new key (8) |
| 7 | Pedal, Clefs and the Whole Keyboard | Sustain pedal marks; the LH in the treble clef and the RH in the bass clef | A: wide pedalled LH broken chords (root, fifth, tenth), the pedal changing with each chord (8). B: Gymnopédie-style LH, a low bass note then a chord in the middle of the keyboard, pedalled; 3/4 (8). C: clef changes and crossing hands: hands take turns, each reading in the other clef (8) |
| 8 | Counterpoint, Ornaments and Review | Sequences and imitation; trills, mordents and grace notes; review of the course | A: two-part counterpoint built from sequences (a one-bar motive repeated a step lower), the LH imitating (8). B: ornaments on cadence and strong-beat notes (8). C: review: 16-bar pieces in any key with everything from Volume 5 (8) |

Unit 8 doubles as the review, so the course ends after eight units, as the five-volume plan says.

### Generator features (all opt-in; Volumes 1-4 must stay byte-identical)

Run `check_identical.py` after every change. Volume 5 options do nothing unless a part switches
them on, and must not draw random numbers otherwise.

1. **Voices in one staff (Unit 1).** A part option `voices={"rh": "held", "lh": "tenor"}` adds a
   second voice to a staff: `ex["rh2"]` / `ex["lh2"]` hold `[(dur, step|None)]` per bar, and
   `lily_exercise` writes `<< { upper } \\ { lower } >>` (stems up and down; rests for a silent
   voice). `held`: the lower RH voice holds chord tones a 3rd or 6th below the tune, changing
   with the chord (no crossing, no unisons, never above the tune). `tenor`: a held LH bass plus a
   quarter-note tenor line on chord tones and passing notes. Hand span in one staff at most an
   octave. This is the foundation for chorales.
2. **Chorales (Unit 2).** `mode: "chorale"` (`voices: 3` or `4`). A chord vocabulary `CHORDS4`
   by scale degree (I ii IV V V7 vi, and `6` for first inversion) with its own move table
   (`CHORD_MOVES4`: ii -> V, IV -> V, vi -> ii or IV, V -> I or vi; cadences V-I and I-V at
   fermatas). The soprano comes from `gen_melody` (chord tone on every beat); alto, tenor and
   bass are found by a search over voicings, chord by chord: voice ranges (S C4-G5, A G3-D5,
   T C3-G4, B E2-D4), S-A and A-T within an octave, T-B at most a 12th but each hand within an
   octave, no crossing, no parallel 5ths or octaves, the leading note rising, the 7th falling,
   common tones held, root doubled (third doubled allowed in first inversion of ii and vi). The
   cheapest legal voicing (least total motion) wins, with a random tie-break. Minor uses the
   existing `minor` spelling. `\fermata` at bars 2/4/6/8.
3. **Chromatic notes (Unit 3).** Notes can carry an alteration: `ex["alter"][(bar, i)] = +1/-1`,
   used by `spell()`. `chromatic={"passing": p, "neighbour": p}`: a chromatic passing note on a
   weak eighth between two notes a whole tone apart (sharps going up, flats going down), or a
   lower chromatic neighbour (E-D#-E). `secondary: ["V/V"]` adds V7 of V to the chord plan
   (always followed by V or V7); its raised 4th is spelled in both hands, like the raised 7th of
   `minor`. `melodic_minor: True` raises the 6th and 7th in rising lines to the tonic and keeps
   them natural in falling lines. LilyPond's `modern` accidental style prints the courtesy
   naturals in the next bar.
4. **Triplets and new meters (Unit 4).** `grid: 3` counts durations in triplet eighths (a
   quarter = 3). Straight eighths cannot occur in such parts. The rhythm tables `R44_T` and
   `R34_T` mix quarters, halves and triplet groups (1+1+1, 2+1). `staff_music` wraps each beat's
   triplet notes in `\tuplet 3/2 { }`. Bass patterns: `block`, `oompah`, `waltz` scale by the
   grid; a new `"triplet"` pattern (bottom-middle-top triplets, the Moonlight pattern). Meters:
   `3/8` (`BAR_LEN` 3), `9/8` (9), `12/8` (12), with rhythm tables built from `R68`, and `2/2`
   (8, strong beats 0 and 4, `tempo_unit "2"`, printed as alla breve).
5. **Every key (Units 5-6).** `KEY_E`, `KEY_AB`, `KEY_CSM`, `KEY_FM`, `KEY_B`, `KEY_DB`,
   `KEY_FS`, `KEY_GB`, `KEY_BBM`, `KEY_GSM` (and the rest of the 15 major and 15 minor keys for
   the circle-of-fifths part). Positions are no longer written by hand: a helper
   `make_position(hand, tonic_name, octave)` builds the five-finger position and its chord shapes
   from the key, so new keys cannot be mistyped. `twin: True` prints each exercise a second time
   in the enharmonic key (same notes on the keyboard, every name changed). The keyboard pictures
   already shade black keys with white finger numbers.
6. **Pedal and wide basses (Unit 7).** `pedal: True` with `chords`: `\sustainOn` at the start
   and `\sustainOff\sustainOn` at every chord change (bracket style), released at the end. New
   bass patterns `"wide"` (root, fifth, tenth, fifth: needs the pedal) and `"leap"` (a low root on
   beat 1, the chord an octave or more higher on beats 2-3). `bass_leap` up to 14 (two octaves)
   for these.
7. **Clef changes (Unit 7).** In `alt` mode, segments may use a high LH position (`LH_G4`, G4-D5)
   or a low RH position (`RH_C3`, C3-G3); `clef_switch: True` prints `\clef treble` in the LH
   staff (or `\clef bass` in the RH staff) for those segments and switches back afterwards.
8. **Sequences and ornaments (Unit 8).** `sequence={"len": 1, "step": -1, "times": 3}`: bars 1-3
   are a one-bar motive in both hands and its copies a step lower (the hand position moves with
   it, so the finger numbers repeat), then a cadence; in 8 bars, a second sequence in bars 5-7.
   `ornaments={"trill": p, "mordent": p, "grace": p}`: `\trill` on the cadence's penultimate
   note when it is a quarter or longer, `\prall` (mordent) on strong-beat quarters, and
   `\acciaccatura` grace notes a step above. `bars: 16`: two 8-bar phrases, the first ending on V
   (half cadence), the second on I; bars 9-12 may repeat bars 1-4.
9. **Checker and build.** `check_pieces.py` for Volume 5 checks what has been taught rather than
   hand positions: keys (up to 3 sharps or flats until Unit 4, 4 in Unit 5, any from Unit 6),
   meters and triplets (from Unit 4), pedal and clef changes (from Unit 7), ornaments (Unit 8),
   each hand's range, its largest leap and its span within one chord or two voices (an octave,
   unless `allow_span`). It must parse `<< { } \\ { } >>`, `\tuplet`, `\clef`, `\sustainOn/Off`,
   `\trill`, `\prall`, `\mordent`, `\turn`, `\acciaccatura`, `\appoggiatura`, `\fermata` and
   `\repeat volta`. `build.py`: `VOLUMES[5]` with its front matter; piece option `"long": True`
   lets a piece break across pages at a system break; an "Ornaments" box in Unit 8 shows how each
   sign is played.

### Pieces

Public-domain sources from Mutopia (every composer is long out of copyright). Each is
transcribed from the downloaded `.ly`, rendered to check the notes, shortened or simplified to
the unit's level (the credit says so), and checked with `check_pieces.py`. PD = public-domain
engraving; CC = a CC BY-SA engraving: we retype the notes ourselves and name the source.

| Unit | Piece | Mutopia id | Licence | Key, time | Notes |
| --- | --- | --- | --- | --- | --- |
| 1 | Schumann, Melody, Op. 68 No. 1 | 647 | CC | C, 4/4 | RH tune with a second voice at cadences, LH bass plus an eighth-note inner voice |
| 1 | Burgmüller, Consolation, Op. 100 No. 13 (opening) | 224 | PD | C, 4/4 | tune over sixteenths in the same hand; simplified |
| 2 | Bach, chorale "Aus meines Herzens Grunde", BWV 269 | 378 | PD | G, 3/4 | first two phrases |
| 2 | Bach, chorale "O Haupt voll Blut und Wunden" (St Matthew Passion) | 107 | PD | D minor, 4/4 | |
| 2 | Bach, chorale "Ich dank dir, lieber Herre", BWV 347 | 379 | PD | A, 4/4 | source uses Italian note names |
| 2 | Schumann, Chorale, Op. 68 No. 4 | 782 | CC | G, 4/4 | the chorale "Freue dich, o meine Seele" |
| 3 | Schumann, First Loss, Op. 68 No. 16 (first part) | 676 | CC | E minor, 2/4 | D-sharp and chromatic inner voices |
| 3 | Schumann, Poor Orphan, Op. 68 No. 6 (first part) | 687 | CC | A minor, 2/4 | RH two voices; chromatic |
| 4 | Beethoven, Für Elise, WoO 59 (A section) | 931 | PD | A minor, 3/8 | chromatic neighbour D#-E; pedal marks left out until Unit 7 |
| 4 | Burgmüller, Ballade, Op. 100 No. 15 (first part) | 227 | PD | C minor, 3/8 | |
| 4 | Schumann, Of Foreign Lands and Peoples, Op. 15 No. 1 (first part) | 354 | PD | G, 2/4 | tune over triplets in the same hand |
| 5 | Schubert, Moment musical No. 3, D. 780 (opening) | 1023 | PD | F minor, 2/4 | |
| 5 | Schubert, Impromptu in A-flat, D. 935 No. 2 (opening) | 1195 | PD | A-flat, 3/4 | chordal; simplified |
| 5 | Beethoven, "Moonlight" Sonata, Op. 27 No. 2, first movement (opening) | 276 | CC | C-sharp minor, 2/2 | triplets; simplified |
| 6 | Chopin, Prelude in D-flat ("Raindrop"), Op. 28 No. 15 (opening) | 471 | PD | D-flat, 4/4 | simplified |
| 6 | Schubert, Impromptu in G-flat, D. 899 No. 3 (opening) | 1193 | PD | G-flat, 4/2 | tune and a simplified bass; Schubert's 4/2 bars halved into 2/2 |
| 7 | Satie, Gymnopédie No. 1 (first part) | 37 | PD | D, 3/4 | leap bass, pedal |
| 7 | Chopin, Prelude in A, Op. 28 No. 7 | 470 | PD | A, 3/4 | complete (16 bars), pedal |
| 7 | Schumann, Träumerei, Op. 15 No. 7 (first part) | 504 | PD | F, 4/4 | four voices, pedal |
| 7 | Schumann, Little Piece, Op. 68 No. 5 | 653 | CC | C, 4/4 | LH moves into the treble clef |
| 8 | Bach, Invention No. 8 in F, BWV 779 (opening) | 61 | PD | F, 3/4 | imitation and sequences |
| 8 | Bach, Little Prelude in F, BWV 928 | 63 | PD | F, 4/4 | |
| 8 | Bach notebook, Polonaise in D minor, BWV Anh. 128 | 1615 | PD | D minor, 3/4 | mordents, trills and appoggiaturas |
| 8 | Burgmüller, Pastorale, Op. 100 No. 3 | 218 | PD | G, 6/8 | grace notes |
| 8 | Bach, Prelude in C, BWV 846 (Well-Tempered Clavier I; opening) | 5 | PD | C, 4/4 | review: reading chord patterns |
| 8 | Chopin, Prelude in C minor, Op. 28 No. 20 | 472 | PD | C minor, 4/4 | complete (13 bars); four-voice chords; the last piece of the course |

That is 26 pieces from Mutopia. Each unit adds originals (8-16 bars) where the repertoire is
thin: two each in Units 1, 3 and 6, one each in Units 4, 5 and 7, none in Units 2 and 8: 9
originals, 35 pieces in all. Spare candidates, all checked on Mutopia: Bach Invention No. 4 in D minor (67, PD) and No. 13 in A minor (59, PD),
Little Prelude in D minor BWV 926 (69, PD; mordents), Minuet in A minor Anh. 120 (1612, PD;
trills), Polonaise in G minor Anh. 119 (1016, PD), Chopin Preludes Nos. 4 and 6 (468 and 469, PD), Tchaikovsky's March of the Wooden Soldiers (1806, PD),
Mendelssohn's Venetian Gondola Song Op. 19 No. 6 (1679), Schumann's Sicilienne Op. 68 No. 11
(783, CC). Already used in earlier volumes, so not used again: Anh. 114, 115, 121, 126, Op. 68
Nos. 2, 3 and 10, Op. 39 Nos. 1 and 16, K. 545.

Keys with five or more sharps or flats have little easy repertoire, which is why Unit 6 leans
on the generator (the twin and circle-of-fifths parts) and on originals.

### Build order

Same routine as Volume 4: feature 9 (checker and build) first, then for each unit add its parts
and features, write `content/v5unitNN.py`, run `check_pieces.py --vol 5 N`, build, look at every
page, run `check_identical.py` (and `--add 5 N` once the unit is done), commit and push. Unit
titles go into `VOLUME5` at the start, because the contents page prints them. The chorale search
(feature 2) is the largest piece of new code; build it with a small test script that prints
voicings and their rule checks before it goes into the book.

## Files

```
course/units.py         Course spec: hand positions, rhythm vocabularies, unit/part rules
course/generator.py     Exercise generator + validator + LilyPond emitter
course/build.py         Page template, keyboard diagrams, front matter, contents, book assembly
course/check_pieces.py  Checks hand-written pieces against what each unit has taught
course/check_identical.py  Regression check: finished units must not change (fingerprints.json)
content/unitNN.py       Hand-written text and pieces for unit NN (one file per unit)
build/                  Output PDFs (plus the .ly source of the last build)
```

## Build

```bash
pip install --break-system-packages lilypond     # bundles the LilyPond binary
cd course
python3 check_pieces.py                          # Volume 1; must print OK for every unit
python3 check_pieces.py --vol 2                  # Volume 2
python3 build.py 3                               # one unit -> build/read-at-sight-vol1-unit3.pdf
python3 build.py 1 2 3 4 5 6 7 8 9 10            # whole book -> build/read-at-sight-vol1.pdf
python3 build.py --vol 2 1 2 3 4 5 6 7 8 9 10    # Volume 2 book -> build/read-at-sight-vol2.pdf
python3 check_pieces.py --vol 3 1                # Volume 3 (units not written yet are skipped)
python3 build.py --vol 3 1                       # Volume 3, Unit 1 (with front matter)
python3 build.py --vol 4 1 2 3 4 5 6 7 8        # Volume 4 book -> build/read-at-sight-vol4.pdf
python3 check_pieces.py --vol 5                  # Volume 5 (add --verbose for every problem)
python3 build.py --vol 5 1 2 3 4 5 6 7 8        # Volume 5 book -> build/read-at-sight-vol5.pdf
python3 check_identical.py                       # every finished unit must print "identical"
python3 check_identical.py --add 5 1             # record a newly finished unit (here Volume 5, Unit 1)
```
Content modules: Volume 1 uses `content/unitNN.py`; Volume 2 uses `content/v2unitNN.py`;
Volume 3 uses `content/v3unitNN.py`; Volume 4 uses `content/v4unitNN.py`. Volume 3 book:
`python3 build.py --vol 3 1 2 3 4 5 6 7 8 9 10`.
Seeds are `volume * 1000 + unit id`.
- The front matter (title, how-to, contents) is included only when Unit 1 is part of the
  build.
- A unit with no `content/unitNN.py` builds as a **preview** (exercises plus placeholder text).
- Pages are filled greedily (`ly:minimal-breaking`). `\noPageBreak` after each `\break`
  keeps an exercise or piece on one page.

Output is deterministic: each unit uses seed `1000 + unit id`. **Don't change a finished
unit's parts:** that changes its exercises, and the user may already have printed them.
New options only use the random generator when they are switched on. `check_identical.py`
stores a SHA-256 of every unit's generated LilyPond (and the front matter) in
`course/fingerprints.json`; run it before every commit. A change it reports must be explained
(e.g. a text fix in an unfinished volume) and re-recorded with `--add`.

## Part spec options (course/units.py)

| Key | Meaning |
| --- | --- |
| `mode` | `RH`, `LH`, `alt` (hands alternate every 2 bars), `together` (RH melody + LH bass) |
| `rh`, `lh` | Position keys from `POSITIONS` (e.g. `RH_C`, `LH_G`, `RH_D`, `LH_F`) |
| `meter` | `4/4` or `3/4` |
| `rhythms` | A key, or a list of keys, of `R44`/`R34` (`whole`, `half`, `quarter`, `q_rich`, `eighths`, `basic`) |
| `motion` | Allowed intervals with weights (`STEPS_ONLY`, `STEPS_SKIPS`, `UP_TO_FIFTH`) |
| `bars`, `count`, `tempo` | 4 or 8 bars; number of exercises; suggested metronome mark |
| `tonic` | Step of the home note (default C4 = 28); the melody starts on degree 1/3/5 and ends on the tonic |
| `repeat_prob` | In 8-bar exercises, chance that bars 5–6 repeat bars 1–2 |
| `bass` | For `together`: `whole` or `half`. LH plays the position's lowest note (I) or the note a 5th above it (V) |
| `tie_prob` | Chance of tying a bar's last note into the next bar (same hand, same pitch) |
| `rest_prob` | Chance of turning a note into a rest. Never the first note of an entry, the cadence, the final bar or tied notes; half rests only on beats 1 and 3 |
| `key`, `key_acc` | Key signature and spelling, e.g. `KEY_D` = `d \major` with `{'f':'is','c':'is'}`; also `KEY_G`, `KEY_F`, `KEY_AM`, `KEY_EM`, `KEY_DM` |
| `rh_positions`, `lh_positions` | (Vol 2) Positions the hand moves between; the first is home. Shifts happen at segment boundaries (`shift_every`, default 2 bars) with probability `shift_prob` (default 0.7); the interval at a shift uses `shift_motion`. The last segment always contains the tonic |
| `extend` | (Vol 2) `1` lets a hand reach one key beyond its position; the stretch note is fingered 1 or 5 |
| `artic` | (Vol 2) `{"slur": p, "stacc": p}` per two-bar segment: a slur over the whole segment (only if it has no rests), or staccato dots on quarters and eighths |
| `dynamics` | (Vol 2) `True` adds a starting dynamic; 8-bar exercises get a hairpin in bar 3 leading to a new level in bar 5 |
| `chords` | (Vol 3) Chords the LH plays, from `CHORDS` in units.py: `I`, `IV`, `V7`. A chord plan is chosen first (start on I, end V7-I, bar 4 of 8 is V7 or I, never V7 -> IV, weights in `CHORD_MOVES`); the melody then puts a chord tone on beat 1 and on every half note or longer, never doubles the leading note over V7, and avoids parallel 5ths/8ves with the bass on beat 1 |
| `bass` | (Vol 3) With `chords`, one chord per bar (`BASS_PATTERNS`); the last bar holds the root. `broken`: 4/4 bottom-middle-top-middle quarters, 3/4 bottom-middle-top, 6/8 six rolling eighths. `alberti`: eighths bottom-top-middle-top (4/4 and 3/4). `lilt` (6/8): bottom quarter, top eighth, middle quarter, top eighth |
| `bass_leap` | (Vol 3) Largest LH leap in the bass, default 5 (a sixth, `CHORD_MAX_LEAP`); Alberti and lilting basses need 6 for IV -> V7 |
| `require_chords` | (Vol 3) Chords that must appear in every exercise, e.g. `["IV"]` |
| `chord_fingers` | (Vol 3) Print a LH finger number on the first note of every new chord shape |
| `beat_tones` | (Vol 3) With `chords`: every note on a strong beat (beats 1 and 3; both beats of 6/8) belongs to the chord |
| `minor` | (Vol 3) Minor key: the chords are i, iv and V7, and the leading note is raised in V7 bars, in both hands (printed as an accidental, with `\accidentalStyle modern` so the next bar gets a reminder). No augmented seconds in the melody. Use with `extend=1` so the RH thumb reaches the raised 7th below the tonic |
| `lead_weight` | (Vol 3) With `minor`: makes the melody favour the raised 7th in V7 bars (e.g. 6 or 20) |
| `dyads` | (Vol 3) RH two-note chords: `{"prob": p, "intervals": (2, 5), "weights": {5: 4.0}, "min": n}`; a third (2) or sixth (5) is added below melody notes of a quarter or longer (not tied ones); with `chords` both notes must be chord tones and the leading note is never doubled. `min` two-note chords per exercise |
| `tempo_unit` | (Vol 3) Note value of the metronome mark, e.g. `"4."` for 6/8 |
| `meter` `"2/4"` | (Vol 4) Two quarter beats; rhythm tables `R24` (`basic24`, `e24`, `synco24`), bass patterns `block`, `oompah`, `broken`, `alberti` |
| `bass` (Vol 4) | With `chords`, LH three-note chords (`BASS_PATTERNS`): `block` (held all bar), `block2` (two half-note chords, 4/4), `oompah` (bottom note, upper two notes; 4/4 and 2/4), `waltz` (3/4: bottom, upper two, upper two). The last bar holds the whole chord |
| `rh_chords` | (Vol 4) `{"prob": p, "where": "strong", "min": n, "min_dur": 4, "size": 3}`: adds the two chord tones below a melody note (a full three-note chord or nothing) on notes of `min_dur` eighths or longer, or, with `where: "strong"`, on strong beats; never on tied notes; `min` chords per exercise |
| `mode` `"lhtune"` | (Vol 4) The LH plays the tune; the RH plays chords from `RH_PATTERNS[(accomp, meter)]`, e.g. `accomp: "afterbeat"` (rest, chord, rest, chord); `accomp_size` notes per chord (default 2) |
| `grid` | (Vol 4) `2` counts durations in sixteenths (`DUR16`); bar lengths, strong beats, staccato and beat-tone thresholds scale with it. Rhythm tables `R24_16` (`s24`, `dot24`) and `R44_16` (`s44`, `dot44`) |
| `fast_steps` | (Vol 4) With `grid: 2`, sixteenths move only by step, and no A-B-A-B trills |
| `anticip_prob` | (Vol 4) Chance of tying a bar's last eighth into the next bar (an anticipation); at least one per exercise |
| `accents` | (Vol 4) `->` on off-beat notes longer than an eighth (syncopations) |
| `modulate` | (Vol 4) `{"home_bars": n, "show": "signature"\|"accidentals", "to": [segment, ...]}`; each segment overrides part keys for `bars` bars (`rh`, `lh`, `tonic`, `key`, `key_acc`, `minor`, `lead_weight`). A new segment starts V7-I in its key; the tune moves into it by at most a fifth; the new leading note must appear; the exercise ends on the last segment's tonic. `"signature"` prints `\bar "||" \key ...` at the change |

Modes added for Volume 3:
- `duet`: the `lead` hand (`"RH"` default, or `"LH"`) plays the melody; the other hand plays a
  counter-melody with rhythms from `counter_rhythms` and intervals from `counter_motion` (default
  `COUNTER_MOTION`). Every attack of the second voice is a 3rd, 6th, 5th or octave against the
  other voice; a note the other voice moves to while it holds may be a passing note on a weak beat;
  no parallel 5ths or octaves; contrary motion is preferred; both hands end on the tonic.
- `imitate`: the RH plays a two-bar tune, then the LH plays it an octave (or two) lower while the
  RH plays a counter-melody (`counter_rhythms`). In 8 bars this happens twice, with a LH
  counter-melody under the second tune. `rh` and `lh` must be positions an exact number of
  octaves apart (e.g. `RH_C`/`LH_C`, `RH_G`/`LH_G`).

Chord shapes are built on the LH position's lowest note: I = 1-3-5 (fingers 5 3 1), IV = 1-4-6
(5 2 1), V7 = 7-4-5 (5 2 1, the dominant seventh without its fifth), e.g. C E G / C F A / B F G.

A finger number is printed on the first note of every hand entry **and every shift**, so in
Volume 2 a mid-line finger number means "move the hand". Rhythm vocabularies added for
Volume 2: `R44["dotted"]`, `R34["dotted34"]`, `R34["e34"]`.

Every exercise is validated (bar lengths, notes inside the hand position, allowed
intervals, tonic ending, variety, ties join equal notes) and deduplicated across the unit.

## Content files (content/unitNN.py)

Use the same names as the existing files:
- `INTRO` — paragraphs
- `NEW_IDEAS` — list of `(heading, explanation)` pairs
- `TIPS` — 3–5 reading tips
- `PART_NOTES` — dict mapping part name to an instruction
- `PIECES` — dicts with `title, credit, meter, tempo, note, rh, lh` and optionally
  `key` (e.g. `"d \\major"`) and `allow_leap` (a documented exception for one larger leap)
- `CHECKPOINT` — pass criteria; optional `CHECKPOINT_TITLE`
- optional `KEYBOARDS` — list of position groups to draw, e.g. `[["LH_D","RH_D"],["LH_F","RH_F"]]`
- optional `STRETCH` — `(step, finger, hand)` keys drawn pale on the keyboard (stretch notes)
- optional `CHORD_SHAPES` — (Vol 3) `(title, lh position, lily key, key_acc[, minor])` per key:
  draws the LH's I, IV and V7 shapes as keyboards, then all of them on one bass staff (two keys per
  line when there are four or more). With `minor` True the chords are labelled i, iv, V7 and V7
  carries the raised 7th. Use `KEYBOARDS = []` to draw no position keyboard.
- piece option `tempo_unit` (e.g. `"4."` in 6/8), and two-note chords `<e' g'>4` in piece strings
  (the checker checks every note's range and follows the top note for leaps).
- piece options: `positions` (extra position keys the checker allows for that piece, e.g.
  `["LH_MC"]`), `allow_range: True` (skip the range check, e.g. for a challenge piece), and
  `allow_leap: N`. Every exception should be explained in the piece's `note`.

### Rules for pieces
- `rh`/`lh` are absolute-pitch LilyPond (`c` = C3, `c'` = middle C, `g,` = G2). Put
  `\break` after every 4 bars in **rh**, and use `R1`/`R2.` for silent bars.
- Put a finger number on the first note of each hand's entry: `e'4^3` for RH, `c4_5` for LH.
- Use only notes, rhythms and leaps taught by that unit. `check_pieces.py` enforces this.
  In Volume 2 a hand may reach one key beyond its positions from Unit 2, and dotted quarters
  are allowed from Unit 3. In Volume 3 stretches, eighths and dotted rhythms are allowed from
  Unit 1; leaps up to a sixth in Unit 1, a seventh from Unit 2 (Alberti) and an octave from Unit 8.
  In Volume 4 leaps up to an octave are allowed throughout, sixteenths from Unit 6, and the checker
  ignores `\key` and `\time` changes and finger numbers inside chords (`<c-5 e-3 g-1>`).
  Slurs `(` `)`, staccato `-.`, dynamics `\p` and hairpins `\<` `\>` are written straight into
  the piece strings.
- **Public-domain pieces:** only use melodies whose notes are certain (folk tunes, famous
  themes), or transcribe from a verified source such as Mutopia. Say "simplified" in
  `credit` whenever anything was changed.
- **Original pieces:** 8 bars, question and answer, ending on the tonic. Credit as "Original".

## Style conventions
- A4 paper; staff size 22; numeric time signatures; no bar numbers; always a grand staff.
- Exercise label: tick box followed by "unit.number". Keyboard diagrams use green for the
  left hand and blue for the right hand; black keys in a position are shaded darker with a
  white finger number.
- Plain words, short sentences, every term explained when it first appears.

## QA checklist (after every build)
1. `python3 check_pieces.py` prints OK for every unit, and `build.py` prints no `WARN:` lines
   (LilyPond reports bar-length errors as warnings).
2. Render every page (`pdftoppm -r 45 -png ...`) and look at all of them. Look at pieces
   pages at about 100 dpi.
3. Check that no text overlaps, nothing is split across pages, keyboards and note maps match
   the unit, and key signatures and accidentals appear where expected.
4. Check that the contents page numbers land on each unit's title page (use `pdftotext`).
