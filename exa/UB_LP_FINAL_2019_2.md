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

1. [2 puntos]: Enúnciese cinco "otros paradigmas".

    * **Solución:**
    * Concurrente, Scripting, Visual, Computación cuántica, Orientado a eventos.

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

1. [4 puntos]: Impleméntese las reglas madre, padre y abuelo en el lenguaje Prolog, sabiendo que existen los siguientes hechos: progenitor(clara,jose). mujer(clara). hombre(jose).

    * **Solución:**

    ```prolog
    /* Equivale a: Para todo X e Y, si X es mujer y X es el progenitor de Y, entonces X es la madre de Y */
    madre(X,Y):- mujer(X), progenitor(X,Y).

    /* Equivale a: Para todo X e Y, si X es hombre y X es el progenitor de Y, entonces X es el padre de Y */
    padre(X,Y):- hombre(X), progenitor(X,Y).

    /*  El abuelo se define como el progenitor de mi progenitor */ 
    abuelo(X,Y):- progenitor(X,Z), progenitor(Z,Y).
    ```

1. [2 puntos]: Defínase, enúnciese ventajas y ejemplifíquese la diferencia entre: compatibilidad de tipos por nombre y compatibilidad de tipos por estructura.

    * **Solución:**
    * Compatibilidad de tipos por nombre: dos variables que tengan el mismo nombre de tipo son compatibles. Ventajas: mayor seguridad en las operaciones y mejor legibilidad de los programas. Ejemplo:

    ```ada
    type Entero is new Integer;
    a : Integer;
    b : Entero;
    a := a + b;
    ```

    * Compatibilidad de tipos por estructura: dos variables que tengan la misma representación en memoria son compatibles. Ventajas: mayor flexibilidad para operar entre tipos diferentes y mayor facilidad de escritura de los programas.

    ```c
    typedef int entero;
    int a;
    entero b;
    a := a + b; 
    ```

---
