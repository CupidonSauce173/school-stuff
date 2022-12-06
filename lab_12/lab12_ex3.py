"""
Module contenant l'exercice 3 du labo 12.
"""

def count_remove_doubles(base_lst: list) -> list:
    """
    Lis, compte et retire les doublons dans une liste

    Paramètres :
    - base_lst : Liste de base

    Retourne : Une liste contenant la nouvelle liste sans doublon [0] et
    le nombre de doublons trouvés [1]
    """

    filtered_lst = []
    occurences = 0
    for elem in base_lst:
        if filtered_lst.count(elem) == 0:
            filtered_lst.append(elem)
        else:
            occurences += 1
        # end if
    # end for
    return [filtered_lst, occurences]
