def swap_case(s):
    #La palabra que es dada hay que convertiarla a una lista 
    word_list = []
    for letter in s:
        word_list.append(letter)
        #print(word_list)

    # recorrer la lista con cada carater y revisar condicionalmente si es mayusculas, convertira la minusculas y viceverca
    final_word = []
    for x in word_list:
        letter_to_evaluated = x
        if letter_to_evaluated.isupper():
            new_letter = letter_to_evaluated.lower()
            final_word.append(new_letter)
        else:
            new_letter = letter_to_evaluated.upper()
            final_word.append(new_letter)
    #print(final_word)
    #luego unir toda la palabra y regresarlo
    s_final_word = "".join(final_word)
    #print(s_final_word)
    return s_final_word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


