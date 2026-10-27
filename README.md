# Read at Sight — piano sight-reading course (build system)

A print-ready A4 course book, typeset with LilyPond.

## Status (2026-10-27)

| Volume | Status | Book | Contents |
| --- | --- | --- | --- |
| 1 · First Steps | complete | `build/Read at Sight - Volume 1.pdf` (130 pp.) | 10 units, 322 exercises, 39 pieces |
| 2 · Moving Hands | complete | `build/Read at Sight - Volume 2.pdf` (133 pp.) | 10 units, 306 exercises, 35 pieces |
| 3 · Two Voices | complete | `build/Read at Sight - Volume 3.pdf` (159 pp.) | 10 units, 342 exercises, 32 pieces |
| 4 · Patterns and Keys | in progress: Units 1-1 done | `build/units/` (Vol4 - Unit 1 to 1) | Units 1-1: 34 exercises, 3 pieces |

Single units are in `build/units/` (`Read at Sight - VolN - Unit M.pdf`).

**Next: Volume 4.** The full plan is in "Volume 4 plan" below: units, parts, generator features,
candidate pieces with their Mutopia sources, and the build order.

Note: the Volume 1 PDFs were built before two small layout tweaks (the "What is new" heading
now stays with its first item, and keyboards widen to fit every key). Rebuilding Volume 1
would only change the page layout; exercises are identical.

## Five-volume plan

| Volume | Levels | Main new skills | Units |
| --- | --- | --- | --- |
| 1 · First Steps (done) | 0–1 | Both clefs, C/G/middle-C positions, hands together, rests and ties, eighths, D and F positions | 10 |
| 2 · Moving Hands (done) | 2 | Leaving five-finger positions, hand shifts and extensions, 1 sharp or flat keys and their relative minors, dotted quarters, slurs, simple dynamics | 10 |
| 3 · Two Voices (done) | 3 | Real left-hand independence, Alberti and broken-chord basses, 6/8, keys up to 2 sharps or flats, simple counterpoint | 8–10 |
| 4 · Patterns and Keys | 4 | Chords in both hands, syncopation, sixteenths, ledger lines, changing key mid-piece | 8 |
| 5 · Repertoire Reading | 5–6 | 3–4 voices, chromatic notes, all keys, chorales | 6–8 |

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

## Volume 4 plan (Patterns and Keys, Level 4)

**Goal.** A Level 4 reader plays both hands with three-note chords, reads up to three ledger lines
above the treble staff and below the bass staff, keeps a steady beat through syncopation and
sixteenth notes, reads keys with up to three sharps or flats, and follows a change of key in the
middle of a piece. The texture is mostly melody plus accompaniment patterns (the "patterns" of the
title): block chords, oom-pah and waltz basses, Alberti, chorale.

**Size.** 8 units, about 34 exercises each (about 270), 3-4 pieces per unit (about 28), so roughly
140 pages. About half the pieces are public-domain music transcribed from Mutopia (see "Pieces"
below); the rest are originals.

**New time signature.** 2/4 joins in Unit 2: marches, the Musette, the Entertainer and the Old
French Song are all in 2/4. No triplets in Volume 4 (pieces that have them are simplified).

### Units

| Unit | Title | New ("New:" line) | Parts (count) |
| --- | --- | --- | --- |
| 1 | Block Chords | The left hand plays I, IV and V7 as three-note chords: held, oom-pah and waltz | A: C major, held chords under a tune, 4 bars (8). B: G major, oom-pah bass in 4/4, 8 bars (10). C: F major, waltz bass in 3/4, 8 bars (8). D: D and B-flat major, mixed, 8 bars (8) |
| 2 | Chords in Both Hands | Right-hand three-note chords; 2/4 time | A: C major, RH chords on long notes and cadences, 4 bars (8). B: G major march in 2/4, RH chords on beat 1, LH oom-pah (10). C: F major chorale: both hands in chords, half notes (8). D: B-flat major waltz with RH chords (8) |
| 3 | High Notes | Ledger lines above the treble staff, up to C6; the hand moves up an octave | A: RH alone in high C position (C5-G5) (10). B: RH moving between C position and high C position, octave moves (8). C: G major, RH in high G position (G5-D6) over broken chords (8). D: D major in 2/4, high and low positions (8) |
| 4 | Low Notes and the Middle | Ledger lines below the bass staff, down to C2; both hands near middle C | A: LH alone in low C and low F positions (C2-G2, F2-C3) (10). B: the tune low in the LH, RH off-beat chords (8). C: RH below middle C (ledger lines below the treble staff) (8). D: both hands around middle C, the tune passing between them (8) |
| 5 | Syncopation | Notes that start between the beats: eighth-quarter-eighth, ties over the beat and over the bar line, accents | A: RH alone, 4/4 syncopated rhythms (10). B: 2/4 ragtime: syncopated tune over an oom-pah bass (8). C: anticipations tied across the bar line (8). D: syncopation in two voices (8) |
| 6 | Sixteenth Notes | Four sixteenths, eighth plus two sixteenths, dotted eighth plus sixteenth | A: RH alone in 2/4 (10). B: LH alone in 2/4 (8). C: 4/4, RH sixteenths over block chords (8). D: dotted eighth-sixteenth over a waltz bass (8) |
| 7 | Three Sharps and Three Flats | A major, E-flat major, F-sharp minor (E-sharp) and C minor (B-natural) | A: A major, Alberti bass (8). B: E-flat major waltz (8). C: F-sharp minor, raised 7th E-sharp (9). D: C minor, raised 7th B-natural (9) |
| 8 | Changing Key | A new key in the middle of a piece: to the dominant and to the relative minor or major, with a new key signature or with accidentals only; review of Volume 4 | A: to the dominant with a new key signature (C to G, F to C, G to D) (8). B: to the relative minor or major, accidentals only (8). C: away and back home, 8 bars (8). D: review: everything in Volume 4 (10) |

Unit 8 doubles as the review, so Volume 4 keeps the eight units of the five-volume plan.

### Generator features (all opt-in; Volumes 1-3 must stay byte-identical)

0. **Regression check first.** Add `course/check_identical.py` with a stored fingerprint file
   (SHA-256 of every generated exercise and every unit page of Volumes 1-3). Run it before every
   commit; it replaces the ad-hoc hash scripts used while building Volume 3.
1. **LH block chords (Unit 1).** New `bass` values for `chords` parts: `"block"` (the chord held
   for the bar or half bar), `"oompah"` (4/4: root, chord, root, chord in quarters) and
   `"waltz"` (3/4: root, chord, chord). The chord is the shape from `CHORDS` written as
   `<c e g>`; on the "oom" the hand plays the shape's bottom note. Fingers (5 3 1, 5 2 1) on each
   new shape, as `chord_fingers` does now.
2. **RH chords and 2/4 (Unit 2).** `rh_chords={"prob": p, "where": "long"|"strong", "min": n}`
   adds the two chord tones below a melody note that fit the RH position, making a three-note
   chord; a generalisation of `dyads`. A `"chorale"` texture puts block chords in both hands on
   every half note. 2/4: `BAR_LEN["2/4"] = 4`, `FULL_REST "R2"`, `STRONG (0,)`, rhythm table
   `R24` (`basic24`, `e24`), cadences, bass patterns for 2/4, checker `BAR`.
3. **High and low positions (Units 3-4).** New positions `RH_C5` (C5-G5), `RH_G5` (G5-D6),
   `RH_A3` (A3-E4, RH below middle C), `LH_C2` (C2-G2), `LH_F2` (F2-C3), `LH_C4` (C4-G4, LH
   above middle C). Octave moves use `shift_motion` with 7 (an octave) allowed. The keyboard
   pictures already widen to fit any position. A "LH tune, RH off-beat chords" texture
   (`accomp: "rh_offbeat"`, the Happy Farmer pattern) for Unit 4 Part B.
4. **Syncopation (Unit 5).** Rhythm tables `R44["synco"]` and `R24["synco24"]` built only from
   patterns that keep the middle of a 4/4 bar visible (e.g. 8th-quarter-8th-half,
   quarter-8th-quarter-8th-quarter); `anticip_prob` ties the bar's last eighth to the next bar's
   first note (a variant of `tie_prob` that allows short notes); `accents: True` puts `->` on
   syncopated notes.
5. **Sixteenths (Unit 6).** Durations are counted in eighths today. A part option `grid: 2`
   counts in sixteenths instead: `bar_len(part)`, `DUR16` (1 = "16", 3 = "8.", ...), and every
   threshold (long notes, rests, staccato, strong beats, bass patterns) scaled by the grid.
   Parts without `grid` keep the eighth grid, so nothing old changes. Rhythm tables `R24_16`,
   `R44_16`; sixteenth groups move only by step (`fast_motion`).
6. **Three sharps and flats (Unit 7).** `KEY_A`, `KEY_EB`, `KEY_FSM`, `KEY_CM`; positions for A
   major, E-flat major (E-flat F G A-flat B-flat), F-sharp minor and C minor; chord shapes. The
   existing `minor` option already spells the raised 7th: E-sharp (`eis`) in F-sharp minor and
   B-natural in C minor.
7. **Key change (Unit 8).** `modulate={"at": 5, "to": {key, key_acc, tonic, rh, lh},
   "show": "signature"|"accidentals"}`. The chord plan pivots: the last bar before the change is
   V7 of the new key. Spelling, positions and chords follow the key of each bar; the output
   prints `\key` at the change (LilyPond adds the cancelling naturals). Validation: the new
   key's leading note appears after the change; the piece ends on the new tonic, or on the old
   one for "away and back".
8. **Checker and build.** `check_pieces.py`: skip `\key x \major` and `\time` changes inside
   piece strings, add `VOLS[4]` rows (`MAX_LEAP` an octave from Unit 3), allow the new
   positions. `build.py`: `VOLUMES[4]` with its front-matter text; chord-shape pictures for the
   new keys; three-note chords in the LH fingerings.

### Pieces (candidates)

Public-domain sources from Mutopia (the composer is long out of copyright in every case). Each
is transcribed from the downloaded `.ly`, simplified to the unit's level (credit says
"simplified"), and checked with `check_pieces.py`. Sources marked PD have a public-domain
engraving; CC BY-SA ones are Mutopia engravings under that licence: we retype the notes
ourselves and name the source.

| Unit | Piece | Mutopia id | Licence | Notes |
| --- | --- | --- | --- | --- |
| 1 | Burgmüller, La Candeur, Op. 100 No. 1 | 202 | PD | LH held block chords; RH simplified |
| 2 | Tchaikovsky, Morning Prayer, Op. 39 No. 1 | 2032 | PD | chorale in both hands, G major 3/4 |
| 2 | Schumann, Soldiers' March, Op. 68 No. 2 | 650 | CC BY-SA | chords in both hands, 2/4 |
| 3 | Mozart, Sonata K. 545, first movement (opening) | 998 | CC BY-SA | high RH, Alberti bass |
| 3 | Schumann, Humming Song, Op. 68 No. 3 | 651 | CC BY-SA | tune and accompaniment in the RH register |
| 4 | Schumann, The Happy Farmer, Op. 68 No. 10 | 659 | CC BY-SA | LH tune low, RH off-beat chords |
| 5 | Joplin, The Entertainer (opening strain) | 263 | PD | 2/4 syncopation; heavily simplified |
| 6 | Bach, Musette in D, BWV Anh. 126 | 79 | PD | 2/4, sixteenths, moves to A major |
| 6 | Clementi, Sonatina Op. 36 No. 1, first movement | 804 | PD | sixteenth scales; moves to G major |
| 7 | Bach, Minuet in C minor, BWV Anh. 121 | 1613 | PD | three flats, B-natural; triplets simplified |
| 7 | Mozart, Sonata K. 331, Menuetto (opening) | 613 | PD | A major; much simplified |
| 8 | Bach, Minuet in G minor, BWV Anh. 115 | 76 | PD | G minor to B-flat major |
| 8 | Bach, Minuet in G, BWV Anh. 116 | 77 | PD | G major to D major |
| 8 | Tchaikovsky, Old French Song, Op. 39 No. 16 | 2080 | PD | G minor, 2/4, LH chords (review) |

That is 14 public-domain pieces; each unit adds one or two originals (8 bars, question and
answer, ending on the tonic) to reach 3-4 pieces.

### Build order

Same routine as Volume 3: feature 0 first, then for each unit add its parts and generator
features, write `content/v4unitNN.py`, run `check_pieces.py --vol 4 N`, build, look at every
page, run the regression check, commit and push. Seeds stay `volume * 1000 + unit id`
(4001-4008). Unit titles go into `VOLUME4` at the start, because the contents page prints them.

## Files

```
course/units.py         Course spec: hand positions, rhythm vocabularies, unit/part rules
course/generator.py     Exercise generator + validator + LilyPond emitter
course/build.py         Page template, keyboard diagrams, front matter, contents, book assembly
course/check_pieces.py  Checks hand-written pieces against what each unit has taught
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
```
Content modules: Volume 1 uses `content/unitNN.py`; Volume 2 uses `content/v2unitNN.py`;
Volume 3 uses `content/v3unitNN.py`. Volume 3 book: `python3 build.py --vol 3 1 2 3 4 5 6 7 8 9 10`.
Seeds are `volume * 1000 + unit id`.
- The front matter (title, how-to, contents) is included only when Unit 1 is part of the
  build.
- A unit with no `content/unitNN.py` builds as a **preview** (exercises plus placeholder text).
- Pages are filled greedily (`ly:minimal-breaking`). `\noPageBreak` after each `\break`
  keeps an exercise or piece on one page.

Output is deterministic: each unit uses seed `1000 + unit id`. **Don't change a finished
unit's parts:** that changes its exercises, and the user may already have printed them.
Units 1–2 were checked to be byte-identical after the Unit 7/10 generator features were
added; new options only use the random generator when they are switched on.

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
