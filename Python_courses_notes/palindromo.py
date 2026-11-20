def palindromo(palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def init():
    palabra = input("Escribe una palabra: ")
    es_palindormo = palindromo(palabra)
    if es_palindormo == True:
        print("Es Palindromo")
    else:
        print("No es Palindromo")


#Punto de entrada del programa
if __name__ == "__main__":
    init()
