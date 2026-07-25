#Clave esta en leer en un foor lopp las tres ultima letras de rango y comparar si son parecedias al sub string 


def count_substring(string, sub_string):
    # traer las string y sub string
    mayor_word_len = len(string)
    minor_word_len = len(sub_string)
        #print(mayor_word)
    # hacer un for loop en el que siempre me trago las 3 ultimas letras de la cadena de texto 
    conteo = 0
    for l in range(mayor_word_len - minor_word_len + 1):
        if string[l:l+minor_word_len] == sub_string:
            conteo += 1

    # regresar el conteo
    
    return conteo

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)