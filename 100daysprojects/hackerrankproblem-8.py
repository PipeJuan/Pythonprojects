#Door Mat Problem 
    #Tratando de hacer la mitad del carpet 
    # N es el alto del tapete
    # M es el largo del tapete y es 3 veces N
    # el patron a inprimir es .|. y este se incrementa por dos en cada linea 


N, M = map(int, input().split())
pattern = ".|."
message = "WELCOME"

mat_midle_size = int((N - 1) / 2)
#top part
for times in range (1,N,2):
     print((pattern * times).center(M,'-'))

#CENTER       
print(message.center(M,'-'))    

#bottom part
for times in reversed(range (1,N,2)):
     print((pattern * times).center(M,'-'))    

