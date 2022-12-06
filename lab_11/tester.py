"""
Fichier de test pour les différents exercices du lab11.
"""

# pylint:disable=no-member
import lab11_methods as methods

print("*** DÉBUT DU PROGRAMME TEST ***")
# Exercice 1
print(methods.remove_spaces("OWIGJwo WOIEGmWO Ieg jweiogj "))
sum_average = methods.sum_average([1,2,3,5,643,1,352])

# Exercice 2
print(f"Total: {sum_average[0]} Moyenne: {sum_average[1]}")

# Exercice 3
OCCURENCES = methods.count_occurences("IO#gjoGIMedwoICVN#OIGKJ4etj)jowkdmgw", 'o')
print(f"Occurences: {OCCURENCES}")

# Exercice 4
NBR = -3269083
print(f"Valeur absoluede {NBR}: {methods.absolute_value(NBR)}")

# Exercice 5
FIRST_LAST = methods.first_last_string("gfO#In3oikjf")
print(f"Premier: {FIRST_LAST[0]} Dernier: {FIRST_LAST[1]}")

# Exercice 6
print(methods.sort_highest_lowest([1,25,3,6,37,6,352,24,62,3,5,523,6,2346,34,67]))

# Exercice 7
BASE = 3
EXPOSANT = 3
print(f"Puissance de {BASE} (B) et {EXPOSANT} (exposant) est de: {methods.power(BASE, EXPOSANT)}")

print("*** FIN DU PROGRAMME TEST ***")
