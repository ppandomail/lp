habla(ale,ruso).
habla(juan,ingles).
habla(maria,ruso).
habla(maria,ingles).
seComunicaCon(X,Y) :- habla(X,L), habla(Y,L), X\=Y