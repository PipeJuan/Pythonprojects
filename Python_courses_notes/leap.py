def is_leap(year):
    leap = False
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):   
        leap = True
    return leap
#Evalua solo las condiciones en que verdadero, es decir para que sea leap year, 
# debe ser divisible entre 4, no ser divisible entre 100 y ser divisible entre 400.


if __name__ == "__main__":
    year = int(input())
    print(is_leap(year))