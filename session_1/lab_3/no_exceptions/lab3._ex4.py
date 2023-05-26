# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''
''' Afficher combien de nombres sont supérieurs à 20 dans une série de X nombres, la valeur de X étant lue en entrée '''
''' Données: x entrées numériques, Sorties: Un message affichant les nombres strictement supérieurs à 20. '''

# ---- Variables
# ---- i, entrees, higher: Int

print('Afficher combien de nombres sont supérieurs à 20 dans une série de X nombres.')

i = 0                                                                      # Init variable de contrôle à 0.
higher = 0                                                                 # Init variable higher à 0.
entrees = int(input("Saisir un nombres d'entrées numériques à saisir: "))  # Init variable entrees à une saisie.
while i < entrees:                                                         # Entrer dans la boucle.
    if float(input('Saisir un nombres ' + str(i + 1) + ': ')) > 20:        # Rajouter une saisie numérique à la liste nombres.
        higher += 1                                                        # Incrementer la variable higher de +1.
    i += 1                                                                 # Incrementer la variable de contrôle de +1.
print('Il y a ' + str(higher) + ' de nombres plus grand que 20.')          # Afficher un message avec le nombre de valeurs plus grandes que 20.
