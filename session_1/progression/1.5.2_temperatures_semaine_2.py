MAX_TEMP = 7
nbre_temp = 0
somme_temp = 0

# Entrée de température répétée dans une boucle
while nbre_temp < MAX_TEMP:
    température = float(input())
    # Calcul de la somme des températures entrées. À faire
    somme_temp += température
    nbre_temp += 1
# end while

# Calcul et sortie de la moyenne. À faire
print(somme_temp / nbre_temp)
