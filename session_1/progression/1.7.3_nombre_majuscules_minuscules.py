# Entrée
adresse = input()

# Comptage des lettres majuscules et minuscles. À faire
nbre_lettres_maj = 0
nbre_lettres_minus = 0

# Traitement
for ch in adresse:
    if ch.isalpha():
        if ch.isupper():
            nbre_lettres_maj += 1
        else:
            nbre_lettres_minus += 1
        # end if
    # end if
# end for

# Sorties
print( nbre_lettres_maj )
print( nbre_lettres_minus )
