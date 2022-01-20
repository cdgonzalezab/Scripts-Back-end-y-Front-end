def hornos(x):
    if 0 < x < 21:
        a = 'uno'
        return a
    elif 21 <= x < 31:
        a ='dos'
        return a
    elif 31 <= x < 51:
        a = 'tres'
        return a
    elif 51 <= x:
        a = 'cuatro'
        return a
    else:
        print('No se usa ningún horno')


elizabeth = int(input('Buen día señoritas Olsen, ¿cuántos buñuelos desean llevar?: '))
mary = 2*elizabeth + 4
ashley = int((mary + elizabeth)/5)
horno = hornos(ashley)
print(str(elizabeth), str(mary), str(ashley))
print(horno)


