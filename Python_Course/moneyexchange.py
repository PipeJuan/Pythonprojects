def conversor(tipo_dato, valor_dolar):
    pesos = int(input("Cuantos pesos " + tipo_dato + " tienes ?"))
    pesos = float(pesos)
    dolares = (pesos / valor_dolar)
    dolares =round(dolares, 2)
    dolares = str(dolares)
    print("Tienes en total $ " + dolares + " dolares")

Menu = """""
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos chilenos

Elige una opcion: 
"""
pais = int(input(Menu))

#definicion de conversion

if pais == 1:
    conversor("Colombianos",3840)
elif pais == 2:
    conversor("Argentinos",60)
elif pais == 3:
    conversor("Chilenos",24)
else:
    print("El valor ingresado no corresponde a un pais del menu")





