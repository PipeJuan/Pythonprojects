#Ejercicios de practica de Hacker Ranks


def is_leap(year):
    leap = False
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):   
        leap = True
    return leap

#Evalua solo las condiciones en que verdadero, es decir para que sea leap year, 
# debe ser divisible entre 4, no ser divisible entre 100 y ser divisible entre 400.


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))


# Se usa conversion de datos, funciones con parametros y condicionales



#List Challenge 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    runner = arr[n-1]   
    runner_up = 0
    for i in arr:
        if i < runner:
            runner_up = i
    print(runner_up)



# NESTED LIST CHALLENGE 



if __name__ == '__main__':

    python_students = []

    for _ in range(int(input())): #N
        name = input()
        score = float(input())
        student = [name,score]
        python_students.append(student)

    python_students.sort(key=lambda x:x[1]) #como organizar una nested lisy teniendo en cuenta el index



    second_lowest_grade = python_students[1][1]
    names = []

    for i in python_students:
        if i[1] == second_lowest_grade:
            names.append(i[1])

    names.sort()
    for i in names:
        print(i)


    #print(python_students)
    #print(second_lowest_grade)
    #print(names)



