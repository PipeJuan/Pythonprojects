def run(name):
    for letra in name:
        print(letra)


if __name__ == "__main__":
    name = input("Por favor dame tu nombre: ")
    run(name)




#Otra forma de usar la funcion

def run():
    name = input("Por favor dame tu nombre:")
    for letra in name:
        print(letra)


if __name__ == "__main__":
   run()