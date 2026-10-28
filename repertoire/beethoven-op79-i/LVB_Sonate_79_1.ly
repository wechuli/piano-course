\version "2.25.12"

 

\score {

 \new GrandStaff
 <<
 \new Staff = "up" {
 \clef treble
 \key g \major
 \time 3/4
 \override Score.MetronomeMark.transparent = ##t
 \tempo 2 = 124
 \override TextScript.padding = #3.0
 <g' g''>4\f\staccato^\markup { \large "Presto alla tedesca." } <b' b''>\staccato <g' g''>\staccato
 \repeat volta 2 {
 <d'' d'''>2( c'''8 b'' a'' g'' fis'' g'' b'') g'' fis''4( e'') d''8( c'' b' a' gis' a' c'' a')
 fis'2 a'4\staccato c''4\staccato a'\staccato fis'\staccato
 g'8\f d' cis' d' fis' g' a' d' cis' d' g' a' b' g' fis' g' c''! d'' e'' d'' c'' b' a' g'
 fis'4\p r8 d'_\markup { \italic "leggiermente" }[ fis' a'] d'' fis' a' d'' fis'' a' d'' fis'' a'' d'' fis'' a''
 d'''8 fis'' a'' d''' fis''' e''' d'''4 r8 d'8[ fis' b'] d'' fis' b' d'' fis'' b' d'' fis'' b'' d'' fis'' b'' d''' fis'' b'' d''' fis''' e'''
 d'''4 r8 d'8[ e' gis'] b' e' gis' b' d'' gis' b' d'' gis'' b' d'' gis'' b''8( gis'' e'' fis'' e'' fis''
 <cis'' e''>2._\markup { \italic "cresc." }) <d'' e''>2. <e'' g''!>2.\sf <d'' fis''>4\p <d'' fis''> <d'' fis''>
 <cis'' e''>2._\markup { \italic "cresc." } <d'' e''>2. <e'' g''!>2.\sf <d'' fis''>4\p <d'' fis''> <d'' fis''>
 <cis'' e''>8 d''( e'' fis'' gis'' a'' gis'' fis'' e'' d'' cis'' b') d''( e'' fis'' gis'' a'' b'' a'' g''! fis'' e'' d'' cis'')
 e''8_\markup { \italic "cresc." } g'' cis''' g'' e''' cis''' e''' cis''' e''' cis''' e''' cis''' e''' cis''' a'' b'' cis''' a''
 d'''8_\markup { \italic "dim." } a'' d''' a'' fis'' d'' e''_\markup { \italic "cresc." } g'' cis''' g'' e''' cis'''
 e'''8\sf cis''' e''' cis''' e''' cis''' e''' cis''' a'' b'' cis''' a''
 d'''8_\markup { \italic "dim." } a'' d''' a'' fis'' d'' b''\p g'' b'' g'' d'' b' a'2 e''4^\trill
 d''4\f <a' a''>\staccato <d' d''>\staccato r4 <g' g''>\staccato <cis' cis''>\staccato
 r4 <d' d''>\p\staccato <b b'>\staccato r <c'! c''!>\staccato <a a'>\staccato }
 \alternative { { <g' g''>4\f\staccato <b' b''>\staccato <g' g''>\staccato }
 { r4 <b' b''>\f\staccato <gis' gis''>\staccato r4 <a' a''>\staccato <fis' fis''>\staccato } }
 \repeat volta 2 {
 <e' e''>4\f\staccato <gis' gis''>\staccato <e' e''>\staccato <b' b''>2\sf( a''8 gis'' fis'' e'' dis'' e'' gis'' e'')
 dis''4( cis'') b'8( a' gis' fis' eis' fis' a' fis') dis'2 fis'4\staccato a'4\staccato fis'\staccato dis'\staccato
 e'8 b\p gis' b e' b e' b gis' b e' b e' b gis' b e' b dis' b fis' b dis' b dis' b fis' b dis' b
 dis'8 b fis' b dis' b dis' b fis' b dis' b e'\p b e' b e' b c' g_\markup { \italic "dolce" } e' g c' g c' g e' g c' g
 c' g e' g c' g b g_\markup { \italic "dolce" } d' g b g b g d' g b g b g d' g b g b g d' g b g
 c' g c' g c' g c' g fis! g b c' d' g fis! g c' d' e' c' b c' f' g' a' g' f' e' d' c' b4 r4 f''8\p g'' a'' g'' f'' e'' d'' c''
 b'4 r4 f'8\p g' aes'_\markup { \italic "cresc." } g' f' ees' d' g' c'8\f g ees' g c' g c' g ees' g c' g
 c' g ees' g c' g b g d' g b g b g d' g b g b g d' g b g b g d' g b g c'\p g c' g d' bes
 <ees' g'>\p bes_\markup { \italic "dolce" } g' bes ees' bes
 ees' bes g' bes ees' bes ees' bes g' bes ees' bes d' bes f' bes d' bes d' bes f' bes d' bes
 d' bes f' bes d' bes d' bes f' bes d' bes ees' bes ees' bes ees' bes ees'\f bes a! bes d' ees'
 f' bes a bes ees' f' g' ees' d' ees' aes' bes' c'' bes' aes' g' f' ees' d'4 r4 aes''8\p bes''
 c'''8 bes'' aes'' g'' f'' ees'' d''4 r4 c'8\f d' ees' d' c' bes a! g fis!4 r4 c'''8\p d'''
 ees'''8_\markup { \italic "cresc." } d''' c''' bes'' a'' g'' fis''! ees'' d'' c'' bes' a' g'\p fis'! g' a' bes' g'
 fis'4_\markup { \italic "dolce" } fis'8 a d' a d' a fis' a d' a d' a fis' a d' a cis' a e'! a cis' a
 cis' a e' a cis' a cis' a e' a cis' a cis' a e' a cis' a d' a a' d' a' fis'
 <a' d''> d'_\markup { \italic "cresc." } <a' d''> d' <a' d''> d' <a' d''> d' <a' d''> d' <a' d''> d'
 <a' c''!> d' <a' c''> d' <a' c''> d' <a' c''> d' <a' c''> d' <a' c''> d'
 <g' g''>4\f\staccato <b' b''>\staccato <g' g''>\staccato <d'' d'''>2\sf( c'''8 b'' a'' g'' fis'' g'' b'' g'')
 fis''4( e'') d''8( c'' b' a' gis' a' c'' a') fis'2 \grace { b'16[ a' gis'] } a'4\staccato c''4\staccato a'\staccato fis'\staccato
 g'8\f d' cis' d' fis' g' a' d' cis' d' g' a' b' g' fis' g' a' b' c''! g' fis' g' b' c''
 d''4 r8 d'8_\markup { \italic "leggiermente" }[ g' b'] d'' g' b' d'' g'' b' d'' g'' b'' d'' g'' b'' d''' c''' b'' a'' g'' f''
 e''4 r8 e' g' c'' e'' e' g' c'' e'' g' c'' e'' g'' c'' e'' g'' c''' e'' g'' c''' e''' d'''
 cis'''4 r8 cis'[ e' g'] cis'' e' g' cis'' e'' g' cis'' e'' g'' cis'' e'' g'' cis'''( e''' a'' b'' a'' b''
 <fis'' a''>2._\markup { \italic "cresc." }) <g'' a''>2. <a'' c'''!>2.\sf <g'' b''>4\p <g'' b''> <g'' b''>
 <fis'' a''>2._\markup { \italic "cresc." } <g'' a''>2. <a'' c'''!>2.\sf <g'' b''>4\p <g'' b''> <g'' b''>
 <fis'' a''>8( g'' a'' b'' cis''' d''' cis''' b'' a'' g'' fis'' e'') g''( a'' b'' cis''' d''' e''' d''' c'''! b'' a'' g'' fis'')
 a''_\markup { \italic "cresc." } c''' fis''' c''' a''' fis''' a'''\sf fis''' a''' fis''' a''' fis''' a'''\sf fis''' d''' e''' fis''' d'''
 g'''_\markup { \italic "dimin." } d''' g''' d''' b'' g''
 a''_\markup { \italic "cresc." } c''' fis''' c''' a''' fis''' a'''\sf fis''' a''' fis''' a''' fis''' a'''\sf fis''' d''' e''' fis''' d'''
 g'''_\markup { \italic "dimin." } d''' g''' d''' b'' g'' e'''\p c''' e''' c''' g'' e'' d''2 a''4^\trill
 g''4\f <d'' d'''>\staccato <g' g''>\staccato r4 <c'' c'''>\staccato <fis' fis''>\staccato }
 \alternative {
 { r4 <d' d''>4\p\staccato <b b'>\staccato r <c' c''>\staccato <a a'>\staccato
 r4 <b' b''>4\f\staccato <gis' gis''>\staccato r <a' a''>\staccato <fis' fis''>\staccato }
 { r4 <d' d''>\p <g g'> r <c' c''> <fis fis'> } }
 r4 <d'' d'''>4\f <g' g''> r <c'' c'''> <fis' fis''> r4 <d' d''>\p <g g'> r <c' c''> <fis fis'>
 <g' b'>8\f d' <g' b'> d' <g' b'> d' <g' b'> d' <g' b'> d' <g' b'> d' <g' b'> d' <g' b'> d' <g' b'> d'
 <g' c''> c' <g' c''> c' <g' c''> c' a'4\f\staccato c''\staccato a'\staccato e''2\sf( d''8 c'' b' a' c'' a' fis' a') a'4( g') g'
 <b' d''>8\f g' <b' d''> g' <b' d''> g' <b' d''> g' <b' d''> g' <b' d''> g' <b' d''> g' <b' d''> g' <b' d''> g'
 <c'' g''> g' <c'' g''> g' <c'' g''> g'
 \acciaccatura gis''8 a''4\f \acciaccatura b''8 c'''4 \acciaccatura gis''8 a''4 \acciaccatura dis'''8 e'''2\sf( d'''8 c'''
 b''8 a'' c''' a'' fis'' a'') g''\p d''_\markup { \italic "dolce e leggiermente" } b'' g'' d'' b' g'' d'' b'' g'' d'' b'
 g'' d'' b'' g'' d'' b' fis'' d'' a'' fis'' d'' c'' d'' b' g'' d'' b' g' d'' b' g'' d'' b' g' d'' b' g'' d'' b' g'
 c''8 a' d'' c'' a' fis' g'4 r8 g b d' g' b' d'' g'' b'' d''' g'''4 r4 r4^\fermata \bar "|."
}

 \new Staff = "down" {
 \clef bass
 \key g \major
 \time 3/4
 <g b>8\f d' <g b> d' <g b> d'
 \repeat volta 2 {
 <g b>8 d' <g b> d' <g b> d' <g b> d' <g b> d' <g b> d' <g c'> e' <g c'> e' <g c'> e' <g c'> e' <g c'> e' <g a c'> d'
 <g a c'> d' <g a c'> d' <g a c'> d' <g a c'> d' <g a c'> d' <g a c'> d'
 <g b>2. <fis, d fis>2. <g, d g>2 <a, a>8 <b, b> <c c'>4 <c c'> <cis cis'> <d d'>8\p[ d fis a] r4 R2. R2. R2.
 b,8 d fis b r4 R2. R2. R2. gis,8[ b, d e] gis4 R2. R2. r4 <gis b>4 <b d'>
 << { cis'8 d'( e' fis' gis' a' \stemDown gis' fis' e' d' cis' b a g! fis e d cis) } \\
 { a4 c4\rest c4\rest s2. s2. } >> d8 e fis gis a b
 << { cis'8 d'( e' fis' gis' a' \stemDown gis' fis' e' d' cis' b a g! fis e d cis) } \\
 { a4 c4\rest c4\rest s2. s2. } >> d8 e fis gis a b
 << { <cis' e'>2. <b d'>2. <d' gis'>2. <cis' e'>2. } \\ { a2.~ a2. a2.~ a2. } >>
 <a cis' e' g'>2. <bes cis' e' g'>2. <a cis' e' g'>2 <g cis' e'>4 <fis a d'>2 <d a d'>4
 <a cis' e' g'>2. <bes cis' e' g'>2. <a cis' e' g'>2 <g cis' e'>4 <fis a d'>2 <d a d'>4
 <g b d'>4 r <g b e'> <a d' fis'> r <a cis' g'> <d fis>8\f a <d fis> a <d fis> a <d e g> a <d e g> a <d e g> a
 r4 d\p\staccato b,\staccato r c!\staccato a,\staccato }
 \alternative { { g,4\f <g b>8 d' <g b> d' }
 { r4 <b, b>\f\staccato <gis, gis>\staccato r4 <a, a>\staccato <fis, fis>\staccato } }
 \repeat volta 2 {
 <e gis>8\f b <e gis> b <e gis> b <e gis> b <e gis> b <e gis> b <e gis> b <e gis> b <e gis> b
 <e a> cis' <e a> cis' <e a> cis' <e a> cis' <e a> cis' <e fis a> b <e fis a> b <e fis a> b <e fis a> b
 <e fis a> b <e fis a> b <e fis a> b e4 \clef treble b'4\sf gis' \clef bass e4 \clef treble b'\sf gis'
 \clef bass e4 \clef treble b'\sf gis' \clef bass b,4 \clef treble a'\sf fis' \clef bass b,4 \clef treble a'\sf fis'
 \clef bass b,4 \clef treble a'\sf fis' \clef bass b,4 \clef treble a' fis' \clef bass e4\p \clef treble g'! g'
 \clef bass c4\sustainOn g' e' c g' e' c g' e'\sustainOff g,4\sustainOn f' d'
 g,4 f' d' g, f' d' g, f' d'\sustainOff c4\sustainOn e' e'\sustainOff <c, g, c>2. <b,, g, b,>2. <c, g, c>2 a,8( e,)
 f,4\staccato f,\staccato fis,\staccato g,4 r4 \clef treble d'8\p e' f'4\staccato f'\staccato fis'\staccato
 g'4 r4 \clef bass f8\p g aes8 g f ees d g c4 g'\sf ees' c g'\sf ees' c g'\sf ees' g, f'\sf d' g, f'\sf d' g, f'\sf d'
 g,4 f'\sf d' c ees'( f') ees4\sustainOn^\p \clef treble bes' g' \clef bass ees \clef treble bes' g'
 \clef bass ees4 \clef treble bes' g'\sustainOff \clef bass bes,\sustainOn \clef treble aes' f'
 \clef bass bes, \clef treble aes' f' \clef bass bes, \clef treble aes' f' \clef bass bes, \clef treble aes' f'\sustainOff
 \clef bass ees4\sustainOn \clef treble g'4 g'\sustainOff
 \clef bass <ees, bes, ees>2.\f <d, bes, d>2. <ees, bes, ees>2 c8( g,) aes,4\staccato aes,\staccato a,\staccato
 bes,4 r4 \clef treble c''8\p( bes') aes'4\staccato aes'\staccato a'\staccato bes'4 r \clef bass c8\f d
 ees8 d c bes, a,! g, fis,!4 r4 \clef treble c''8\p d'' ees'' d'' c'' bes' a' g' fis'! ees' d' c' bes a
 \clef bass g4 ees cis d\sustainOn \clef treble a' fis' \clef bass d4 \clef treble a' fis'
 \clef bass d4 \clef treble a' fis'\sustainOff \clef bass a,4\sustainOn g' e'! a, g' e' a, g' e' a, g' e'\sustainOff
 d4\sustainOn fis' d' fis\staccato\sustainOff d\staccato fis,\staccato d,\staccato fis d fis, d, fis d fis, d,
 g,4\sustainOn <g b>8 d' <g b> d' <g b> d' <g b> d' <g b>\sustainOff d' <g b> d' <g b> d' <g b> d'
 <g c'> e' <g c'> e' <g c'> e' <g c'> e' <g c'> e' <g a c'> d' <g a c'> d' <g a c'> d' <g a c'> d'
 <g a c'> d' <g a c'> d' <g a c'> d' <g b>2. <fis a>2. <g b>2. <a c'!>2. b,8 d g b r4 R2. R2. R2. c8 e g c' r4
 R2. R2. R2. a,8 cis e g r4 R2. R2. r4 \clef treble <cis' e'>4 <e' g'>
 << { fis'8( g' a' b' cis'' d'' cis'' b' a' g' fis' e') } \\ { d'4 c'4\rest c'4\rest s2 s4 } >>
 \clef bass d'8 c'! b a g fis g a b cis' d' e'
 \clef treble << { fis'8( g' a' b' cis'' d'' cis'' b' a' g' fis' e') } \\ { d'4 c'4\rest c'4\rest s2 s4 } >>
 \clef bass d'8 c'! b a g fis g a b cis' d' e'
 \clef treble << { <fis' a'>2. <e' g'>2. <g' cis''>2. <fis' a'>2. } \\ { d'2.~ d'2. d'2.~ d'2. } >>
 <d' fis' a' c''!>2. <ees' fis' a' c''>2. <d' fis' a' c''>2 <c' fis' a'>4 <b d' g'>2 <g d' g'>4
 <d' fis' a' c''>2. <ees' fis' a' c''>2. <d' fis' a' c''>2 <c' fis' a'>4 <b d' g'>2 <g d' g'>4
 <c' e' g'>4\p r <c' e' a'> <d' g' b'> r <d' fis' c''>
 \clef bass <g b>8\f d' <g b> d' <g b> d' <g a c'> d' <g a c'> d' <g a c'> d' }
 \alternative {
 { r4 d\p\staccato b,\staccato r c\staccato a,\staccato
 r4 <b, b>\f\staccato <gis, gis>\staccato r <a, a>\staccato <fis, fis>\staccato }
 { b,8\p d b, d b, d a, d a, d d, d } }
 <g b>8\f d' <g b> d' <g b> d' <g a c'> d' <g a c'> d' <g a c'> d' b,\p d b, d b, d a, d a, d d, d
 g,4\f\staccato b,\staccato g,\staccato d2\sf( c8 b, a, g, fis, g, b, g,) fis,4( e,) e,
 <c e>8\f a <c e> a <c e> a <c e> a <c e> a <c e> a <d a> c' <d a> c' <d a> c' <g b> d' <g b> d' <g b> d'
 \acciaccatura fis8 g4\f \acciaccatura ais8 b4 \acciaccatura fis8 g4 \acciaccatura cis'8 d'2\sf( c'8 b
 a8 g fis g b g) fis4( e) e <c e>8\f a <c e> a <c e> a <c e> a <c e> a <c e> a
 <d a> c' <d a> c' <d a> c' g,4\p <b d'> <g b> g, <b d'> <g b> g, <b d'> <g b> d <a c'> <fis a>
 g,4 <b d'> <g b> g, <b d'> <g b> g, <b d'> <g b> d <a c'> <d a>
 g,,8 b,, d, g, b, d g,4 r r r2.^\fermata \bar "|."
}
>>

 \layout { }

 

}
