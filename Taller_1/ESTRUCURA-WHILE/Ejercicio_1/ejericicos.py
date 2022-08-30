""" Ejercicio N° 1 """
import random

n = int(input("Digite las veces que el dado se lanza: "))
tirar = 0
contador = 0

while tirar < n:
    dado = random.randint(1 , 6)
    print(dado)
    if dado == 3:
        contador = contador + 1 
    tirar = tirar + 1

print(" El numero 3 se repite " + str(contador) + " veces ")