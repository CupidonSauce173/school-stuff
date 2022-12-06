''' Parcourir la liste des produits pour l'afficher cette fois comme ci-dessous. '''
produits = [["clavier", 25.5, 50], ["souris", 57.1, 60], ["Clé USB", 42.25, 90]]

i = 0
for produit in produits:
    print("==> Produit numéro", i + 1)
    print("Nom du produit:", produit[0])
    print("Prix du produit:", produit[1])
    print("Quantité en stock:", produit[2])
    i += 1
    print('\n')
# end for

i = 0
for produit in produits:
    print("==> Produit numéro", i + 1)
    for elem in produit:
        if isinstance(elem, str):
            print("Nom du produit:", elem)
        elif isinstance(elem, float):
            print("Prix du produit:", elem)
        elif isinstance(elem, int):
            print("Quantité en stock:", elem)
        # end if
    # end for
    i += 1
    print('\n')
# end for
