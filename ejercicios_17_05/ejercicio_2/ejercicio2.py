""""EJERCICIO N° 2"""

# INPUT

c = int(input("Digite el valor del capital c: "))
b = 2 * c
n = 0
#PROCESSING

while(c <= b):
    c = 1.05 * c
    n = n + 1
    
# OUTPUT
print("El capital se duplica a los " + str(n) + " Meses ")