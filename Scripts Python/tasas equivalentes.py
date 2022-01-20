#Nominal o no
def run(nml):
    if nml == 'si':
        n1 = True
        return n1
    elif nml == 'no':
        n2 = False
        return n2
    else:
        print(f"Escriba una opción válida, usted escribió '{nominal}'")

#Principal
def change_rates(nom1, y, p, z):
    if nom1 is True:
        if p == 'dv':  # significa que debo dividir en 360 días
            t1 = y / 360
            anual_rate = efectivo_anual(t1, 'dv')
            nueva_periodicidad = formula2(anual_rate, z)
            return nueva_periodicidad

        elif p == 'mv':  # significa que debo dividir en 12 meses
            t1 = y / 12
            anual_rate = (efectivo_anual(t1, 'mv'))
            nueva_periodicidad = formula2(anual_rate, z)
            return nueva_periodicidad

        elif p == 'bv':  # significa que debo dividir en 6 meses
            t1 = y / 6
            anual_rate = efectivo_anual(t1, 'bv')
            nueva_periodicidad = formula2(anual_rate, z)
            return nueva_periodicidad

        elif p == 'tv':  # significa que debo dividir en 4 trimestres
            t1 = y / 4
            anual_rate = efectivo_anual(t1, 'tv')
            nueva_periodicidad = formula2(anual_rate, z)
            return nueva_periodicidad

        elif p == 'sv':  # significa que debo dividir en 2 semestres
            t1 = y / 2
            anual_rate = efectivo_anual(t1, 'sv')
            nueva_periodicidad = formula2(anual_rate, z)
            return nueva_periodicidad

        else:  # La tasa nominal anual es igual a efectiva anual
            t1 = p
            nueva_periodicidad = formula2(t1, z)
            return nueva_periodicidad

    elif nom1 is False:
        if p == 'dv':
            nuevo = efectivo_anual(y, 'dv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'mv':  # significa que debo dividir en 12 meses
            nuevo = efectivo_anual(y, 'mv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'bv':  # significa que debo dividir en 6 meses
            nuevo = efectivo_anual(y, 'bv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'tv':  # significa que debo dividir en 4 trimestres
            nuevo = efectivo_anual(y, 'tv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'sv':  # significa que debo dividir en 2 semestres
            nuevo = efectivo_anual(y, 'sv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'da':
            nuevo = efectivo_anual(y, 'dv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'ma':  # significa que debo dividir en 12 meses
            nuevo = efectivo_anual(y, 'mv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'ba':  # significa que debo dividir en 6 meses
            nuevo = efectivo_anual(y, 'bv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'ta':  # significa que debo dividir en 4 trimestres
            nuevo = efectivo_anual(y, 'tv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'sa':  # significa que debo dividir en 2 semestres
            nuevo = efectivo_anual(y, 'sv')
            nueva_periodicidad = formula2(nuevo, z)
            return nueva_periodicidad

        elif p == 'ea':  # La tasa nominal anual es igual a efectiva anual
            nueva_periodicidad = formula2(y, z)
            return nueva_periodicidad

        else:
            print('Ese valor no es válido')

    else:
        print('No sé pudo realizar el cálculo, revisa el código')

#################################################################################
# Pasar a efectivo anual

def efectivo_anual(t, av):
    if av == 'dv':
        change = formula1(t, 360)
        return change
    elif av == 'mv':
        change = formula1(t, 12)
        return change
    elif av == 'bv':
        change = formula1(t, 6)
        return change
    elif av == 'tv':
        change = formula1(t, 4)
        return change
    elif av == 'sv':
        change = formula1(t, 2)
        return change
    elif av == 'ea':
        change = formula1(t, 1)
        return change
    elif av == 'da':
        change = formula5(t, 360)
        return change
    elif av == 'ma':
        change = formula5(t, 12)
        return change
    elif av == 'ba':
        change = formula5(t, 6)
        return change
    elif av == 'ta':
        change = formula5(t, 4)
        return change
    elif av == 'sa':
        change = formula5(t, 2)
        return change
    else:
        print('No ingresaste un dato válido, empieza de nuevo')

##################################################################################
# pasa de un periodo menor vencido a un año, a EA

def formula1(t, n):
    term = ((1 + (t/100)) ** n) - 1
    return term

##################################################################################
def formula2(t, z):
    if z == 'dv':
        final_rate = formula3(t, 360)
        return final_rate
    elif z == 'mv':
        final_rate = formula3(t, 12)
        return final_rate
    elif z == 'bv':
        final_rate = formula3(t, 6)
        return final_rate
    elif z == 'tv':
        final_rate = formula3(t, 4)
        return final_rate
    elif z == 'sv':
        final_rate = formula3(t, 2)
        return final_rate
    elif z == 'ea':
        final_rate = t
        return final_rate
    elif z == 'da':
        final_rate = formula4(t, 360)
        return final_rate
    elif z == 'ma':
        final_rate = formula4(t, 12)
        return final_rate
    elif z == 'ba':
        final_rate = formula4(t, 6)
        return final_rate
    elif z == 'ta':
        final_rate = formula4(t, 4)
        return final_rate
    elif z == 'sa':
        final_rate = formula4(t, 2)
        return final_rate
    else:
        print('No ingresaste un dato válido, empieza de nuevo')

###################################################################################
# pasar de efectivo anual a otra periodicidad vencida
def formula3(x, n):
    end = (((1 + x) ** (1 / n)) - 1)
    return end

###################################################################################
# pasar de efectivo anual a otra periodicidad anticipada

def formula4(x, n):
    y = (x / (1 + x))  # este es el cambio de vencido a anticipado
    end = (((1 + (y/100)) ** (1 / n)) - 1)
    return end

##################################################################################
# pasa de un periodo menor anticipado a un año, a EA

def formula5(x, n):
    y = (x / (1 - x))  # este es el cambio de vencido a anticipado
    term = (((1 + y) ** n) - 1)
    return term

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

if nom is True or nom is False:
    taxa = float(input('Ingrese el valor de la tasa que quiere convertir: '))
    periodicity = input('Ingrese la periodicidad de la tasa: ')
    want = input('¿A qué tasa quiere convertirla?: (ingrese periodicidad)  ')

    taxa1 = change_rates(nom, taxa, periodicity, want)
    taxa2 = taxa1*100

    if nom is True:
        print('la tasa equivalente de la tasa ', taxa, '%', 'n', periodicity, ' es ', str(taxa2), '%', str(want))
    else:
        print('la tasa equivalente de la tasa ', taxa, '%', periodicity, ' es ', str(taxa2), '%', str(want))
else:
    print('Toca volver a empezar')



