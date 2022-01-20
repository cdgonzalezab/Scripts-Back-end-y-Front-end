# def imprimir_msj():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_msj()
# imprimir_msj()
# imprimir_msj()

# def conversacion(mensaje):
#     print('Hola')
#     print('¿Cómo estás?')
#     print(mensaje)
#     print('Adiós')

# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opcion 1')
# elif opcion == 2:
#     conversacion('Elegiste la opcion 2')
# elif opcion == 3:
#     conversacion('Elegiste la opcion 3')
# else:
#     print('Elige una opción válida')


# def suma (a, b):
#      print('Se suman dos números')
#      resultado = a + b
#      return resultado

# sumatoria = suma(1, 4)
# print(sumatoria)

#### MINTIC ####

# def f(x):
#      return x * x

# f(2)
# print(f(2))


# import math

# def area_circulo(r):
#      area = math.pi * r ** 2
#      return area

### ejemplo


# def area_rectangulo(l,a):
#      area = l*a
#      return area

# largo = float(input('Largo del rectangulo: '))
# ancho = float(input('Ancho del rectangulo: '))
# print("El área del rectángulo es: ", end= ' ')
# print(area_rectangulo(largo,ancho))

#### ejemplo 

# def area_rectangulo(l,a):
#      area = l*a
#      return area

# largo = float(input('Largo del rectangulo: '))
# ancho = float(input('Ancho del rectangulo: '))

# area1 = area_rectangulo(largo,ancho)

# print('El área del rectángulo es: ', str(area1), end= '...')

#### ejemplo 

KAPPA: float = 9E+9
def ley_coulomb(Q1, Q2, r):
     modulo = KAPPA * Q1 * Q2 / r **2
     return modulo

carga1 = float(input('Carga 1: '))
carga2 = float(input('Carga 2: '))
distancia = float(input('Distancia entre cargas: '))
print('El módulo de la fuerza es: ', end = "...")
print(ley_coulomb(carga1,carga2,distancia))






























