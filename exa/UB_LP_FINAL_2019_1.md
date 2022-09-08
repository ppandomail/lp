# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Final diciembre 2019

* ALUMNO:  
* LU:
* CARRERA:

---

### NOTA: EL EXAMEN ESCRITO ES UN DOCUMENTO DE GRAN IMPORTANCIA PARA LA EVALUACIÓN DE LOS CONOCIMIENTOS ADQUIRIDOS, POR LO TANTO, SE SOLICITA LEER ATENTAMENTE LO SIGUIENTE

* Responda claramente cada punto, detallando con la mayor precisión posible lo solicitado.
* Sea prolijo y ordenado en el desarrollo de los temas.
* Sea cuidadoso con las faltas de ortografía y sus oraciones.
* No desarrollar el examen en lápiz.
* Aprobación del examen: Con nota mayor o igual a 4 (cuatro)
* Condiciones de aprobación: 60%
* Duración de examen: 2 horas.

---

1. [2 puntos]: Enúnciese tres producciones de la sintaxis básica del lenguaje de programación Prolog.

    * **Solución:**

    ```grammar
    <hecho> ::= <termino>.
    <regla> ::= <terminos> :- <terminos>.
    <consulta> ::= <terminos>.
    <termino> ::= <numero> | <atomo> | <variable> | <atomo> (<terminos>)
    <terminos> ::= <termino> | <termino>,<terminos>
    ```

1. [2 puntos]: Ejemplifíquese regla léxica y regla sintáctica para una asignación.

    * **Solución:**

    ```grammar
    Léxica: 
    var -> letra | var letra | var digito
    cte -> digito | cte digito
    letra -> A |…| Z | a |…| z
    digito -> 0 |…| 9            
    Sintáctica: 
    exp -> exp + termino
    asig -> var := exp
    ```

1. [4 puntos]: Impleméntese la regla crédito(x) en el lenguaje Prolog, sabiendo que se da crédito a sueldos mayores que 50000 pesos y antigüedad mayor a 3 años. Los hechos son: sueldo(juan,40000). sueldo(pedro,55000). sueldo(ana, 45000). antigüedad(juan,2). antigüedad(pedro,5). antigüedad(ana,6).

    * **Solución:**

    ```prolog
    historial(x):-sueldo(x, y), y>50000.
    permanencia(x):-antigüedad(x,z), z>=3.
    crédito(x):-historial(x),permanencia(x).
    ```

1. [2 puntos]: Defínase y ejemplifíquese la diferencia entre: constructor y destructor.

    * **Solución:**
    * Constructor: inicializa los atributos del objeto. Ejemplo en C++: Stack() { tope = new int[100]; }
    * Destructor: limpieza de memoria luego de que una instancia es destruida. Ejemplo en C++: ~Stack() { tope = delete [] tope; }

---
