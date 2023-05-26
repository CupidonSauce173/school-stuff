MAX_TEMP = 7
somme_temp_pos = 0
nbre_temp_pos = 0

# Entrée des températures
for nbreTemp in range (MAX_TEMP ):
    température = float(input())
    # Compter le nombre de températures positives et
    # accumuler dans la variable somme_temp_pos. À faire
    if température > 0:
        somme_temp_pos += température
        nbre_temp_pos += 1
    # end if
# end for

# Calcul et sortie. À faire
if nbre_temp_pos > 0:
    print(somme_temp_pos / nbre_temp_pos)
else:
    print("AUCUNE")
#end if
