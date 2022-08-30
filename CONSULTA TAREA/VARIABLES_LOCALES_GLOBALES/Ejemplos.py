"Variables locales"
#En Python las variables locales son aquellas definidas dentro de una función. Solamente son accesibles desde la propia
#función y dejan de existir cuando esta termina su ejecución. Los parámetros de una función también son considerados 
#como variables locales.

#EJEMPLO
def saludar():
	saludo = '¡Hola!' #esta variable local pertenece al ámbito local de la función saludar
	print(saludo)


def sumar(sumando1, sumando2):
	#sumando1, sumando2 y suma son variables locales que corresponden al ámbito local de la función sumar
	suma = sumando1 + sumando2

	return suma


saludar()
print(sumar(4, 5))

#ERROR NAME
def saludar():
	saludo = '¡Hola!' 
	print(saludo)

saludar()
print(saludo)

"Variables globales"
#Las variables globales en Python son aquellas definidas en el cuerpo principal del programa fuera de cualquier función. 
#Son accesibles desde cualquier punto del programa, incluso desde dentro de funciones. También se puede acceder a las 
#variables globales de otros programas o módulos importados.

def saludar():
	print(saludo)


saludo = '¡Hola, Mundo!' #variable global definida en el cuerpo principal del programa
saludar()