'''Écrire un programme qui lit un entier strictement positif et affiche
si cet entier est en progression
croissante ou non'''

nombre = input('Entrer un nombre entier strictement positif: ') # 0,1,2 -- 1,2,3 

if int(nombre) > 0:
    index = 0
    croissant = True
    while index < len(nombre) - 1:
        if int(nombre[index]) > int(nombre[index+1]):
            croissant = False
        # end if
        index += 1
    # end while
    if croissant:
        print('Croissant')
    else:
        print('Non croissant')
    # end if
else:
    print('Entrer un nombre positif.')
# end if
