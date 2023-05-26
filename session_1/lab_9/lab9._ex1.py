''' Utiliser une boucle imbriquée pour afficher la liste des produits comme ci-dessous '''
produits = [["clavier", 25.5, 50], ["souris", 57.1, 60], ["Clé USB", 42.25, 90]]

i = 0
for produit in produits:
    print("==> Produit numéro", i + 1)
    for elem in produit:
        print(elem)
    # end for
    i += 1
    print('\n')
# end for
