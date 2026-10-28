# Piano sight-reading course ("Read at Sight")

Read README.md first: it holds the status, the plan of all six volumes, every generator option,
the build commands and the QA checklist.

Working rules for this repo:
- Never change the parts of a finished unit (Volumes 1-6, all finished): that regenerates its exercises,
  and the user may have printed them. New generator options must not consume randomness
  unless switched on; Volume 5 uses course/gen5.py and Volume 6 course/gen6.py (Volume 1-6 output must stay byte-identical: `python3 course/check_identical.py`
  must print "identical" for every volume; run it from course/). Volume 7 (repertoire books 7A and 7B,
  course/rep7.py) is finished too: `python3 course/rep7.py identical` must print "identical".
- Before committing a unit: `python3 course/check_pieces.py --vol N` prints OK, the build has
  no `WARN:` lines, and every rendered page has been looked at (see README QA checklist).
- Commit finished PDFs to build/ ("Read at Sight - Volume N.pdf") and build/units/.
- Commit after each finished unit, with a clear message, so work survives across sessions.
