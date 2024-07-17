  PROGRAM Hanoi(input, output); 
  VAR N:integer; 
  PROCEDURE dohanoi(N, Tfrom, Tto, Tusing : integer); 
  BEGIN 
      IF N > 0 THEN 
      BEGIN 
            dohanoi(N-1, Tfrom, Tusing, Tto); 
            writeln('move ', Tfrom:1, ' --> ', Tto:1); 
            dohanoi(N-1, Tusing, Tto, Tfrom); 
      END 
  END; 
  BEGIN 
      dohanoi(5, 1, 3, 2)
  END.