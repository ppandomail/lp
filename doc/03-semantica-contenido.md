# Semántica

|||
| -- | -- |
| **¿Qué es?**            | Describe el significado (interpretaciones) de los símbolos, palabras y frases de un lenguaje, Ejemplo: en este LP, cuando se asigna un float a una entero se trunca por la parte entera inferior |
| **¿Cómo se escribe?**   | Manuales de referencia (impreciso, ambiguo), uso de un traductor, definiciones formales (cálculo lambda) |
| **¿Qué vamos a hacer?** | Recurrir a la pragmática, reconociendo la influencia de la pragmática en la semántica |

## Cálculo Lambda

* Creado en 1930 por los matemáticos estadounidenses Alonzo Church (1903-1995) y Stephen Kleene (1909-1994)
* La operatoria con los términos lambda se rige por el lambda-calculus o cálculo-λ.
* Es un sistema formal diseñado para investigar la definición de función, noción de aplicación de funciones y recursión.
* Una función es una expresión matemática y = f(x) que relaciona el valor de dos variables.
* Se lo puede considerar como el lenguaje universal de programación más pequeño, ya que cualquier función computable puede ser expresada y evaluada a través de él.
* Uno de los méritos de Church fue introducir una nueva sintaxis con la que representar a esta clase de expresiones matemáticas.
* Así, por ejemplo, si se evalúa la expresión (+(\* 2 3)(\* 5 6)) = 36. Por consiguiente, una función matemática sería una abstracción.
* Por si algo es célebre el cálculo λ es porque Church utilizó este formalismo para estudiar el llamado Problema de la Parada, obteniendo como resultado la noción de Problema Computable, que es precisamente la idea que subyace en la Máquina de Turing.
* A su vez, Turing demostró en 1937 que tanto el cálculo λ como su máquina eran equivalentes, es decir, permitían llegar por dos vías diferentes a los mismos resultados.
* Cuando una máquina de Turing procesa alguna de las expresiones indicadas, por ejemplo (+ 3 1), se detiene una vez obtenido un resultado, 4 en el ejemplo, siendo esta la expresión computable.
* Desde un punto de vista práctico, el cálculo λ inspiró el desarrollo de los llamados LP funcionales, uno cuyos ejemplos es Lisp, uno de los LP más importantes en IA.

### Sintaxis

```plain
expr -> var | λ var. expr | expr expr | (expr)
var -> x | y | z | f | n 
```

* Una expresión λ puede ser:
  * variable. Ejemplo:  x
  * abstracción sobre una variable (λ var. expr):
    * λ: abstracción
    * var: representa la entrada
    * .: separa la entrada de la salida
    * expr: representa la salida (indica qué es lo que hace la máquina con la entrada para obtener la salida). Es el cuerpo de la abstracción
    * Ejemplo 1: λx. x
    * Ejemplo 2: λa. λb. abc  (en este caso λb. abc es componente de λa. λb. abc)
  * aplicación de funciones (expr expr):
    * Ejemplo 1: λx.x λy.y
    * Ejemplo 2: λa.λb.ab λx.x (la expr λa.λb.ab está por procesar la expr λx.x)

### Codificación de Church

| Nombre | Expresión |
| -- | -- |
| + | λm.λn.λf.λx.mfnfx |
| * | λa.λb.λz.(a(bz)) |
| ^ | λa.λb.(ba) |
| 0 | λf.λx.x |
| 1 | λw.λy.wy |

* (+ 1 1)

```plain
(λm. λn. λf. λx. mfnfx) (λa. λb.ab) (λc. λd.cd)
(λn. λf. λx. (λa. λb.ab)fnfx) (λc. λd.cd)
λf. λx. (λa. λb.ab)f (λc. λd.cd)fx
λf. λx. (λb.fb)(λc. λd.cd)fx
λf. λx. f(λc. λd.cd)fx
λf. λx. f(λd.fd)x
λf. λx. f(fx) //(Es la M2)
```

* (* 0 1)

```plain
(λa. λb.λz (a(bz))) (λf. λx.x) (λw. λy.wy)
λb.λz (λf. λx.x(bz)) (λw. λy.wy)
λz (λf. λx.x((λw. λy.wy)z))
λz (λf. λx.x(λy.(zy)))
λf. λx.x   //(Es la M0)
```

## Ligadura o binding

* Es el estudio del momento preciso en el que un atributo (propiedad) de un elemento (entidad) del lenguaje es conocida
* Es la asociación entre el elemento y el atributo

| Elementos |
| -- |
| Variable |
| Función/método |
| Parámetro |
| Bloque |
| Sentencia |
| ... (depende del LP) |

| Atributos |
| -- |
| Valor |
| Almacenamiento |
| Tipo |
| Alcance |
| Nombre |
| Acción asociada |
| ... (depende del LP) |

* Ejemplos:

| Tipo | |
| -- | -- |
| **Binding del tipo de las variables**          | es el momento en el que se conoce el tipo de la variable |
| **Binding de almacenamiento de las variables** | es el momento en el que se conoce la dirección de la celda donde se almacenan las variables |
| **...**                                        | es el momento en el que se conoce ... |

* Por ejemplo, la declaración o definición en el LP C:

    ```c
    const int n = 5;
    int x;
    double f(int n) { ... }
    ```

  * asocia al identificador n el atributo de tipo de dato constante entera y el atributo de valor 5
  * asocia el atributo variable y el tipo de dato entero al identificador x
  * asocia el atributo función al identificador f y parámetros y tipo de dato devuelto y cuerpo del código que se ejecuta cuando se llama a la función

| Binding Time | | Ejemplo 1 | Ejemplo 2 |
| -- | -- | -- | -- |
| **Estático** | Tiempo de definición (diseño e implementación) del lenguaje    | %i **BASIC** (las variables seguidas con % son enteras | @a **Perl** (las variables que comienzan con @ tienen estructura de tipo arreglo) |
| **Estático** | Tiempo de escritura del programa (gralmente. en LP compilados) | i: interger; **Pascal, Delphi** | int i; **C/C++, Java** |
| **Dinámico** | Tiempo de ejecución (gralmente. en LP interpretados)           | if (a == 1): b  = 'Hola' else b = 2.0 **Python** | if. T do, i=:3 else. i=:a end. **J** |

## Variables

* Es un elemento fundamental en los LP.
* Es una abstracción de una celda de memoria.
* Memoria principal: celdas elementales, identificadas por una dirección (referencia donde está almacenada la variable).
* El contenido de una celda es una representación codificada de un valor.
* Sintaxis de asignación: \<identificador> \<símbolo de asignación> \<expresión>
  * \<identificador>: l-value (lugar de memoria asociado con la variable)
  * \<expresión>: r-value (valor codificado almacenado en la ubicación de la variable)

* Ejemplos:

  ```plain
  a = b          Java, C, C++, Perl, FORTRAN
  a := b         Pascal, Delphi, Ada, ALGOL  
  a <- b         APL, Smalltalk
  (setq a b)     Lisp
  MOVE B TO A    COBOL
  set a b        Tcl
  a =: b         J
  LET a = b      Basic
  ```

  | Binding | | Estático | Dinámico | Ejemplo dinámico |
  | -- | -- | -- | -- | -- |
  | **De valor**   | El patrón de bits almacenado en la celda asociada a la variable | Muy pocos lenguajes funcionales puros / Inmutabilidad | Paracticamente todos | float x; <br> x = 1.0; <br> input(x); <br> x = rand(); |
  | **De tipo**    | El conjunto de valores posibles que puede adquirir la variable | Pascal, C, C++, Java, Kotlin, Rust, Go | Inferencia: J, LISP, Python, PHP, Javascript, Perl, Dart | v = new Persona("Pepe"); <br> v = new Comprobante(123); |
  | **De alcance** | Cuáles instrucciones pueden usar una variable | Pascal, C, C++, Java, Kotlin, Rust, Go, Python | APL, J, BASIC, Perl | 10 INPUT A <br> 20 B = 5 <br> 30 IF (A > 4) C = 3 <br> 40 D = B + C <-- no se puede saber si C está al alcance o no |
  | **De almacenamiento** | Almacenamiento: el lugar de memoria donde está la variable | COBOL, FORTRAN | Mayoría | void a() { int x = 4: } --> <br> mov ax, 4 <br> mov ?, ax |
  | **De nombre**         | Identificador que utiliza el programador para referirse a la celda de memoria de la variable: longitud, casesensitive, caracteres | | | |
  | **De tiempo de vida** | Tiempo en el que la variable tiene lugar en memoria y puede ser accedida | | | a1 = new A(); <br> ... <br> if (...) delete a1; <br> ... |
