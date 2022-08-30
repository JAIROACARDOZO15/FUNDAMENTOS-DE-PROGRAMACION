""""EJERCICIO N°1"""

# INPUT

n = int(input("Digite el valor de N: "))

#PROCESSING
i=1
suma=0
while(i <= n):
    suma = suma + i
    i = i + 1

# OUTPUT
print("La suma de las " + str(n) + " primeros naturales " + str(suma))