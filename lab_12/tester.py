"""
Module contenant les tests pour les exercices du laboratoire 12.
"""

# pylint:disable=no-member
import lab12_ex1 as ex1
import lab12_ex2 as ex2
import lab12_ex3 as ex3
import Valider_Nombre_A22 as nbr_input

limite = nbr_input.saisir_entier_mini("Entrez une limite: ", 0)
data = ex2.get_sub_list(
    ex1.square_cube_list(limite),
    nbr_input.saisir_entier_mini_maxi("Indice: ", 0, limite)
    )
print(data)

result = ex3.count_remove_doubles([9, 9, 12, 1, 2, 2, 3, 4, 5, 3, 1, 6, 2, 7, 2, 0, 0])
print(f"Doublons: {result[1]} Nouvelle liste: {result[0]}")
