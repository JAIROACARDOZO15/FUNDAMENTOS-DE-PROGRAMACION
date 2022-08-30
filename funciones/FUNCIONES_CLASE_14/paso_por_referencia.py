def funcion(x):
    x.append(5)

# Programa principal
x = [1 , 2]
funcion(x)
print(x)

"""
SALIDA
[1, 2, 5]

El programa principal general la lista [1, 2] que se pasa a la función.
La función agrega el elemento 5 al final de la lista 
Como la lista se pasa por referencia, automáticamente aparece
en el programa principal en ola llamada de la función
Todos los arreglos, de cualquier tipo, y de cualquier dimensión, se pasan por referencia"""