# ejercicio quiz

import random

numero = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

b = ''

with open('10m-contrasenas.txt', 'r') as descriptor_de_archivo:
    palabras = descriptor_de_archivo.readlines()

contador = 0

while contador < 4:
    nuevapalabra = random.choice(palabras).capitalize()

    if nuevapalabra[0] in numero:
      print('No sirve')
    elif nuevapalabra not in numero:
        a = str(nuevapalabra)
        c = b + a
        contador += 1

print(b)
