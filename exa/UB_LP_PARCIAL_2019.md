# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Parcial octubre 2019

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

1. [2 puntos]: Ordénese los siguientes lenguajes según su año de creación: Assembler, C++, Ruby, Java, C, Fortran.

    * **Solución:**
    * Assembler, Fortran, C, C++, Java, Ruby.

1. [2 puntos]: Conceptualícese "lenguaje ortogonal".

    * **Solución:**
    * Conjunto pequeño de constructores primitivos, pueda ser combinado en número relativamente pequeño a la hora de construir estructuras de control y datos. Cada combinación es legal y con sentido.

1. [2 puntos]: Impleméntese una regla y un hecho en el lenguaje Prolog.

    * **Solución:**

    ```prolog
    longitud([], 0).
    longitud([X|Y], N) :- longitud(Y, M), N = M+1.
    ```

1. [4 puntos]: Defínase formalmente la sintaxis a través de una gramática independiente de contexto de una sentencia válida de un lenguaje infinito. Construir el árbol de parsing para una determinada palabra.

    * **Solución:**

    ```grammar
    ASIG -> variable := EXP
    EXP -> EXP + TER | EXP - TER | TER
    TER -> TER * FACTOR | TER / FACTOR | FACTOR
    FACTOR -> variable | cte
    ```

1. [2 puntos]: Ejemplifíquese cuatro asociaciones sintácticas entre parámetros reales y formales.

    * **Solución:**
    * Posicional: void m(String str, Double d) {}                      m("Hola", 9.8);
    * Implícito:  void m(String str, Double d) {}                      m("Hola");
    * Explícito:  void m(int i, String str=“Hola”, Double d=1.0) {}    m(2, d:3.2);
    * Anónimo:    void m(String str, Double…d) {}                      m("Hola", 1.2, 2.3);

---
