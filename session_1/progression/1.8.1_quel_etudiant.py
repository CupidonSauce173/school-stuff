MAX = 5
codes = []
notes = []

# Entrées des codes, notes et position
for i in range (MAX):
    codes += [input()]
# Fin for
for i in range (MAX):
    notes += [int(input())]
# Fin for
position = int(input())

# Calculs et sorties. À faire
if position > len(codes):
    print('position incorrecte')
else:
    print(codes[position - 1])
    print(notes[position - 1])
# Fin si