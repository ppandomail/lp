# Sintaxis

## Ejercicios

1. ¿Por qué conviene utilizar mecanismos formales como BNF para estudiar la sintaxis de los lenguajes de Programación?
1. ¿Pueden dos instrucciones de asignación en diferentes lenguajes poseer igual sintaxis, igual semántica y diferente pragmática?
1. ¿Pueden dos instrucciones de asignación en diferentes lenguajes poseer igual sintaxis y diferente semántica?
1. ¿Pueden dos instrucciones de asignación en el mismo lenguaje con diferente sintaxis poseer diferente semántica?
1. ¿Puede limitarse desde la gramática el valor máximo que puede adoptar una variable?
1. Responder si es verdadera o falsa la siguiente afirmación: Si un lenguaje tiene dos formas sintácticas diferentes para escribir una instrucción condicional, entonces existe una ambigüedad en la gramática.
1. Considere la siguiente expresión: 8 / 2 \* 4 – 12 \* 2 / 6 + 2 \* 2. Escribir una gramática de expresiones para cada uno de los siguientes casos:
    * Absolutamente recursiva a izquierda.
    * Absolutamente recursiva a derecha.
    * Suma y resta recursiva a izquierda y producto y división recursiva a derecha.
    * Suma y resta recursiva a derecha y producto y división recursiva a izquierda.
    * En cada caso construir el árbol de parsing de la expresión y calcular el resultado.
1. Dadas las siguientes reglas extraídas del conjunto de reglas del lenguaje Python

    ```bnf
    <asignacion> ::= <destino> "=" <expresión>
    <destino> ::= <identificador> | <elemento_arreglo>
    <elemento_arreglo> ::= <identificador> "[" <subindices> "]"
    <subindices> ::= <identificador> | <identificador> , <subindices>
    ```

    * Proponer las reglas que faltan para poder representar sintácticamente una asignación
    * Agregar reglas para permitir expresiones como subíndices de arreglos
    * Proponer reglas para permitir asignaciones múltiples por ejemplo: a,b,c = d, e+f, g+3
    * Construir el árbol de parsing para las siguientes sentencias con las reglas que haya agregado  B:= A - B \* (C + D / A)  y   B[2]:= A[(E + 1), 9] \* D
1. Dada la siguiente gramática en BNF:

    ```bnf
    <comienzo> ::= <declaración> | <invocación>
    <declaración> ::= PROCEDURE <id> ( < lis_param> ) <cuerpo> ;
    <lis_param> ::= <param> ; <lis_param> | <param>
    <param> ::= <list_id> : <tipo>
    <tipo> ::= INT | STRING
    <list_id> ::= <id> | <id> , <list_id>
    <invocación> ::= <id> ( <list_id> ) ;
    <cuerpo> ::= // { … }
    <id> ::= // [a-z][a-z]* cualquier conjunto de letras en minúscula
    ```

    * Enuncie en forma general qué forma deben tener las sentencias para que sean aceptadas por esta gramática.
    * Analice si la gramática planteada es ambigua. Si su respuesta es afirmativa indique por qué lo es y muestre la existencia de ambigüedad mediante un ejemplo. Si su respuesta en negativa, escriba dos expresiones que sean aceptadas por la gramática para cada una de las alternativas de la regla \<comienzo\>.
    * ¿Qué puede deducir de la semántica y de la sintaxis de los elementos del lenguaje que se reconocerían a través de esta gramática?

1. Se tiene el lenguaje Pascal definido en parte por las siguientes reglas BNF:

    ```bnf
    <Bloque> ::= <Declaracion Etiqueta><Definición Constantes><Definicion de tipos><Declaracion Variables><Declaracion de procedimientos><Instruccion compuesta>
    <Instruccion> ::== <Instruccion sin etiqueta> | <etiqueta> : <Instruccion sin etiqueta>
    <Instruccion sin etiqueta> ::= <Instruccion simple> | <Instruccion estructurada>
    <Instruccion simple> ::= <Instruccion de asignación> | <Instruccion de procedimiento> | <Instruccion goto> |
    <Instruccion vacía>
    <Instruccion compuesta> ::= begin <Instruccion> {; <Instruccion> } end;
    <Instruccion de procedimiento> ::= <Identificador de procedimiento> | <Identificador de procedimiento>(<Parámetro real> {, <Parámetro real> })
    <Instruccion estructurada> ::= <Instruccion compuesta> | <Instruccion condicional> | <Instruccion de repetición>
    <Declaración de procedimiento> ::= <Encabezado de Procedimiento> <Bloque>
    ```

    * Responder si cada una de las siguientes afirmaciones son verdaderas o falsas, justificando con las reglas anteriores que implican que el lenguaje posee esa característica.
      * El lenguaje posee anidamiento de bloques de instrucciones dentro de bloques de instrucciones
      * El lenguaje siempre permite la declaración de variables en las instrucciones que se encuentran enmarcadas dentro de las palabras begin y end
      * Es posible declarar un procedimiento dentro de las instrucciones enmarcadas por begin y end
      * El lenguaje admite más de un parámetro real en una instrucción de pasaje de parámetros

1. Teniendo las siguientes reglas en BNF que nos definen la sintaxis de las sentencias de la asignación de un determinado lenguaje:

    ```bnf
    <asig> ::= <variable> := <exp>
    <exp> ::= <término> | <exp> + <término> | <exp> - término>
    <término> ::= <factor> | <. término> * <factor> |<término> / <factor>
    <factor> ::= <primario> | <factor> ^ <primario>
    <primario> ::= <variable> | <número> | (<exp>)
    <variable> ::= <identif> | <identif> [<lista_índices>]
    <lista_índices> ::= <exp> | <lista_índices>, <exp>
    ```

    * Construya el árbol de parsing para las siguientes sentencias de asignación:
      * A : = B * (C + D) c) X[4] : = Y + 3
      * E : = C - D ^A + E / B d) X[I,J] : = X[J,I]

1. Se tiene un lenguaje que permite emplear los tipos de pasaje de parámetros por nombre, por referencia, por copia valor resultado y por copia valor, según lo descrito por la siguiente gramática:

    ```bnf
    <comienzo> ::= <declaración> | <invocación>
    <declaración> ::= FUNCTION <identificador> ( <lista_parametros> )
    <lista_parametros> ::= <parametro> | <parametro>; <lista_parametros>
    <parámetro> ::= <tipo de pasaje> : <identificador> : <tipo de datos> = <valor por defecto>
    <tipo_de_pasaje>::= name | reference | inout | in
    <tipo_de_datos> ::= integer | float | string | array | ...
    <invocación> ::= <identificador> ( <list_id> ) ;
    <list_id> ::= <identificador> | <identificador> , <list_id>
    <valor_por_defecto> ::= <constante> | <expresion> | <invocacion_funcion> | ... 
    <asignación> ::= <identificador> = <resultado>;
    <resultado> ::= <identificador> | <expresión> | <invocacion_funcion> | ...
    <identificador> ::= // [a-z][a-z]* 
    ```

    * Indicar si las siguientes declaraciones e invocaciones de funciones son aceptadas por esta gramática. Justifique sus respuestas especificando las reglas por las cuales son aceptadas.
      * ``` function imprimir(mensaje){...} ```
      * ``` PQ(); ```
      * ``` PP(x,t,y,z,PQ); ```
      * ``` function PP(name:a:integer; name:e:integer; reference:b:integer; inout:c:integer; in:d:integer=3) ```
      * ``` PQ(x,t,y,z,w); ```
      * ``` function PQ(name:a:integer=5; name:e:integer=8; reference:b:integer=0; inout:c:integer =1; in:d:integer=3) ```
      * ``` PP(3, ,x); ```
      * Para aquellas expresiones que no sean aceptadas ¿qué reglas agregaría, quitaría o modificaría de la gramática? Responda por cada inciso.

1. Dado el siguiente subconjunto de reglas BNF del lenguaje Pascal basadas en la definición de función y procedimiento:

    ```bnf
    <P> ::= <Identificador> | <Identificador> (<R> {, <R>})
    <PFD> ::= <PD>|<FD>
    <PD> ::= <PH><Bloque>
    <PH> ::= procedure<Identificador> : <T> | procedure<Identificador>(<F>{;<F>});
    <F> ::= <PG>|var <PG>| function<PG>|procedure<Identificador>{,<Identificador>}
    <PG> ::= <Identificador>{,<Identificador>}:<Tipo>
    <FD> ::= <FH><Bloque>
    <FH> ::= function<Identificador>: <T>; | function<Identificador>(<F>{;<F>}) : <T>;
    <T> ::= <Integer>|<-Real>|<Boolean>|<String>|<Char>
    ```

    * Aclaración: las llaves indican que puede haber repeticiones de los elementos que contienen.
    * Escribir 2 ejemplos diferentes de definición y llamada, uno a función y otro a procedimiento, aceptadas por esta gramática.
    * Modificar/agregar reglas para: a) No permitir el pasaje de parámetros por referencia. b) Lograr que una función sólo pueda devolver los tipos: Integer y Char. c)Que la máxima cantidad de parámetros sea tres.

1. Considere el siguiente fragmento BNF de un lenguaje y responda los incisos:

    ```bnf
    <type> ::= <primitive type> | <reference type>
    <primitive type> ::= <numeric type> | boolean
    <numeric type> ::= <integral type> | <floating-point type>
    <integral type> ::= byte | short | int | long | char
    <floating-point type> ::= float | double
    <reference type> ::= <class or interface type> | <array type>
    <class type> ::= <type name>
    <interface type> ::= <type name>
    <array type> ::= <type> [ ]
    <field declaration> ::= <field modifiers>? <type> <variable declarator id>
    ```

    * ¿Puede declararse arreglo como atributo mezclando tipos numéricos diferentes? Fundamentar la respuesta.
    * Agregar y/o modificar las reglas necesarias para que los arreglos de punto flotante se declaren utilizando los símbolos “[“ y “]” y los arreglos de tipos integrales se declaren utilizando los símbolos “(“ y “)”
    * Agregar y/o modificar las reglas necesarias para que no se puedan declarar arreglos de tipos booleanos
    * Agregar y/o modificar las reglas necesarias para que los modificadores de declaración en variables no puedan aplicarse sobre tipos interfaces.
    * ¿Es posible agregar/modificar reglas que permitan habilitar / deshabilitar operaciones sobre variables cuyo tipo pertenece a alguna clase determinada? Fundamentar la respuesta.

1. Proporcione GIC para describir la sintaxis de cada uno de los siguientes casos:
    1. Cadenas de longitud uno o mayores definidas sobre el conjunto de símbolos terminales {blanco, tab, línea nueva}.
    1. Secuencias de letras o dígitos, comenzando con una letra.
    1. Números reales en los cuales tanto la parte entera como la fraccionaria pueden estar vacías, pero no ambas a la vez. Así, la gramática debe permitir 31., 3.1 y .13, pero no un punto decimal solo.

1. Realice el diagrama sintáctico (esquema de sintaxis) de la gramática  BNFE:

    ```bnf
    Expresión ::= Término {(‘+’ |’-’) Término}
    Término ::= Factor {(‘*’ | div) Factor}
    Factor ::= ‘(’ Expresión ‘)’ | Variable | Constante
    ```

1. La siguiente gramática EBNF se basa en la sintaxis de los enunciados del lenguaje de programación Módula-2:

   ```bnf
    S ::= []
    | id := expr
    | if expr then SL {elsif expr then SL} [else SL] end 
    | loop SL end
    | while expr do SL end
    SL ::= S {; S}
    ```

    * El componente léxico id representa una variable, mientras que expr representa una expresión. Observe que [] representa la cadena vacía.
    * Escriba una versión BNF de esta gramática.
    * Escriba un esquema de sintaxis para esta gramática.

1. Sea la siguiente gramática expresada en notación EBNF:

    ```bnf
    <expresion> : := <termino> { OR <termino> }
    <termino> ::= <factor> { AND <factor> }
    <factor> ::= ‘(‘ <expresion> ‘)’' | <valor>
    <valor> ::= verdadero | falso | a | b | c
    ```

    * Para cada una de las siguientes cadenas de la gramática, dibujar su árbol sintáctico.
      * verdadero AND ( falso OR verdadero)
      * verdadero AND falso OR verdadero
      * ((a AND b) OR (c AND a))
      * a AND (c OR verdadero) AND (verdadero AND b)

1. Dibujar las reglas de la gramática EBNF del ejercicio anterior como diagramas sintácticos.
