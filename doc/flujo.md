# Control de Flujos

* La manera cómo se incorpora en el LP determina el orden de ejecución de un programa.
* Los mecanismos del LP utilizados para especificar el orden de ejecución, pueden ordenarse en categorías:
  * Secuencia. Selección. Iteración.
  * Abstracción procedural.
  * Recursión.
  * Concurrencia.
  * Manejo de excepciones.

## Expresión

* Es una forma fundamental de especificar computación en un LP.
* Consiste de un objeto simple (constante o variable) o un operador o una función aplicada a una colección de operandos o argumentos (cada uno de los cuales define una expresión).
* Consta de:
  * Operadores (unarios, binarios o ternarios)
  * Operandos
  * Paréntesis
  * Llamadas a función
* La mayoría de los lenguajes imperativos adoptan una notación infija para los operadores, pero hay otras opciones:
  * Prefija: op a b | op (a, b) | (op a b)
  * Infija: a op b
  * Posfija: a b op
* Aspectos de diseño:
  * Reglas de precedencia y asociatividad de operadores: orden en el cual operadores con diferente precedencia son evaluados. Pueden modificarse con el uso de paréntesis.
  * Orden de evaluación de los operandos
  * Sobrecarga de un operador
  * Errores en las expresiones

## Asignación

* En el **paradigma declarativo**, el cómputo consiste en **evaluar expresiones**.
* En el **paradigma operacional**, el cómputo consiste en una **serie ordenada de cambios** (de los valores de las variables en memoria).
* La sintaxis general tiene la siguiente forma:
  * \<variable destino> \<operador de asignación> <expresión>
* Se puede definir la operación de asignación como:
  1. Computar el valor del lado izquierdo (l-value, denotan locaciones).
  2. Computar el valor de la expresión del lado derecho (r-value, denotan valores).
  3. Asignar el valor computado del lado derecho al computado como objeto de dato del lado derecho.
  4. Retornar el valor computado como valor del lado derecho como resultado de la asignación.
* La asignación puede en algunas circunstancias darse en forma implícita. Generalmente esto sucede en:
  * La inicialización en las declaraciones.
  * El pasaje de parámetros.

## Evaluación de Operandos

* Variables: cargar el valor desde memoria.
* Constantes: algunas veces son cargadas desde la memoria, otras veces la constante puede ser parte de las instrucciones del lenguaje máquina.
* Expresiones parentizadas: se evalúan las expresiones de acuerdo al modo de evaluación elegido.

* Si ninguno de los operandos y operadores tienen efectos colaterales, entonces el orden de evaluación es irrelevante.

## Evaluación de Expresiones

* **Evaluación Estricta o Ansiosa**:
  * Los argumentos de una función o los operandos de la expresión son siempre completamente evaluados antes de la aplicación de la función u operador.
  * Es la tradicionalmente utilizada por los LP.
  * En este tipo de evaluación una expresión se evalúa al momento de establecer la ligadura con una variable.
  * Ventaja: el programador puede determinar el orden de ejecución.
  * Desventaja: fuerza la evaluación de expresiones que pueden no ser necesarias en tiempo de ejecución.
  
* **Evaluación No Estricta o Perezosa**:
  * Los argumentos de una función o los operandos de la expresión no son evaluados a menos que sean utilizados en el cuerpo de la función o sean necesarios para determinar el valor de la expresión.
  * Las funciones se aplican antes de evaluar sus argumentos.
  * Ejemplo:

      ```python
      def sumar(x):
        y = 2+3 * 2
        z = 2+3 + 10
      ```

    * Considerar la siguiente llamada sumar(2+3)
    * El resultado, se obtiene sustituyendo x con la expresión 2+3. La expresión 2+3 y no el valor 5, es pasado como el de valor de x en la función.

## Tipos de Control de Flujo

* **No estructurado**:
  * Se provee a través de saltos condicionales e incondicionales.
  * Los primeros LP cercanos al hardware de la máquina trabajaban con tipos básicos y con etiquetas o rótulo y saltos como instrucciones.
  * Ejemplo:

      ```c
      if E1  
        C1: goto L1
      else 
        C2: goto L2
      ```

    * El uso de la instrucción el goto conduce a programas con diseño no estructurado, haciendo muy difícil utilizar modelos de correctitud para los programas.
    * El uso de este tipo de instrucciones es superfluo ya que puede fácilmente simularse con secuencias de control estructuradas.

* **Estructurado**:

* Opciones de alto nivel:
  * **Break**: salida incondicional. Esta instrucción provoca que el programa avance hacia adelante a un punto explícito al final de la estructura de control.
  * **Continue**: se utiliza en las iteraciones. El control salta al final del bucle, con lo que el contador se incrementa y comienza otra comprobación.

* Diseño: para obtener programas más fáciles de entender, verificar, corregir, modificar y reverificar se debe enfatizar:
  * Organización jerárquica de la estructura del programa.
  * Uso de estructuras de control estructuradas.
  * Correspondencia entre el orden del texto del programa y el orden de la ejecución.
  * Usar grupos de sentencias con propósito simple.

## Estructuras de control estructuradas

* **Secuencia**:
  * Una sentencia compuesta es una secuencia de instrucciones que pueden ser tratadas como una sola sentencia en la construcción de sentencias más grandes.
  * Representa la composición.
  * El orden en el que aparecen en el texto del programa es el orden en el cual son ejecutadas.

* **Condicional**:
  * Expresa una alternativa entre dos o más sentencias.
  * El control de las alternativas es controlado por una condición, usualmente expresada a través de una expresión booleana.
  * La forma más común de condicional es la sentencia if-then-else.
  * La mayoría de los LP permiten anidar sentencias condicionales, lo que puede provocar algunos problemas semánticos (interpretación del programa resultante). Convención: asociar el else al if más cercano: C, C++, C# y Java.
  * Sentencia condicional múltiple: permite la selección de una de un grupo no fijo de sentencias o grupos de sentencias. Forma más común es la sentencia switch.

* **Iteración o loop o ciclos**:
  * Es aquella que causa que una sentencia o colección de sentencias se ejecute cero o más veces.
  * Los LP que proveen facilidades para definir iteración conducen a programas menos extensos, flexibles, más simples de escribir y almacenar.
  * Tipos:
    * Simple: Ejemplo en COBOL

      ```COBOL
      PERFORM <cuerpo> <variable> TIMES
      ```

    * Con contador: Ejemplo en Pascal

      ```Pascal
      for <variable> := <expresion>  to| downto <expresion> by <expresion> do <instrucción>
      ```

    * Con condición: Ejemplo en C

      ```C
      for ([<expresion>]; [<expresion>]; [<expresion>]) {<instrucción>}
      while (<expresion>) {<instrucción>}
      ```

    * Infinitos: Ejemplo en Java

      ```java
      while (true) {
      }

      i = 1; 
      while (i<10) {
        i = i-1;
      }
      ```

    * En base a datos: Ejemplo en Java (iterador)

    ```java
      for(<tipo> <variable> : <colección>) {

      }

      for(Iterator<T> it = <colección>.iterator(); it.hasNext();) {

      }

    ```

## Recursión

* Es un mecanismo de control que no requiere sintaxis adicional.
* Aquellos LP que proveen abstracciones procedurales y/o funcionales sólo deben habilitar que las mismas tengan la posibilidad de llamarse a sí mismas.
* Esta manera de estructurar el control permite llegar en algunas oportunidades a códigos más elegantes.

## Excepciones

* Son eventos inusuales que deberían controlarse sin oscurecer la legibilidad.
  * División por cero.
  * Apertura de un archivo que no existe.
  * Indices de arreglo fuera de rango.
  * Valores de parámetros que no concuerdan con los especificados.
  * Operación no válida para un tipo de dato.
* Es un proceso que la unidad dónde se provocó está incapacitada para atenderlo de manera que termine normalmente.
* Un software que provee excepciones es confiable y tolerante a fallas.
* Pueden ser:
  * Detectadas por el HW o SW.
  * Situaciones de error o no previstas.
  * Controladas a través de mecanismos generales específicos.
* ¿Qué acción toman los LP cuando se termina de manejar las excepciones?
  * **Reasunción**: se maneja la excepción y se devuelve el control al punto siguiente donde se invocó a la excepción, permitiendo **continuación** de la ejecución de la unidad.
  * **Terminación**: se **termina** la ejecución de la unidad que alcanza la excepción y se transfiere el control al manejador.
* LP que incorporan el manejo de excepciones: ADA, C++, Java, Python, Kotlin, etc.
* Ejemplo Java

  ```java
  try {
    // bloque
  } catch (NombreExcepción1) {
    // bloque manejador 1
  } catch (NombreExcepciónN) {
    // bloque manejador N
  } finally {
    // bloque final
  }
  ```

* Ejemplo Python

  ```python
  try:
    # bloque
  except nombre de la excepción 1:
    # bloque manejador 1
  except nombre de la excepción N:
    # bloque manejador N
  else: 
    # bloque que se ejecuta solo si no se levanta una excepción
  finally:
    # bloque que se ejecuta siempre
  ```

### Mecanismos no específicos

* La situación la detecta el subprograma y puede ser manejada por el mismo subprograma, decidiendo qué acciones ejecutar.

```plain
proc A
if Cond1 then Manejador1
         else if Cond2 then Manejador2
                       else S
end A
```

## Eventos

* Por conveniencia, en algunos casos, los programas son estructurados como sistemas reactivos, sistemas donde determinados eventos que ocurren en el entorno determinan el orden de ejecución.
* En la programación basada en eventos el control de ejecución se basa en acciones producidas por el usuario o por el entorno.
* Un manejador de eventos es un código que se ejecuta en respuesta a un evento.
* Ejemplos donde se requiere programación orientada a eventos: sistemas reactivos, interfaces gráficas, sistemas operativos.
* En una GUI los eventos se producen a partir de la interacción del usuario con las componentes reactivas de la interfaz.
* Un evento es una notificación de que el usuario ha realizado un acción que requiere respuesta por parte del sistema.
* Un manejador de eventos es el segmento de código que ejecuta en respuesta al evento.

  ```javascript
  on event
  when condition
    do action


  boton = document.getElementById('idBoton')
  boton.addEventLister('click', validar)

  function validar() {
    // validar datos
  }

  ```

* Una GUI es una colección de componentes con una representación gráfica y capacidad para percibir eventos generados por el usuario.
* Las componentes son las partes individuales a partir de las cuales se conforma una interfaz gráfica. Por ejemplo, el botón para cerrar una ventana, la barra de desplazamiento de una ventana o la ventana misma
* Un usuario realiza una acción que provoca un evento ante el cual una componente tiene una reacción.
* Una componente está asociada a un objeto gráfico que puede interactuar con el usuario.
* La implementación de una interfaz gráfica consiste en:
  1. Crear un objeto gráfico para cada componente de la GUI e insertarlo en otras componentes contenedoras.
  1. Definir el comportamiento de las componentes reactivas en respuesta a las acciones del usuario.

## Subprogramas

* Los LP operativos brindan mecanismos para dividir el programa en unidades cada una de las cuales tiene cierta coherencia y lógica. Su incorporación fomenta:
  * Eficiencia: permiten factorizar el código.
  * Legibilidad: metodología de diseño top-down.
  * Verificación: una unidad puede pensarse como una mapeo entre dominios de valores.
* Los LP permiten que un programa esté compuesto por subprogramas (secuencia de sentencias de un programa).
* En general se las llama rutinas, procedimientos, métodos, funciones (un valor), llaves o delimitadores, closures o funciones lambda.
* Ejemplo:

  ```c
  int f1() {
    return 3 + 2;

  }
  int main() {
    int y = f1(); 
  }
  ```

  ```pascal
  Program Programa;
  procedure B;
  var x: integer;
  begin
  ...
  end;
  begin
    B();
  end.
  ```

  ```java
  public class Cliente {
    private int codigo;
    public Cliente() {
      codigo = 0;
    }
  }
  ```

### Aspectos de diseño a tener en cuenta por el LP

* Generales:
  * Entidades
  * Ligaduras
  * Reglas de alcance
  * Sistemas de tipos
  * Soporte para definir subprogramas

* Específicos:
  * Estructura estática
  * Recursividad
  * Control
  * Métodos de pasaje de parámetros
  * Correspondencia entre parámetros formales y actuales
  * Sobrecarga y polimorfismo
  * Tipos de los parámetros: datos y unidades
  * Ambiente de referenciamiento de los subprogramas que recibe como parámetro (chequeo estático o dinámico de subprogramas)

### Atributos del subprograma

* Nombre:
  * Cadena de caracteres (identificador) que se introduce en su declaración.
  * Se usa para invocar a la rutina.

* Alcance:
  * Segmento de código dentro del cual el subprograma puede invocarse (si incluye al mismo subprograma acepta recursividad).
  * Rango de instrucciones donde se conoce su nombre.

* Ambiente de referenciamiento:
  * Local: entidades declaradas dentro de la rutina (visibles dentro de la rutina).
  * No local: referencias a entidades declaradas en otros subprogramas cuyo alcance es visible en la rutina. Toda variable no locales que pueda ser referenciada por cualquier subprograma en el programa se llaman variables globales.

* Lista de parámetros y tipos
  * Permiten la comunicación del subprograma con el resto del programa.
  * Si se admiten parámetros de diferentes tipos el subprograma es polimórfico.
  * El encabezado de la rutina define el tipo de los parámetros y el tipo del valor de retorno (si lo hay).
  * Signatura: permite especificar el tipo de una rutina. Una rutina fun que tiene como entrada parámetros de tipo T1, T2, Tn y devuelve un valor de tipo R, puede especificarse con la siguiente signatura fun: T1xT2x....Tn  --> R
  * Un llamado a una rutina es correcto si está de acuerdo al tipo de la rutina. La conformidad requiere la correspondencia de tipos entre parámetros formales y reales.
  * Un subprograma tiene:
    * Encabezado: formado por el nombre del subprograma, la lista de parámetros y el tipo del resultado.
    * Cuerpo: formado por las declaraciones locales y la sección ejecutable.
  * Declaración = encabezado
  * Definición = Declaración + Cuerpo

  ```c
  int suma(int n) {                // ENCABEZADO = DECLARACIÓN
    int s = 0;                     // CUERPO
    for(int i = 1; i <= n; ++i)    // CUERPO
      s += i;                      // CUERPO 
    return s;                      // CUERPO 
  }
  ```

### Parámetros

* Hay dos maneras de hacerle llegar los datos sobre los cuales computar a una unidad, a través del:
  * acceso a variables no locales visibles para la unidad.
  * pasaje de parámetros.
* Los datos pasados como parámetros son accedidos a través de nombres que son locales a la unidad.
* El pasaje de parámetros es más flexible, ya que define computación parametrizada.
* El uso de variables no locales puede conducir a programas menos confiable.
* Tipos:
  * **Parámetro formal**:
    * Se declaran/definen en el encabezado de la unidad; aclarando en general su tipo.

      ```python
      def sumar(a, b):    # a y b son parámetros formales
        return a + b
      ```

  * **Parámetro actual o real o argumentos**:
    * Son variables, constantes, expresiones que se utilizan en la invocación de la unidad.

      ```python
      sumar(2, 3) # 2 y 3 son parámetros actuales
      ```

### Binding entre parámetros formales y reales

* **Aspecto sintáctico**: cómo se asocian sintácticamente los parámetros reales y formales.
  * **Posicional**: asociación por la posición de los parámetros en la definición (formales) y la invocación (reales). Se ligan uno a uno.

    ```plain
    PROCEDURE P(x:INTEGER; y:FLOAT; z:INTEGER);
    BEGIN
    ...
    END;
    ...
    P(a, b, c);
    ...
    ```

  * **Faltantes o implícitos**: sólo pueden estar al final de los parámetros de la función. No es posible que un parámetro del medio pueda faltar.

    ```python
    def ff(str1, a=1, str2='No'):
      pass

    ff('Hola')
    ff('Hola', 2)
    ff('Hola', 2, 'que tal')
    ```

  * **Explícito**: el llamador debe conocer los nombres de los parámetros formales. Útil cuando existen muchos parámetros faltantes y se quieren pasar pocos.

    ```python
    def ff(str1, a=1, str2='No'):
      pass

    ff('Hola', a=3)
    ff('Hola', str2='¿cómo andas?')
    ```

  * **Anónimo**: cantidad variable de parámetros. El invocado no conoce la cantidad ni el tipo de los parámetros.

    ```c
    void ff(int a, ...);
    ...
    ff(x, y, 3);
    ```

* **Aspecto semántico**: que es lo que ocurre cuando se pasan parámetros.
  * **Referencia**:
    * Se crea un "alias" entre cada parámetro real y su correspondiente parámetro formal.
    * Referencian la misma celda de memoria.
    * Las modificaciones sobre el parámetro formal se reflejan en el parámetro real.
  
    ```c
    void ff(int& i) {
      i = 3;
      printf("%d\n", &i);
    }
    int main() {
      int a = 4;
      ff(a);
      printf("%d\n", a);
      printf("%d\n", &a);
    }
    ```

  * **Copia o valor**:
    * Se copian los valores  de los parámetros reales en los parámetros formales.
    * Los parámetros reales y formales se desacoplan.

    ```c
    void ff(int a, int b) {
    }

    void gg() {
      int x = 3;
      int y = 4;
      ff(x, y);
    }
    ```

### Subprogramas genéricos

* Los subprogramas factorean un segmento de código, que se ejecutará en diferentes puntos mediante una invocación customizada a través de los parámetros.
* Si difieren en algún detalle que no pueden resolver los parámetros debe repetirse la codificación.
  * Una rutina para ordenar arreglos de enteros.
  * Otra rutina para ordenar arreglos de strings.
* Se puede parametrizar el tipo (C++, Ada, Java).
* Una rutina genérica es un molde.
* Cada instanciación genera una rutina específica ligando el parámetro genérico al parámetro real durante la compilación.

### Pasaje de funciones como parámetros

```python
def x(a):
  print a

def y(z, t):
  z(t)

y(x, 1)
```

```haskell
func1 :: (a -> b) -> a -> b
func1 f x = f x

duplicar :: Int -> Int
duplicar x = x * 2

resultado :: Int
resultado = func1 duplicar 5
```

### Sobrecarga

* Un nombre con mas de una entidades.
* Hay suficiente información para permitir establecer la ligadura unívocamente.

```java
class A {

  void m() {}
  void m(int i) {}
  void m(boolean b) {}
}
```

### Closures

* Aportan características funcionales al LP.
* Permite igualar las funciones con las variables.
* Proporcionan mayor flexibilidad a las funciones.
* Permiten que un objeto retorne un método sin necesidad de dar acceso a sus propios atributos.
* Permite implementar funciones generadoras de funciones.
* LP que tienen closures: ML, Lisp, Perl, Ruby, Python, JavaScript, PHP, C++14, Java+8, Rust, GO, entre otros.
* Función evaluada o ejecutada en un ámbito diferente al cual fue definida.
* Puede hacer uso de variables no presentes en su ámbito de evaluación.
* El LP debe proveer un mecanismo para que la función acceda a las variables del ámbito correspondiente.
* Ejemplo Python (b() es un closure)

```python
def a():
  x = 2
  def b():
    y = 3
    print x+y
  return b

z = a
z()
```

* Ejemplo javascript

```javascript
function fn() {
  var x = 3;
  var lambdaFun = () => x + 1;
  x++;
  console.log(lambdaFun()); // Imprime 5
}
```

## Ejercicios

1. Considere el siguiente programa en el lenguaje Python:

    ```python
    x = 1
    def a():
      x = 2
      b()
    def b():
      print x
    b()
    ```

    1. ¿Qué imprime este programa y qué característica implica que el lenguaje tiene ámbito estático?
    1. ¿Qué imprimiría si el lenguaje tuviese ámbito dinámico?

1. Considere el siguiente programa en el lenguaje Python:

    ```python
    y = 1
    def a():
      x = 2
      def b():
        print x
        print y
      b()
      return b
    a()
    z = a
    y = 3
    x = 4
    z()
    ```

    1. ¿Qué imprime el programa? ¿Por qué?
    1. ¿Por qué las dos veces que se ejecuta la instrucción “print x” imprime el mismo valor?

1. Explique brevemente los siguientes conceptos:

   * Parámetro.
   * Parámetro real.
   * Parámetro formal.
   * Ligadura posicional.
   * Ligadura por palabra clave o nombre.

1. Complete el siguiente cuadro según lo correspondiente a cada lenguaje:

   | Tipo de pasaje de parámetros | Lenguaje |
   | -- | --     |
   |    | ADA    |
   |    | C      |
   |    | Ruby   |
   |    | Java   |
   |    | Python |

1. Ada es más seguro que Pascal, respecto al pasaje de parámetros en las funciones. Explique por qué.
1. Explique cómo maneja Ada los tipos de parámetros in/out de acuerdo al tipo de dato.
1. Indique con un ejemplo el comportamiento del parámetro formal por nombre (en el parámetro formal) para los siguientes casos de parámetros reales:
    1. Un valor entero.
    1. Una constante.
    1. Un elemento de un arreglo.
    1. Una expresión.
    1. ¿Qué sucede en cada caso?
1. Sea el siguiente programa escrito en Pascal-like:
    1. Plantee diferencias, relacionada con la forma de implementación de cada uno y los resultados sobre este ejemplo considerando los siguientes tipos de pasajes parámetros nombre, referencia y valor resultado.
    1. ¿Qué sucede si en Uno se agrega la siguiente declaración: x: integer? Indique el resultado para cada uno de los tipos de pasajes de parámetros (nombre, referencia y valor resultado)

    ![Pascal](img/ej1.png)

1. Sea el siguiente un programa escrito en Pascal:
    1. Explique cómo simularía en Pascal el pasaje por valor resultado y hágalo sobre este ejemplo. Nota: No se pueden agregar más variables, ni cambiar el nombre de las que están.
    1. Transcriba este ejemplo en Ada de manera tal que el resultado de la ejecución sea diferente si el pasaje de parámetros es por referencia y luego por valor – resultado.

    ![Pascal](img/ej2.png)
