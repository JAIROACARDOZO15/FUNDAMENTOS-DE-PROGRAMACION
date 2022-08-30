"""Programa para calcular la potencia 
x ^ y"""

print("-------------------------------------------")
print("-----------POTENCIA x ^ y -----------------")
print("-------------------------------------------")

# input
x = input("Digite el valor de x")
x = int(x)
y = input("Digite el valor de y")
y = int(y)

# processing
z = x**y

# output
print(str(x) + " elevado a la " + str(y) + " es igual a " + str(z))
