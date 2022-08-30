#Sintaxis de una función Lambda
#lambda argumentos: expresión
#Las funciones Lambda pueden tener cualquier número de argumentos, pero solo una expresión.

"""Funcion lamdba para calcular el cuadrado de un numero"""
square = lambda x: x ** 2
print(square(3)) # EL RESULTADO ES 9

#En el ejemplo de lambda anterior, lambda x: x ** 2 produce un objeto de función anónimo que se puede asociar con cualquier nombre. Entonces, asociamos el objeto de función con square. De ahora en adelante, podemos llamar al objeto square como cualquier función tradicional, por ejemplo, square(10)

"""Ejemplos de funciones Lamdba"""
lambda_func = lambda x: x**2
lambda_func(3) # EL RESULTADO RETORNA A 9


lambda_func = lambda x: True if x**2 >10 else False
lambda_func(3) #RETORNA FALSE
lambda_func(4) #RETORNA TRUE