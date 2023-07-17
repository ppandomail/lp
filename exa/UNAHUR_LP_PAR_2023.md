# UNIVERSIDAD NACIONAL DE HURLINGHAM

## Instituto de Tecnología e Ingeniería

## CARACTERÍSTICAS DE LOS LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Parcial julio 2023

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

* El lenguaje de programación U# puede ser descrito como sigue:
  * Las variables y nombres se forman con la combinación de las letras A, B, C y siempre deben terminar con un número. Ejemplos: A5, BCA15, AABA2.
  * Las sentencias válidas son:
    * Sentencia declarativa: variable 1, variable 2,..., variable n : tipo

        ```plain
        Ejemplo:
        A5, BCA15: entero
        ```

    * Sentencia de impresión: Imprimir variables separadas por ;

        ```plain
        Ejemplo: 
        imprimir A5; BCA15
        ```

  * Los tipos de datos válidos son: entero, letra o palabra.
  * Un programa tiene una estructura de la forma:

    ```plain
    INICIO nombrePrograma Sentencias...FIN.
    (No es obligatorio darle un nombre al programa)
    ```

1. [1 punto]: Clasifíquese U#

    ```plain
    Nivel de abstracción: MEDIO/ALTO
    Dominio de aplicación: ESPECIFICO
    Tipo de traducción: COMPILADO
    Paradigma: IMPERATIVO
    Realización del programa: TEXTUAL
    ```

1. [2 puntos]: Describir formalmente la gramática con BNF.

    ```grammar
    <PROG> ::= INICIO <ID> <SENTS> FIN. | INICIO <SENTs> FIN.
    <SENTS> ::= <SENT> <SENTS> | <SENT>
    <SENT> ::= <DECL> | <IMPR>
    <DECL> ::= <ID> , <DECL> | <ID> : <TIPO>
    <TIPO> ::= entero | letra | palabra
    <IMPR> ::= imprimir <VAR>
    <VAR>  ::= <ID> ; <VAR> | <ID>
    <ID>   ::= <LS> <DS>
    <LS>   ::= <L> <LS> | <L>
    <DS>   ::= <D> <DS> | <D>
    <L>    ::= A | B | C
    <D>    ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    ```

1. [2 puntos]: Describir formalmente la gramática con EBNF.
1. [2 puntos]: Describir formalmente la gramática con Diagrama de Sintaxis.
1. [1 punto]: Derívese verticalmente una palabra de U#.
1. [1 punto]: Enumérese elementos y vínculos semánticos deseables para U#
1. [1 punto]: Justifíquese: **U# es un lenguaje de programación fuertemente tipado**

---
