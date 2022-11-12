'''
Écrire un programme en Python qui remplit une liste de 10 caractères de manière aléatoire et
remplir une autre liste par le code ASCII des caractères de la première liste.
'''
# pylint: disable=invalid-name
from random import randint

LIMITE = 10

lst_char = []
lst_ASCII = []

for i in range(LIMITE):
    random_char = randint(0, 126)
    lst_char.append(chr(random_char))
    lst_ASCII.append(random_char)

print("*** Liste de chars ***")
print(lst_char)
print("*** Liste de la valeur ASCII des chars ***")
print(lst_ASCII)
