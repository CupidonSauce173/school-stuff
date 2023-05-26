# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''
''' Afficher combien de nombres sont supérieurs strictement à 20 dans une série de 10 nombres. '''
''' Données: 10 entrées numériques, Sorties: Un message affichant les nombres strictement supérieurs à 20. '''

# ---- Variables
# ---- i, higher: Int

print('Afficher combien de nombres sont supérieurs strictement à 20 dans une série de 10 nombres.')

i = 0                                                                     # Init variable de contrôle à 0.
higher = 0                                                                # Init variable higher à 0.
while i < 10:                                                             # Entrer dans la boucle.
    if float(input('Saisir un nombre ' + str(i + 1) + ': ')) > 20:        # Comparer la saisie numérique à plus grand que 20.
        higher += 1                                                       # Incrementer la variable higher de +1.
    i += 1                                                                # Incrementer la variable de contrôle de +1
print('Il y a ' + str(higher) + ' nombres supérieur à 20.')               # Afficher un message indiquant la variable higher.
