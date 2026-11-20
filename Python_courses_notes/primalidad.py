def es_primo(num):
    contador = 0
    for i in range (1, num + 1):
        if i == 1 or i == num:
            continue
        elif num % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
        

def run():
    num = int(input("Por favor, escribe tu numero: "))
    if es_primo(num):
         print(f"El numero {num} es primo")
    else:
        print(f"El numero {num} no es primo")



if __name__ == "__main__":
    run()
