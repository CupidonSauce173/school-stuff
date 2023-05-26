LIMITE = 8
message = ''

# Entrées
mot_passe = input()
mot_passe_confirmation = input()

# Traitement. À faire
if len(mot_passe) >= 8:
    message = 'valide'
# end if
hasDigit = False
hasUpper = False
nbre_special_ch = 0
for ch in mot_passe:
    if ch.isupper():
        hasUpper = True
    elif ch.isdigit():
        hasDigit = True
    elif not ch.isalpha():
        nbre_special_ch += 1
    # end if
# end for
if hasDigit and hasUpper and nbre_special_ch >= 2:
    message = 'valide'
    if mot_passe != mot_passe_confirmation:
        message = 'valide mais non confirmé'
    # end if
else:
    message = 'non valide'
# end if

# Sortie
print( message )
