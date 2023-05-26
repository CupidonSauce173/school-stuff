'''
Écrire un programme qui commence par demander à l’utilisateur combien d’entiers il veut
saisir. Le programme va ensuite lire les entiers et les ranger dans la liste. On va nommer cette
liste lst_entiers
'''
# pylint: disable=invalid-name

try:
    NBRE_ENTIERS = int(input("Entrez le nombre d'entiers à saisir: "))
    if NBRE_ENTIERS < 0:
        print("Entrez une valeur positive.")
    # end if
except ValueError:
    print("Entrez strictement un entier.")
# end try-except

lst_entiers = []
try:
    for i in range(NBRE_ENTIERS):
        lst_entiers.append(int(input(f"Entier #{i + 1}: ")))
    # end for
except ValueError:
    print("Entrez strictement un entier.")
# end try-except

# Traitements
LST_LENGTH = len(lst_entiers)

pair = 0
for num in range(LST_LENGTH):
    if num % 2:
        pair += 1
    # end if
# end for

lst_entiers_reverse = list(reversed(lst_entiers))

# Affichage des données
print("*** Affficher la liste des entiers avec un simple print() ***")
print(lst_entiers)
print("*** Afficher le nombre d'entiers pairs ***")
print(pair)
print("*** Afficher le nombre d'entiers impairs ***")
print(LST_LENGTH - pair)
print("*** Afficher la liste et la liste inverse avec un simple print()")
print(" Original: ")
print(lst_entiers)
print(" Inversé: ")
print(lst_entiers_reverse)
print("*** Afficher lst-entiers en utilisant 3 façons")
print("Boucle for sans range()")
for i in lst_entiers:
    print(i)
# end for
print("Boucle for avec range()")
for i in range(LST_LENGTH): # pylint: disable=consider-using-enumerate
    print(lst_entiers[i])
# end for
print("Boucle avec while")
i = 0
while i < LST_LENGTH:
    print(lst_entiers[i])
    i += 1
# end while
print("*** Sortie du programme... ***")
