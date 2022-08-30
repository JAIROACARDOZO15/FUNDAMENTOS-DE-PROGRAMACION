"EJERCICIO N° 1"
# Realice un programa que implemente el juego de los números donde el usuario va a 
# escoger un número entero generado de manera aleatoria.

import random

bien = False
intentos = 0
nombre = input("Hola, ¿cómo te llamas? ")
n = random.randint(1, 20)

while bien == False:
    intentos += 1
    intento = int(input("Muy bien " + nombre + ", adivina el número entre 1 y 20: "))
    if intento == n:
        print(
            "Buen trabajo " + nombre + ", acertaste en " + str(intentos) + " intentos.")
        bien = True
    if intento > n:
        print("Tú número es muy alto. Dame otro número")
    elif intento < n:
        print("Tú número es muy bajo. Dame otro número")
