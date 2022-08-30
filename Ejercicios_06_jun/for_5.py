"Generar la siguiente serie 1,1/2,1/3,1/4,1/5,1/6 ....... n"
n = int(input("Digite el valor de n: "))
s = "series: "
for i in range(1, n+1):
    t= i
    if i < n:
        s = s + "1/"+ str(t) + " , "
    else:
        s = s +"1/" + str(t)

print("---------RESULTADO-------------")
print(s)