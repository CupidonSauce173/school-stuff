
LIMITE = 8
mot_passe = input('Entrer: ')
mot_passe_confirmation = input('Confirmer: ')

nbr_special_char = 0
message = 'valide'
hasUpper = False
hasDigit = False
special_chars = " !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

if mot_passe != mot_passe_confirmation or len(mot_passe) < 8:
    message = 'non valide'
else:
    for ch in mot_passe:
        if ch.isupper():
            hasUpper = True
        # end if
        if ch.isdigit():
            hasDigit = True
        # end if
        for sc in special_chars:
            if mot_passe.find(sc):
                nbr_special_char += 1
            # end if
        # end for
    # end for
# end if

if nbr_special_char != 2 or hasDigit == False or hasUpper == False:
    message = 'non valide'
# end if

print(message)