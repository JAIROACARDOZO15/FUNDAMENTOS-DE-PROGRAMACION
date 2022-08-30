"""Ejercicio No. 6
Programa para determianr si el resultado de sumar sus dos ultimos digitos es un numeo de 1 digito"""

print("------------------------------------------------")
print("--suma de dos digitos es un numero de 1 digito--")
print("------------------------------------------------")

# Input
x = int(input("Ingrese el numero: "))

# Processing
j = int(str(x)[-1])
a = int(str(x)[-2])
i = j + a

if i < 10:
    print("la suma de los dos digitos es: " + str(i) + " el numero tiene un digito")
else:
    print("la suma de los dos digitos es: " + str(i) + " el numero tiene dos digitos")