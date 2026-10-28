\version "2.25.12"

\include "english.ly"



%{ Maintenance note:
   This update includes several pitch edits so that this edition
   matches several scans available in IMSLP that most likely were not
   available when this was transcribed. All changes of this type have
   been marked "Breitkopf" in the comment since Breitkopf was the
   specific reference I used.

   See: http://imslp.org/wiki/Special:ImagefromIndex/56441
   -gl
%}



upper = \relative c' {
	\time 2/2
	\key c \minor
	\override TupletBracket.bracket-visibility = ##f 
	\override TextScript.padding = #2
	\override DynamicText.padding = #3.5
    \tempo "Molto allegro" 2 = 84
	
	c2^^-\f_\markup { \translate #(cons 2 1) \italic ten. } e-flat4-\staccatissimo g-\staccatissimo
	
	c-\staccatissimo e-flat-\staccatissimo r8. e-flat16-.-\p e-flat8-(-[-\trill d16 e-flat-]
	
	g4 c,-.-) c-. c-.
	
	a-flat'-( b,-)-. b-. r       % gl: a->a-flat, Breitkopf
	
	% 5
	g,2^^-\f_\markup { \translate #(cons 2 1) \italic ten. } b4-\staccatissimo d-\staccatissimo
	
	g-\staccatissimo b-\staccatissimo r8. d16-.-\p d8-(-[-\trill c16 d-]
	
	f4 b,-.-) b-. b-.
	
	g'-( c,-)-. c-. r
	
	g2.-\f << { \voiceOne e-flat'4-~ } \\ { g,4-\p-( } >>
		
	% 10
	<< { e-flat' d2 c4-~ } \\ { f-sharp,4 f e-\< e-flat } >>
	
	<< { c'-( b^.-) } \\ { d,2-)-\f-\! } >> r4
	<< { g'-( } \\ { e-flat-~-\p } >>
	
	<< { f-sharp f e e-flat } \\ { e-flat d2-\< c4-~ } >>
	
	<< { d2-)-\f } \\ { c4-(-\! b^.-) } >> r < b d a-flat' >->-~
	
	< b d a-flat' >-( < c e-flat g >-) r8. g16-[-( d'8.-.-) f16-]-(
	
	%15
	e-flat16-\trill-[ d e-flat f-] g4-.-) r < b, d a-flat' >->-~
	
	< b d a-flat' >-( < c e-flat g >-)-. r8. f16-[-( b8.-.-) f'16-]-(
	
	e-flat8-[-\fp g, c e-flat,-]-) r f-[-(-\p a-flat d,-]-)
	
	r e-flat-[-( g c,-]-) r d-[-( f b,-]-)
	
	c2^^ e-flat4-\staccatissimo g-\staccatissimo
	
	% 20
	c-\staccatissimo e-flat-\staccatissimo r8. e-flat,16-. e-flat8-\trill-[-( d16 e-flat-]
	
	\tuplet 3/2 { a-flat!8_>-[ b-flat c-] } \tuplet 3/2 { b-flat-[ a-flat g-] } \tuplet 3/2 { f-[ g a-flat-] } \tuplet 3/2 { g-[ f e-flat-] }
	
	
	\tuplet 3/2 { d-[ e-flat f-] } \tuplet 3/2 { e-flat-[ d c-] } \tuplet 3/2 { b-flat-[-\> c b-flat-] } \tuplet 3/2 { a-flat-[ b-flat a-flat-]-\! }
	
	g4.-\mp-)-( a-flat32-[ g f g-] a-flat4 d,
	
	e-flat8-.-[-)^\< g-.-]^\! b-flat4.-(^\> a8-[^\! a-flat f-sharp-]
	
	% 25
	g4. a-flat32-[ g f! g-] a-flat4 d,
	
	e-flat8-.-)-[ e-flat'-\mf-(-\> d c-] b-flat-[ a a-flat f-sharp-]-\!
	
	g4 b-flat-) r8 b-flat-.-[-(_\markup { \italic cresc. } b-flat-. b-flat-.-]-)
	
	f'_>-[-( e-flat-)-] e-flat4 r8 e-flat-.-[-( e-flat-. e-flat-.-]-)
	
	e-flat8-\f-[-( f16 g-] f8-.-)-[ e-flat-.-] d-.-[-\> c-. b-flat-. a-.-\!-]
	
	% 30
	c4-(-\> b-flat-)-\! r-\p e-flat8-. e-flat-.
	
	b-flat'4 r r e-flat,8-. e-flat-.
	
	b-flat'4 r r e-flat,8-. e-flat-.
	
	b-flat'4-\< e-flat,8-. e-flat-. b-flat'4 e-flat,8-. e-flat-.
	
	b-flat'4-.-( b-flat-. b-flat-. b-flat-.-)-\!
	
	% 35
	b-flat8-[-(-\> a a-flat f-] b-flat8-[ a a-flat f-]-)-\!
	
	e-flat4.-\p-( f16 e-flat d4 e-flat
	
	e2-\> f4-)-\! r
	
	\clef "bass"
	\relative c' {
	a-flat4.-(^\markup { \italic cantabile } g16 a-flat b-flat8-[ a-flat g f-]-)
	
	e-flat2-(-\> d4-)-\! r
	}
	
	% 40
	\clef "treble"
	f4.-( g16 f e-flat4 f
	
	f-sharp2 g4-) r4
	
	\clef "bass"
	\relative c' {
	b-flat4.-( a16-[ b-flat-]-\> c8-[ b-flat a-flat g-]-)-\!
	
	f2-(-\> e-flat4-)-\! r
	}
	
	\clef "treble"
	< b-flat, b-flat' >2^^-\mf-\< < b b' >^^
	
	% 45
	< c c' >4-\f-(-\! < d-flat d-flat' >-\fz-) r2
	
	r8 c'-\p-[-( b-flat a-flat-] g-[ f g a-flat-]-)
	
	<< { e-flat2.-( g8 f \stemDown e-flat4-) } \\ { s2. d4 } >>
	
	r8 e-flat-( d-[ d-flat-\< c c-flat-]-\!
	%%% NOTE: I bumped beat 1 up to the previous bar. Hope you don't mind.
	
	b-flat2-^-\mf-)-\< < b, b' >^^
	
	% 50
	< c c' >4-\f-(-\! < d-flat d-flat' >-\fz-) r2
	
	\override TupletBracket.transparent = ##t
	\tuplet 3/2 { c'8-\f-[ f g,-] } \tuplet 3/2 { a-flat-[ c e,-] } \tuplet 3/2 { f-[ a-flat b,-] } \tuplet 3/2 { c-[ f g,-] }
	
	\clef "bass"
	\relative c' {
	\tuplet 3/2 { a-flat-[ c e,-] } \tuplet 3/2 { f-[ a-flat b,-] } \tuplet 3/2 { c-[ f g,-] } \tuplet 3/2 { a-flat-[ c e,-] }
	
	\change Staff = "down"
	\clef bass
	r4 r8 c8-( a-flat'-[  f c' a-flat-]
	
	f'-[ c a-flat' f-]
	\change Staff = "up"
	\clef "treble"
	c'8-[ a-flat f' c-]
%	\revert Slur.beautiful
	
	% 55
	a-flat'-[ f c' a-flat-] f'-[ c a-flat' f-]
	
	c'4_>-) r e-flat_> r
	
	r8 b-flat,-\p-[-( b-flat' a-] a-flat-[ g-\< g-flat f-]-)-\!
	
	f-(-\> e-flat-)-\! e-flat2-( << { g!8 f } \\ { d4 } >>
	
	e-flat4-) r8 e-flat-( e_>-[ f-]-) r8 f-(
	
	% 60
	f-sharp_> g-) r8 g-(_\markup { \italic cresc. } b-flat_>-[ a-flat-]-) r8 a-flat-(
	
	a b-flat_>-) r b-flat-( b_>-[ c-]-) r e-flat
	
	e-flat_>-\f-( e-flat,-\> e-flat2 g8 f-\!
	
	e-flat-.-\f-) e-flat-. e-flat-\trill-[-( d16 e-flat-] f8-.-)-[ f-.-] f-\trill-[-( e-flat16 f-]
	
	g8-.-\f-)_\markup { \translate #(cons 2.2 0) \italic cresc. } g-. g-\trill-[-( f16 g-] a-flat8-.-)-[ a-flat-.-] a-flat-\trill-[-( g16 a-flat-]
	
	% 65
	\tuplet 3/2 { b-flat8-\ff-)-[-( c d-] } \tuplet 3/2 { e-flat-[ d c-] } \tuplet 3/2 { b-flat-[ a-flat g-] } \tuplet 3/2 { f-[ e-flat d-] }
	
	c4-.-) < e-flat a-flat c >-. < e-flat g b-flat >-. < f, a-flat d >-.
	
	< g e-flat' >-. \tuplet 3/2 { b-flat'8_>-[-( a-flat g-] } \tuplet 3/2 { f-[ e-flat d-] } \tuplet 3/2 { e-flat-[ d-flat b-] }
	
	c4-.-) \tuplet 3/2 { c'8_>-[-( b-flat a-flat-] } \tuplet 3/2 { g-[ f e-flat-] } \tuplet 3/2 { d!-[ a-flat' f-] }
	
	e-flat4-.-) \tuplet 3/2 { b-flat8->-\mf-[-( a-flat g-] } \tuplet 3/2 { f-[ e-flat d-] } \tuplet 3/2 { e-flat-[ d-flat b-] }
	
	% 70
	c4-.-) \tuplet 3/2 { c'8_>-[-( b-flat! a-flat-] } \tuplet 3/2 { g-[ f e-flat-] } \tuplet 3/2 { d!-[ a-flat' f-] }
	
	e-flat2^^-\f-) g4-\staccatissimo b-flat-\staccatissimo
	
	e-flat-\staccatissimo g-\staccatissimo r8. g16-. g8-\trill-[-( f16 g-]
	
	b-flat4 e-flat,-.-)_\markup { \italic dim. } e-flat-. e-flat-.
	
	a-flat-\p-( b,-) b r
	
	\bar ":..:"
	
	% 75
	c,2^^-\f e4-\staccatissimo g-\staccatissimo
	
	c-\staccatissimo e-\staccatissimo r8. g16-. g8-\trill-[-( f16 g-]
	
	\tuplet 3/2 { b-flat8_>-)-[-( c d-flat-] } \tuplet 3/2 { c-[ b-flat a-flat-] } \tuplet 3/2 { g-[ a-flat b-flat-] } \tuplet 3/2 { a-flat-[ g f-] }
	
	\tuplet 3/2 { e-[ g e-] } \tuplet 3/2 { d-flat-[ e d-flat-] } \tuplet 3/2 { b-flat-[-\> d-flat b-flat-] } \tuplet 3/2 { g-[ b-flat g-]-\! }
	
	a-flat4.-)-\mp-( b-flat32 a-flat g a-flat b-flat4 e,
	
	\override TupletBracket.transparent = ##t
	
	% 80
	f8-.-) a-flat-. c4.-(-\> b8-\! b-flat g
	
	a-flat4. b-flat32 a-flat g a-flat b-flat4 e,
	
	f8-.-)-[ f'-\mf-(-\> e-flat! d-flat-] c-[ b b-flat g-]-)-\!
	
	a-flat2^^-\f c4-\staccatissimo f-\staccatissimo
	
	a-flat-\staccatissimo c-\staccatissimo r2
	
	% 85
	\tuplet 3/2 { c8_>-[-( d e-flat-] } \tuplet 3/2 { d-[ c b-flat-] } \tuplet 3/2 { a-[ b-flat c-] } \tuplet 3/2 { b-flat-[ a g-]-) }
	
	\tuplet 3/2 { f-sharp-[-( a f-sharp-] } \tuplet 3/2 { e-flat-[ a e-flat-] } \tuplet 3/2 { d-[ a' d,-] } \tuplet 3/2 { c-[ a' c,-] }
	
	b-flat2^^-) d4-\staccatissimo g-\staccatissimo
	
	b-flat-\staccatissimo d-\staccatissimo r2
	
	b,2^^ d4-\staccatissimo f-\staccatissimo
	
	% 90
	b-\staccatissimo d-\staccatissimo r2
	
	c,2^^ e-flat4-\staccatissimo g-\staccatissimo
	
	c-\staccatissimo e-flat-\staccatissimo r2
	
	< d,, d' >2_-^^ < f f' >4-\staccatissimo < g g' >-\staccatissimo
	
	< d' d' >-\staccatissimo < f f' >-\staccatissimo r2
	
	% 95
	f4-.-\p a-flat-. r2
	
	d,4-. f-. r2
	
	b,4-._\markup { \italic calando } d-. d,-. f-.
	
	\clef "bass"
	< d, f a-flat >1-\pp-(
	
	< d f g >4-) r4 r2-\fermata
	
	% 100
	\clef "treble"
	c'2^^-\f-1 e-flat4-\staccatissimo-2 g-\staccatissimo-1
	
	c-\staccatissimo-2 e-flat-\staccatissimo-4 r8. e-flat16-.-\p e-flat8-(-[-\trill d16 e-flat-]
	
	g4 c,-.-) c-. c-.
	
	a-flat'-( b,-)-. b-. r       % a->a-flat, Breitkopf
	
	g,2^^-\f-1 b4-\staccatissimo-2 d-\staccatissimo-1
	
	% 105
	g-\staccatissimo-2 b-\staccatissimo-4 r8. d16-.-\p d8-(-[-\trill c16 d-]
	
	f4 b,-.-) b-. b-.
	
	g'-( c,-)-. c-. r
	
	g2.-\f << { \voiceOne e-flat'4-~ } \\ { g,4-( } >>
		
	<< { e-flat' d2 c4-~ } \\ { f-sharp,4 f e e-flat } >>
	
	% 110
	<< { c'-( b^.-) } \\ { d,2-)-\f } >> r4 << { g'-( } \\ { e-flat-~-\p } >>
	
	<< { f-sharp f-\< e e-flat } \\ { e-flat d2 c4-~ } >>
	
	<< { d2-\f-)-\! } \\ { c4-( b^.-) } >> r < b d a-flat' >->-~
	
	< b d a-flat' >-( < c e-flat g >-) r8. g16-[-( d'8.-.-) f16-]-(

	e-flat16-\trill-[ d e-flat f-] g4-.-) r < b, d a-flat' >->-~
	
	% 115
	< b d a-flat' >-( < c e-flat g >-)-. r8. f16-[-( b8.-.-) f'16-]-(
	
	e-flat8-[-\fp g, c e-flat,-]-) r f-[-(-\p a-flat d,-]-)
	
	r e-flat-[-( g c,-]-) r d-[-( f b,-]-)
	
	c2^^-\f e-flat4-\staccatissimo g-\staccatissimo
	
	c-\staccatissimo e-flat-\staccatissimo < c, a-flat' >-\staccatissimo < e-flat c' >-\staccatissimo
	
	% 120
	< a-flat, f' >-\staccatissimo < c a-flat' >-\staccatissimo < f, d-flat' >-\staccatissimo < a-flat f' >-\staccatissimo
	
	c2.-\mp-( a-flat'4-)
	
	a-flat4.-( f8 d-flat4-) r
	
	c2-~ c8-[ a-flat'-( b-flat a-flat-]-)

	a-flat4.-( f8 d-flat4-) d-flat4-~
		
	% 125
	d-flat8-[ b-( c d-] f!-[ e-flat d c-]
	
	g'4-) r-\p r c,8-. c-.
	
	g'4 r r c,8-. c-.
	
	g'4-\< c,8 c g'4 c,8 c

	g'4-.-( g-. g-. g-.-)-\!
		
	% 130
	g8-[-(-\> f-sharp f d-] g-[ f-sharp f d-.-]-)-\!
	
	c4.-\p-( d16 c b4 c
	
	c-sharp2-\> d4-)-\! r
	
	\clef "bass"
	\relative c' {
	f,4.-( e16 f g8-[ f e-flat d-]-)
	
	c2-(-\> b4-)-\! r
	}
	
	% 135
	\clef "treble"
	d4.-( e-flat32 d c d e-flat4 f
	
	f-sharp2-\> g4-)-\! r4
	
	\clef "bass"
	\relative c' {
	g4.-( f-sharp16-[ g-] a-flat8-[ g f e-flat-]-)
	
	d2-(-\> c4-)-\! r
	}
	
	\clef "treble"
	< c, c' >2^^-\mf-(-\< < d-flat d-flat' >^^-)
	
	% 140
	< c c' >4-\f-(-\! < e-flat e-flat' >-\fz-) r8 e-flat'-\p-[-( d! c-]
	
	b_> d f,4-) r8 a-flat-[-( g f-]
	
	e_> g b-flat,!4-) r8 d-flat-[-( c b-flat-]
	
	a-flat-.-)-[-\< a-flat'-( g f-] e-flat-[ d e-flat f-]-)-\!
	
	c2.-( << { e-flat8 d } \\ { b4 } >>
	
	% 145
	\slurUp
	< c, c' >2^^-\mf-)-(-\< < d-flat d-flat' >^^-)-\!
	
	< c c' >4-\f-(
	\slurNeutral < e-flat e-flat' >-\fz-) r8 e-flat'-\p-[-( d! c-]
	
	b^> d f,4-) r8 a-flat-[-( g f-]
	
	e g b-flat,4-) r8 d-flat-[-(_\markup { \italic cresc. } c b-flat-]-)
	
	\clef "bass"
	\tuplet 3/2 { a-flat8-\f-[-( c e,-] } \tuplet 3/2 { f-[ a-flat b,-] } \tuplet 3/2 { c-[ f g,-] } \tuplet 3/2 { a-flat-[ c e,-] }
	
	% 150
	f8-) r r4 r2

	\change Staff = "down"
	R1	
	
	R
	
	R
	
	\change Staff = "up"
	\clef "treble"
	r8-\p g''-[-(-\< g' f-sharp-] f-[ e e-flat d-]-)-\!
	
	% 155
	d-( c-) << { c2( e-flat8 d } \\ { s2 b4 } >>
	
	<< { c4-\p-) } \\ { c4 } >> r8 c-( c-sharp_>-[ d-]-) r8 d-(
	
	f_>_\markup { \italic cresc. } e-flat-) r e-flat-( e_>-[ f-]-) r f-(
	
	f-sharp_> g-) r g-( b-flat_>-[ a-flat-]-) r c
	
	c-\f-(-\> c, c2 e-flat8 d
	
	% 160
	c-.-\f-) c-. c-\trill-[-( b16 c-] d8-.-)-[ d-.-] d-\trill-[-( c16 d-]
	
	e-flat8-.-)_\markup { \italic cresc. } e-flat-. e-flat-\trill-[-( d16 e-flat-] f8-.-)-[ f-.-] f-\trill-[-( e-flat16 f-]
	
	\tuplet 3/2 { g8-\ff-)-[-( c b-flat!-] } \tuplet 3/2 { a-flat-[ g f-] } \tuplet 3/2 { e-flat-[ d c-] } \tuplet 3/2 { b-flat-[ a-flat g-] }
	
	a-flat4-.-) < c f a-flat >-. < c e-flat g >-. < d, f b >-.
	
	< e-flat c' >-. \tuplet 3/2 { g'8_>-\f-[-( f-sharp a-flat-] } \tuplet 3/2 { g-[ f e-flat-] } \tuplet 3/2 { d-[ e-flat c-] }
	
	% 165
  % b-flat->b, Breitkopf
	b4-.-) \tuplet 3/2 { f'8_>-[-( e g-] } \tuplet 3/2 { f-[ e-flat d-] } \tuplet 3/2 { c-[ b d-] }
	
	c4-.-) \tuplet 3/2 { g'8_>-[-( f-sharp a-flat-] } \tuplet 3/2 { g-[ f e-flat-] } \tuplet 3/2 { d-[ e-flat c-] }
	
	\tuplet 3/2 { a-flat'-\fz-[ g f-] } \tuplet 3/2 { e-flat-[ d c-] } \tuplet 3/2 { b-[ a-flat g-] } \tuplet 3/2 { f-[ e-flat d-] }
	\bar ":|."
	
	c4-\ff-) r r2
	
	c'2_> e-flat4-\staccatissimo g-\staccatissimo
	
	% 170
	c-\staccatissimo e-flat-\staccatissimo r2
	
	a-flat,,2_> c4-\staccatissimo e-flat-\staccatissimo
	
	a-\staccatissimo c-\staccatissimo r \tuplet 3/2 { c8-[-( e-flat c-] }
	
	\tuplet 3/2 { a-[ c a-] } \tuplet 3/2 { f-sharp-[ a f-sharp-] } \tuplet 3/2 { e-flat-[ f-sharp e-flat-] } \tuplet 3/2 { c-[ e-flat c-] }
	
	g4-.-\f-) g'2_>-( f!16 e-flat d c-)
	
	% 175
    #(define afterGraceFraction (cons 31 32))
	\appoggiatura e-flat8 \afterGrace d1 \startTrillSpan ( { c16[ d] ) \stopTrillSpan }
	%\grace e-flat8-( d1-\trill-)-(-\> \bar "" \grace { c16-[ d-]-) } \bar "|"

	\tuplet 3/2 { r8 c-\p-[-( c'-]-) } \tuplet 3/2 { r8 b,-[-( b'-]-) } \tuplet 3/2 { r8 c,-[-( c'-]-) } \tuplet 3/2 { r8 g,-\f-[-( g'-]-) }
	
	\tuplet 3/2 { r8 a-flat,-\p-[-( a-flat'-]-) } \tuplet 3/2 { r8 g,-[-( g'-]-) } \tuplet 3/2 { r8 a-flat,-[-( a-flat'-]-) } \tuplet 3/2 { r8 e-flat,-\f-[-( e-flat'-]-) }
	
	\tuplet 3/2 { r8 f,-\p-[-( f'-]-) } \tuplet 3/2 { r8 f-sharp,-[-( f-sharp'-]-) } \tuplet 3/2 { r8 g,-[-( g'-]-) } \tuplet 3/2 { r8 g,,-\f-[-( g'-]-) }
	
	\tuplet 3/2 { r8 c,-\p-[-( c'-]-) } \tuplet 3/2 { r8 b,-[-( b'-]-) } \tuplet 3/2 { r8 c,-[-( c'-]-) } \tuplet 3/2 { r8 g,-\f-[-( g'-]-) }
	
	% 180
	\stemUp \slurUp
	\tuplet 3/2 { \change Staff = "down" r8 a-flat,-[-( \change Staff = "up" a-flat'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 g,-[-( \change Staff = "up" g'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 a-flat,-[-( \change Staff = "up" a-flat'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 e-flat,-[-( \change Staff = "up" e-flat'-]-) }
	
	\tuplet 3/2 { \change Staff = "down" r8 f,^\p-[-( \change Staff = "up" f'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 f-sharp,-[-( \change Staff = "up" f-sharp'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 g,-[-( \change Staff = "up" g'-]-) }
	\tuplet 3/2 { \change Staff = "down" r8 g,,^\f-[-( g'-]-) }
	
	\tuplet 3/2 { r8^\p c,-( e-flat } \tuplet 3/2 { g-[ e-flat c-] } \tuplet 3/2 { g'-[ e-flat c-] } \tuplet 3/2 { f!-[ d b-]-) }
	
	\tuplet 3/2 { r8^\markup { \italic dim. } g-( c } \tuplet 3/2 { e-flat-[ c g-] } \tuplet 3/2 { e-flat'-[ c g-] } \tuplet 3/2 { d'-[ b g-]-) }
	
	s1
	
	% 185
	s
	
	\bar "|."
		}
	}
	
	%%%%%%%%%% BASS STAVE %%%%%%%%%%

lower = \relative c, {
	\time 2/2
	\key c \minor
	\tupletSpan 4
	
	< c c' >2^^-\sustainOn < e-flat e-flat' >4-\staccatissimo-\sustainOff < g g' >-\staccatissimo
	
	< c c' >-\staccatissimo < e-flat e-flat' >-\staccatissimo r2
	
	\clef "treble"
	r4 < e-flat' g >-. < e-flat g >-. < e-flat g >-. % gl: lowered an octave
	
	r < d f a-flat >-.	< d f a-flat >-. r
	
	% 5
	\clef "bass"
	< g,,, g' >2^^-\sustainOn < b b' >4-\staccatissimo-\sustainOff < d d' >-\staccatissimo
	
	< g g' >-\staccatissimo < b b' >-\staccatissimo r2

	\clef "treble"
	\relative c' {
	r4 
	\once \override DynamicText.transparent = ##t
	< d f a-flat >-\mp-. < d f a-flat >-. < d f a-flat >-.
	
	r < e-flat g >-. < e-flat g >-. r
	}
	
	\clef "bass" \stemDown
	g8-[-(-\sustainOn g' g, g'-] g,-[ g' g, g'-]-)-\sustainOff
	
	% 10
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	g,-[-( g'-.-) g-. g-.-] f,->-[-( f'-.-) f-. f-.-]
	
	\stemUp
	e-flat,->-[-( e-flat'-.-) e-flat-. e-flat-.-] b,->-[-( b'-.-) b-. b-.-]
	
	% 15
	c,->-[-( c'-.-) c-. c-.-] f,->-[-( f'-.-) f-. f-.-]
	
	e-flat,->-[-( e-flat'-.-) e-flat-. e-flat-.-] d,->-[-( d'-.-) d-. d-.-]
	
	\stemNeutral
	c4 r f r
	
	g r g, r
	
	\clef "treble"
	\relative c' {
	c2^^-\f-\sustainOn e-flat4-\staccatissimo-\sustainOff g-\staccatissimo
	
	% 20
	c-\staccatissimo e-flat-\staccatissimo r2
	}
	
	\clef "bass"
	< b-flat,! b-flat'! >2^^-\sustainOn < d d' >4-\staccatissimo-\sustainOff < f f' >-\staccatissimo
	
	< b-flat b-flat' > < d d' > r2
	
	e-flat8-\p-[-( b-flat' g b-flat-] f-[ b-flat a-flat b-flat-]
	
	g-[ b-flat e-flat, b-flat'-] d,-[ b-flat' b-flat, b-flat'-]-)
	
	% 25
	e-flat,-[ b-flat' g b-flat-] f-[ b-flat a-flat b-flat-]
	
	g-\p-[ b-flat e-flat, b-flat'-] d,-[ b-flat' b-flat, b-flat'-]
	
	e-flat,-[ b-flat' g b-flat-] d-[ b-flat f b-flat-]
	
	c,-[ b-flat' g b-flat-] c,-[ b-flat' g b-flat-]
	
	< c, f a >1
	
	%30
	r4 < b-flat' d >-( < c-flat e-flat >-) r
	
	r4 < b-flat d >-( < c-flat e-flat >-) r
	
	r4 < b-flat d >-( < c-flat e-flat >-) r
	
	< b-flat d >-( < c-flat e-flat > < b-flat d > < c-flat e-flat >
	
	< b-flat d >-) r4 r2
	
	% 35
	r1
	
	\clef "treble"
	\relative c' {
	g'8-[-( b-flat g b-flat-] f-[ b-flat g b-flat-]-)
	
	g-[-( b-flat g b-flat-] a-flat-[ b-flat a-flat b-flat-]-)
	
	f-[ b-flat f b-flat-] f-[ b-flat g b-flat-]
	
	a-flat-[ b-flat f b-flat-] a-flat-[ b-flat f b-flat-]
	
	% 40
	d,-[ b-flat' d, b-flat'-] c,-[ b-flat' d, b-flat'-]
	
	d,-[ b-flat' d, b-flat'-] e-flat,-[ b-flat' e-flat, b-flat'-]
	
	g-[ b-flat e-flat, b-flat'-] g-[ b-flat e-flat, b-flat'-]
	
	a-flat-[ b-flat a-flat b-flat-] g-[ b-flat g b-flat-]
	
	e-flat,->-[-( g e-flat g-] d-flat->-[ f d-flat f-]
	
	% 45
	c e-) < b-flat! e >4 r2
	
	< a-flat f' >4 r r2
	
	r4 << { g'4-( a-flat2 } \\ { b-flat,2-( b4 } >>
	
	<< { g'4-) } \\ { c,4-) } >> r4 r2
	}
	
	\clef "bass"
	e-flat,8-[-( g e-flat g-] d-flat-[ f d-flat f-]
	
	% 50
	c e-) < b-flat! e >4 r2
	
	< a-flat c f >1^^
	
	< f, f' >^^
	
	\change Staff = "up"
	f'4.-> r8 r2
	
	r2 % another translator from lower stave
	\change Staff = "down"
	r2
	
	% 55
	R1
	
	r4 < a-flat' c f > r < a c g-flat' >
	
	< b-flat e-flat g! > r r2
	
	\clef "treble"
	r4 << { g'4-( a-flat2-) } \\ { b-flat,2. } >>
	
	e-flat8-[ b-flat' g b-flat-] d,-[ b-flat' a-flat b-flat-]
	
	%60
	e-flat,!8-[ b-flat' g b-flat-] f,-[ d' a-flat d-]
	
	g,8-[ e-flat' b-flat e-flat-] a-flat,-[ e-flat' c e-flat-]
	
	b-flat!8-[ g' e-flat g-] b-flat,-[ a-flat' d, a-flat'-]
	
	\clef "bass"
	e-flat,8-[ b-flat' g b-flat-] d,-[ b-flat' a-flat b-flat-]
	
	e-flat,8-[ b-flat' g b-flat-] f-[ d' g, d'-]
	
	% 65
	< g, b-flat e-flat >4 r4 r2
	
	r4 a-flat-. b-flat-. b-flat,-.
	
	e-flat-. r r
	\clef "treble"
	< e-flat' g >-(
	
	< e-flat a-flat >-.-) r r < b-flat f' a-flat >-(
	
	< e-flat g >-.-) r r
	\clef "bass"
	< e-flat, g >-(
	
	% 70
	% gl (Breitkopf): < e-flat a-flat >-.-) r r < e-flat f a-flat >-(
	< e-flat a-flat >-.-) r r < b-flat f' a-flat >-(
	
	< e-flat g >-.-)-\sustainOn r r2-\sustainOff
	
	< e-flat, e-flat' >2^^-\sustainOn < g g' >4-\staccatissimo-\sustainOff < b-flat b-flat' >-\staccatissimo
	
	< e-flat e-flat' >-\staccatissimo < g g' >-\staccatissimo r2
	
	< g d' f >2. r4
	
	% 75
	< c,, c' >2^^-\sustainOn < e e' >4-\staccatissimo-\sustainOff < g g' >-\staccatissimo
	
	< c c' >-\staccatissimo < e e' >-\staccatissimo r2
	
	< b-flat, b-flat' >2^^-\sustainOn < e e' >4-\staccatissimo-\sustainOff < g g' >-\staccatissimo
	
	< b-flat b-flat' >-\staccatissimo < d-flat d-flat' >-\staccatissimo r2
	
	f8-\p-[-( c' a-flat c-] g-[ c b-flat c-]-)
	
	a-flat8-[-( c f, c'-] e,-[ c' c, c'-]-)
	
	f,8-[ c' a-flat c-] g-[ c b-flat c-]
	
	% 80
	a-flat8-[ c f, c'-] e,-[ c' c, c'-]
	
	\tuplet 3/2 { f,-[-( a-flat c-] } \tuplet 3/2 { b-flat-[ a-flat g-] } \tuplet 3/2 { f-[ a-flat c-] } \tuplet 3/2 { b-flat-[ a-flat g-] }
	
	\tuplet 3/2 { f-[ a-flat c-] } \tuplet 3/2 { b-flat-[ a-flat g-] } \tuplet 3/2 { f-[ g f-] } \tuplet 3/2 { e-flat!-[ f e-flat-]-) }
		
	% 85
	< d, d' >2^^-\sustainOn < f-sharp f-sharp' >4-\staccatissimo-\sustainOff < a a' >-\staccatissimo

	< d d' >-\staccatissimo < f-sharp f-sharp' >-\staccatissimo r2
	
	\override TupletBracket.transparent = ##t
	\tuplet 3/2 { g8-[ b-flat d-] } \tuplet 3/2 { c-[ b-flat a-] } \tuplet 3/2 { g-[ b-flat d-] } \tuplet 3/2 { c-[ b-flat a-] }
	
	\tuplet 3/2 { g-[ b-flat d-] } \tuplet 3/2 { c-[ b-flat a-] } \tuplet 3/2 { g-[ b-flat d-] } \tuplet 3/2 { g,-[ b-flat d-] }
	
	\tuplet 3/2 { f,!-[ b d-] } \tuplet 3/2 { g,-[ b d-] } \tuplet 3/2 { a-flat!-[ b d-] } \tuplet 3/2 { g,-[ b d-] }
	
	% 90
	\tuplet 3/2 { f,-[ b d-] } \tuplet 3/2 { g,-[ b d-] } \tuplet 3/2 { a-flat-[ b d-] } \tuplet 3/2 { f,-[ b d-] }
	
	\tuplet 3/2 { e-flat,-[ g c-] } \tuplet 3/2 { f,-[ a-flat c-] } \tuplet 3/2 { e-flat,-[ g c-] } \tuplet 3/2 { d,-[ f c'-] }
	
	\tuplet 3/2 { e-flat,-[ g c-] } \tuplet 3/2 { d,-[ f c'-] } \tuplet 3/2 { e-flat,-[ g c-] } \tuplet 3/2 { c,-[ e-flat g-] }
	
	\tuplet 3/2 { b,-[ d g-] } \tuplet 3/2 { c,-[ d g-] } \tuplet 3/2 { b,-[ d g-] } \tuplet 3/2 { a,-[ d g-] }
	
	\tuplet 3/2 { b,-[ d g-] } g,4-\staccatissimo r2
	
	% 95
	\clef "treble"
	r2 < d'' b' >
	
	r < b a-flat' >
	
	r1
	
	\clef "bass"
	< b,, b' >1-\sustainOn-(
	
	< b-flat b-flat' >4-\sustainOff-) r4 r2-\fermata % gl: Breitkopf
	
	% 100
	< c c' >2^^-\sustainOn < e-flat e-flat' >4-\staccatissimo-\sustainOff < g g' >-\staccatissimo
	
	< c c' >-\staccatissimo < e-flat e-flat' >-\staccatissimo r2
	
	\clef "treble"
	r4 < e-flat' g >-. < e-flat g >-. < e-flat g >-. % gl: Breitkopf
	
	r < d f a-flat >-.	< d f a-flat >-. r
	
	\clef "bass"
	< g,,, g' >2^^-\sustainOn < b b' >4-\staccatissimo-\sustainOff < d d' >-\staccatissimo
	
	% 105
	< g g' >-\staccatissimo < b b' >-\staccatissimo r2

	\clef "treble"
	\relative c' {
	r4 
	\once \override DynamicText.transparent = ##t
	< d f a-flat >-\mp-. < d f a-flat >-. < d f a-flat >-.
	
	r < e-flat g >-. < e-flat g >-. r
	
	}
	
	\clef "bass" \stemDown
	g8-[-(-\sustainOn g' g, g'-] g,-[ g' g, g'-]-)-\sustainOff
	
	
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	% 110
	g,-[ g' g, g'-] g,-[ g' g, g'-]
	
	g,-[-( g'-.-) g-. g-.-] f,->-[-( f'-.-) f-. f-.-]
	
	\stemUp
	e-flat,->-[-( e-flat'-.-) e-flat-. e-flat-.-] b,->-[-( b'-.-) b-. b-.-]

	c,->-[-( c'-.-) c-. c-.-] f,->-[-( f'-.-) f-. f-.-]
	
	e-flat,->-[-( e-flat'-.-) e-flat-. e-flat-.-] d,->-[-( d'-.-) d-. d-.-]
		
	% 115
	\stemNeutral
	c4 r f r
	
	g r g, r

	r2-\sustainOn c'2^^

	e-flat4-\staccatissimo-\sustainOff g-\staccatissimo < a-flat,,, a-flat' >2-\sustainOn
				
	% 120
	< c c' >4-\staccatissimo-\sustainOff < f f' >-\staccatissimo < a-flat a-flat' >2

	\clef "treble"
	r8 g-flat''-\p-[-( e-flat g-flat-] a-flat,-[ g-flat' e-flat g-flat-]-)
	
	a-flat,-[ f' d-flat f-] a-flat,-[ f' d-flat f-]

	a-flat,-[ g-flat' e-flat g-flat-] a-flat,-[ g-flat' e-flat g-flat-]

	a-flat,-[ f' d-flat f-] a-flat,-[ f' d-flat f-]
				
	% 125
	< a, c e-flat f-sharp >1^\fz

	\clef "bass"
	r4 < g b >-( < a-flat! c >-) r
	
	r4 < g b >-( < a-flat c >-) r

	< g b >-( < a-flat c > < g b > < a-flat c >-)

	< g b-flat > r r2            %gl: Breitkopf
			
	% 130
	r1
	
	\clef "treble"
	e-flat'8-\p-[-( g e-flat g-] d-[ g e-flat g-]-)
	
	e-[ g e g-] f-[ g f g-]
	
	d-[ g d g-] d-[ g e-flat! g-]
	
	f-[ g d g-] f-[ g d g-]
	
	% 135
	b,-[ g' b, g'-] c,-[ g' c, g'-]
	
	d-[ g d g-] e-flat-[ g e-flat g-]
	
	e-flat-[ g c, g'-] e-flat-[ g c, g'-]
	
	f-[ g d g-] e-flat-[ g c, g'-]

    % gl: added b-flat as 4th note in bass (Breitkopf)
	<< { e-flat-[-( g e-flat g-]-) e-[-( g e g-]-) } \\ { c,4 c b-flat! b-flat } >>
	
	% 140
	<< { c8-( f f-sharp4-) } \\ { a,4 < a-flat c > } >> r2
	
	\clef "bass"
	r4 < g b >-( < b d >-) r
	
	r < c, e >-( < e g >-) r
	
	f r r2
	
	<< { r4 < e-flat' g >-( < d f >2-) } \\ { g,1 } >>
	
	% 145
	<< { e-flat8-[-( g e-flat g-]-) e-[-( g e g-]-) } \\ { c,4 c b-flat! b-flat } >>
	
	<< { c8-( f f-sharp4-) } \\ { a,4 < a-flat c > } >> r2
	
	r4 < g b >-( < b d >-) r
	
	r < c, e >-( < e g >-) r
	
	< f, f' >1->
	
	% 150
	\tuplet 3/2 { r8 c'-[-( f-] } \tuplet 3/2 { a-flat-[ f a-flat-] } \tuplet 3/2 { c-[ a-flat c-] } \tuplet 3/2 { f-[ c f-] }
	
	\change Staff = "up"
	\tuplet 3/2 { a-flat-[ f a-flat-] } \tuplet 3/2 { c-[ a-flat c-] }
	\clef "treble"
	\tuplet 3/2 { f-[ c f-] } \tuplet 3/2 { a-flat-[ f a-flat-] }
	
	\tuplet 3/2 { c-[ a-flat c-] } \tuplet 3/2 { f-[ c f-] } \tuplet 3/2 { a-flat-[ f a-flat-] } c-.-)-[ g-\mp-]-(
	
	a-flat-[ e f c-sharp-] d-)-[ a-flat'-(-\> f d-]-)-\!
	
	\change Staff = "down"
	\clef "bass"
	< g,, c e-flat >4 r r2
	
	% 155
	\clef "treble"
	<< { e-flat'8-[-( g e-flat g-] f-[ g f g-]-) } \\ { g,1 } >>
	
	c8-[-( g' e-flat g-] b,-[ g' f g-]-)
	
	c,!-[ g' e-flat g-]
	\clef "bass"
	d,-[ b' f b-]
	
	e-flat,!-[ c' e, c'-] f,-[ c' f-sharp, e-flat'!-]
	
	g,-[ e-flat' c e-flat-] g,-[ f'! b, f'-] 
	
	% 160
	c,-[ g' e-flat g-] b,-[ g' f g-] 
	
	c,-[ g' e-flat a-flat-] d,-[ b' g b-]
	
	<< { c1-( } \\ { e-flat,2. e4 } >>
	
	<< { \stemDown < f c' >4-.-) } \\ { s4 } >> f-. g-. g,-.
	
	c-. r r < c' e-flat >-(
	
	% 165
	< g d' f >-.-) r r < g d' f >-(
	
	< c e-flat >-.-) r r < c, e-flat >-(
	
	< g b d f >1-)
	
	< c, c' >2->-\sustainOn < e-flat e-flat' >4-\staccatissimo-\sustainOff < g g' >-\staccatissimo
	
	< c c' >-\staccatissimo < e-flat e-flat' >-\staccatissimo r2
	
	% 170
	< a-flat,, a-flat' >2->-\sustainOn < c c' >4-\staccatissimo-\sustainOff < e-flat e-flat' >-\staccatissimo
	
	< a-flat a-flat' >-\staccatissimo < c c' >-\staccatissimo r2
	
	< f-sharp,, f-sharp' >2->-\sustainOn < a a' >4-\staccatissimo-\sustainOff < c c' >-\staccatissimo
	
	< f-sharp f-sharp' >-\staccatissimo < a a' >-\staccatissimo < c c' >-\staccatissimo < e-flat e-flat' >-\staccatissimo
	
	\tuplet 3/2 { g8-[-( c e-flat-] } \tuplet 3/2 { g,-[ c e-flat-] } \tuplet 3/2 { g,-[ c e-flat-] } \tuplet 3/2 { g,-[ c e-flat-]-) }
	
	% 175
	\tuplet 3/2 { g,-\sustainOn-[-( b f'-] } \tuplet 3/2 { g,-[ b f'-] } \tuplet 3/2 { g,-[ b f'-] } \tuplet 3/2 { g,-[ b f'-\sustainOff-]-) }
	
	c4-( b c-) g_>-(
	
	a-flat g a-flat-) e-flat_>-(
	
	\slurDown
	f f-sharp g-) g,_>-(
	
	c b c-) g_>-(
	
	% 180
	\stemDown
	a-flat g a-flat-) e-flat_>-(
	
	f f-sharp g-) g,_>
	
	c2.-( g4-)
	
	c2.-( g4-)
	
	<< { c'4 r < g c >^\pp r } \\ { c,4 r < c e-flat > r } >>
	
	% 185
	<< { \stemUp < g' c >2 r2 } \\ { \stemDown < c, e-flat >2 r2 } >>
		}

\score {
  \context PianoStaff << 
    \context Staff = "up" <<
    	\upper
    	>>
    \context Staff = "down" <<
      \clef bass
      \lower
      >>  
  >>
  \layout { }  
  
  

}
