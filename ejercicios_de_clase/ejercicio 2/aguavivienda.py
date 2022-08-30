"""Ejercicio No.2
calcular el gasto de agua de una vivienda, basando el gasto de m3, siendo el sistema de cobro el siguente"""

metros_gastados = int(input("Ingrese la cantidad de metros cuadrados gastados: "))
cuota_fija = 10000

if metros_gastados <=50:
    print(" Su valor a pagar es " + "$" + str(cuota_fija))
elif metros_gastados >50 and metros_gastados <=200:
    print(" Su valor a pagar es " + "$" + str(cuota_fija + (metros_gastados - 50) * 2000))
elif metros_gastados >200:
    print(" Su valor a pagar es " + "$" + str(cuota_fija + (metros_gastados - 50) * 3000))
else:
    print(" Porfavor verifique la informacion ingresada ") 