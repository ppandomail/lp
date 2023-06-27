# UNIVERSIDAD NACIONAL DE HURLINGHAM

## Instituto de Tecnología e Ingeniería

## CARACTERÍSTICAS DE LOS LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Parcial mayo 2022

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

1. [1 punto]: Clasifíquese a los lenguajes de programación vistos en la carrera.

1. [3 puntos]: Resuélvase mediante programación operacional y declarativa el siguiente problema: Se consulta por ejemplo: parse([comienzo, norte, norte, este, fin]) y tiene que devolver true si es aceptado por el AF que reconoce las palabras del lenguaje representado por la ER: comienzo (norte | sur | este | oeste)* fin

1. [2 puntos]: Diséñese en BNF la gramática que genera las palabras del siguiente lenguaje:
    * Una expresión puede ser un átomo o una lista.
    * Un átomo puede ser un número o un símbolo.
    * Un número es una secuencia continua de uno o más dígitos decimales, precedido opcionalmente por un signo (+) o un signo (-).
    * Un símbolo es una letra seguida de cero o más caracteres (dígitos o letras)
    * Una lista es un par de paréntesis que abren y cierran. (con cero o más expresiones en medio separadas por punto y coma).

1. [2 puntos]: Escríbase la gramática BNF para el siguiente Diagrama de Sintaxis, el símbolo de inicio es \<statement\>.

```graph
                                            -->(init)--->[expression]----
                                            ^                            |
                                            |                            | 
--->(new)--->[identifier]--->(:)---->[type]-|->(alias)--->[expression]---|
                                            |                            |
                                            |<--------------------------- 
                                            |
                                            v
                                            --->(in)--->[statement]--->(ni)--->   

```

1. [2 puntos]: Derívese verticalmente, mediante el árbol de análisis sintáctico la palabra c(g(g(g(r1))), g(r1)) del lenguaje generado por la siguiente GIC en BNF:

    ```grammar
    <S> ::= r1 | c(<S>,<S>) | g(<S>)
    ```

---
