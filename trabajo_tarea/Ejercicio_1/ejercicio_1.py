" Ejercicio N° 1 "

import random

n = int(input(" Digite la cnatidad de numeros: "))
par = 0
impar = 0
rta = "Numeros = ("

for i in range(n):
    n = random.randint(1 , 200)
    if (n % 2) == 0:
        par += 1
    else:
        impar += 1
    if i < n-1:
        rta = rta+str(n) + " , "
    else:
        rta = rta+str(n)
rta = rta+ ")"

print("-----------RESULTADOS----------")
print(rta)
print("Cantidad de pares " + str(par))
print("cantidad de impares " + str(impar))