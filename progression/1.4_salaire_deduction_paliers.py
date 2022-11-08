TAUX_1 = 30
TAUX_2 = 40
LIMITE_SALAIRE = 30000

# Entrée
salaire_brut = float(input())

# Calcul et sortie. À faire
taux = 0
if salaire_brut > LIMITE_SALAIRE:
    taux += ((salaire_brut - LIMITE_SALAIRE) * TAUX_2) / 100
    taux += (LIMITE_SALAIRE * TAUX_1) / 100
else:
    taux += (salaire_brut * TAUX_1) / 100
# end if
salaire_net = salaire_brut - taux
print(salaire_net)
