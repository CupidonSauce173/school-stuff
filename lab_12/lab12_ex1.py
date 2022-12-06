"""
Écrire une fonction qui crée une liste des carrées et des cubes de 1 à une limite, un nombre >=
1 donné par l’utilisateur, chaque élément de cette liste est une liste comprenant le carré et le
cube respectivement de 1 à cette limite. La fonction a comme paramètre la limite et retourne la
liste construite. Écrire un programme pour tester votre fonction.
"""

def square_cube_list(limite: int) -> list:
    """
    Créer une liste des carrées et des cubes de 1 à une limite.

    Paramètres :
    - limite : Entier positif limitant la liste.

    Retourne : Une liste avec les carrées et cubes.
    """
    square_cube_lst = []
    for i in range(1, limite + 1):
        square_cube_lst.append([i ** 2, i ** 3])
    return square_cube_lst
