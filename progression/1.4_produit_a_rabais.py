TAUX_TAXE = 15
TAUX_RABAIS = 20
LIMITE = 100

# entrées
quantité = int(input())
prix = float(input())

# Calcul et sortie. À faire
montant = quantité * prix
montant = montant + (montant * (TAUX_TAXE / 100))

if montant > 100:
    montant = montant - (montant * (TAUX_RABAIS / 100))
# end if
print(montant)
