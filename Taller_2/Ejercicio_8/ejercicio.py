"""Ejercicio No. 8
Programa para resolver una ecuacion de segundo grado """

print("-------------------------------")
print("-- ecuacion de segundo grado --")
print("-------------------------------")

print("\n una ecuacion de segundo grado es por la forma ax^2 +bx + c = 0 \n")
#Input

a = int(input("Ingrese el valor: "))
b = int(input("Ingrese el valor: "))
c = int(input("Ingrese el valor: "))

from math import sqrt

w = (b**2)-4*a*c

if w < 0:
    print("Esto equivale al grupo de los complejos: ")
else:
    q1 = (-b+sqrt(b**2+(4*a*c)))/(2*a)
    q2 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    print("Las x son: " + str(q1) + "tambien" + str(q2))