" Ejercicio N° 4 "

import random

d1 = ""
d2 = ""
d3 = ""
d4 = ""
d5 = ""
d6 = ""

numeros_dados = int(input(" Ingrese el numero de dados que desea lanzar: "))

for dados in range(numeros_dados):
    r_dado = random.randint(1, 6)
    if r_dado == 1:
        d1 += "#"
    elif r_dado == 2:
        d2 += "#"
    elif r_dado == 3:
        d3 += "#"
    elif r_dado == 4:
        d4 += "#"
    elif r_dado == 5:
        d5 += "#"
    elif r_dado == 6:
        d6 += "#"

print("1: " + d1)
print("2: " + d2)
print("3: " + d3)
print("4: " + d4)
print("5: " + d5)
print("6: " + d6)