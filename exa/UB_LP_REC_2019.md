# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Recuperatorio noviembre 2019

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

1. [2 puntos]: Enúnciese cinco lenguajes de programación creados en la década del 80.

    **Solución:**

    * Eiffel, Oberon, C++, Miranda, Haskell.

1. [2 puntos]: Diferénciese los siguientes conceptos: Sintaxis, Semántica y Pragmática. Proporciónese un ejemplo para cada uno de ellos.

    **Solución:**

    * Sintaxis: como se escriben los diferentes elementos del lenguaje. En el lenguaje Z, las asignaciones se escriben con el símbolo “<-”.
    * Semántica: que significado tienen las sentencias. En el lenguaje Y, cuando se divide por cero, se debe mostrar tal mensaje de error.
    * Pragmática: como se hace para que las sentencias logren el efecto deseado. Ejemplo: Una gran cantidad de invocaciones recursivas a tal procedimiento puede dar lugar a un desbordamiento de la pila.

1. [2 puntos]: Impleméntese la regla hermano(A, B) en el lenguaje Prolog, sabiendo que existen los siguientes hechos padre(Juan, Mauro). padre(Luis, Mauro). padre(Mauro, Leoncio). padre(Pablo, Leoncio). padre(Luis, Pablo).

    **Solución:**

    ```prolog
    hermano(A, B) :- padre(A, P), padre(B, P), A \== B.
    ```

1. [2 puntos]: Defínase formalmente la sintaxis de un lenguaje a través de una gramática independiente de contexto. Cada programa comienza con begin y termina con end. Dentro del cuerpo puede haber una o más sentencias. Las sentencias son de la forma a = a; Construir el árbol de parsing para “begin a=a;a=a;a=a;end”.

    **Solución:**

    ```grammar
    P -> begin S end
    S -> a = a | a = a; S
    ```

1. [2 puntos]: Defínase y ejemplifíquese un clousure.

    **Solución:**

    * Clousure: es la manera en como una función dentro de otra función contenedora puede hacer referencia a las variables después de que la función contenedora ha terminado de ejecutarse. El lenguaje debe proveer un mecanismo para que la función acceda a las variables del ámbito correspondiente, proporcionando mayor flexibilidad a las funciones.

    ```javascript
    function sayHi(seconds) {
        var hi = 'Hi folks!';  
        setTimeout(function() {
            console.info(hi); // Referenciando a la variable ‘hi’
        }, seconds*1000);
    }
    sayHi(2);
    ```

---
