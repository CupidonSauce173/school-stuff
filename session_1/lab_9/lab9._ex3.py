'''Écrire un programme qui permet de construire une liste de n produits.
n'est un entier à lire. Chaque élément de la liste est une liste qui comprend
le nom du produit, son prix et sa quantité en stock. Afficher la liste
à l'aide d'un simple print, elle doit ressembler à la liste de l'exercice 1.'''

produits = []
nbre_articles = int(input('Combien de produit à créer?: '))
for i in range(nbre_articles):
    produits.append([
        input('Nom du produit: '),
        float(input('Prix du produit: ')),
        int(input('Quantité en stock: '))
    ])
# end for
print(produits)
