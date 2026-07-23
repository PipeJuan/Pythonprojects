if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()



#Desde aca hice el codigo

#meter en una variable el listado de notas
    grades = student_marks[query_name]
# recorrer la lista y sumas cada valor 
    sum_of_grade = 0
    for grade in grades:
        sum_of_grade = sum_of_grade + grade
# y dividirlo entre el numero de notas y imprimer el resultado con dos decimales 
    percentage = sum_of_grade / len(grades)
    print(f"{percentage:.2f}")