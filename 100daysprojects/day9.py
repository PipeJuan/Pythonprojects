
#Practice how to manipulate and use values from dictionaries. 
"""
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


student_grades = {}

for key in student_scores:
    #print(student_scores[key])
    if student_scores[key] <= 70:
        student_grades[key] = "Fail"
    elif student_scores[key] > 70 and student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] > 80 and student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 90 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    else:
        pass
print(student_grades)

"""

# Secret actuion program
"""Programa que permite escoger la apuesta mas grande entre usuarios, sin que los usuario
   anteriores sepan cual fue la apuesta de sus competidores, usando dictionarios.
"""

#1 Pensemos en la logica de encendido y apagado del programa
#2 funcionamiento de recolección y guardado de datos y borrado o limpieza de la pantalla al poner un bid
#3 funcion que nos ayudará a decidir el mejor apostador
#4 test para ver si funciona 