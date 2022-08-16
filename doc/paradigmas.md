# Paradigmas

## Paradigma de programación

* Conjunto coherente de métodos para resolver un problema.
* Colección de patrones conceptuales integrados que orientan (guían) el proceso de desarrollo de software y determinan la estructura de un programa válido.
* Es un modelo básico de diseño e implementación de programas.
Un modelo que permite desarrollar programas conforme a ciertos principios o fundamentos específicos que se aceptan como válidos.
* En otras palabras, es una colección de modelos conceptuales que juntos modelan el proceso de diseño, orientan la forma de pensar y solucionar los problemas y, por lo tanto, determinan la estructura final de un programa.

## Lenguajes y Paradigmas: “soportar” o “admitir”

* Un LP “soporta” un paradigma si provee mecanismos que facilitan su implementación eficiente. Es decir, implementa mecanismos que permiten la sencilla aplicación del paradigma (impone restricciones para respetarlo).
* Un LP “admite” un paradigma si es posible escribir programas siguiendo los lineamientos del paradigma, pero hacerlo demanda un esfuerzo notable.
* El LP no exige la aplicación del paradigma, permite programar de acuerdo al paradigma pero sin proveer facilidades.
* Los LP, necesariamente, se encuadran en uno o varios paradigmas a la vez a partir del tipo de órdenes que permiten implementar, algo que tiene una relación directa con su sintaxis.

## Clasificación de los paradigmas de programación

* Procedimentales u operacionales:
  * Imperativo. Sentencias + secuencias de comandos.
  * Orientado a objetos. Objetos + mensajes.

* Declarativos o no convencionales:
  * Lógico. Aserciones lógicas: hechos + reglas.
  * Funcional. Los programas se componen de funciones.

![Mapa conceptual paradigmas](img/mapa-paradigmas.png)

### Paradigmas procedimentales u operacionales

* Indican el modo de construir la solución, es decir detallan paso a paso el mecanismo para obtenerla.
* Se basan en “cómo” lograr la solución.
* Características: secuencia computacional e instrucciones de control (decisiones e iteraciones).

### Paradigmas declarativos

* Describen las características que debe tener la solución. Es decir especifican “qué” se desea obtener pero no requieren indicar “cómo” obtenerla.
* Se basan en desarrollar programas especificando o “declarando” un conjunto de proposiciones, condiciones, restricciones, afirmaciones, ecuaciones o transformaciones que caracterizan al problema y describen su solución

## Paradigma Imperativo

* Un programa es una secuencia de instrucciones que indican el flujo de la ejecución.
* Ejecución secuencial de instrucciones.
* Uso de variables representando valores de locaciones de memoria.
* Uso de sentencias de asignación para cambiar los valores de las variables, permitiendo así al programa operar sobre las locaciones de memoria.
* Su esencia es resolver un problema mediante la ejecución repetitiva y paso a paso de operaciones y cálculos con la asignación de los valores calculados a posiciones de memoria.
* La programación consiste en determinar qué datos son requeridos para el cálculo, asociar a esos datos una dirección de memoria, y efectuar, paso a paso, una secuencia de transformaciones en los datos almacenados, de forma que el estado final represente el resultado correcto.
* Se busca estructurar el control realizando una programación estructurada y modular con abstracción de datos para fomentar la reusabilidad y extensibilidad.
* Los programas se construyen siguiendo una aproximación Top-Down y Modular:
  * Sólo subprogramas.
  * Dividir para conquistar.
  * Existen abstracciones algorítmicas: abstracción a nivel instrucción (agrupar instrucciones en unidades – Procedure de Pascal) y abstracción de expresiones (Function de Pascal).
* Los programas se construyen siguiendo una aproximación Modular:
  * Programación estructurada: estructuras de control a nivel instrucción (secuencia, selección e iteración).
  * Programación modular: descomponer el problema priorizando recombinación y reutilización en otros problemas. Los módulos deben realizar conceptualmente una sola tarea.
  * Abstracción de datos: reconocer entidades abstractas (hallar representación para los datos) y operaciones lógicas (transformar en operaciones concretas).
* Lenguajes: PASCAL, C, Fortran, Algol, COBOL, ADA, CLIPPER, FOX, PL/1, etc.

### Torres de Hanoi en Pascal

  ```pascal
  PROGRAM Hanoi(input, output); 
  VAR N:integer; 
  PROCEDURE dohanoi(N, Tfrom, Tto, Tusing : integer); 
  BEGIN 
      IF N > 0 THEN 
      BEGIN 
            dohanoi(N-1, Tfrom, Tusing, Tto); 
            writeln('move ', Tfrom:1, ' --> ', Tto:1); 
            dohanoi(N-1, Tusing, Tto, Tfrom); 
      END 
  END; 
  BEGIN 
      dohanoi(5, 1, 3, 2)
  END.
  ```

### Torres de Hanoi en C

  ```C
  #include <stdio.h>
  #include <conio.h>
  void hanoi(int n,int com, int aux, int fin);
  void main(void) {
      hanoi(5, 'A', 'B', 'C');
  }
  void hanoi(int n,int com, int aux, int fin){
        if(n==1)
            printf("%c->%c",com,fin);
        else {
            hanoi(n-1,com,fin,aux);
            printf("\n%c->%c\n",com,fin);
            hanoi(n-1,aux,com,fin);
        }
  }
  ```

## Paradigma Orientado a Objetos

* Se caracteriza por reconocer las entidades del problema (similar a la abstracción de datos).
* Caracterizado por atributos y comportamiento (de acuerdo a su propósito y habilidades).
* Entidad = Objeto (abstracciones que representan las entidades del mundo real que forman parte del dominio del problema).
* Todo es pensado como un objeto.
* Comunicación por mensajes, diferente a la semántica de llamadas a procedimiento.
* Mensaje: invocación de un método de un objeto en particular.
* Concibe a un sistema como un conjunto de entidades que representan al mundo real, los “objetos”, que tienen distribuida la funcionalidad e información necesaria y cooperan entre sí para el logro de un objetivo común.
* Estructura de desarrollo modular basada en objetos, que son definidos a partir de clases, como implementación de tipos abstractos de datos.
* Encapsulamiento: separa las interfaces de las implementaciones de la funcionalidad del sistema (método) y oculta la información (variables).
* Mecanismo de envío de mensajes (permite delegación de responsabilidades).
* Polimorfismo: responden a un mismo mensaje: 3 + 5; “Ho” + “la”;
* Herencia: permite que una clase sea definida como una extensión o modificación de otra (Subclase es una SuperClase)
* Lenguajes: Smalltalk, Eiffel, Java, C++, C#, Python, Simula, Objective C, etc.

### Torres de Hanoi en Java

  ```java
  public class MainClass { 
      public static void main(String[] args) { 
            doTowers(5, 'A', 'B', 'C'); 
      } 
      public static void doTowers(int topN, char from, char inter, char to) { 
            if (topN == 1)  
                System.out.println("Disk 1 from " + from + " to " + to); 
          else { 
                doTowers(topN - 1, from, to, inter); 
                System.out.println("Disco " + topN + " desde " + from + " hacia " + to);
              doTowers(topN - 1, inter, from, to);
          }
      }
  }
  ```

### Torres de Hanoi en Smalltalk

  ```smalltalk
  moveTower: height from: fromPin to: toPin using: usingPin
  (height > 0) ifTrue: [
      self moveTower: (height-1) from: fromPin to: usingPin using: toPin.
      self moveDisk: fromPin to: toPin.
      self moveTower: (height-1) from: usingPin to: toPin using: fromPin]
  moveDisk: fromPin to: toPin
  Transcript cr.
  Transcript show: (fromPin printString,' - > ', toPin printString). 
  ```

### Torres de Hanoi en Python

  ```python
  def hanoi(n, inc='1', temp='2', fin='3'):
    if n > 0:
        hanoi(n-1, inc, fin, temp)
        print('se mueve de torre', inc, 'a torre', fin)
        hanoi(n-1, temp, inc, fin)

  hanoi(5)
  ```

## Paradigma Lógico

* Basado en lógica de predicados de primer orden y más en particular aún, las Claúsulas de Horn (reglas de la lógica, lenguaje preciso para expresar conocimiento). Dichas cláusulas son una forma de lógica de predicados con una sola conclusión en cada cláusula y un conjunto de premisas de cuyo valor de verdad se deduce el valor de verdad de la conclusión: una conclusión es cierta si lo son simultáneamente todas sus premisas.
* LP representativo: Prolog. Existen diferentes versiones y variantes (dialectos), pero todas basadas en la misma raíz del lenguaje PROLOG.
* Los fundamentos del paradigma son:
  * Deducir consecuencias a partir de premisas (inferir conclusiones a partir de datos).
  * Estudiar o decidir el valor de verdad de una sentencia a partir del valor de verdad de otras.
  * Establecer la consistencia entre hechos y verificar la validez de argumentos.
* Características de los lenguajes lógicos:
  * Eliminación del control. Internamente, existe un mecanismo interno llamado backtracking que actúa como control de secuencia.
  * El concepto de variable es más matemático, son nombres que retienen valores. Las variables son “unificadas” con valores particulares temporalmente y se van sustituyendo durante la ejecución del programa.
  * Establecen “que” es lo que se debe hacer sin dar ninguna especificación sobre el “cómo” hacerlo.
* Características de los programas lógicos:
  * No tiene un algoritmo que indique los pasos que detallen la manera de llegar a un resultado.
  * Conjuntos de axiomas que establecen relaciones.
  * Definen un conjunto de consecuencias que determinan el significado.
  * Son teoremas y la ejecución es una prueba automática.
  * Es decir, que los programas lógicos se consideran como una serie de aserciones lógicas.
  * Contiene una base de conocimiento sobre la que se hacen consultas.
  * La base de conocimiento está formada por hechos, que representan la información del sistema expresada como relaciones entre datos, y reglas lógicas que permiten deducir consecuencias a partir de combinaciones entre los hechos y, en general, otras reglas.
  * Se construye especificando la información del problema real en una base de conocimiento en un lenguaje formal y el problema se resuelve mediante un mecanismo de inferencia que actúa sobre ella. Así pues, una clave de la programación lógica es poder expresar apropiadamente todos los hechos y reglas necesarios que definen el dominio de un problema.

### Prolog

* Desarrollado en 1972 por Alain Colmerauer, Robert Kowalski y Philippe Roussel.
* Un programa escrito en un lenguaje lógico es una secuencia de “cláusulas”.
* Las cláusulas pueden ser:
  * Hecho: Ejemplo: tiene(coche,ruedas).
  * Regla: Ejemplo: virus(X):- programa(X),propaga(X).
* Ejemplo 1:

  ```prolog
  padre(juan, alberto).
  padre(luis, alberto).
  padre(alberto, leoncio).
  padre(gerónimo, leoncio).
  padre(luis, gerónimo).
  hermano(A,B) :- padre(A,P), padre(B,P), A \== B.
  nieto(A,B) :- padre(A,P), padre(P,B).
  ```

* Ejemplo 2:

  ```prolog
  persona(ana).
  persona(pepe).
  persona(juan).
  persona(josé).
  edad(ana, 23).
  edad(pepe, 19).
  edad(juan, 14).
  edad(josé, 5).
  persona_mayor_edad(P) :- persona(P), edad(P,E), E>18.
  persona_mayor_que(P1,P2) :- persona(P1), persona(P2), edad(P1,E1), edad(P2,E2), E1>E2.
  ```

* Ejemplo 3:

  ```prolog
  habla(ale,ruso).
  habla(juan,ingles).
  habla(maria,ruso).
  habla(maria,ingles).
  seComunicaCon(X,Y) :- habla(X,L), habla(Y,L), X\=Y
  ```

* Ejemplo 4:

```prolog
longitud([],0).
longitud([X|Y],N) :- longitud(Y,M), N=M+1.
```

### Torres de Hanoi en Prolog

  ```prolog
  hanoi(1,A,B,C) :- write("Mueve del ",A," al ",C), nl.
  hanoi(N,A,B,C) :- N>1, M is N-1, hanoi(M,A,C,B), hanoi(1,A,B,C), hanoi(M,B,A,C). 
  ```
