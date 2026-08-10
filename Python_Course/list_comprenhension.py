import random
# Definición de listas de forma mas breve

#Forma normal 

my_list = []


for element in range(1,11):
    my_list.append(element * 2)

print(my_list)

# En forma de list comprenhension 


my_list_2 = [element * 2 for element in range(1,11)] #Por cada elemento del iterable, multiplica por 2 el elemento y lovamos agregar un elemento a lalista 

print(my_list_2)



# Tambien podemos agregarles condiciones al iterable de forma que 
#Verifica si se puede agregar el elemento o no 

odd = [i *2  for i in range(1,11) if i % 2 == 0] # Acción que vas hacer, teniendo en cuenta los elemento y el rango y esta condición
print(odd)


# Se puede aplicar par dictionaries - Dictionaries comprehension

#Versión larga 

My_dict = {}

for i in range(1,5):
    My_dict[i] = i * 2

print(My_dict)


# Versión con list comprehenssion 

My_dictionary = {i: i *2 for i in range(1,5)}
print(My_dictionary)



# Generar el diccionario a partir de una lista predeterminada

countries = ["COL", "PE", "BR"]

population = {}

for country in countries:
    population[country] = random.randint(1,100)

print(population)


# Con list comprehenssion 

countries = ["COL", "PE", "BR"]

population_2 = {country: random.randint(1,100) for country in countries} #country es el elemento inventado o element de la lista cpuntries(rango)

print(population_2)

# Interacción con dos listas 

names = ["Nico", "Santi", "Gero"]
ages = [9, 8, 7]

ages_names = {name : age for (name, age) in zip(names, ages)} #Zip ayuda a unior dos lista 

print(ages_names)


# Dictonoary comprehension con condionales

countries = ["COL", "PE", "BR"]

population_2 = {country: random.randint(1,100) for country in countries}

result = {country: population for (country, population)
           in population_2.items() if population > 5}

print(population_2)

# Dictonary de una cadena de texto 

text = "Hola, soy Felipe"

unique = {c: c.upper() for c in text if c in "aeiou"}

print(unique)


