# Paradigma Funcional

## Características de Lenguajes de Programación

**Profesor**:

- Pablo Miguel Angel Pandolfo

**Integrantes**:

- Angeli, Matias
- Cichello, Alan
- Toloza, Tomás

## Descripción

El paradigma funcional es un paradigma declarativo que se basa en un modelo matemático de composición de funciones.
En este modelo, el resultado de un cálculo es la entrada del siguiente, y así sucesivamente hasta que una composición produce el
valor deseado, tal como sucede en la composición de funciones matemáticas.
Los programas funcionales expresan mejor qué hay que calcular, y no detallan tanto cómo realizar dicho cálculo a diferencia de lo
que ocurre en los programas imperativos.
La característica principal de la programación funcional es que los cálculos se ven como una función matemática que hacen
corresponder entradas y salidas.

## Breve historia

### 1930

La programación funcional encuentra sus raíces en el Lambda Calculus, cuya historia comienza en el 1930 cuando Alonzo Church lo
introdujo, aunque todavía no era utilizado para computadoras claramente.

### 1960

No fue hasta 1960 que un científico e informático americano llamado John McCarthy publicó su libro Recursive Functions of Symbolic
Expressions and Their Computation by Machine. Como resultado de su investigación, McCarthy desarrolló lo que sería reconocido como
el primer lenguaje de programación funcional: LISP

### 1978

Casi dos décadas después, el siguiente gran avance pasó en la Universidad de Edinburgh investigadores definieron el Metalenguaje.
Los investigadores requerían un lenguaje que pudiera funcionar para sus Sistemas automáticos para probar teoremas. El Metalenguaje
servía para eso, y luego se dieron cuenta de que podría servir como un lenguaje de programación general.

### 1990 a la actualidad

Haskell, nombrado así por el lógico Haskell B. Curry, fue el producto de un comité que tenía como objetivo formar un lenguaje en
1987 y lanzó su primera versión en 1990. La última versión de Haskell salió en 2020 y se volvió un lenguaje super popular en la
enseñanza del paradigma.

## Haskell

Haskell es un lenguaje funcional puro, de propósito general, que incluye muchas de las últimas innovaciones en el desarrollo de
los lenguajes de programación funcional.

### ¿Por qué usarlo?

- Un incremento sustancial de la productividad de los programas.
- Código más claro y más corto
- Una “semántica de huecos” más pequeña entre el programador y el lenguaje
- Tiempos de computación más cortos.

## Funciones

En Haskell, una función es una expresión que toma uno o más argumentos y devuelve un resultado. Las funciones en Haskell son
definidas utilizando la sintaxis siguiente:
nombreFuncion :: tipoArgumento1 -> tipoArgumento2 -> tipoResultado
nombreFuncion argumento1 argumento2 = expresion

### Ejemplo de aplicación

```haskell
-- Definición de una función que eleva al cuadrado un número
cuadrado :: Int -> Int
cuadrado x = x * x

-- Definición de una lista de números
numeros :: [Int]
numeros = [1, 2, 3, 4, 5]

-- Aplicación de map para elevar al cuadrado cada elemento de la lista  'numeros'
cuadrados :: [Int]
cuadrados = map cuadrado numeros

-- Imprime la lista resultante
main :: IO ()
main = print cuadrados
```

## Características

### Transparencia referencial

Establece que una función siempre devolverá el mismo resultado para un mismo conjunto de entradas, sin importar en qué contexto se
llame a la función. En otras palabras, si una función se llama dos veces con los mismos argumentos, siempre se obtendrá el mismo
resultado. Esto hace que las funciones sean más predecibles y fáciles de razonar, lo que es una ventaja importante en el diseño de
software.

```haskell
sumaTerna :: Num a => (a, a, a) -> a
sumaTerna (x,y,z) = x + y + z
```

### Utilización de tipos de datos genéricos

Se refiere a la capacidad de definir estructuras de datos y funciones que trabajen con cualquier tipo de dato sin necesidad de
especificar explícitamente cada tipo de dato en particular.

```haskell
suma :: Num a => a -> a -> a
suma x y = x + y
-- > suma 2 3
-- 5
-- > suma (1/2) (1/3)
-- 5/6
```

### Recursividad

Basada en el principio matemático de inducción, que se ve expresada en el uso de tipos de datos recursivos, como las listas, y
funciones recursivas que las operan.

```haskell
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n-1)
```

### Orden superior

Posibilidad de tratar a las funciones como datos mediante la definición de funciones de orden superior, que permiten un gran nivel
de abstracción y generalidad en las soluciones. El uso correcto de las funciones de orden superior puede mejorar substancialmente
la estructura y la modularidad de muchos programas.

```haskell
  aplicarFuncion :: (a -> b) -> a -> b
  aplicarFuncion f x = f x
```

### Memoria

Los lenguajes funcionales relevan al programa de la compleja tarea de gestión de memoria. El almacenamiento se asigna y se
inicializa implícitamente, y es recuperado automáticamente por un recolector de la basura (garbage collector). La tecnología para
la asignación de memoria y de la recolección de la basura están actualmente bien desarrollados por lo que su costo de
funcionamiento es leve.

### Abstracción

La manera de construir abstracciones es a través de funciones, ya que no existen los conceptos de variables o el concepto de
cambio de estado.

### Funciones matemáticas

Basado en la matemática y en la teoría de funciones.

## Ejemplo

### Ejemplo JavaScript

Esta función utiliza un bucle for para iterar desde 1 hasta el número n y va acumulando la suma de los números en una variable
llamada suma. Finalmente, se retorna el resultado de la suma.

```js
function sumatoria(n) {
    let suma = 0;
    for (let i = 1; i <= n; i++) {
        suma += i;
    }
    return suma;
}
```

### Ejemplo Haskell

La función sumatoria toma un número entero n y devuelve la suma de los primeros n números enteros. La definición utiliza una
definición recursiva, en la que sumatoria n se define en términos de sumatoria (n-1), lo que significa que la función se llama a
sí misma con un argumento menor en cada paso hasta que se llega al caso base de sumatoria 0, que devuelve 0.

```haskell
sumatoria :: Int -> Int
sumatoria 0 = 0
sumatoria n = n + sumatoria (n-1)
```

## Ventajas y limitaciones

Se enumeran a continuación algunas de las ventajas y limitaciones de trabajar con este paradigma.

### Ventajas

- Tratamiento de funciones como datos
- Administración automática de la memoria.
- Simplicidad en el código.
- Rapidez en la codificación de los programas.

### Limitaciones

- No es fácilmente escalable.
- Difícil de integrar con otras aplicaciones.
- Ineficiencia de ejecución.

## Áreas de aplicación

El paradigma funcional tiene diversas áreas de aplicación entre las cuales podemos enumerar a las siguientes:

- **Demostraciones de teoremas**: Por su naturaleza “funcional” este paradigma es útiles en la demostración automática de teoremas, ya que permite especificar de manera adecuada y precisa problemas matemáticos.
- **Creación de compiladores, analizadores sintácticos**: Su naturaleza inherentemente recursiva le permite modelar adecuadamente estos problemas.
- Resolver problemas que requieran demostraciones por inducciones.
- En la industria se puede usar para resolver problemas matemáticos complejos.
