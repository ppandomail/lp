# Control de Flujos

## Ejercicios

1. Considere el siguiente programa en el lenguaje Python:

    ```py
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

    ```py
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
    1. ¿Por qué las dos veces que se ejecuta la instrucción "print x" imprime el mismo valor?

1. Explique brevemente los siguientes conceptos:

   * Parámetro
   * Parámetro real
   * Parámetro formal
   * Ligadura posicional
   * Ligadura por palabra clave o nombre

1. Complete el siguiente cuadro según lo correspondiente a cada lenguaje:

   | Tipo de pasaje de parámetros | Lenguaje |
   | -- | --     |
   |    | ADA    |
   |    | C      |
   |    | Ruby   |
   |    | Java   |
   |    | Python |

1. Ada es más seguro que Pascal, respecto al pasaje de parámetros en las funciones. Justificar
1. Explique cómo maneja Ada los tipos de parámetros in/out de acuerdo al tipo de dato
1. Indique con un ejemplo el comportamiento del parámetro formal por nombre (en el parámetro formal) para los siguientes casos de parámetros reales:
    1. valor entero
    1. constante
    1. elemento de un arreglo
    1. expresión
    1. ¿Qué sucede en cada caso?
1. Sea el siguiente programa escrito en Pascal-like:
    1. Plantee diferencias, relacionada con la forma de implementación de cada uno y los resultados sobre este ejemplo considerando los siguientes tipos de pasajes parámetros nombre, referencia y valor resultado
    1. ¿Qué sucede si en Uno se agrega la siguiente declaración: x: integer? Indique el resultado para cada uno de los tipos de pasajes de parámetros (nombre, referencia y valor resultado)

    ![Pascal](img/ej1.png)

1. Sea el siguiente un programa escrito en Pascal:
    1. Explique cómo simularía en Pascal el pasaje por valor resultado y hágalo sobre este ejemplo. Nota: No se pueden agregar más variables, ni cambiar el nombre de las que están
    1. Transcriba este ejemplo en Ada de manera tal que el resultado de la ejecución sea diferente si el pasaje de parámetros es por referencia y luego por valor – resultado

    ![Pascal](img/ej2.png)
