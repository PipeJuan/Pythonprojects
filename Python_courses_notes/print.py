def imprimir():

    n = int(input())
    nums = ""

    for i in range(1, n + 1):
        nums = nums + str(i)

    print(nums)


if __name__ == '__main__':
    imprimir()