# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Final noviembre 2021

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

1. [3 puntos]: Constrúyase un anagrama con la palabra LENGUAJES

1. [2 puntos]: Formúlese 3 consultas para el siguiente programa en PROLOG:

    ```prolog
    arc(a, b). 
    arc(b, c). 
    arc(b, d). 
    arc(d, c). 
    path(X, Y) :- arc(X, Y). 
    path(X, Y) :- arc(X, Z), path(Z, Y).
    ```

1. [5 puntos]: Dada la siguiente GIC del LP While:

    ```grammar
    <Programa> ::= <Instrucción> | { <Rutina> }
    <Rutina> ::= <Instrucción> ; <Instrucción> | <Instrucción> ; <Rutina>
    <Instrucción> ::= nil | a++ | a-- | While <Prueba> do <Programa>
    <Prueba> ::= a≠0 | a=0 
    ```

    1. [2] Clasifíquese el lenguaje. Justifíquese.
    1. [1] Enumérese 3 programas del lenguaje.
    1. [2] Identifíquese aspectos sintácticos (elementos, estructuras) y semánticos del lenguaje.

---
