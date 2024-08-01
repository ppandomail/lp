# Tipos

## Ejercicios

1. ¿Qué características encierra el concepto de “tipo de datos”?
1. En todos los lenguajes ¿Una variable se liga estáticamente con su tipo? En caso de respuesta negativa, de al menos un ejemplo.
1. Enumere y explique las diferencias que existen entre el manejo de los tipos enumerativos entre Pascal y Ada. ¿Qué diferencias hay entre subtipo y subrango para cada lenguaje?
1. ¿Cómo es el manejo de punteros en C y en Java?
1. ¿Qué problemas de seguridad existen en el manejo de punteros? Ejemplifique.
1. En Python se habla de tipos de datos mutables e inmutables. ¿Para que se utiliza este tipo de datos? De al menos un ejemplo donde se puede utilizar. ¿Cómo? ¿Sucede lo mismo para Ruby? Explique la forma en que un objeto mutable puede convertirse en inmutable.
1. De un ejemplo de un lenguaje que sea fuertemente tipado y un lenguaje que no. Explicando en cada caso porque lo es y porque no lo es.
1. Ante las siguientes declaraciones de variables siguiendo la sintaxis de C:

    ```c
    typedef struct {
        int i;
        char c;
    } IntChar;

    IntChar  x;

    typedef IntChar2 IntChar;
    IntChar2 xx;

    struct {
        int i;
        char c;
    } y;

    typedef struct {
        int ii;
        char c;
    } IntChar3;

    IntChar3 z;
    ```

    * ¿Qué mecanismo de compatibilidades de tipos debería tener un lenguaje para que se cumplan las siguientes afirmaciones? ¿Por qué?
      * Las variables x e y tienen tipos compatibles.
      * Las variables x y xx tienen tipos compatibles.
      * Las variables x y z tienen tipos compatibles.
