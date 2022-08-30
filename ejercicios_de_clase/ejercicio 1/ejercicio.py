"""Ejercicio
Programa para determinar si dados 3 numeros enteros, la suma de los dos primeros es igual al tercero"""

print("-------------------------------------------------")
print("---3 numeros, la suma de los dos es igual al 3---")
print("-------------------------------------------------")

# input
x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un segundo numero: "))
z = int(input("Ingrese un tercer numero: "))

# processing
if (x + y) == z:
    print("Los numeros son iguales por que la suma de:  " + str(x) + " + " + str(y)+ " es el mismo numero "
    + str(z))
else: 
    print("No son iguales por que la suma de: " + str(x) + " + " + str(y) + " no da " + str(z))