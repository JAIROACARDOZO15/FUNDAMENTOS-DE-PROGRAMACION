"""EJERCICIO N° 2"""
#Construir una funcion que reciba una cadena digitada (como parametro) por el usuario y que lo muestre n veces en la pantalla. El valor de n tambien es digitado por el ususario.

print("---------------------------------------")
print("-------- CADENA DE PARAMETROS ---------")
print("----------- MOSTRADO N VECES ----------")
print("---------------------------------------")


#DEFINICION DE LA FUNCION
def mostrar_nombre(nombre, veces):
    for i in range(veces):
        print(nombre)

#ENTRADA
nombre = input("Digite nombre: ")#se recibe el dato del usuario
veces = int(input("Digite el numero de veces: "))
mostrar_nombre(nombre , veces)