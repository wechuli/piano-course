\version "2.25.12"
\include "schumann-romanze-op28-2-notes.ly"








\layout {
  \context {
    \Staff
    \RemoveEmptyStaves
    \mergeDifferentlyDottedOn
    \mergeDifferentlyHeadedOn
    \override Fingering.staff-padding = #'()
    \override Fingering.add-stem-support = ##t
  }
}

\score {
  \thePianoStaff
  \layout {}
  
}
