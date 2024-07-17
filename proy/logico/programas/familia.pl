padre(juan, alberto).
  padre(luis, alberto).
  padre(alberto, leoncio).
  padre(gerónimo, leoncio).
  padre(luis, gerónimo).
  hermano(A,B) :- padre(A,P), padre(B,P), A \== B.
  nieto(A,B) :- padre(A,P), padre(P,B).