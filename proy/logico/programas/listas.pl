longitud([],0).
longitud([X|Y],N) :- longitud(Y,M), N=M+1.