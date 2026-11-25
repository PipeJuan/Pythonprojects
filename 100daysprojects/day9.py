
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

#1 Pensemos en la logica de encendido y apagado del programa - Check
#2 funcionamiento de recolección y guardado de datos y borrado o limpieza de la pantalla al poner un bid - check 
#3 funcion que nos ayudará a decidir el mejor apostador
#4 test para ver si funciona 


def init():
    
    def best_bidder(bids):
        pass
    
    
    more_bids = True
    name = ""
    person_bid = 0
    bids = {}

    while more_bids != False:
        
        print("Welcome to secret auction program.")
        #Recolección de la data 

        name = str(input("What is your name: \n"))
        person_bid = int(input("What is your bid $: \n"))

        bids[name] = person_bid


        # Control para seguir el programa o finalizar el programa 
        additional_bids = input("Are there any other bidders: Type 'yes' or 'no'.\n")

        if additional_bids == "yes":
            print("\n"* 100)
            more_bids = True
        else:
            # ejecuta la función decisiora del mejor bid 
            
            more_bids = False
            print(bids)
            print("Programa termina")



if __name__ == '__main__':
    init()