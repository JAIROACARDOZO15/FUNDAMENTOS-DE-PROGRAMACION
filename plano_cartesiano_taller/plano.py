""" EJERCICIO 5 CREAR UN PROGRAMA PARA CALCULAR EL CUADRANTE DE UN PUNTO EN UN PLANO CARTESIANO """

print("---------------------------------------------------")
print("---PUNTOS EN EL CUADRANTE DEL PLANO----------------")
print("---------------------------------------------------")

x = int(input(" Ingrese la coordenada x: "))
y = int(input(" Ingrese la coordenada en y: "))

if x > 0 and y > 0:
    w = " El punto se encuentra en el cuadrante I"
    print(w)
elif x < 0 and y > 0:
    w = " El punto se encuentra en el cuadrante II"
    print(w)    
elif x < 0 and y < 0:
    w = " El punto se encuentra en el cuadrante III"
    print(w)
elif x > 0 and y < 0:
    w = " El punto se encuentra en el cuadrante IV"
    print(w)
elif x > 0 or x < 0 and y == 0:
    w = " El punto se encuentra en el eje X"
    print(w)
elif x == 0 and y > 0 or y < 0:
    w = " El punto se encuentra en el cuadrante Y"
    print(w)
elif x == 0 and y == 0:
    w = " El punto se encuentra en el origen del plano"
    print(w)
else:
    w = "Por favor ingrese las coordenadas precisas"
    print(w)