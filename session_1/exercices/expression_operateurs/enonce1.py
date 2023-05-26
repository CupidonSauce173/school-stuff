''' Affiche si le nombre est un jour de la semaine ou
fin de semaine ou message d'erreur. '''

# ---- Variables
# ---- nbr: Entier

nbr = int(input('Entrez un nombre entre 1 et 7: '))
if 1 <= nbr <= 5:
    print('Semaine')
elif nbr in (6, 7):
    print('Fin de semaine')
else:
    print('Jour invalide, entrez un nombre entre 1 et 7.')
