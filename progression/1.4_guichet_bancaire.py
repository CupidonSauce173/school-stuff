nouveau_solde = 0
# Entrées
solde = float(input())
choix = int(input())

# Sélective multiple. À faire
if choix == 1:
    montant = float(input())
    solde += montant
elif choix == 2:
    montant = float( input() )
    if montant < solde:
        solde -= montant
    # end if
# end if
# choix: 1 = déposer, 2 = retirer, 3 = fermer compte

# Sortie. À faire
if choix == 3:
    solde = 0.0
    print(solde)
else:
    print(solde)
# end if
