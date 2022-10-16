# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long

''' Author: Antoine Langevin Date: 2022-09-22, Update: 2022-09-22. '''

from random import randint

''' Lire 3000 nombres et indiquer combien il y a de valeurs positives, négatives et nulles. '''
''' Données: 3000 données numériques, Sorties: Un message affichant le nombre de valeurs positives, négatives et nulles. '''

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
