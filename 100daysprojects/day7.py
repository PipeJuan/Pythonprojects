import random

def init():

    # From a list choose a random word
    words_list = ['felipe','meillys','salomon','carmen']
    chosen_word = random.choice(words_list)


    place_holder = ""
    word_length = len(chosen_word)

    for position in range(word_length):
        place_holder += "_"

    print(chosen_word)
    print(place_holder)
    

    # Aks for the user a word
    pre_guess = input("Guess a letter for the word:")
    guess = pre_guess.lower()


    #Verify is the letter user guessed is in the word select before

    display = ""

    for l in chosen_word:
        if l == guess:
            display += l
        else:
            display += "_"

    print(display)

    


if __name__ == '__main__':
    init()