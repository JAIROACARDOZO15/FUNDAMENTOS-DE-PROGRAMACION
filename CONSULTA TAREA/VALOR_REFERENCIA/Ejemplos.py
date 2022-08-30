"Ejemplo de paso por valor"
def doblar_valor(numero):
    numero *= 2

n = 10
doblar_valor(n)
print(n)

"Ejemplo de paso por referencia"
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns)
print(ns)

"Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:"
def doblar_valor(numero):
    return numero * 2

n = 10
n = doblar_valor(n)
print(n)

"Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:"
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2

ns = [10,50,100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns)