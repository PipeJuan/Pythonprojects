from itertools import permutations


if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    

lista_completa = [x, y, z]

permutaciones = list(permutations(lista_completa))

print(permutaciones)