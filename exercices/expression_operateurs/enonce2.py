''' Affiche un message selon la note donnée. '''

# ---- Variables
# ---- note: Float

note = float(input('Entrez une note: '))
if 60 <= note <= 69:
    print('Passable')
elif 70 <= note <= 79:
    print('Bien')
elif 80 <= note <= 89:
    print('Très bien')
elif note >= 90:
    print('Excellent')
else:
    print('Insuffisant')
