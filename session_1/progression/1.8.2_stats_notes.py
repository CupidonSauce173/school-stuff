notes = []
SEUIL_RÉUSSITE = 60
taux_succès = 0.0
taux_échec = 0.0

# Entrée des notes
NBRE_ÉTUDIANTS = int(input())
for i in range (NBRE_ÉTUDIANTS):
    note = float(input())
    notes += [note]

# Calculs. À faire
russites = 0
for elem in notes:
    if elem >= 60:
        russites += 1
    # end if
# end for
if NBRE_ÉTUDIANTS > 0:
    taux_succès = 100 * russites / NBRE_ÉTUDIANTS
    taux_échec = 100 - taux_succès
# end if
# Sorties
print(taux_succès)
print(taux_échec)
