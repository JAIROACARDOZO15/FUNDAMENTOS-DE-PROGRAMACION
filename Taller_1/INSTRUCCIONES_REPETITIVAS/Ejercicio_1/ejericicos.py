""" Ejercicio N° 1 """

# INPUT
c1 = int(input(" Ingrese el valor del capital: $ "))
c2 = int(input(" Ingrese el valor del capital: $ "))
c3 = int(input(" Ingrese el valor del capital: $ "))
n = 0
# PROCESSING
while((c1 + c2) < c3):
    c1 = c1 + (c1 * 0.3)
    c2 = c2 + (c2 * 0.4)
    n = n + 1
    
# OUTPUT
print(" Los meses necesarios son " + str(n))