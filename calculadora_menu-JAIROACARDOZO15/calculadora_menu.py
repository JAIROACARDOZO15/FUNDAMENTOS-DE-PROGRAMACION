# CALCULADORA CON MENU

from math import log

#input
bandera = False 
x = float(input("Dame el valor del numero x: "))
y = float(input("Dame el valor del numero y: "))

print("Dame la opcion que deseas realizar: \n")
# Se despliega menu para seleccionar la opcion que deseas realizar
print(" 1. Sumar")
print(" 2. Restar")
print(" 3. Multiplicar")
print(" 4. Dividir")
print(" 5. Potencia")
print(" 6. Logaritmo")
opcion = int(input(" Dame la opción: "))

#processing
if opcion == 1:
    z = x + y
    print(x, " + " ,y)
elif opcion == 2:
    z = x - y
    print(x, " - " ,y)
elif opcion == 3:
    z = x * y
    print(x, " x " ,y)
elif (opcion == 4 and y != 0):
    z = x / y
    print(x, " / " ,y)
elif (opcion == 4 and y == 0):
    print(" El denomindador es igual a cero y")
    print(" no se puede realizar la division")
    bandera = True
elif opcion == 5:
    z = pow(x, y)
    print(x, " ^ " ,y)
elif (opcion == 6 and x > 0):
    z = log(x)
    print("Logaritmo de ", x)
elif (opcion == 6 and x > 0):
    print(" El valor de x es <= a cero y ")
    print(" No se puede calcular el logaritmo")
    bandera = True
else:
    print("Opcion desconocida")

#Se escribe el resultado con otra condicion
if opcion < 7 and bandera == False:
    print("Resultado", z)

