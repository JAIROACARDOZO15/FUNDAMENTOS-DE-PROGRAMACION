"Generar la siguiente serie 3,8,13,18,23,28 ....... n"
n = int(input("Digite el valor de n: "))
s = "series: "
for i in range(1, n+1):
    t = i*5-1-1
    if i < n:
        s = s + str(t) + " , "
    else:
        s = s + str(t)

print("---------RESULTADO-------------")
print(s)