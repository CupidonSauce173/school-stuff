SENTINELLE = -1
no_joueur = 0
nbre_joueurs = 0

# Entrée de no_joueur répétée dans une boucle, tant que
# ce n'est pas SENTINELLE. À faire
while no_joueur != SENTINELLE:
    no_joueur = int(input())
    if no_joueur != -1:
        nbre_joueurs += 1
    # end if
# end while

# Sortie de nbre_joueurs
print(nbre_joueurs)
