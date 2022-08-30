"""PROGRAMA PARA ORDENAR DE FORMA INVERSA UN NUMERO DE 4 DIGITOS"""

print("-----------------------------------------------------")
print("---- ORDEN INVERSO DE UN NUMERO DE 4 DIGITOS --------")
print("-----------------------------------------------------")

# input
x = int(input(" ingrese el numero de cuatro cifras "))

# processing
x1 = x % 10
x2 = int((x % 100 ) / 10)
x3 = int((x % 1000 ) / 100)
x4 = int((x - (x % 1000 )) / 1000 )
z= str(x1) + str(x2) + str(x3) + str(x4)

# output
print(" El numero " + str(x) + " es al reves " + str(z))
