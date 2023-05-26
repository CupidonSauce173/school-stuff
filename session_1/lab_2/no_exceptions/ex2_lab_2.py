'''
Écrire un programme qui lit deux entiers a et b
au clavier et affiche un message indiquant s’ils sont
successifs ou non. On définit deux
nombres successifs si leur différence en absolue est égale à 1.
 '''

a = int(input('Entrez un premier nombre: '))
b = int(input('Entrez un deuxième nombre: '))

if a + 1 == b or b + 1 == a:
    print('Nombres successifs.')
else:
    print('Nombres non successifs.')
