"""Ejercicio N° 2 """
n = int(input("Ingrese un número: "))
par = 0
impar = 0

while n != 0:
    d = n % 2
    
    if d == 0:
        impar += 1
    else:
        par += 1
        
    n = int(input("Ingrese un número: "))
else:
    print("Los números impares son: " + str(impar) + " y los números pares son: " + str(par))