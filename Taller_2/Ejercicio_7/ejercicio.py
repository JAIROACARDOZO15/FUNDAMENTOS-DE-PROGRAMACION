"""Ejercicio No. 7
Programa para resolver una ecuacion de primer grado """

print("------------------------------")
print("-- ecuacion de primer grado --")
print("------------------------------")

# Input
x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de Y: "))

#Processing
if x != 0:
    a = (-y/x)
    print("La solucion de la ecuacion es a: " + str(a))
elif x == 0 and y != 0:
    print("La ecuacion no tiene solucion ")
else:
    print("La ecuacion tiene infinitas soluciones")