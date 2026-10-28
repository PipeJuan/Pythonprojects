import random

def init():

    # From a list choose a random word
    words_list = ['Felipe','Meillys','Salomon','Carmen']
    chosen_word = random.choice(words_list)
    #print(chosen_word)

    letters = list(chosen_word)
    guessed_blanks = []
    for l in letters: 
        guessed_blanks.append("_")

    guessed_blanks = ",".join(guessed_blanks)
    
    print(guessed_blanks)

    # Aks for the user a word
    pre_guess = input("Guess a letter for the word:")
    guess = pre_guess.lower()
    #print(guess)

    #Verify is the letter user guessed is in the word select before

    list_chose_word = list(chosen_word)

    for l in list_chose_word:
        if l == guess:
            print("Right")
        else:
            print("Wrong")


    # Step 1 finalizado 

#Ask 2 

    


if __name__ == '__main__':
    init()