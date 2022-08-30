""" Ejercicio N° 2 """

# INPUT
numero = int(input("Ingrese el numero: "))
i = numero
n = 1
# PROCESSING
while i >=1:
    n *= i
    i -=1

# OUTPUT
print(" El factorial de : " + str(numero) + " es " + str(n))