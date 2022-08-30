"""Ejercicio No.2 
Programa para determinar tres numeros enteros, cual de ellos es el mayor"""

print("--------------------------------------")
print("----Numero entero cual es el mayor----")
print("--------------------------------------")

# Input 
a = int(input("Digite el numero entero: "))
b = int(input("Digite el numero entero: "))
c = int(input("Digite el numero entero: "))

# Processing

if a > b and a > c: 
    print("El numero entero mayor: ",a)
elif b > a and b > c:
    print("El numero entero mayor:" ,b)
elif c > a and c > b:
    print(" el numero entero mayor:",c)
else:
    print("No se encuentra un numero mayor")