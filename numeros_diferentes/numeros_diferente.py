""" Programa 7 
Verificar si dos numeros son diferentes """

print("-----------------------------------")
print("--------Numeros diferentes? -------")
print("-----------------------------------")

# input
x = int(input(" Digite el valor de x: "))
y = int(input(" Digite el valor de y: "))

# Processing
if x != y: 
    msj = " son diferentes "
    print(" son diferentes ")
else: 
    msj = " son iguales "


# output
print(" Los numeros " + msj)