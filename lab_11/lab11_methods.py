'''
Liste de méthodes pour le laboratoir 11.
'''

import sys

HIGHEST = sys.maxsize

def remove_spaces(target_string: str) -> str:
    """
    Retire les espaces d'une chaîne de caractères.
    LAB_11 -> EX1

    Paramètres :
    target_string : Chaîne de caractères à modifier.

    Retourne : Une chaîne de caractères (str) sans espaces.
    """
    lst_string = target_string.split(' ')
    return ''.join(lst_string)

def sum_average(target_list: list) -> list:
    """
    Calcule la somme et la moyenne d'une liste.
    LAB_11 -> EX2

    Paramètres :
    target_list : Liste de nombres

    Retourne : Une liste à deux éléments [sum, average]
    """
    total = 0
    for nbr in target_list:
        try:
            total += nbr
        except ValueError:
            print('Une ou plusieurs valeurs dans la liste ne sont pas des nombres.')
    try:
        average = total / len(target_list)
    except ZeroDivisionError:
        print("La valeur des nombres de la liste est de zéro.")
    return [total, average]

def count_occurences(target_string: str, search: str) -> int:
    """
    Compte le nombre de fois que search est dans target_string.
    Ignore la case.
    LAB_11 -> EX3

    Paramètres :
    target_string : La chaîne de caractères à lire.
    search        : Le caractère à chercher.

    Retourne : Un entier étant le nombre de fois que search est dans target_string.
    """
    if search.isdigit():
        print("search n'est pas un caractère valide.")
    else:
        occurences = 0
        for char in target_string:
            if char.lower() == search.lower():
                occurences += 1
        return occurences
    return 0

def absolute_value(nbr: int) -> int:
    """
    Lis et retourne la valeur absolue d'un nombre.
    LAB_11 -> EX4

    Paramètres :
    nbr : Un nombre quelconque.

    Retourne : La valeur absolue de nbr
    """
    if nbr >= 0:
        return nbr
    nbr = str(nbr)
    if nbr[0] == '-':
        return int(nbr[1:])
    print("Problème avec la conversion... Retourne 0")
    return 0

def first_last_string(target_string: str) -> list:
    """
    Lis et retourne le premier et le dernier caractère d'une
    chaine de caractères.
    LAB_11 -> EX5

    Paramètres :
    - target_string : Chaîne de caractères.

    Retourne : Une liste contenant le premiet et le dernier caractère.
    """
    if len(target_string) < 0:
        print("Chaîne trop courte Retourn une liste avec [0,0]")
        return [0,0]
    return [target_string[0], target_string[-1]]

def sort_highest_lowest(target_lst: list) -> list:
    """
    Lis et retourne deux liste, une contenant les nombres les plus hautes
    et une autre contenant les nombres les plus bas.
    LAB_11 -> EX6

    Paramètres :
    - target_lst : Une liste contenant des nombres réels ou entiers.

    Retourne : Deux listes [highest, lowest].
    """
    # Smallest to highest.
    smallest_lst = []
    while len(target_lst) > 0:
        i = 0
        smallest = [0, HIGHEST]
        for elem in target_lst:
            if elem < smallest[1]:
                smallest = [i, elem]
            i += 1
        smallest_lst.append(smallest[1])
        target_lst.pop(smallest[0])

    # Highest to smallest.
    reversed_lst = smallest_lst.copy()
    reversed_lst.reverse()

    return [reversed_lst, smallest_lst]

def power(base: int, exposant: int) -> int:
    """
    Calcule la puissance entre une base (B) et un exposant.
    LAB_11 -> EX7

    Paramètres :
    - base     : Un nombre positif représentant la base.
    - exposant : Un nombre positif représentant l'exposant.

    Retourne : La puissance des deux nombres positifs.
    """
    if base < 0 and exposant < 0:
        print("La base ou l'exposant n'est pas un nombre positif. Retourne 0")
        return 0
    return base ** exposant
