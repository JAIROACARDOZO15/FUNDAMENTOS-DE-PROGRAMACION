""""EJERCICIO N° 1"""

# INPUT

h = int(input("Digite la altura de h : "))
q = h / 5
n = 0

#PROCESSING

while(h > q):
    h = h - (0.1 * h) 
    n = n + 1
    print(" La altura " + str(round(h ,1 )) + " se alcanza el rebote " + str(n))
# OUTPUT
print("El rebote # " + str(n) + " no alcanza a subir la quinta parte de la altura inicial ")