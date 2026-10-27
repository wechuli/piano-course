# Instructions for GitHub Copilot: "Read at Sight" piano course

This repository builds a print-ready piano sight-reading course with LilyPond. Volumes 1-6
are finished (Volume 6 is described in the README sections "Volume 6 (done)" and "Volume 6 plan
(as written before it was built)"). Read the README first (status,
plan, generator options, build commands, QA checklist), then `CLAUDE.md`.

## Rules that must never be broken

- **Never change the output of Volumes 1-6.** People may have printed them. Do not edit
  `content/unitNN.py`, `content/v2..v6unitNN.py`, the Volume 1-6 entries in
  `course/units.py`, or behaviour of `generator.py` / `gen5.py` / `gen6.py` that those volumes use.
- New generator options must not consume randomness unless they are switched on.
- Before every commit, from `course/`: `python check_identical.py` must print "identical" for
  every volume. If it reports a difference in any volume, undo the change that caused it.
- A new volume gets its own generator module that imports and extends the last one (as `gen6.py` extends `gen5.py`).

## How to build and check (run from `course/`)

```bash
python check_pieces.py --vol 6            # must print OK (add --verbose to see problems)
python build.py --vol 6 1                 # one unit (Unit 1 includes the front matter)
python build.py --vol 6 1 2 3 4 5 6 7 8   # the whole book
python check_identical.py                 # Volumes 1-6 must stay identical
```

The build must print no `WARN:` lines (LilyPond reports bar-length errors as warnings).

## Definition of done for a unit

1. `content/v6unitNN.py` written (intro, new ideas, tips, part notes, 4 pieces, checkpoint),
   in the same style as `content/v5unitNN.py`.
2. `check_pieces.py --vol 6` prints OK; the build has no `WARN:` lines.
3. Every page checked: render with `pdftoppm -r 45 -png` (pieces pages at about 100 dpi) and
   look at them if you can view images. Check for overlapping text, exercises or pieces split
   across pages, wrong clefs, key signatures or accidentals. If you cannot view images, say
   so in the pull request and list the pages a person should look at.
4. Contents page numbers match each unit's title page (`pdftotext`).
5. Unit PDF committed to `build/units/` ("Read at Sight - Vol6 - Unit N.pdf"); when the
   volume is finished, the book to `build/` ("Read at Sight - Volume 6.pdf").
6. README status table updated; fingerprints recorded with `check_identical.py --add 6 N`.

## Pieces

- Use only the public-domain or Creative Commons sources listed in the plan (the Mutopia
  Project, github.com/MutopiaProject/MutopiaProject). Credit every source in the piece's
  note, as the Volume 5 pieces do (Mutopia number and licence).
- Transcribe by running `convert-ly` on the Mutopia file and printing the music with
  `\displayLilyMusic`; shorten excerpts to a musical close.
- If a piece needs an exception in the checker (`allow_span`, `allow_leap`, ...), explain it
  in the piece's note for the reader.

## Working style

- Follow the plan's build order: shared groundwork (multi-staff scores, checker and build
  changes) first, then one unit at a time. Keep each pull request to one stage.
- Write plain, short English for the reader (an adult learning to sight-read).
- If something in the plan does not work musically or technically, change it, and record
  the change in the README ("Changes from plan"), as was done for Volume 5.
