'''
Écrire un programme en Python qui remplit une liste de 10 entiers. La valeur du ième élément
est le carré de son indice. Afficher la liste.
'''

from random import randint

LIMITE = 10

# Remplissage de la liste lst_entiers
lst_entiers = []
for i in range(LIMITE):
    if i == 8:
        lst_entiers.append(8 ** 2)
    else:
        lst_entiers.append(randint(0, 100))
    # end if
# end for
print(lst_entiers)
