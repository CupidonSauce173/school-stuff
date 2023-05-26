# Entrée
texte = input()

# Construction du texte majuscule vertical. À faire
texte_vertical = ''
texte = texte.upper()
for ch in texte:
    texte_vertical += ch + '\n'
# end for
texte_vertical = texte_vertical[:len(texte_vertical) - 1]
# Sortie
print( texte_vertical )
