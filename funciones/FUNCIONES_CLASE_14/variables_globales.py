"""Se omite el parámetro x en el llamado de la función ya que la varioable es global"""

def f():
    global x
    print("Valor de x dentro de f(x) = " , x)
    return x

# Algoritmo principal
x = 3
print("Valor inicial de x = " , x)
z = f()
print("Valor de x despues de llamar a f(x) = ", x)

"""
SALIDA:
valor inicial de x = 3
Valor de x dentro de f(x) = 4
Valor de x despues de llamar a f(x) = 4"""