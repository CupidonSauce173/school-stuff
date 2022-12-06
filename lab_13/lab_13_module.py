"""
Author : Antoine Langevin
Module ayant plusieurs functions pour créer des tables de multiplications.
"""

def multiplication_table_hardcoded() -> None:
    """
    Affiche une table de muiltiplication pour 7, sur 12 étages.
    EX1
    """

    for i in range(12):
        print(f"7 * {i + 1} = {(i + 1) * 7}")
    # end for

def multiplication_table(base: int) -> None:
    """
    Affiche une table de multiplication selon la base donnée, sur 12 étages.
    EX2

    Paramètres :
    - base : Le nombre à multiplier.

    Retourne : None
    """
    for i in range(12):
        print(f"{base} * {i + 1} = {(i + 1) * base}")
    # end for

def multiplication_table_limite(base: int, limite: int) -> None:
    """
    Affiche une table de multiplication selon la base donnée,
    avec une limite donnée.
    EX3

    Paramètres :
    - base   : Le nombre à multiplier.
    - limite : Le nombre d'étages limite pour la base.

    Retourne : None
    """
    for i in range(limite):
        print(f"{base} * {i + 1} = {(i + 1) * base}")
    # end for

def multiplication_table_custom(base: int, start: int, end: int) -> None:
    """
    Affiche une table de multiplication selon la base donnée avec
    l'étage du début et de fin.
    EX4

    Paramètres :
    - base  : Le nombe à multiplier.
    - start : L'étage du début.
    - end   : L'étage de fin.

    Retourne : None
    """
    for i in range(start - 1, end):
        print(f"{base} * {i + 1} = {(i + 1) * base}")
    # end for

def multiplication_table_custom_ref(base: int, start: int = 1, end: int = 12) -> None:
    """
    Affiche une table de multiplication selon la base donnée avec
    l'étage du début et de fin, avec paramètres non obligatoires.
    EX5

    Paramètres :
    - base  : Le nombe à multiplier.
    - start : L'étage du début.      (optional)
    - end   : L'étage de fin.        (optional)

    Retourne : None
    """
    for i in range(start - 1, end):
        print(f"{base} * {i + 1} = {(i + 1) * base}")
    # end for
