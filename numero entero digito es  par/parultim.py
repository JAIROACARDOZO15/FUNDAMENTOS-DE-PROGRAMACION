""" Programa para saber si el ultimo digito de un numero entero es par """

print("----------------------------------------")
print("----------Ultimo digito es par----------")
print("----------------------------------------")

x = int(input(" Ingrese el valor de x: "))
a = (x % 10)

if (a % 2) == 0: 
    z = "El numero es par"
    print(z)
else: 
    z = "El numero es impar"
    print(z)