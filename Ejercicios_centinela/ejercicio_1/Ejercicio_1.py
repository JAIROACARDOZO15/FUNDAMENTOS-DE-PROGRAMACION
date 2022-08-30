print("----------------------------------------")
print("------------Caso 1 Centinela------------")
print("------------NOTAS ESTUDIANTES-----------")
print("----------------------------------------")

# ENTRADA
cod = int(input("Digite el codigo del estudiante: "))
nombre = input(	"Digite el nombre del estudiante: ")
if cod != 0:
    nota1 = float(input("Digite la nota del parcial N° 1: "))
    nota2 = float(input("Digite la nota del parical N° 2: "))
    nota3 = float(input("Digite la nota del parcial N° 3 : "))
else: 
    print("Fin de los datos de entrada")

# PROCESAMIENTO
reprobados = 0
while cod != 0:
    nota_final = (nota1 + nota2 + nota3)/3
    print("El estudiante de codigo " + str(cod) + ", cuyo nombre es " + nombre + ", obtuvo una nota definitiva de " 
    + str(nota_final))  
    if nota_final < 3:
        reprobados = reprobados + 1
# ENTRADA
    cod = int(input("Digite el codigo del estudiante: "))
    nombre = input("Digite el nombre del estudiante: ")
    if cod != 0:
        nota1 = float(input("Digite la nota del parcial N° 1: "))
        nota2 = float(input("Digite la nota del parical N° 2: "))
        nota3 = float(input("Digite la nota del parcial N° 3 : "))
    else:
        print("Fin de los datos de entrada")
# SALIDA
print(" Cantidad de estudiantes que reprobaron la materia: " + str(reprobados))