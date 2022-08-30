""" Problema No. 4:
Verificar si el ultimo digito es un numero PAR"""

print("-------------------------------------------")
print("--------------ULTIMO DIGITO PAR? ----------")
print("-------------------------------------------")

# Input
x = int(input("Digite el valor de x: "))

# Processing
ultimo_digito = x % 10
r = ultimo_digito % 2

if r == 0:
    print("El ultimo digito de " + str(x) + "es PAR")

print("eso era ..... ")