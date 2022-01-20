#ASÍ FUE COMO YO LO HICE ANTES

# def conversor(mensaje):
#     pesos = input(mensaje)
#     pesos = float(pesos)
#     dolares = pesos/valor_dolar
#     dolares = round(dolares, 2)
#     dolares =str(dolares)
#     print("Tienes $" + dolares + " dólares")

# opcion = int(input(menu))
# if opcion == 1:
#     valor_dolar = 3643.2
#     conversor("¿Cuántos pesos colombianos tienes?: ")
# elif opcion	== 2:
#     valor_dolar = 94.79
#     conversor("¿Cuántos pesos argentinos tienes?: ")
# elif opcion == 3:
#     valor_dolar = 19.96
#     conversor("¿Cuántos pesos mexicanos tienes?: ")
# else:
#     print("ingresa una opción válida")

#ASÍ ES COMO SE HACE CON NUEVAS FNS

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares =str(dolares)
    print("Tienes $" + dolares + " dólares")

menu = """
Bienvenido al conversor de monedas 😊

1 - Pesos colombianos
2 - Pesos argentinos 
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    conversor("colombianos", 3643.2)
elif opcion	== 2:
    conversor("argentinos", 94.79)
elif opcion == 3:
    conversor("mexicanos", 19.96)
else:
    print("ingresa una opción válida")