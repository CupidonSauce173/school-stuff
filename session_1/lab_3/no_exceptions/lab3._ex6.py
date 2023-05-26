# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''
''' Calculer et afficher la moyenne d’une série de nombres lus en entrée. La dernière valeur est -99 et ne doit pas être considérée dans le calcul de la moyenne. '''
''' Données: x entrées numériques, Sorties: La moyenne des entrées numériques. '''

# ---- Variables
# ---- i, entrees: Int
# ---- somme, nbr: Float

print('Calculer et afficher la moyenne d’une série de nombres lus en entrée.')

i = 0                                                               # Init variable de contrôle à 0.
somme = 0                                                           # Init variable somme à 0.
entrees = int(input("Entrez un nombre de saisis à faire: "))        # Init variable entrees à une saisie numérique.
while i < entrees:                                                  # Entrer dans la boucle.
    i += 1                                                          # Incrementer la variable de contrôle de + 1.
    if i == entrees:                                                # Comparer variable de contrôle à égal à entrees.
        print("Dernière valeur est de -99 et n'est pas comptée...") # Afficher un message indiquant que la dernière valeur est hardcoded.
        continue                                                    # Passer cette itération.
    somme += float(input('Entrez un nombre ' + str(i) + ': '))      # Incrementer la variable somme avec une entrée numérique.
print('Moyenne des nombres est de:', somme / (entrees - 1))         # Afficher la moyenne de la somme, excluant une entrée.
