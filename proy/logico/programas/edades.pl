persona(ana).
persona(pepe).
persona(juan).
persona(josé).
edad(ana, 23).
edad(pepe, 19).
edad(juan, 14).
edad(josé, 5).
persona_mayor_edad(P) :- persona(P), edad(P,E), E>18.
persona_mayor_que(P1,P2) :- persona(P1), persona(P2), edad(P1,E1), edad(P2,E2), E1>E2.