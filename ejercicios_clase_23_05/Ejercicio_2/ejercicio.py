""""EJERCICIO N° 2"""

# INPUT

n = 1980
a = 3.5
b = 5

#PROCESSING

while(a < b):
    n = n + 1
    a = a + 0.07 * a 
    b = b + 0.05 * b
    print(" En el año " + str(round(n ,1 )) + " la ciudad A es mayor que " + str(n) + " la ciudad B ")
# OUTPUT
print("En el año " + str(n) + " la poblacion de la ciudad A es mayor que de la ciudad B.")