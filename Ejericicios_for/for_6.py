import random

cara_1 = 0
cara_2 = 0
cara_3 = 0
cara_4 = 0
cara_5 = 0
cara_6 = 0
rta = "Lanzamientos = ("

n = int(input("DIigte el valor: "))
for i in range(n):
    dado = random.randint(1,6)
    if dado == 1:
        cara_1 += 1
    elif dado == 2:
        cara_2 += 1
    elif dado == 3:
        cara_3 += 1
    elif dado == 4:
        cara_4 += 1
    elif dado == 5:
        cara_5 += 1
    elif dado == 6:
        cara_6 += 1
    else:
        print("Cara no valida ")
    
    if i < n-1:
        rta = rta + str(dado) + " , "
    else: 
        rta = rta + str(dado)
rta = rta + ")\ncara 1 :"

for i in range(cara_1):
    rta = rta + "#"
rta = rta + " -> " + str(cara_1)

print("-----RESULTADOS-----")
print(rta)