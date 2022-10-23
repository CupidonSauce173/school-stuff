# pylint: disable=pointless-string-statement
# pylint: disable=line-too-long
# pylint: disable=invalid-name

''' Author: Antoine Langevin Date: 2022-10.23, Update: 2022-09-22. Version: 22102313:51'''

COEFFICIENTS = [25,35,15,25]

# Initialisation des variables
continuer = True
notes_eleves = []
codes = []
min_note = [0,100]
max_note = [0,0]
intervalle_25 = 0
intervalle_50 = 0
intervalle_75 = 0
intervalle_100 = 0
moyenne_total = 0

while continuer:
    try:
        # Entrée des données
        code_Permanent = int(input('Entrez votre code permanent: '))
        if len(str(code_Permanent)) > 4 or len(str(code_Permanent)) < 4:
            raise ValueError()
        codes.append(code_Permanent)
        i = 0
        notes = []
        while i < 4:
            notes.append(int(input('Entrez votre note ' + str(i + 1) + ': ')))
            i += 1
    except ValueError:
        print('Entrez des informations correctes!')
    else:
        # Pré-traitement des données
        k = 0
        moyenne_pond = 0
        coefficient_total = 0
        while k < len(notes):
            moyenne_pond += notes[k] * COEFFICIENTS[k]
            coefficient_total += COEFFICIENTS[k]
            k += 1
        moyenne_pond = moyenne_pond / coefficient_total
        notes_eleves.append(moyenne_pond)
        continuer = input('Continuez?: y/Y ') in ('Y','y')

i = 0
# Traitement des données
print('----- Notes des élèves -----')
while i < len(codes):
    moyenne_total += notes_eleves[i]
    print(f' - Note Finale Élève ({codes[i]}): {notes_eleves[i]}')
    if notes_eleves[i] > max_note[1]:
        max_note[1] = notes_eleves[i]
        max_note[0] = codes[i]
    if notes_eleves[i] < min_note[1]:
        min_note[1] = notes_eleves[i]
        min_note[0] = codes[i]
    # Recherche de l'intervalle de l'élève
    if notes_eleves[i] <= 25:
        intervalle_25 += 1
    elif notes_eleves[i] <= 50:
        intervalle_50 += 1
    elif notes_eleves[i] <= 75:
        intervalle_75 += 1
    elif notes_eleves[i] <= 100:
        intervalle_100 += 1
    i += 1
# Affichages des résultats des traitements
print('----------------------------')
print(f'Nombre élèves: {len(codes)}')
moyenne_total = moyenne_total / len(codes)
print(f'Moyenne Total: {moyenne_total}')
print(f'Plus basse note ({min_note[0]}): {min_note[1]}')
print(f'Plus haute note ({max_note[0]}): {max_note[1]}')
print(f'Élèves avec une note finale entre 0 et 25: {intervalle_25}')
print(f'Élèves avec une note finale entre 26 et 50: {intervalle_50}')
print(f'Élèves avec une note finale entre 51 et 75: {intervalle_75}')
print(f'Élèves avec une note finale entre 76 et 100: {intervalle_100}')
