# UNIVERSIDAD NACIONAL DE HURLINGHAM

## Instituto de Tecnología e Ingeniería

## CARACTERÍSTICAS DE LOS LENGUAJES DE PROGRAMACIÓN

### Profesor: Mag. Ing. Pablo Pandolfo

---

### Parcial julio 2024

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

1. [3 puntos]: Clasifíquese cada ocurrencia de la cadena "if" según a cuál tipo de elemento del lenguaje corresponda: tipo, variable, componente de estructura, atributo, nombre de función, nombre de método, palabra clave, constante, etc.

    ```c
    static struct {
        int if = 0;
    } if;
    class if {
        int if;
        void if(int if) {
            if = 2;
        }
    }
    void if(if x) {
        if.if = 5
        x.f = 4;
    }
    void if() {
        print(if.if);
        if (true) {
            if if,
            if.if = 3;
            if(if);
            if (if.if == 4)
                if.if(if.if);
            print(if.if);
        }
        print(if.if);
    }
    void main() {
        if();
    }
    ```

1. [3 puntos]: Escríbase un programa de 5 líneas del lenguaje generado por la siguiente gramática:

    ```grammar
    01. start: programa 
    02. programa: instruccion | bloque
    03. instrucciones: instruccion | instrucciones instruccion
    04. bloque: "_comienza_bloque_" instrucciones "_termina_bloque_" 
    05. instruccion: declaracion ";" | invocacion ";" | asignacion ";" | seleccion ";" | iteracion ";"
    06. declaracion: "_se_declaran_con_el_tipo_" tipo "_las_variables_" listavariables
    07. tipo: "entero" | "largo" | "flotante" | "doble" | "cadena" 
    08. listavariables: NAME | listavariables NAME
    09. invocacion: "_se_llama_a" NAME "_con_parametros_" "_abre_parentesis_" expresion "_cierra_parentesis_" 
    10. asignacion: NAME "_se_vuelve_" expresion
    11. seleccion: "_si_" comparacion "_entonces_" bloque ";" "_sino_" bloque
    12. iteracion: "_mientras_que_" comparacion bloque 
    13. expresion: expresionsimple | comparacion 
    14. comparacion: expresionsimple comparador expresionsimple 
    15. comparador: "_es_menor_que_" | "_es_mayor_que_" | "_es_igual_que_" | "_es_mayor_o_igual_que_" | "_es_menor_o_igual_que_" | "_es_distinto_" 
    16. expresionsimple: termino
    17. termino: factor | termino "_mas_" factor | termino "_menos_" factor
    18.factor: atomo | factor "_por_" atomo | factor "_dividido_" atomo | invocacion ?atomo: NUMBER | "_menos_" atomo | NAME
    ```

1. [4 puntos]: Ejemplifíquese los siguientes enunciados:
    * una problema resuelto en 2 paradigmas distintos, ejemplo: cambio $ 156 => 100 + 50 + 5 + 1
    * una BNF para un mini lenguaje de programación esotérico
    * árbol sintáctico de una palabra del lenguaje anterior
    * polimorfismo vs no polimorfismo

---
