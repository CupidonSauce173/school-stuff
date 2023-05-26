températures = []
somme = 0
moyenne = 0

# Entrées des températures
NBRE_TEMPÉRATURES = int(input())
for i in range(NBRE_TEMPÉRATURES):
    température = float(input())
    températures += [température]

# Calcul du min des températures.
if NBRE_TEMPÉRATURES != 0:
    min = températures[0]
    for i in range(NBRE_TEMPÉRATURES):
        if températures[i] < min:
            min = températures[i]

# Calcul du max des températures. À faire
if NBRE_TEMPÉRATURES != 0:
    max = températures[0]
    for i in range(NBRE_TEMPÉRATURES):
        if températures[i] > max:
            max = températures[i]
        # Fin si
    # Fin for
# Fin si

# Sorties. À faire
if NBRE_TEMPÉRATURES != 0:
    print(min)
    print(max)
else:
    print('aucune')
# Fin si