
# ---- Variables
# ---- cote: int
# ---- choix: str

cote = int(input('saisir la mesure du côté (>0) : '))
if cote <= 0:
    print('Vous devez saisir un côté > 0')
else:
    choix = input('Saisir P pour le calcul du '
     + 'périmètre ou S pour le calcul de la surface du carré : ')
    if choix in ('P', 'p'):
        print('Le périmètre du carré est ', 4 * cote)
    elif choix in ('S', 's'):
        print('La surface du carré est ', cote * cote)
    else:
        print('choix invalide, il faut taper S ou s (surface) ou P ou p (périmètre ')
