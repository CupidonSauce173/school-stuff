LIMITE_1 = 100
LIMITE_2 = 300
RABAIS_1 = 20
RABAIS_2 = 30
rabais = 0
montant_total = 0

# Entrée
montant = float(input())

# Calcul du montant après rabais. À faire
if montant >= LIMITE_1:
    rabais = RABAIS_1
# end if
if montant >= LIMITE_2:
    rabais += RABAIS_2
# end if
montant_total = montant - rabais

# Sortie
print(montant_total)
