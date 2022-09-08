# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Final diciembre 2018

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

1. [5 puntos]: Enumere 3:
    1. Lenguajes creados en la década del 80.
    1. Características que contribuyen a la legibilidad.
    1. Producciones de la sintaxis básica de Prolog.
    1. Atributos de una rutina.
    1. Partes de una GIC.

1. [1 punto]: Dada la siguiente BD en Prolog: edad(a, 23). edad(b, 14). edad(c, 21). Resolver  persona_mayor_edad(P).

    * **Solución:**

    ```prolog
    persona_mayor_edad(P) :- persona(P), edad(P, E), E>18.
    ```

1. [1 punto]: Implementar en Lisp una función que reciba 3 argumentos enteros: los dos primeros se suman y su resultado se comprueba si es mayor o no al tercer argumento. Ejemplo:  (suma-mayor-que 1 4 3) retornará T.

    * **Solución:**

    ```lisp
    (defun suma-mayor-que (x y z) (> (+ x y) z))
    ```

1. [3 puntos]: Diseñe una GIC para el lenguaje Colchita. Construya el árbol análisis sintáctico para la palabra: c(g(r1),r2).

    * **Solución:**

    ```lisp
    S -> c(S, S) | g(S) | r1 | r2

    S => c(S, S) => c(g(S), S) => c(g(r1), S) => c(g(r1), r2)
    ```

---
