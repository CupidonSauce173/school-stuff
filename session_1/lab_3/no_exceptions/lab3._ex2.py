# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''
''' Calculer et afficher la moyenne de 100 nombres lus en entrée. '''
''' Données: 100 entrées numériques, Sorties: La moyenne de 100 nombres. '''

# ---- Variables
# ---- i: Int
# ---- somme: Float

print('Calculer et afficher la moyenne de 100 nombres lus en entrée.')

i = 0                                                              # Init variable de contrôle à 0.
somme = 0                                                          # Init variable somme à 0.
while i < 100:                                                     # Entrer dans la boucle.
    somme += float(input('Saisir un nombre ' + str(i + 1) + ': ')) # Incrementer la variable de somme par la saisie.
    i += 1                                                         # Incrementer la variable de contrôle de +1.
print('La moyenne est de:', somme / 100)                           # Calculer et afficher la moyenne de la somme.
