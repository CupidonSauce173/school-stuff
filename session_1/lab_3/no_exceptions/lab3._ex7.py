# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''

from random import randint

''' Afficher le plus grand de chacune de 50 paires de nombres lus. '''
''' Données: 50 paires de nombres aléatoires, Sorties: Un message affichant le plus grand d'une paire. '''

# ---- Variables
# ---- i, repetitions: Int
# ---- nbr1, nbr2: Float

print('Afficher le plus grand de chacune de 50 paires de nombres lus.')

i = 0                                                     # Init variable de contrôle à 0.
while i < 50:                                             # Entrer dans la boucle.
    nbr1 = randint(0, 50)                                 # Créer un nombre 1 aléatoire entre 0 et 50.
    nbr2 = randint(0, 50)                                 # Créer un nombre 2 aléatoire entre 0 et 50.
    print('Paire: {' + str(nbr1) + ',' + str(nbr2) + '}') # Afficher la paire de nbr1 et nbr2.
    if nbr1 < nbr2:                                       # Comparer nbr1 à plus petit que nbr2.
        print('Le plus grand nombre est: ' + str(nbr2))   # Afficher un message si nbr1 est plus petit que nbr2.
    else:                                                 # Sinon.
        print('Le plus grand nombres est: ' + str(nbr1))  # Afficher un message si nbr1 est plus grand que nbr2.
    print('\n')
    i += 1                                                # Incrementer la variable de contrôle de +1.
