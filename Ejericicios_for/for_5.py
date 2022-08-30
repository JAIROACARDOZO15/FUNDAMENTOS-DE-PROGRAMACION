# Digite su nombre y le cuente cuantas vocales tiene su nombre 
n = input("Digte su nombre: ")
a1 = 0
e1 = 0
i1 = 0
o1 = 0
u1 = 0
for vocal in n:
    if vocal == "a":
        a1 += 1
    elif vocal == "e":
        e1 += 1
    elif vocal == "i":
        i1 += 1
    elif vocal == "o":
        o1 += 1
    elif vocal == "u":
        u1 += 1

print(" La vocal a " + str(a1) + " se repite ")
print(" La vocal e " + str(e1) + " se repite ")
print(" La vocal i " + str(i1) + " se repite ")
print(" La vocal o " + str(o1) + " se repite ")
print(" La vocal u " + str(u1) + " se repite ")