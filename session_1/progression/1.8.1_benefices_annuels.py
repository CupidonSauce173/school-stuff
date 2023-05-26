NBRE_MOIS = 12
bénéfices = []

# Entrées des bénéfices et du mois
for i in range( NBRE_MOIS ):
    bénéfices += [int(input())]
mois = int(input())
# end for

# Détermination du bénéfice correspondant au mois. À faire
if mois <= 12:
    print(bénéfices[mois - 1])
else:
    print('mois incorrect')
# end if
