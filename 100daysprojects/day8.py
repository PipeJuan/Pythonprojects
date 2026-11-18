
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

greet_w_2parameters(name,location) 


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




calculate_love_score("Felipe","Angela")"""


#Caeser Cipher 

# Design a econder and decoder mesaages

#1 Pensemos en la logica de construcción 
#2 funcionamiento de la logica 
#3 Herramientas que necesiot para que funciones 
#4 test para ver si funciona 


import string



def init():

    def decrypt():
        pass


    def encrypt(word,shift):

        alphabet = list(string.ascii_lowercase)
        encoder_word = []

        for l in word: 
            initial_position = alphabet.index(l)
            final_position = initial_position + shift
            encoder_word.append(alphabet[final_position])

        word_encoder = "".join(encoder_word)
        
        #print(word_encoder)

        return word_encoder
            
        
    active = True
    decision = ""
    word = ""
    shift = 0
    word_encoder = ""
    decoder_word = ""
    
    while active != False:
        

        decision = input("What do you want to do Encrypt a phrase, Decrypt a phrase or logout the tool. n/ E for Encrypt, D for Decrypt & L for logout : ").upper()
        #print(decision)

        if decision == "L":

            print("See you next time")
            active = False

        elif decision == "D":

            if word == "":
                print("There is no word for Decrypt!")
            else:
                decrypt(word)

        elif decision == "E":

            if word == "":
                word = input("What phrase do you wnat to encrypt?: ")
                shift = int(input("How many shift your phrase will be encrypted?: "))
                word_encoder = encrypt(word,shift)
                print(f"Your encoder phrase is {word_encoder}")
                
            else:
                print("You have a message to decrypt first, decrypte it and then encryp a new message")

        else:
            print("You chosee an invalid option, rembember E for Encrypt, D for Decrypt & L for logout")


if __name__ == '__main__':
    init()