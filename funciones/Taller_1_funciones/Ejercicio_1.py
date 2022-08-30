"""Ejercicio N° 1"""
#Construir una funcion que reciba su nombre como parametro y que lo muestre 5 veces en la pantalla.

print("---------------------------------------")
print("------- MOSTRAR NOMBRE 5 VECES  -------")
print("---------------------------------------")

#DEFINICION DE LA FUNCION
def mostrar_nombre(nombre):
    for i in range(5):
        print(nombre)

#ENTRADA
nombre = input("Digite nombre: ")#se recibe el dato del usuario
mostrar_nombre(nombre)
