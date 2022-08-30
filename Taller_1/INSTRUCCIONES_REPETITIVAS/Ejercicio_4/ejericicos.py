""" Ejercicio N° 3 """

n = str(input("Ingrese un numero: "))
l = str(len(str(n)))
indice = 1
inverso = ""

while indice <= int(l):
    v = str(n[-indice])
    indice += 1
    inverso = inverso + str(v)

if n == inverso:
    print(" El numero " + str(n) + " es capicúa")
else:
    print(" El numero " + str(n) + " No es capicúa")