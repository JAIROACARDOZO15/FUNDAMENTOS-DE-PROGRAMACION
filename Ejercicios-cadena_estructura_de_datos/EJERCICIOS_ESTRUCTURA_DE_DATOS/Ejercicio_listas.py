"Ejericio N° 1"
#Calcule la longitud(cantidad de elementos) de la lista a
#Obtener el maximo de la lista b
#El minimo de la lista b
#Añadir el elemento -2015 en la lista a e imprimir la lista a
#Unir la lista a con la lista c
#Insertar 47 en la posicion 2 de la lista b
#Regresar y borrar el ultimo de la lista b

a =["Pedro" , 555 , "Python" , "Intel" , "HP"]
b =[45 , -67.8 , 999.99 , -2702.0 , 1858]
c =["Mouse" , "Teclado"]

print(len(a))
print(max(b))
print(min(b))
a.append(-2015)
print(a) #
a.extend(c)
print(a)  #
b.insert(2, 47)
print(b)  #
b.pop()
print(b)  #
b.pop(3)
b.sort()
print(b)


#