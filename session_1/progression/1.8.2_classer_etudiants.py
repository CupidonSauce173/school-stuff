notes = []

# Entrée du tableau
NBRE_ÉTUDIANTS = int(input())
for i in range(NBRE_ÉTUDIANTS):
    notes += [float(input())]

# Tri et sorties du tableau trié. À faire.

highest = [0,0]
sortedList = []
i = 0
while len(notes) > 0:
    for elem in notes:
        if elem > highest[0]:
            highest = [elem, i]
        i += 1
    notes.pop(highest[1])
    sortedList.append(highest[0])
    highest = []

sortedList.reverse()
print(sortedList)
