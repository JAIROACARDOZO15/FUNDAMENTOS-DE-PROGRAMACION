# CON FUNCIONES

print("---------------------------------------")
print("---- BUSCAR UN NUMERO EN CONJUNTO -----")
print("---------------------------------------")

#DEFINICION DE LA FUNCION
def buscardatoEnlista(datoABuscar, lista):
    r = False
    for i in lista: 
        if i == datoABuscar:
            r = True
    return r

#ENTRADA
dato = int(input("Numero o buscar: "))#se recibe el dato del usuario

# PROCESSING
lista = [1,2,3,4,5] #Se almacena una lista de datos
if buscardatoEnlista(dato, lista):
    print("Lo encontre")
else: 
    print("No lo encontre")

# SALIDA
print("\n Eso era ...........")