import math

def area_circulo (r):
     print('El área del círculo está definida por: pi * r^2')
     area1 = math.pi * r**2
     return area1

def run():
    radio1 = int(input('Escriba el radio del círculo: '))
    resultado = area_circulo(radio1)
    print (resultado)

if __name__ == '__main__':
    run()

