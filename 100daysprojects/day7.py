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
    

    # Fixed Variables
    game_over = False
    correct_letter = []
    life = 6

    # Aks for the user a word
    while not game_over : 
        guess = input("Guess a letter for the word:").lower()

        if guess in chosen_word:
            pass
        else:
            life -= 1
            print(f"You lose a live! You have now {life}")

    #Verify is the letter user guessed is in the word select before
        display = ""
        for l in chosen_word:
            if l == guess:
                display += l
                correct_letter.append(l)
            elif l in correct_letter:
                display += l
            else:
                display += "_"

        if life > 0:
            pass
            print(display)
        else:
            game_over = True
            print("You lose the game!")

        if "_" not in display:
            game_over = True
            print("You win!")


if __name__ == '__main__':
    init()