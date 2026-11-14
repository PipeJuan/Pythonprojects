
"""
# Simple function
def greet():
    print("Hello world")

#greet()


def greet_w_name(name):
    print(f"Hello {name}")
    print(f"How are you ? {name}")

name = str(input("What is your name: "))
greet_w_name(name)




#Con una parametro 
def life_in_weeks(years):
    total_weeks = 52 * 90
    actual_weeks = int(years * 52)
    time_left = total_weeks - actual_weeks
    print(f"You have {time_left} weeks left.")


years = int(input("How old are you in years?"))

life_in_weeks(years)


# con dos parametros

def greet_w_2parameters(name,location):
    print(f"Hello {name}")
    print(f"What is like in {location}")

name = "Angela"
location = "Soplaviento"

greet_w_2parameters(name,location) """


# Dos parametros y for loop

def calculate_love_score(name1,name2):
    name_together = name1 + name2
    comparision1 = "true"
    comparision2 = "love"
    first_digit = 0
    second_digit = 0
    
    for l in comparision1:
        ocurrence = name_together.count(l)
        first_digit += ocurrence

    for l in comparision2:
        ocurrence = name_together.count(l)
        second_digit += ocurrence
    
    print(f"{first_digit}{second_digit}")




calculate_love_score("Felipe","Angela")