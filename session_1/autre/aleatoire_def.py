from random import randint
from random import shuffle


cartes_org = [1,2,3,4,5,6,7,8,9]

def retirer_carte(index: int, cartes: list) -> list:
    ''' Retire une carte des cartes '''
    cartes.pop(index)

def brasser_cartes(cartes: list) -> None:
    ''' Brasse les cartes aléatoirement '''
    return shuffle(cartes)

def former_equipe(carte_1: int, carte_2: int) -> list:
    ''' Retourne une liste de deux personnes '''
    return []

def aleatoire(nbre_cartes: int) -> int:
    ''' Returne un entier aléatoire entre 0 et nbre_cartes '''
    return randint(0, nbre_cartes - 1)
