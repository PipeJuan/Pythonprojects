
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

    lowest_grade = python_students[0][1]
    second_lowest_grade = 0
    #for i in python_students:
        #if i[1] > lowest_grade:
            #second_lowest_grade = i

    print(python_students)
    print(lowest_grade)
    print(second_lowest_grade)