"""Ejercicio No. 5
Programa para determinar si un numero entero sus dos ultimos numeros son iguales"""

print("-------------------------------------------")
print("---ENTERO DOS ULTIMOS NUMEROS SON IGUALES--")
print("-------------------------------------------")

# Input
numero = int(input("Ingrese un numero de dos cifras o mayor: "))
ultimo_digito = int(str(numero)[-1])
penultimo_digito = int(str(numero)[-2])

# Processing
if ultimo_digito == penultimo_digito:
    print("Los dos ultimos numeros son iguales")
else:
    print("Los dos ultimos numeros no son iguales")