def run (nominal):
  if nominal == 'si':
    n1 = True
    return n1
  elif nominal == 'no':
    n2 = False
    return n2
  else:
    print(f"Escriba una opción válida, usted escribió '{nominal}'")
    

##################################################################################
### pasa de un periodo menor vencido a un año, a EA

def formula1 (t,n):
    formula_terminada : float
    formula_terminada = ((1+t)**n)-1

##################################################################################
### pasa de un periodo menor anticipado a un año, a EA

def formula5 (x,n):
    y = (x/(1-x)) ## este es el cambio de vencido a anticipado
    formula_terminada = ((1+y)**n)-1

##################################################################################
## Pasar a efectivo anual
def efectivo_anual(t,av):
    if av == 'dv':
        cambio = formula1(t,360)
        
    elif av == 'mv':
        cambio = formula1(t,int(12))
        
    elif av == 'bv':
        cambio = formula1(t,6)
        
    elif av == 'tv':
        cambio = formula1(t,4)
        
    elif av == 'sv':
        cambio = formula1(t,2)
        
    elif av == 'ea':
        cambio = formula1(t,1)
        
    elif av == 'da':
        cambio = formula5(t,360)
        
    elif av == 'ma':
        cambio = formula5(t,12)
        
    elif av == 'ba':
        cambio = formula5(t,6)
        
    elif av == 'ta':
        cambio = formula5(t,4)
        
    elif av == 'sa':
        cambio = formula5(t,2)
        
    else:
        print('No ingresaste un dato válido, empieza de nuevo')
###################################################################################
### pasar de efectivo anual a otra periodicidad vencida
def formula3(x,n):
    formula_vencida = (((1+x)**(1/n))-1)

###################################################################################
### pasar de efectivo anual a otra periodicidad anticipada
def formula4(x,n):
    y = float(x/(1+x)) ## este es el cambio de vencido a anticipado
    formula_vencida = float(((1+y)**(1/n))-1)

####################

yoquiero : str

##################################################################################
def formula2(t, z):
    if z == 'dv':
        tasa_final = formula3(t,int(360))
        
    elif z == 'mv':
        tasa_final = formula3(t,int(12))
        
    elif z == 'bv':
        tasa_final = formula3(t,6)
        
    elif z == 'tv':
        tasa_final = formula3(t,4)
        
    elif z == 'sv':
        tasa_final = formula3(t,2)
        
    elif z == 'ea':
        tasa_final = t
        
    elif z == 'da':
        tasa_final = formula4(t,360)
        
    elif z == 'ma':
        tasa_final = formula4(t,12)
                
    elif z == 'ba':
        tasa_final = formula4(t,6)
                
    elif z == 'ta':
        tasa_final = formula4(t,4)
                
    elif z == 'sa':
        tasa_final = formula4(t,2)
                
    else:
        print('No ingresaste un dato válido, empieza de nuevo')
            

##################################################################################


def cambiotasas (nom1,y,p,z):
    if nom1 == True:
        if p == 'dv': #significa que debo dividir en 360 días
            t1 = y/360
            tasa_anual = efectivo_anual(t1, 'dv')
            nueva_periodicidad = formula2(tasa_anual, z)

        elif p == 'mv': #significa que debo dividir en 12 meses
            t1 = y/12
            tasa_anual = (efectivo_anual(t1, 'mv'))
            nueva_periodicidad = formula2(tasa_anual, z)

        elif p == 'bv': #significa que debo dividir en 6 meses
            t1 = y/6
            tasa_anual = efectivo_anual(t1, 'bv')
            nueva_periodicidad = formula2(tasa_anual, z)

        elif p == 'tv': #significa que debo dividir en 4 trimestres
            t1 = y/4
            tasa_anual = efectivo_anual(t1, 'tv')
            nueva_periodicidad = formula2(tasa_anual, z)

        elif p == 'sv': #significa que debo dividir en 2 semestres
            t1 = y/2
            tasa_anual = efectivo_anual(t1, 'sv')
            nueva_periodicidad = formula2(tasa_anual, z)

        else:         #La tasa nominal anual es igual a efectiva anual
            t1 = p 
            nueva_periodicidad = formula2(t1, z)

    elif nom1 == False: ##############################################
        if p == 'dv':
            nuevo = efectivo_anual(y,'dv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'mv': #significa que debo dividir en 12 meses
            nuevo = efectivo_anual(y,'mv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'bv': #significa que debo dividir en 6 meses
            nuevo = efectivo_anual(y,'bv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'tv': #significa que debo dividir en 4 trimestres
            nuevo = efectivo_anual(y,'tv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'sv': #significa que debo dividir en 2 semestres
            nuevo = efectivo_anual(y,'sv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'da':
            nuevo = efectivo_anual(y,'dv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'ma': #significa que debo dividir en 12 meses
            nuevo = efectivo_anual(y,'mv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'ba': #significa que debo dividir en 6 meses
            nuevo = efectivo_anual(y,'bv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'ta': #significa que debo dividir en 4 trimestres
            nuevo = efectivo_anual(y,'tv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'sa': #significa que debo dividir en 2 semestres
            nuevo = efectivo_anual(y,'sv')
            nueva_periodicidad = formula2(nuevo, z)

        elif p == 'ea':        #La tasa nominal anual es igual a efectiva anual
            t1 = p 
            nueva_periodicidad = formula2(t1, z)
        else:
            print('Ese valor no es válido')
        
    else:
        print('No sé pudo realizar el cálculo, revisa el código')

###################################################################################            

menu = """ Bienvenido al conversor de tasas de interés equivalentes, 
el cálculo consta de 3 variables que se van a preguntar: 

1. ¿Es nominal o efectiva?
2. Tasa de interés. 
3. Periodicidad de la tasa. 

Para la conversión de tasas tome en cuenta lo siguiente:

1. Se responde en minúscula "si" ó "no".

2. La tasa de interés no debe ir acompañada del símbolo %, y debe ser ingresada
de la siguiente forma. ej: 10% = 10, 4.5% = 4.5, 0.1% = 0.1.

3. las periodicidades disponibles son:

dv - día vencido.            da - diario anticipado.
mv - mes vencido.            ma - mes anticipado.
bv - bimestre vencido.       bv - bimestre anticipado.
tv - trimestre vencido.      ta - trimestre anticipado.
sv - semestre vencido.       sa - semestre anticipado.
ea - efectivo anual.

¡Listo, estamos listos para empezar!

"""

print(menu)
nominal = input('¿la tasa que va a ingresar es nominal? responder "si" ó "no": ')
nom = run(nominal)

if nom == True or nom == False:
    tasa = float(input('Ingrese el valor de la tasa que quiere convertir: '))
    periodicidad = input('Ingrese la periodicidad de la tasa: ')
    yoquiero = input('¿A qué tasa quiere convertirla?: (ingrese periodicidad)')
    
    newtasa = float(cambiotasas(nom, tasa, periodicidad, yoquiero))
    
    if nom == True:
        print ('la tasa equivalente de la tasa ', tasa,'n', periodicidad,  ' es ', str(newtasa), str(yoquiero))
    else:
        print ('la tasa equivalente de la tasa ', tasa, periodicidad,  ' es ', str(newtasa), str(yoquiero))
else:
    print('Toca volver a empezar')

    

