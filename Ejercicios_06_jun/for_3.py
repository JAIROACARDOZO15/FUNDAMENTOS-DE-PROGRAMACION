"Generar la siguiente serie 1,4,9,16,25,36 ....... n"
n = int(input("Digite el valor de n: "))
s = "series: "
for i in range(1, n+1):
    t= i*i
    ### t = i**2
    if i < n:
        s = s + str(t) + " , "
    else:
        s = s + str(t)

print("---------RESULTADO-------------")
print(s)