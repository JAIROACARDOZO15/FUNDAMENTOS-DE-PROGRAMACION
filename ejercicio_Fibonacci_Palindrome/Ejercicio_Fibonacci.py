def serie_fibonacci(terminos):
    resultado = []
    primero = 1
    resultado.append(str(primero))
    segundo = 1
    resultado.append(str(segundo))

    for numero in range(terminos - 2):
        total = primero + segundo
        segundo = primero
        primero = total
        resultado.append(str(total))
    return resultado

numero = int(input("ingrese el numero de terminos: "))