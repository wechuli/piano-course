\version "2.25.12"
                             %                 "PRELUDE Op28 No4"
                             %                 by Frederic Chopin
                             %
                             %
                             
\include "english.ly"




%


barRest =  {\skip 2 |}

paperOFF = { \set Score.skipTypesetting = ##t }
paperON = { \set Score.skipTypesetting = ##f }

hidePP = \tweak #'stencil ##f \pp
ppWhiteOut = \markup { \whiteout { \dynamic "pp" } }

posBeamA = \once \override Beam.damping = #2

shpSlurA = \shape #'( ((0 . -0.3) (8 . 0.5) (0 . 1) (0 . 0))
                      ((0 . 0) (0 . 0) (-3 . -0.7) (0 . -0.7)) ) PhrasingSlur
shpSlurB = \shape #'((0 . 2.8) (0 . 1) (0 . -0.6) (0 . 0)) PhrasingSlur
shpSlurC = \shape #'( ((0.8 . 0) (0.8 . 0) (0 . 0) (0 . 0))
                      ((0 . -0.5) (0 . -0.5) (-1 . 1) (-0.5 . 2)) ) PhrasingSlur
shpSlurD = \shape #'( ((0.3 . 0) (3 . 1) (-3 . 1) (0 . 0))
                      ((0 . 0) (0 . 0.3) (0 . 0.8) (0 . -0.7)) ) PhrasingSlur

shpSlurE = \shape #'((0 . 1) (0 . 0.6) (0 . 0.5) (0 . 0)) PhrasingSlur

posScriptA = \once \override Script.extra-offset = #'(-3 . 0)
posScriptB = \once \override TextScript.extra-offset = #'(-1.8 . -2.6)
posAccidental = \once \override Staff.AccidentalPlacement.right-padding = #1.5

playRH =  \relative c' {
    \clef treble
    \time 2/2
    \key e \minor

                                % 0
    \phrasingSlurUp
    \partial 4 \posBeamA \shpSlurA b8.\(\p b'16_\markup{ \italic \whiteout "espressivo"} |

                                % 1 - 4
    b2. c4 |
    b2. c4 |
    b2. c4 |
    b2. bf4 |

                                % 5 - 8
    a2. b!4 |
    a2. b4 |
    a2. b8. a16 |
    a2.\)
    \shpSlurB
    gs4->\(~ |

                                % 9 - 12
    gs4 << {a8 b} \\
           {s32\< s s s s s s s\!} >> d8\> c e, a\! |           %% double voice to give hairpin a nicer length
    fs2.\) a4( |
    fs2.) \acciaccatura b8 \shpSlurC a4_\( |
    g!8 fs c\<^> b ds fs\! \tuplet 3/2 {d'\> c b\!} |

                                % 13 - 15
    \shpSlurD b2.\p\)\( c4 |
    b2. c4 |
    b2. c4 |
                                % 16 - 20
    << {  b8. as16 as4 } \\
       { s16\< s s s s s\! s s } >> \posScriptA \posAccidental gss'4\turn\> fs8. e16\! |  %% double voice to give hairpin a nicer length
    %\once\override Staff.Hairpin.extra-offset = #'(0 . 2.5)
    e8\f\< ds c' ds,\! ds\> e g b, |
    \stemUp
    d! c \tupletDown \tuplet 3/2 {e e, a\! } fs4._\markup{ \italic "dim." } a8 |
    \stemNeutral
    fs2.\p\) \acciaccatura b8 a4\( |
    fs2.~ fs8.\< e16\! |

                                % 21 - 23
    e2._\markup{\italic smorz.}\> fs4 |
    e2.\! fs4 |
    e2\) r\fermata |

                                % 24 - 25
    << { 
         \posScriptB \shpSlurE e2^\(-\hidePP_\ppWhiteOut ds | e1\)\fermata
       } \\ {
         \change Staff = "lh" \stemUp
         \crossStaff { <fs, b e,>2 <b ds, fs> } | <g b e,>1
    } >>
    \bar "|."
}


playLH =  \relative c' {
    \clef bass
    \time 2/2
    \key e \minor
                                % 0
    \partial 4 r4 |

                                % 1 - 4
    <g b e>8\sustainOn\(-\hidePP <g b e>8 <g b e>8 <g b e>8 <g b e>8 <g b e>8 <g b e>8\sustainOff <g b e>8 |
    <fs a e'>\sustainOn <fs a e'> <fs a e'> <fs a e'>\sustainOff <fs a ds>\sustainOn <fs a ds> <fs a ds> <fs a ds>\sustainOff |
    <f a ds>\sustainOn <f a ds> <f a ds> <f a ds>\sustainOff <f a d> <f a d> <f gs d'> <f gs d'> |
    <e gs d'>\sustainOn <e gs d'> <e gs d'> <e gs d'>\sustainOff <e g d'> <e g d'> <e g cs> <e g cs> |

                                % 5 - 8
    <e g c>\sustainOn <e g c> <e g c> <e g c>\sustainOff <e fs c'> <e fs c'> <e fs c'> <e fs c'> |
    <e fs c'>\sustainOn <e fs c'> <e fs c'> <e fs c'>\sustainOff <ds fs c'>\sustainOn <ds fs c'> <ds fs c'> <ds fs c'>\sustainOff |
    <d fs c'>\sustainOn <d fs c'> <d fs c'> <d fs c'> <d fs c'> <d fs c'> <d fs c'>\sustainOff <d fs c'> |
    <d f c'>\sustainOn <d f c'> <d f c'> <d f c'>\sustainOff <d f b> <d f b> <d f b> <d f b> |

                                % 9 - 12
    <c e b'> <c e b'> <c e a> <c e a> <c e a> <c e a> <c e a> <c e a> |
    <b e a> <b e a> <b ds a'> <b ds a'> <c e a>\sustainOn <c e a> <c e a> <c e a>\sustainOff |
    <b ds a'>\sustainOn <b ds a'> <b ds a'> <b ds a'>\sustainOff <c e a>\sustainOn <c e a> <c e a> <c e a>\sustainOff |
    <b ds a'>4\) r r2 |

                                % 13 - 16
    <g' b e>8\sustainOn\( <g b e>8 <g b e>8 <g b e>8 <g b e>8 <g b e>8 <g b e>8\sustainOff <g b e>8 |
    <fs a e'>\sustainOn <fs a e'> <fs a e'> <fs a e'>\sustainOff <f a ds>\sustainOn <f a ds> <f a ds> <f a ds>\sustainOff |
    <f gs ds'> <f gs ds'> <f gs d'> <f gs d'> <e gs d'>\sustainOn <e gs d'> <e gs d'> <e gs d'>\sustainOff |
    <e g d'> <e g d'> <e g cs> <e g cs> <cs e as> <cs e as> <c e a> <c e a> |

                                % 17 - 20
    <b, b'>\)\sustainOn <a'' c fs a>\( <a c fs a> <a c fs a>\sustainOff <g b ds fs> <g b e> <g b e> <g b e> |
    \override Staff.PianoPedalBracket.shorten-pair = #'(0 . -2.0)
    <a c e>[ <a c e>] a,\sustainOn <e' fs c'>\sustainOff <b e b'> <b e b'> <c e a> <c e a> |
    \revert Staff.PianoPedalBracket.shorten-pair
    <b e b'>\sustainOn <b e b'> <b e b'> <b e b'>\sustainOff <c e a> <c e a> <c e a> <c e a> |
    <b e b'>\sustainOn <b e b'> <b e b'> <b e b'>\sustainOff <b ds b'>\sustainOn <b ds b'> <b ds a'> <b ds a'>\sustainOff |

                                % 21 - 23
    <c g'>\sustainOn <c g'> <c g'> <c g'> <c bf'> <c bf'> <c e a>\sustainOff <c e a> |
    <b e a> <b e a> <b e gs> <b e gs> <b e g>\sustainOn <b e g> <b e g> <b e g>\sustainOff |
    <bf c g'>2\) r\fermata |

                                % 24 - 25
        \relative b,, { \stemDown <b! b'!>2_( <b b'fs> | <e, e'>1)_\fermata | }
        
}

superMarks =  {
    \partial 4 s4^\markup{ \center-align \bold\large \raise #1 "Largo" }  |
    \repeat unfold 15 { s1 }
    \set decrescendoText = \markup { \italic "stretto" }
    \set decrescendoSpanner = #'text
    s4 s8^\> s s2 |
    s4 s s s  |
    s s s\! s |
}


scoreAll =  {
    \new PianoStaff {
        \set PianoStaff.midiInstrument = "acoustic grand"
        <<
            \context Staff = "rh" {
%                \accidentalStyle modern
                \override Staff.TextScript.staff-padding = #2
                \override Staff.DynamicLineSpanner.staff-padding = #3  % (forced-distance - 6) / 2
                \override Staff.Hairpin.minimum-length = #3
                <<
                    \playRH
                    \superMarks
                >>
            }
            \context Staff = "lh" {
%                \accidentalStyle modern
                \set Staff.pedalSustainStyle = #'bracket
                \override Staff.PianoPedalBracket.shorten-pair = #'(0 . -1.0)
                \playLH
            }
        >>
    }
}

\score
{
    
    {
        \scoreAll
    }
    \layout {
      \context {
        \PianoStaff
        \consists #Span_stem_engraver
  }
    }
    
}

