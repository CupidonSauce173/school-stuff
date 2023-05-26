'''
Écrire un programme qui commence par demander à l’utilisateur combien il a de notes à saisir.
Le programme stocke toutes les notes que l’utilisateur saisi dans une liste. Les notes sont
comprises entre 0 et 100.
'''
# pylint: disable=invalid-name
# pylint: disable=chained-comparison

try:
    NBRE_NOTES = int(input("Entrez le nombre de note à saisir: "))
    if NBRE_NOTES < 0:
        print("Entrez une valeur positive.")
    # end if
except ValueError:
    print("Entrez strictement un entier.")
# end try-except

lst_notes = []
try:
    for i in range(NBRE_NOTES):
        note = float(input(f"Note #{i + 1}: "))
        if note <= 100 and note >= 0:
            lst_notes.append(note)
        else:
            print("Entrez une note entre 0 et 100, veuillez recommencer depuis le début.")
        # end if
    # end for
except ValueError:
    print("Entrez strictement un entier.")
# end try-except

# Traitements
intervalle_60_100 = []
highest = 0
for note in lst_notes:
    if note >= 60 and note <= 100:
        intervalle_60_100.append(note)
    # end if
    if note > highest:
        highest = note
    # end if
# end for
moyenne = sum(lst_notes) / len(lst_notes)

nbre_highest = 0
for note in lst_notes:
    if note == highest:
        nbre_highest += 1
    # end if
# end for

# Affichage
print("*** Afficher la liste avec un simple print()")
print(lst_notes)
print("*** Afficher toutes les notes comprises entre 60 et 100 inclusivement")
print(intervalle_60_100)
print("*** Afficher la moyenne des notes")
print(moyenne)
print("*** Meilleure note ***")
print(highest)
print("*** Afficher le nombre des élèves ayant la meilleure note")
print(nbre_highest)
print("*** Sortie du programme... ***")
