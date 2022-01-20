import math
from typing import Pattern
from typing_extensions import get_type_hints

# def vol_esfera(r):
#     vol1 = (4/3) * math.pi * r**3
#     return vol1

# def vol_cono(r1, h):
#     vol2 = math.pi * r1**2 * h / 3
#     return vol2

# def vol_total(esf1, con1):
#     total1 = esf1 + con1
#     return total1
    
# resf = int(input( 'Escriba el valor del radio de la esfera: '))
# rcon = int(input(' Escriba el valor del radio del cono: '))
# hcon = int(input(' Escriba el valor de la altura del cono: '))

# esf1 = vol_esfera(resf)
# con1 = vol_cono(rcon, hcon)

# total = vol_total(esf1, con1)

# print ('el Volumen total es: ' + str(total) )

########################################################

# def vol_esfera(r):
#     vol1 = (4/3) * math.pi * r**3
#     return vol1

# resf = int(input( 'Escriba el valor del radio de la esfera: '))
# esf1 = vol_esfera(resf)
# print (esf1)

###########################################################

# def vol_cono(r1, h):
#      vol2 = math.pi * r1**2 * h / 3
#      return vol2

# rcon = int(input(' Escriba el valor del radio del cono: '))
# hcon = int(input(' Escriba el valor de la altura del cono: '))

# con1 = vol_cono(rcon, hcon)
# print (con1)

#################

# Ejemplo del carro 
# 1. área del carro, 2 rectangulos y 2 circulos

# import math

# def area_rectangulo(b,h):
#      area1 = b * h
#      return area1

# def area_circulo(r):
#      area2 = math.pi * r ** 2
#      return area2

# b1 = int(input('Escriba el valor de la base del rectángulo 1: '))
# h1 = int(input('Escriba el valor de la altura del rectángulo 1: '))
# b2 = int(input('Escriba el valor de la base del rectángulo 2: '))
# h2 = int(input('Escriba el valor de la altura del rectángulo 2: '))
# r1 = int(input('Escriba el valor del radio del circulo 1: '))
# r2 = int(input('Escriba el valor del radio del circulo 2: '))

# rec1 = area_rectangulo(b1,h1)
# rec2 = area_rectangulo(b2,h2)
# cir1 = area_circulo(r1)
# cir2 = area_circulo(r2)

# totalarea = rec1 + rec2 + cir1 + cir2

# print('El área total del carro es: ' + str(totalarea))

# if __name__ == '__main__':
#      run()


##### ejercicio 

# def kilo(n):
#     if n == gallina:
#        return n * 6
#     elif n == gallo:
#          return n * 7
#     else:
#          return n * 1


# gallina = int(input('Cuántas gallinas tiene: '))
# gallo =  int(input('Cuántos gallos tiene: '))
# pollo = int(input('Cuántos pollos tiene: '))

# kg = kilo(gallina)
# kgll = kilo(gallo)
# kpollo = kilo(pollo)

# peso = kg + kgll + kpollo

# print ('El peso total es de: ', str(peso))


####### ejercicio

# def tienda (p, m, h):
#      costo = p * 300 + m*3300 + h *350
#      return costo

# pan = int(input('¿Cuántos panes va a comprar?: '))
# leche = int(input('¿Cuántas bolsas de leche va a comprar?: '))
# huevos = int(input('¿Cuántos huevos va a comprar?: '))
# billete = int(input('¿Con qué billete va a pagar?: '))

# mandado = tienda(pan, leche, huevos)
# vueltas = billete - mandado

# if billete > mandado:
#      vueltas = billete - mandado
#      print('Las vueltas son: ', str(vueltas))
# else:
#      vueltas = billete - mandado
#      print('Se está debiendo a la tienda: ', str(-vueltas))


######## 






































