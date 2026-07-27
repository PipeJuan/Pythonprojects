if __name__ == '__main__':
    s = input()
print(s)
#Validar que es alphanumeric 
print(any(l.isalnum() for l in s))
#validar que es characters aplha
print(any(l.isalpha() for l in s))
#validar que es digit
print(any(l.isdigit() for l in s))
#validar que es lowercase
print(any(l.islower() for l in s))
#validar que es uppercase
print(any(l.isupper() for l in s))