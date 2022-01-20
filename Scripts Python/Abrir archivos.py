#Tiene que estar en el mismo lugar de la consola

with open('archivo.txt', 'r') as descriptor_de_archivo:
    cadena_archivo = descriptor_de_archivo.read()
    print(cadena_archivo)

# Leer una parte
with open('archivo.txt', 'r') as descriptor_de_archivo:
    pedazo = descriptor_de_archivo.read(4)

    print(pedazo)

#
lista_pre = []
lista_res = []

with open('preguntas.txt', 'r') as descriptor_de_archivo:
  preguntas = descriptor_de_archivo.readlines()
    for linea in range(2):
      pregun = random.choice(preguntas)
      lista_pre.append(pregun)
      return(pregun)

with open('respuestas.txt', 'r') as descriptor_de_archivo:
  respuestas = descriptor_de_archivo.readlines()
    for linea1 in range (2):
      respuesta = random.choice(respuestas)
      lista_res.append(respuesta)
      return(respuesta)

print(lista_pre)
print(lista_res)




# ejercicio quiz

import random

final = ''

with open('10m-contrasenas.txt', 'r') as descriptor_de_archivo:
    palabras = descriptor_de_archivo.readlines()

contador = 0

while contador < 4:
    nuevapalabra = random.choice(palabras).capitalize()
    if nuevapalabra[0] == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
        print(nuevapalabra)

    else:
        return nuevapalabra
        final = final + nuevapalabra
        contador += 1

print(final)









