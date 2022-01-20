# import json
# import pickle
#
# s = ''
#
# with open("prueba pickle.txt", 'rb') as f:
#   s =pickle(f)
#
# print(s)
#
# #
# import json
#
# diccionardio_de_datos = {
#     'clave' : 'valor',
#     'otra clave' : 'otrovalor'
# }
#
# print(diccionardio_de_datos)
#
# with open ('nuestro_primer_JSON', 'w') as f:
#     json.dump((diccionario_de_datos))
#
# # exercise
#
# import json
#
# miembros_familia = {
#     'tío' : 'Juan',
#     'tía' : 'María',
#     'primo' : 'Carlos',
#     'prima' : 'Juliana'
# }
#
# print(miembros_familia)
#
# with open ('mi_familia_json', 'w') as f:
#     json.dump(miembros_familia, f)
#
#
# cadena = json.dumps(miembros_familia)
# print(cadena)
#
#
# #des - serialización
# import json
#
# d = {}
#
# with open ('mi_familia_json', 'r') as f:
#     d = json.load(f)
#
# print(d)
#
# #


#des - serialización
import json

from pprint import pprint

d = {}

with open ('todos.json', 'r') as f:
    d = json.load(f)

# print(len(d)) son 200
ids = []

for i in range(0, 200):
    user = d[i]['userId']
    ids.append(user)
pprint(min(ids))

####

import json

from pprint import pprint

d = {}

with open ('todos.json', 'r') as f:
    d = json.load(f)

# print(len(d)) son 200
ids = []

for i in range(0, 200):
    user = d[i]['userId']
    ids.append(user)

pprint(set(ids))

