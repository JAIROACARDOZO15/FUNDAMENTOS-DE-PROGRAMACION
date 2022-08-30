""" Ejercicio No. 3
Construir un programa que lea un numero entero y saber si es un numero de 4 digitos"""

print("---------------------------------------")
print("-----NUMERO DE 4 DIGITOS---------------")
print("---------------------------------------")

# Input
x = int(input("Digite el numero entero: "))

# Processing
if x > 999:
    msj = (" ES DE CUATRO DIGITOS ")
else:
    msj = (" NO TIENE CUATRO DIGITOS ")

# output
print("el numero " + str(x) + msj)