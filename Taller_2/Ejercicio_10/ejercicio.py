"""Ejercicio No. 10
Elaborar un programa, que dados 3 números los devuelva en orden ascendente"""

print("-------------------------------------------------------")
print("--NUMERO DE 3 CIFRAS SE DEVUELVA DE  FORMA ASCENDENTE--")
print("-------------------------------------------------------")

x = int(input("Ingrese un numero: "))
y = int(input("Ingrese un segundo numero: "))
z = int(input("Ingrese un tercer numero: "))

if (x > y and y > z):
    print("El numero mayor es: " + str(x))
    print("El numero mayor es: " + str(y))
    print("El numero mayor es: " + str(z))
elif (x > z and z > y):
    print("El numero mayor es: " + str(x))
    print("El numero mayor es: " + str(z))
    print("El numero mayor es: " + str(y))
elif (y > x and x > z):
    print("El numero mayor es: " + str(y))
    print("El numero mayor es: " + str(x))
    print("El numero mayor es: " + str(z))
elif (y > z and z > x):
    print("El numero mayor es: " + str(y))
    print("El numero mayor es: " + str(z))
    print("El numero mayor es: " + str(x))
elif (z > y and y > x):
    print("El numero mayor es: " + str(z))
    print("El numero mayor es: " + str(y))
    print("El numero mayor es: " + str(x))
elif (z > x and x > y):
    print("El numero mayor es: " + str(z))
    print("El numero mayor es: " + str(x))
    print("El numero mayor es: " + str(y))
else:
    print("se agregaron numeros iguales, gracias")