"""PROGRAMA PARA CALCULAR UNA RAÍZ"""

print("-----------------------------------")
print("---- RAÍZ DE UN NUMERO ------------")
print("-----------------------------------")

# input
x = input(" ingrese el valor de la raíz ")
x = int(x)
e = input(" ingrese el exponente ")
e = int(e)

# processing
z = x**(1/e)

# output
print(" el resultado de la raíz es " + str(z))
