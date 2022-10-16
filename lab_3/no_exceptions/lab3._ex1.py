# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''
''' Lire 10 nombres, afficher la somme et la moyeene des 10 nombres si la somme est comprise entre 100 et 200 inclusivement. Afficher la moyeene dans tous les autres cas. '''
''' Données: 10 entrées numériques, Sorties: Somme des 10 entrées et ou la moyenne. '''

# ---- Variables
# ---- i: Int
# ---- somme: Float

print('Afficher la moyenne de 10 nombres et afficher la somme si celle-ci est entre 100 et 200.')

i = 0                                                              # Init variable de contrôle à 0.
somme = 0                                                          # Init somme à 0.
while i < 10:                                                      # Entrer dans la structure itérative.
    somme += float(input('Saisir un nombre ' + str(i + 1) + ': ')) # Afficher un message de saisie et additioner à la somme.
    i += 1                                                         # Incrementation de la variable de contrôle.
if 100 < somme < 200:                                              # Condition pour afficher la somme.
    print('La somme est de:', somme)                               # Afficher la somme si condition True.
print('La moyenne est de:', somme / 10)                            # Afficher la moyenne.