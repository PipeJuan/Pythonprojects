#Door Mat Problem 
    #Tratando de hacer la mitad del carpet 
    # N es el alto del tapete
    # M es el largo del tapete y es 3 veces N
    # el patron a inprimir es .|. y este se incrementa por dos en cada linea 

pattern = ".|."
message = "WELCOME"
N = 7
M = 21
mat_midle_size = int((N - 1) / 2)
for times in range (mat_midle_size):
     print(pattern.center(M,'-'))   
print(message.center(M,'-'))      
for times in range (mat_midle_size):
     print(pattern.center(M,'-'))      

