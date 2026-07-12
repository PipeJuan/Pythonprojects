

# Clase 1 basicos de diccionarios 
contacto = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "email": "juan@ejemplo.com"
}


username = contacto["nombre"]
edad = contacto["edad"]

print(f"El usuario {username} tiene {edad} años")


#clase 2 - diccionarios 

config = {"tema": "claro", "notificaciones": True}

config["tema"] = "oscuro" 
config["volumen"] = 80


#clase 3 funcion .items

calificaciones = {
    "Ana": 85,
    "Beto": 70,
    "Carla": 95,
    "David": 60
}

for nombre,score in calificaciones.items():
    if score >= 70:
        print(f"¡Bien hecho, {nombre}! Pasaste con {score}")
    else:
        print(f"Lo siento, {nombre}. Necesitas estudiar más, tienes {score}")


# clase de funciones ejemplo de funciones

def es_mayor_de_edad(edad):
    mensaje = "Tu edad es:"
    if edad >= 18:
        mensaje = "Es mayor de edad"
    else:
        mensaje = "Es menor de edad"
    return mensaje

edad = 20
resultado = es_mayor_de_edad(edad)
print(resultado)



# ejemplo 2 con dos variables y try error 

def saludar_usuario(nombre,edad):
    if edad >= 18:
        return f"Hola {nombre}, eres mayor de edad"
    else:
        return f"Hola {nombre}, eres menor de edad"


nombre = input("¿Cual es tu nombre?")

try: 
    edad = int(input("¿Cual es tu edad?"))
    mensaje = saludar_usuario(nombre,edad)
    print(mensaje)
except ValueError:
    print("¡Ey! Eso no es un número válido.")

