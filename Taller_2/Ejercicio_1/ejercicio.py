"""Ejercicio No.1 
Programa para calcular el valor de una llamada telefonica"""

print("--------------------------------")
print("-----El valor de la llamda es --")
print("--------------------------------")

# Input
x = int(input("Cuantos minutos se ultilizaron en la llamada: "))

# Processing
if x <= 3:
    print("La llamada tiene un costo de $ 300 ")

elif x > 3:
    a = (((x * 50) + 150 ))
    print(" La llamada tiene un costo de: $ " + str(a))