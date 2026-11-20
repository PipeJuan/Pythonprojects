#recorriendo listas que contienen diccionarios

tienda = [
    {"producto": "Leche", "precio": 25, "stock": 10},
    {"producto": "Pan", "precio": 15, "stock": 5},
    {"producto": "Huevo", "precio": 50, "stock": 2}
]

# El ciclo recorre cada diccionario de la lista
for item in tienda:
    if item["stock"] < 5:
        print(f"¡Alerta! Hay que surtir más {item["producto"]} (quedan {item["stock"]}).")
    else:
        print("Estamos bien de stock")





# 'w' abre el archivo para escribir
with open("mi_info.txt", "w") as archivo:
    archivo.write("Hola mi nombre es Felipe")
    print("Se creó el archivo")