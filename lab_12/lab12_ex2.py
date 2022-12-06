"""
Module contenant l'exercice 2 du labo 12.
"""

def get_sub_list(base_lst: list, index: int) -> list:
    """
    Lis et trouve la sous-liste dans une liste fournie.

    Paramètres :
    base_lst : Une liste de base, la liste target.
    index    : L'indice de la sous-liste dans la liste de base.

    Retourne : La sous-liste de la base ou un message d'erreur avec une liste vide.
    """
    try:
        return base_lst[index]
    except IndexError:
        print("Indice trop grand pour la liste de base, retourne liste vide.")
    return []
