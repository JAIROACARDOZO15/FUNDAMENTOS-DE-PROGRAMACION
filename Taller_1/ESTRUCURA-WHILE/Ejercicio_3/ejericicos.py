""" Ejercicio N° 3 """

rango = []
rango = [int(item) for item in input("Digite los valores del rango: ").split()]

if (rango % 2) == 0:
    b = " El numero es par "
    print(b)
else:
    b = " El numero es impar "
    print(b)