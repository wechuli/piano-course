\version "2.25.12"
\include "english.ly"




     upper = \relative c'' {
       \clef treble
       \key f \major
       \time 2/4

       { \stemUp
\once \override TextScript.extra-offset = #'( -0.5 . 1 )
        c'16[^\markup \bold "Not Fast." a g f]~ f[ a g f] |
        g[ f d c]~ c] f, g a] |
        c,16[ g'8 f16] e8[ g] |
        <e g c>8 r16 c r d[ r e] 

	\stemNeutral
         \repeat volta 2 {
         r16 f[ d' <c a f>]~ <c a f>[ d <c a ds,>8] |
         r16 e,[ d' <c bf e,>]~ <c bf e,>[ d <c bf e,>8] |
         r16 <c a f>[ r <c a>] r <cf af>[ r <bf g>] |
         << { \stemUp a[ c d f] } \\
              { \stemDown f,8[ af] } >>
         <g c e>[ <bf e g>] |

          
          <a f' a>16[ gs' a c]~ c[ a g f] |
          g[ f d f]~ f[ d c a] |
          g[ g' f e] d[ a8 b16] |
          c8 r <c e c'> r |

          
          r16 f,[ d' <c a f>]~ <c a f>[ d <c a ds,>8] |
         r16 e,[ d' <c bf e,>]~ <c bf e,>[ d <c bf e,>8] |
         r16 <c a f>[ r <c a>] r <cf af>[ r <bf g>] |
         << { \stemUp a[ c d f] } \\
              { \stemDown f,8[ af] } >>
         <g c e>[ <bf e g>] |

         
          <a f' a>16[ gs' a c]~ c[ a g f] |
          g[ f d c]~ c[ d a g] |
          <f b,>[ g <a f b,>8] <g e bf>16[ <g e bf>8 <c, bf>16] |
          } % end repeat
         \alternative {
           { <a f'>8 r16 c r d[ r e] }
           { <f a,>8 c'16[ c] c8[ c] }
         }

% end first page

% page two

	\repeat volta 2 {
	e16[ d c bf] a[ bf8 g16] |
	f[ g a c,]~ c[ a' g f] |
	e[ f g c,]~ c[ bf' a g] |
	f[ a d c]~ c8[ c] |
	e16[ d c bf] a[ bf8 e,16]

	
	f[ e f a]~ a[ a g f] |
	e[ c' b a] gs[ b8 e,16] |
	a8 r <c bf e,>4 |
	e16[ d c bf] a[ bf8 g16] |
	f[ g a c,]~ c[ a' g f]

	
	e[ f g c,]~ c[ bf' a g] |
	f[ a d c]~ c8[ c] |
	<d bf>16[ g8 <d bf>16]~ <d bf>[ g <d bf>8] |
	<c a>16[ f8 <c a>16]~ <c a>[ f <c a>8] |
	bf16[ g d' c]~ c[ bf e,8]
	
	}

	\alternative {
		{ f[ c'16 c] c8[ c] }
		{ f, r16 c r d[ r e] }
	} \bar "||"
	r16 f[ d' <c a f>]~ <c a f>[ d <c a ds,>8] |
         r16 e,[ d' <c bf e,>]~ <c bf e,>[ d <c bf e,>8] |
         r16 <c a f>[ r <c a>] r <cf af>[ r <bf g>]

	
         << { \stemUp a[ c d f] } \\
              { \stemDown f,8[ af] } >>
         <g c e>[ <bf e g>] |
          <a f' a>16[ gs' a c]~ c[ a g f] |
          g[ f d f]~ f[ d c a] |
          g[ g' f e] d[ a8 b16] |
          c8 r <c e c'> r


% Page 3

          r16 f,[ d' <c a f>]~ <c a f>[ d <c a ds,>8] |
         r16 e,[ d' <c bf e,>]~ <c bf e,>[ d <c bf e,>8] |
         r16 <c a f>[ r <c a>] r <cf af>[ r <bf g>] |
         << { \stemUp a[ c d f] } \\
              { \stemDown f,8[ af] } >>
         <g c e>[ <bf e g>] |

         
          <a f' a>16[ gs' a c]~ c[ a g f] |
          g[ f d c]~ c[ d a g] |
          <f b,>[ g <a f b,>8] <g e bf>16[ <g e bf>8 <c, bf>16] |
	<a f'>8 r <a' ef' f>4

	
	\key bf \major
	\repeat volta 2 {
	<d bf>16[ g f ef] d[ c bf d] |
	c[ bf g f]~ f[ bf'8 g16] |
	f[ g f d] bf[ c d <c a>]~ |
	<c a>4. f,8

	
	d'16[ g f ef] d[ ef d c] |
	bf[ a g bf]~ bf[ d c bf] |
	a[ d f a] g[ f8 e16] |
	d8 r <f ef! a,>4

	
	<d bf>16[ g f ef] d[ c bf d] |
	c[ bf g f]~ f[ bf'8 g16] |
	f[ g f d] bf[ c d <c a>]~ |
	<c a>4. f,8


% Begin page 4

	d'16[ cs d ef] f[ e f fs] |
	g[ fs g bf]~ bf[ bf a g] |
	f[ d' bf f] g[ ef c a]
	} % end repeat
	\alternative {
		{ bf8[ e,16 f] g[ a bf c] }
		{ bf4. r16 <bf bf'>16~ }
	}

	
	\repeat volta 2 {
	<bf bf'>16[ ef <c c'> ef] g[ <bf bf,>8 ef,16] |
	<c c'>[ ef g <bf bf,>]~ <bf bf,>[ <c c,>8 <bf bf,>16] |
	<f f,>[ bf, <g g'> bf] d[ <f f,>8 bf,16] |
	<g g'>[ bf d <f f,>]~ <f f,>[ <g g,>8 bf,16]

	
	<f f'>16[ a <g g'> a] c[ <f f,>8 a,16] |
	<g g'>16[ a c <f f,>]~ <f f,>[ <g g,>8 a,16] |
	<f f'>16[ bf <g g'> bf] d[ <f f,>8 bf,16] |
	<g g'>16[ bf d <f f,>]~ <f f,>[ <f f,>8 <bf bf,>16]~

	

	<bf bf,>[ ef, <c c'> ef] g[ <bf bf,>8 ef,16] |
	<c c'>[ ef g <bf bf,>]~ <bf bf,>[ <c c,>8 <bf bf,>16] |
	<f f,>[ bf, <g g'> bf] d[ <f f,>8 bf,16] |
	<g g'>[ bf d <f f,>]~ <f f,>[ <f f,>8 <df e,>16]~

	
	<df e,>[ bf <df e,> bf] c[ <df e,>8 bf16] |
	<d! f,>16[ bf c <d f,>]~ <d f,>[ <d f,>8 <f f,>16]~ |
	<f f,>[ c <g g'> c] ef[ <a a,>8 <bf bf,>16]~
	} % end repeat
	\alternative {
		{ <bf bf,>4 r8. <bf bf,>16~ }
		{ <bf bf,>4 <bf d, bf>8 r }
	}
	\bar "|."
       }
     }
     
     lower = \relative c {
       \clef bass
       \key f \major
       \time 2/4
     
 	\stemDown \change Staff = upper
             c''16[ a g f]~ f[ a g f] |
             g[ f d c]~ c[ \change Staff = lower f, g a] \stemNeutral

       c,16[ g'8 f16] e8[ g] |
       c8 <c, c,>[ <d d,> <e e,>] 

        \repeat volta 2 {
        <f f,>4. <fs fs,>8 |
        <g g,>4. <gs gs,>8 |
        <a a,>[ <ef ef'>] <d d'>[ <df df'>] |
        <c c'>[ <b b'>] <bf bf'>[ <c c,>] |

        
        f,8[ <a' c f>] a,[ <a' c f>] |
        bf,[ <bf' d f>] a,[ <a' c f>] |
        b,[ <g' b f'>] g,[ <g' b f'>] |
        <c e> r <c c,>[ <c, c,>] |

        
        <f f,>4. <fs fs,>8 |
        <g g,>4. <gs gs,>8 |
        <a a,>[ <ef ef'>] <d d'>[ <df df'>] |
        <c c'>[ <b b'>] <bf bf'>[ <c c,>] |

        
        f,8[ <a' c f>] a,[ <a' c f>] |
        bf,[ <bf' d f>] a,[ <a' c f>] |
        <d, d,>[ <d d,>] <c c,>[ <e e,>]
        } % end repeat
        \alternative {
            { <f f,> <c c,>[ <d d,> <e e,>] }
            { <f f,> r r4 }
        }
% end page 1

% page two

	\repeat volta 2 {

	g8[ <bf c e>] c,[ <bf' c e>] |
	f[ <a c>] c,[ <a' c>] |
	g[ <bf c>] c,[ <bf' c>] |
	f[ <a c>] a[ <c f>] |
	g[ <bf c e>] e,[ <g bf cs>]

	
	d[ <f a d>] d[ <f a d>] |
	e[ <a c>] e[ <gs d'>] |
	<a c> r <c c,>4 |
	g8[ <bf c e>] c,[ <bf' c e>] |
	f[ <a c>] c,[ <a' c>]

	
	g[ <bf c>] c,[ <bf' c>] |
	f[ <a c>] c,[ <a' c>] |
	bf,[ <g' bf d>] bf,[ <g' bf d>] |
	c,[ <a' c>] c,[ <a' c>] |
	c,[ <bf' c e>] c,[ <g' bf c>]
	
	} % end repeat

	\alternative {
		{ <f a c> r r4 }
		{ <f a c>8 <c c,>[ <d d,> <e e,>] }
	} \bar "||"
	<f f,>4. <fs fs,>8 |
	<g g,>4. <gs gs,>8 |
	<a a,>[ <ef ef'>] <d d'>[ <df df'>] 

	
	<c c'>[ <b b'>] <bf bf'>[ <c c,>] |
	f,8[ <a' c f>] a,[ <a' c f>] |
	bf,[ <bf' d f>] a,[ <a' c f>] |
	b,[ <g' b f'>] g,[ <g' b f'>] |
	<c e> r <c c,>[ <c, c,>] |


% page Three
        <f f,>4. <fs fs,>8 |
        <g g,>4. <gs gs,>8 |
        <a a,>[ <ef ef'>] <d d'>[ <df df'>] |
        <c c'>[ <b b'>] <bf bf'>[ <c c,>] |

        
        f,8[ <a' c f>] a,[ <a' c f>] |
        bf,[ <bf' d f>] a,[ <a' c f>] |
        <d, d,>[ <d d,>] <c c,>[ <e e,>]
	<f f,> r <f f,>4

	
	\key bf \major
	\repeat volta 2 {
	bf,8[ <f' bf d>] d[ <f bf d>] |
	ef[ <g bf ef>] d[ <f bf d>] |
	bf,[ <f' bf d>] c[ <bf' c e>] |
	<f a ef'!>[ <f f,>] <g g,>[ <a a,>]

	
	<bf bf,>[ <f bf d>] d[ <fs c' d>] |
	g[ <bf d>] g[ <bf d>] |
	a[ <d f>] a[ <cs g'>] |
	<d f> r <f, f,>4

	
	<bf, bf,>8[ <f' bf d>] d[ <f bf d>] |
	ef[ <g bf ef>] d[ <f bf d>] |
	bf,[ <f' bf d>] c[ <bf' c e>] |
	<f a ef'!>[ <f f,>] <g g,>[ <a a,>]

%
% Begin Page 4

	<bf bf,>[ <f bf d>] d[ <f bf d>] |
	ef[ <g bf ef>] e[ <g bf cs>] |
	f[ <bf d>] f,[ <f' a ef'>]
	} % end repeat
	\alternative {
		{ <bf d> r r4 }
		{ << d4. \\ {bf8[ <bf, bf,>] <c c,>[ <d d,>] } >> }
	}

	
	\repeat volta 2 {
	<ef ef,>[ <g bf ef>] <g bf ef>[ <d d,>] |
	<ef ef,>[ <f f,>] <g g,>[ <a a,>] |
	<bf bf,>[ <d bf f>] <d bf f>[ <cs cs,>] |
	<d d,>[ <d bf f>] <d bf f>[ <f, f,>]

	
	<c c'>[ <f a ef'>] <f a ef'>[ <f f,>] |
	<c c'>[ <f a ef'>] <c c'>[ <cs cs'>] |
	<d d'>[ <f bf d>] <f bf d>[ <f f,>] |
	<bf bf,>[ <d bf f>] <d bf f>[ <d, d,>]

	
	<ef ef,>[ <g bf ef>] <g bf ef>[ <d d,>] |
	<ef ef,>[ <f f,>] <g g,>[ <a a,>] |
	<bf bf,>[ <d bf f>] f,,[ <f' bf d>] |
	bf,[ <f' bf d>] f,[ <f' bf d>]

	
	<gf gf,>[ <df df'>] <bf bf'>[ <gf gf'>] |
	<f f'>[ <d'! d'!>] <bf bf'>[ <f f'>] |
	<c' c'>[ <f a ef'>] <f f,>[ <f a ef'>] |
	} % end repeat
	\alternative {
		{ << {d'4 s} \\ {bf8[ <bf, bf,>] <c c,>[ <d d,>] } >> }
		{ << {d'4 s8} \\ {bf8[ <f f,>] <bf, bf,> } >> r }
	}
	\bar "|."
     }
     
     dynamics = {
          \skip 2 * 4 |
          \skip 2 * 4 |
          \skip 2 * 4 |
          \skip 2 * 4 |
          \skip 2 * 5 |

% page 2

	\skip 2 * 5 |
	\skip 2 * 5 |
	\skip 2 * 5 |
	\skip 2 % repeat 8va
	\skip 2 * 4 |
	\skip 2 * 5 |

% page 3

	\skip 2 * 4 |
	\skip 2 * 4 |
	\skip 2 * 4 |
	\skip 2 * 4 |
	\skip 2 * 4 |

% page 4

	\skip 2 * 5 |
	\skip 2 * 4 |
	\skip 2 * 4 |
	\skip 2 * 4 |
	\skip 2 * 5

%       s2\fff\> s4
%       s\!\pp
     }
     
     pedal = {
%       s2\sustainOn s2\sustainOff
     }
     
     \score {
       \new PianoStaff <<
         \new Staff = "upper" \upper
         \new Dynamics = "dynamics" \dynamics
         \new Staff = "lower" <<
           \clef bass
           \lower
         >>
         \new Dynamics = "pedal" \pedal
       >>
       \layout {
         % [Convert-ly] The Dynamics context is now included by default.
         \context {
           \PianoStaff
           \accepts Dynamics
         }
       }
     }
     
