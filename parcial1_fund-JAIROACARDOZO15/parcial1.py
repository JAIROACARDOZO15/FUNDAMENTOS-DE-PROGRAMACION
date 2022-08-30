"""Parcial No. 1 - Fundamentos de programación

Realizar el análisis (identificación de variables), diseño (diagrama de flujo) y 
construcción (programa en Python y pantallazos de su funcionamiento) que resuelva 
la siguiente situación:"""

# input
print("-------------------------------------------")
print("-----BIENVENIDO A SOCORRO CENTER ----------")
print("-------------------------------------------")

m = input("Ingrese el nombre del primer producto: ")
x = int(input("Ingrese el valor del primer producto: "))

m1 = input("Ingrese el nombre del segundo producto: ")
y = int(input("Ingrese el valor del segundo producto: "))

m2 = input("Ingrese el nombre del tercer producto: ")
z = int(input("Ingrese el valor del tercer producto: "))

# processing
if x > y and x > z:
    print("La promocion equivale a: " + str(m1) + " + " + str(m2) + " $ " + str(y+z) + " lleva el siguiente producto gratis: "
    + str(m))
elif y > x and y > z:
   print("La promocion equivale a: " + str(m) + " + " + str(m2) + " $ " + str(x+z) + " lleva el siguiente producto gratis: "
    + str(m1))
elif z > x and z > y:
    print("La promocion equivale a: " + str(m) + " + " + str(m1) + " $ " + str(x+y) + " lleva el siguiente producto gratis: "
    + str(m2))

# output
else:
    print("La promoción no se aplica por que los productos tienen el mismo valor verifique el precio o cambielos por otros productos de la tienda")
    