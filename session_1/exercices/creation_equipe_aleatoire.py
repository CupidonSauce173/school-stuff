from random import randint

lst_noms = ['A', 'B', 'C', 'D', 'E', 'F', 'O']
lst_equipes = []
while len(lst_noms) != 0:
    if len(lst_noms) != 1:
        random_1 = lst_noms[randint(0, len(lst_noms) - 1)]
        lst_noms.remove(random_1)
        random_2 = lst_noms[randint(0, len(lst_noms) - 1)]
        lst_noms.remove(random_2)
        lst_equipes.append([random_1, random_2])
    else:
        print("Il reste quelqu'un dans la liste")

print("*** LISTE DES ÉQUIPES ***")
print(lst_equipes)
print("*** RESTE NOMS ***")
print(lst_noms)
