"Generar la siguiente serie 2,4,6,8,10,12 ......... n"

n = int(input("Digite el valor de n: "))
s = "series: "
for i in range(1, n+1):
    t= 2*i
    if i < n:
        s = s + str(t) + " , "
    else:
        s = s + str(t)

print("---------RESULTADO-------------")
print(s)