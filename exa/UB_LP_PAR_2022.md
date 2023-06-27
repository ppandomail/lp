# UNIVERSIDAD DE BELGRANO

## Facultad de Ingeniería y Tecnología Informática

## LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Parcial setiembre 2022

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

1. [2 puntos]: Resuélvase mediante programación lógica el siguiente problema: Si una persona padece una enfermedad que es aliviada por un fármaco entonces se le ha de recetar ese fármaco. Una enfermedad es aliviada por un fármaco cuando este último suprime alguno de los síntomas de la enfermedad. Se sabe que la gripe tiene por síntomas: la fiebre y el cansancio y que la alergia tiene por síntoma los estornudos. Además se conoce que el cansancio es eliminado con vitaminas, la fiebre por paracetamol y los  estornudos por un antihistamínico. En este momento Jon tiene gripe y hepatitis, Ana tiene gripe y Carlos tiene alergia. ¿Qué se le puede recetar a Ana?  Utilizar los siguientes predicados para la representación en el programa:
    * padece (P, E) la persona P sufre la enfermedad E
    * es-sintoma (S, E) S es un síntoma de la enfermedad E
    * suprime (F, S) el fármaco F elimina el síntoma S
    * alivia (F, E) el fármaco F alivia la enfermedad E
    * debe-tomar (P, F) la persona P debe tomar el fármaco F

    **Solución:**

    ```prolog
    padece(jon, gripe).
    padece(jon, hepatitis).
    padece(ana, gripe).
    padece(carlos, alergia).
    es-sintoma(fiebre, gripe).
    es-sintoma(cansancio, gripe).
    es-sintoma(estornudos, alergia).
    suprime(vitamina, cansancio).
    suprime(paracetamol, fiebre).
    suprime(antihistamínico, estornudos).
    alivia(F, E) :- es-sintoma(S, E), suprime(F, S).
    debe-tomar(P, F) :- padece(P, E), alivia(F, E).
    ```

1. [2 puntos]: Diséñese las reglas de la GIC en formato BNF para validar la declaración de un registro en Pascal. Recordar el formato:

    ```pascal
    reg = record 
      campo1: tipo; 
      campo2,campo3: tipo; 
    end; 
    
    // Los tipos pueden ser: real, integer, boolean.
    ```  

    **Solución:**

    ```grammar
    <registro> ::= <id> = record <listacampos> end; 
    <listacampos> ::= <uncampo> | <listacampos> ; <uncampo> 
    <uncampo> ::= <listaiden> : <tipo>
    <listaiden> ::= <id> | <listaiden> , <id>
    <id> ::= <letra> | <id> <letra> | <id> <dig>
    <letra> ::= a | b | ... | z | A | ... | Z
    <dig> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
    <tipo> ::= integer | real | boolean | ...
    ```

1. [2 puntos]: Diséñese el Diagrama de Sintaxis, de la siguiente GIC que valida el encabezamiento de una función en Python:

    ```grammar
    <función> ::= def <id> ( <listaArg> ) : | def <id> ( ) : 
    <listaArg> ::= <unarg> | <listaArg> , <unarg>
    <unarg>::= <id> | self
    ```

1. [2 puntos]: Enumérese las diferencias entre Lenguaje Formal y Lenguaje de Programación. Ejemplifiquese.

    **Solución:**

    ```plain
    Un LP es un LF diseñado para realizar procesos que pueden ser llevados a cabo por máquinas.
    LP = sintaxis + semántica.
    LF = {a, aa, aaa, aaaa, ...}
    LP = {g(r1), c(g(r1), r2), ...} 
    ```

1. [2 puntos]: Constrúyase los árboles sintácticos (o de derivación) descendentes para las siguientes cadenas más cortas del lenguaje de programación C:

    ```c
    int v1;
    int v1,v2;
    ```

    ```grammar
    <decl_var> ::= <unadecl> ; | <unadecl> ; <decl_var> 
    <unadecl> ::= <tipo> <listaDec> 
    <listaDec> ::= <listaiden> | <listaAsig> | <listaCombinada> 
    <listaiden> ::= <id> | <listaiden> , <id> 
    <listaAsig> ::= <unaAsig> | <listaAsig> , <unaAsig> 
    <unaAsig> ::= <id>=<valor>
    <valor> ::= <nro> | <id>
    <listaCombinada> ::= <listaiden> , <listaAsig> 
    <nro> ::= <dig> | <nro> <dig>
    <id> ::= <letra> | <id> <letra> | <id> <dig> 
    <dig> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
    <letra> ::= a | b | ... | z | A | ... | Z 
    <tipo> ::= int | float | string | ...
    ```

---
