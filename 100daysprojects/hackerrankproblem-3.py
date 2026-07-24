def mutate_string(string, position, character):

    #convertir el string a lista
    word_list = list(string)
    new_character = character
        #print(word_list)
    
    #tomar la posicion del string y cambiarla
    word_list[position] = new_character
    #print(word_list)

    #juntar la palabra de nuevo 
    word = "".join(word_list)
    
    return word

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)