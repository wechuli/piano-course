# Piano sight-reading course ("Read at Sight")

Read README.md first: it holds the status, the five-volume plan, every generator option,
the build commands and the QA checklist.

Working rules for this repo:
- Never change the parts of a finished unit (Volumes 1-2): that regenerates its exercises,
  and the user may have printed them. New generator options must not consume randomness
  unless switched on (Volume 1 and 2 output must stay byte-identical).
- Before committing a unit: `python3 course/check_pieces.py --vol N` prints OK, the build has
  no `WARN:` lines, and every rendered page has been looked at (see README QA checklist).
- Commit finished PDFs to build/ ("Read at Sight - Volume N.pdf") and build/units/.
- Commit after each finished unit, with a clear message, so work survives across sessions.
