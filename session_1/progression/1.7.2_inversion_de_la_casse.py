# Entrées
lettre = input()
lettre_convertie = ""

# Inversion de la casse. À faire
if len(lettre) == 1:
    if lettre.isalpha():
        lettre_convertie = lettre.swapcase()
    else:
        lettre_convertie = lettre
    # end if
# end if
# Sortie
print(lettre_convertie)
