" Ejercicio N° 2 "
m = int(input("Digite el valod de m: "))
n = int(input("Digite el valor de n: "))
m_siete = 0
m_nueve = 0

for n in range(m, (n+ 1), 1):
    if (n % 7) == 0:
        m_siete += 1
    elif (n % 9) == 0:
        m_nueve += 1

print(f" Entre {m} y {n} hay : ")
print("Hay " + str(m_siete) + " numeros multiplos de siete " + " y " + str(m_nueve) + " numeros multiplos de nueve ")