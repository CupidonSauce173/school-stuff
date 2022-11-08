# Entrées
côté = int(input())
caractère = input()

# Boucle externe pour répéter la sortie des lignes du triangle. À faire
for i in range(côté):
    print ( caractère * côté )
    côté -= 1
# end for
