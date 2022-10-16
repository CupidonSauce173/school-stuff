# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long
# pylint: disable=invalid-name

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. Version: 2022002214:19'''

from random import randint

# Exercice 1, lab3_ex1.py

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

# Exervice 2, lab3_ex2.py

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

# Exercice 3, lab3_ex3.py

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


# Exervice 4, lab3_ex4.py

# ---- Variables
# ---- i, entrees, higher: Int

print('Afficher combien de nombres sont supérieurs à 20 dans une série de X nombres.')

i = 0                                                                      # Init variable de contrôle à 0.
higher = 0                                                                 # Init variable higher à 0.
entrees = int(input("Saisir un nombres d'entrées numériques à saisir: "))  # Init variable entrees à une saisie.
while i < entrees:                                                         # Entrer dans la boucle.
    if float(input('Saisir un nombres ' + str(i + 1) + ': ')) > 20:        # Comparer la saisi à plus grand que 20
        higher += 1                                                        # Incrementer la variable higher de +1.
    i += 1                                                                 # Incrementer la variable de contrôle de +1.
print('Il y a ' + str(higher) + ' de nombres plus grand que 20.')          # Afficher un message avec le nombre de valeurs plus grandes que 20.

# Exercice 5, lab3_ex5.py

# ---- Variables
# ---- i, entrees: Int
# ---- somme, nbr: Float

print('Calculer et afficher la moyenne d’une série de nombres lus en entrée.')

i = 0                                                             # Init variable de contrôle à 0.
somme = 0                                                         # Init variable somme à 0.
entrees = int(input("Entrez un nombre de saisis à faire: "))      # Init variable entrees à une saisie numérique.
while i < entrees:                                                # Entrer dans la boucle.
    i += 1                                                        # Incrementer la variable de contrôle de + 1.
    if i == entrees:                                              # Comparer variable de contrôle à si égal à entrees.
        print("Dernière valeur est de 0 et n'est pas comptée...") # Afficher un message indiquant que la dernière valeur n'est pas prise en compte.
        continue                                                  # Passer la boucle.
    somme += float(input('Entrez un nombre ' + str(i) + ': '))    # Incrementer la variable somme à une saisie numérique.
print('Moyenne des nombres est de:', somme / (entrees - 1))       # Calculer et afficher la moyenne de la variable somme par la variable entrees - 1.

# Exercice 6, lab3_ex6.py

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

# Exercice 7, lab3_ex7.py

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

# Exervice 8, lab3_ex8.py

# ---- Variables
# ---- i, pos, null, neg: Int
# ---- nbr: Float

print('Lire 3000 nombres et indiquer combien il y a de valeurs positives, négatives et nulles.')

i = 0                         # Init variable de contrôle à 0.
pos = 0                       # Init variable pos à 0.
null = 0                      # Init variable null à 0.
neg = 0                       # Init variable neg à 0.
while i < 3000:               # Entrer dans la boucle.
    nbr = randint(-1000,1000) # Créer un nombre aléatoire.
    if nbr > 0:               # Comparer nbr à plus grand que 0.
        pos += 1              # Incrementer de +1 pos si plus grand que 0.
    if nbr < 0:               # Comparer nbr à plus petit que 0.
        neg += 1              # Incrementer de +1 neg si plus petit que 0.
    if nbr is None:           # Comparer nbr à None (null).
        null += 1             # Incrementer de +1 null si None (null).
    i += 1                    # Incrementer la variable de contrôle de +1.
print('Valeurs positives: '
    + str(pos)                # Valeurs positives.
    + ', négatives: '
    + str(neg) + ', null: '   # Valeurs négatives.
    + str(null))              # Valeurs nulls.
print('Nombre des valeurs comparées: ' + str(i)) # Afficher le total des valeurs comparées.
