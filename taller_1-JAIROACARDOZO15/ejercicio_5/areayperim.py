"""PROGRAMA PARA CALCULAR EL AREA Y EL PERIMETRO DE UN CIRCULO"""

print("--------------------------------------------")
print("---- AREA Y PERIMETRO DE UN CIRCULO --------")
print("--------------------------------------------")

# input
r = int(input(" Digite el valor del radio "))
pi = 3.1416

# processing
a = (pi * r**2)
p = (2*pi * r)

# output
print(" El area es " + str(a))
print(" el perimetro es " + str(p))
