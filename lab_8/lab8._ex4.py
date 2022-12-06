'''
Effectuer la même chose que l’exercice 2 mais cette fois-ci, chaque élément de la liste créé est
une sous liste de 2 éléments, le premier est le caractère et le deuxième est son code ASCII.
Afficher la liste ainsi créé.
'''

# pylint: disable=invalid-name
from random import randint

LIMITE = 10

lst_char_ASCII = []

for i in range(LIMITE):
    random_char = randint(0, 126)
    lst_char_ASCII.append([random_char, chr(random_char)])
# end for

print("*** Liste [char, ASCII] ***")
print(lst_char_ASCII)
