salaires = []
salaire_min = 0
salaire_max = 0
salaire_moyen = 0

# Entrées
NBRE_EMPLOYÉS = int(input())
for i in range (NBRE_EMPLOYÉS):
    salaires += [float(input())]

# Calcul et sortie du salaire min, max, et moyen. À faire
if len(salaires) != 0:
    salaire_min = salaires[0]
    salaire_max = salaires[0]
    for salaire in salaires:
        if salaire > salaire_max:
            salaire_max = salaire
        elif salaire < salaire_min:
            salaire_min = salaire
        salaire_moyen += salaire
        # end if
    # end for
    print(salaire_min)
    print(salaire_max)
    print(salaire_moyen / len(salaires))
else:
    print('aucun')
# end if
