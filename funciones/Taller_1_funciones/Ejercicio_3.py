"""EJERCICIO N° 3"""
#Construir una funcion que reciba como parametro una lista de datos numericos y retome la suma de dichos datos.

print("---------------------------------------")
print("-------- DATOS NUMERICOS Y  -----------")
print("------RETOME LA SUMA DE DATOS ---------")
print("---------------------------------------")


#DEFINICION DE LA FUNCION
def suma(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

lista = int(input("Ingrese dato"))
lista = [1,2,3,4,5,6]
print("La suma es " + str(suma(lista)))