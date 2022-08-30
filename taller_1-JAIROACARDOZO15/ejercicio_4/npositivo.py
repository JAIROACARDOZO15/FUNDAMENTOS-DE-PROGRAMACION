"""PROGRAMA PARA DETERMINAR LA SUMA DE N ENTEROS POSITIVOS"""

print("-----------------------------------")
print("---- N ENTEROS POSITIVOS ----------")
print("-----------------------------------")

# input
n=input("Digite el valor de las primeras cifras: ")
n= int(n)

# processing
s= n*(n+1)/2
s= int(s)

# output
print("La suma de las primeras " +str(n) + " cifras es " +str(s))