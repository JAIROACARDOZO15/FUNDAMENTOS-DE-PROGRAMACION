def es_palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = str(input("ingrese una palabra: "))

if es_palindromo(palabra) == True:
    print("Si es palindromo")
else:
    print("No es palindromo")