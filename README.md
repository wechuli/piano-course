# Read at Sight — piano sight-reading course (build system)

A print-ready A4 course book, typeset with LilyPond.

## Status (2026-10-27)

| Volume | Status | Book | Contents |
| --- | --- | --- | --- |
| 1 · First Steps | complete | `build/Read at Sight - Volume 1.pdf` (130 pp.) | 10 units, 322 exercises, 39 pieces |
| 2 · Moving Hands | complete | `build/Read at Sight - Volume 2.pdf` (133 pp.) | 10 units, 306 exercises, 35 pieces |
| 3 · Two Voices | complete | `build/Read at Sight - Volume 3.pdf` (159 pp.) | 10 units, 342 exercises, 32 pieces |
| 4 · Patterns and Keys | complete | `build/Read at Sight - Volume 4.pdf` (129 pp.) | 8 units, 272 exercises, 24 pieces |

Single units are in `build/units/` (`Read at Sight - VolN - Unit M.pdf`).

**Next: Volume 5 (Repertoire Reading).** Not planned in detail yet. Start by writing a
"Volume 5 plan" section like the Volume 3 and 4 ones below (units, parts, generator features,
pieces with verified sources), then build it unit by unit. Volumes 1-4 are protected by
`course/check_identical.py` (see "Build").

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
