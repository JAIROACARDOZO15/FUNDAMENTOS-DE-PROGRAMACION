" Ejercicio N° 3 "

n = int(input(" Ingrese el numero: "))
r = 1

for i in range(1, n + 1):
    r *= i

print("El factorial de el numero " + str(n) + " es " + str(r))