ch =" Le programme \tqui \n lit \t une chaîne et \n affiche un menu "
print("*** Str originale ***")
print(ch)
temp_ch = ch.split(" ")
new_lst = []
for elem in temp_ch:
    # Remplacer \t, \n et " " pour rien dans une variable new_elem
    new_elem = elem \
        .replace("\t", "") \
        .replace("\n", "") \
        .replace(" ", "")
    if len(new_elem) != 0:
        new_lst.append(new_elem)
print("*** Str Transformée ***")
print(" ".join(new_lst))
