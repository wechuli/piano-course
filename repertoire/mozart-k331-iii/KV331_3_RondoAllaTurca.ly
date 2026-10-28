\version "2.25.12"


\include "KV331_3_RondoAllaTurcaNotes.ly"

\score {
  \new PianoStaff
  <<
    \new Staff {
      \time 2/4
      
      \right
    }
    \new Dynamics {
      \override DynamicTextSpanner.style = #'none
      \dynamics
    }
    \new Staff {
      \left
    }
  >>
  \layout {}
  
}
