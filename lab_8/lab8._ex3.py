'''
Écrire un programme qui remplit une liste automatiquement de toutes les lettres minuscules de
a à z en ordre alphabétique; Afficher-la puis la remplir de nouveau par les lettres majuscules à
partir de la liste des lettres minuscules en utilisant une fois la boucle for, une fois la boucle
while
'''
# pylint: disable=invalid-name

LIMITE = 26

alphabet = []
indice = 97
for i in range(LIMITE):
    alphabet.append(chr(indice))
    indice += 1
# end for
print("*** Afficher la liste d'alphabet minuscule ***")
print(alphabet)

for i in range(LIMITE):
    alphabet[i] = alphabet[i].upper()
# end for
print("*** Afficher la liste d'alphabet majuscule (for)")
for char in alphabet:
    print(char)
# end for
print("*** Afficher la liste d'alphabet majuscule (while)")
i = 0
while i < len(alphabet):
    print(alphabet[i])
    i += 1
# end while
