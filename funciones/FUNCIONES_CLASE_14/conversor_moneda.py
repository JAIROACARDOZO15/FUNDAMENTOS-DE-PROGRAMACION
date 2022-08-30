print("--------------------------------")
print("--CONVERSOR DE MONEDAS--")
print("--------------------------------")

# Funcion para hacer la conversacion
def convertir(tipo_pesos, vlaor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + " tienes? ")
    pesos = float(pesos)
    dolares = pesos / vlaor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares")

def funcion_principal():
    menu = """
    Bienvenidos al conversor de moneda
    1 - Pesos Colombianos
    2 - Pesos Argentinos
    3 - Pesos Mexicanos

    Elige la opción: """ 

    opcion = int(input(menu))
    if opcion == 1:
        convertir("Colombianos" , 3966)
    elif opcion == 2:
        convertir("Argentinos", 122.52)
    elif opcion == 3:
        convertir("Mexicanos", 20.62)
    else:
        print("Ingrese una ocpion correcta")

# Inicializar el programa
if __name__ == "__main__":
    funcion_principal()