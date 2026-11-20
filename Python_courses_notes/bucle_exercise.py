

def init():
    LIMIT = 100
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMIT:
        print(f" 2 elevado a la {contador} es igual a: {potencia_2}")
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    init()
