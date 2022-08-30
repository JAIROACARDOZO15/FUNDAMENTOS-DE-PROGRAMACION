""" Ejercicio N° 3 """

n = int(input(" Ingrese un número: "))
i = 2
bandera = False

if n > 1:
    while i < n:
        if (n % i) == 0:
            bandera = True
    i += 1
else: 
    print(" El numero " + str(n) + " es compuesto ")
if bandera == True:
    print(" El numero " + str(n) + " es compuesto ")
else: 
    print(" El numero " + str(n) + " es primo ")