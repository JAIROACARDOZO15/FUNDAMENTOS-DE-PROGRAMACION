En Python las variables locales son las que se definen en una función y que solo permiten su acceso desde ella. Las globales se definen en el cuerpo principal del programa y permiten su acceso desde cualquier lugar. Las no locales son variables locales que se pueden modificar en funciones anidadas.

# Los principales tipos de ámbitos en Python son dos:

- **Ámbito local:** corresponde con el ámbito de una función, que existe desde que se invoca a una función hasta que termina su ejecución. En un programa, el ámbito local corresponde con las líneas de código de una función. Dicho ámbito se crea cada vez que se invoca a la función. Cada función tiene su ámbito local. No se puede acceder a las variables de una función desde fuera de esa función o desde otra función.

- **Ámbito global:** corresponde con el ámbito que existe desde el comienzo de la ejecución de un programa. Todas las variables definidas fuera de cualquier función corresponden al ámbito global, que es accesible desde cualquier punto del programa, incluidas las funciones. Si desde un módulo A importamos un módulo B mediante un import, desde A podremos acceder a las variables globales de B.