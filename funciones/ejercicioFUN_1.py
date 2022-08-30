#SIN FUNCIONES

print("---------------------------------------")
print("---- BUSCAR UN NUMERO EN CONJUNTO -----")
print("---------------------------------------")

# ENTRADA
b = int(input("Numero o buscar: ")) #se recibe el dato del usuario

# PROCESSING
a = [1,2,3,4,5] #Se almacena una lista de datos
r = False #se inicia la variable r con un valor FALSO

for i in a:
    if i==b:
        print("Lo encontre: ")
        r = True
if r==False:
    print("No lo encontre: ")

# SALIDA
print("\n Eso era ...........")