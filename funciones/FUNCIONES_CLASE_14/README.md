# FUNCIONES

## VARIABLE LOCALES Y GLOBALES

### Varibles Locales
- Variables que se definen dentro de una función.
- Son validas unicamente dentro de la función.
- Las varoables correspondie ntes a la función solamente son accesibles por la función, es decir, se pueden usar solamente por ella. Al usarlas fuera de la función marcará error.
- Una variable del algoritmo principal que se pasa a una función donde se modifica y es variable local, cambia su valor en la función pero NO en el algoritmo principal.

### Variables Globales
- Son aquellas que no importa donde se usen o se modifiquen siempre conservan los valores asignados, ya sea en el algoritmo principal o en las funciones.
- Para hacer que una variable sea global hay que definirla como tal por medio de la instrucción `global nombre_variable`

## Llamado por valor y llamado por referencia

### Paso por valor

- Cuando se pasa una variable a una función creando una nueva localidad de memoria, donde se copian los valores de los parámetros de la función.
- La memoria ocupada aumenta de tamaño.
- Aunque en Python no se aumenta la memoria, el paso de la variable es equivalente a paso por valor.

### Paso por referencia

- La variable se puede modificar en la función y el cambio siempre se realiza usando la referencia a la localidad de memoria donde se almacena la variable. Ej. variables tipo lista.

## Funciones Lambda
- Declaración de una función en un solo renglón
`f = lambda parámetros: expresion