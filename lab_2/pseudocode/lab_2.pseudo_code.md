# Exercice 1

Énoncé: Écrire un algorithme qui lit deux nombres a et b au clavier et affiche le plus grand des deux. Afficher
un message approprié lorsque l’utilisateur saisit deux nombres égaux.
```
Pseudo-Code

Début
     Variables
     a, b: Réels
    Afficher("Entrez un premier nombre: ")
    Lire(a)
    Afficher("Entrez un deuxième nombre: ")
    Lire(b)
    Si a < b alors
        Afficher("Le plus grand nombre est: ", a)
        Fin
    Fin si
    Si a == b alors
        Afficher("Le premier et deuxième nombre sont pareils.")
        Fin
    Fin si
    Afficher("Le plus grand nomrbe est: ", b)
Fin
```
# Exercice 2

Énoncé: Écrire un programme qui lit deux entiers a et b au clavier et affiche un message indiquant s’ils sont
successifs ou non. On définit deux nombres successifs si leur différence en absolue est égale à 1.
```
Pseudo-Code

Début
     Variables
     a, b: Entiers
    Afficher("Entrez un premier entier: ")
    Lire(a)
    Afficher("Entrez un deuxième entier: ")
    Lire(b)
    Si a + 1 == b alors
        Afficher("Les deux entiers sont successifs.")
        Fin
    Fin si
    Si b + 1 == a alors
        Afficher("Les deux entiers sont successfis.")
    Fin si
Fin
```
# Exercice 3

Énoncé: Écrire un programme qui lit un nombre représentant la vitesse d’un véhicule et affiche à l’écran ce qui
suit :
-  Vitesse correcte si la vitesse est entre 60 et 100
-  Trop lent si la vitesse est inférieure strictement à 60
-  Trop rapide si la vitesse est supérieure strictement à 100
```
Pseudo-Code

Début
     Variables
     vitesse: Réel
    Afficher("Entrez la vitesse du véhicule: ")
    Lire(vitesse)
    Si vitesse > 100 alors
        Afficher("La vitesse du véhicule est trop rapide.")
        Fin
    Fin si
    Si vitesse < 60 alors
        Afficher("La vitesse du véhicule est trop lente.")
        Fin
    Fin si
    Afficher("La vitesse du véhicule est correcte.")
Fin
```
# Exercice 4

Énoncé: Écrire un algorithme qui lit trois nombres A, B, C et qui détermine si l’un est égal à la somme des
deux autres. Si un tel nombre existe, l’afficher sinon afficher aucun nombre des 3 n’est égal à la
somme des autres
```
Pseudo-Code

Début
     Variables
     a,b,c: Réels
    Afficher("Entrez un premier nombre: ")
    Lire(a)
    Afficher("Entrez un deuxième nombre: ")
    Lire(b)
    Afficher("Entrez un troisième nombre: ")
    Lire(c)
    Si b + c == a alors
        Afficher("Le premier nombre est égal à la somme des deux autres nombres.")
    Sinon
        Si a + c == b alors
            Afficher("Le deuxième nombre est égal à la somme des deux autres nombres.")
        Sinon
            Si a + b == c alors
                Afficher("Le troisième nombre est égal à la somme des deux autres nombres.")
            Sinon
                Afficher("Aucun n'est égal à la somme des deux autres nombres.")
            Fin si
        Fin si
    Fin si
Fin
```
# Exercice 5

Énoncé: Écrire un algorithme qui permet de calculer le périmètre ou la surface d’un carré selon le choix donné
par l’utilisateur. Si l’utilisateur tape la lettre P comme choix, vous calculez le périmètre et s’il saisit la
lettre S comme choix, on calcule la surface. Sachant que le périmètre du carré est égal au côté
multiplié par 4 et la surface est égale au côté au carré. Le côté est un entier positif à lire sur l'entrée
standard. Vous devez accepter que des nombres positifs et non nuls.
```
Pseudo-code

Début
     Variables
     cmd: Char
     cote: Réel
    Afficher("Entrez P pour calculer le périmètre d'un carré ou S pour calculer la surface du carré: ")
    Lire(cmd)
    Afficher("Entrez les côté du carré: ")
    Lire cote
    Si cmd == 'P' alors
        Afficher("Le périmètre est de: ", cote * 4)
    Sinon
        Si cmd == 'S' alors
            Afficher("La surface est de: ", cote * cote)
        Sinon
            Afficher("Commande non reconnue.")
        Fin si
    Fin si
Fin
```
# Exercice 6

Énoncé: Écrire un algorithme qui, à partir d’un nombre compris entre 0 et 9 inclusivement, affiche le nombre
en toutes lettres sinon affiche un message approprié.
```
Pseudo-Code

Début
     Variables
     nbr: Entier
    Afficher("Entrez un entier entre 0 et 9: ")
    Lire(nbr)
    0 Afficher("zéro")
    1 Afficher("un")
    2 Afficher("deux")
    3 Afficher("trois")
    4 Afficher("quatre")
    5 Afficher("cinq")
    6 Afficher("six")
    7 Afficher("sept")
    8 Afficher("huit")
    9 Afficher("neuf")
    Afficher("Erreur, nombre n'est pas un entier ou n'est pas entre 0 et 9")
Fin
```
# Exercice 7

Énoncé: Écrire un algorithme qui, à partir d’un nombre compris entre 1 et 7, affiche le jour correspondant (1
pour Lundi, 2 pour Mardi et etc.) sinon affiche non valide.
```
Pseudo-Code

Début
     Variables:
     nbr: Entier
    Afficher("Entrez un entier entre 1 et 7: ")
    Lire(nbr)
    1 Afficher("Lundi")
    2 Afficher("Mardi")
    3 Afficher("Mercredi")
    4 Afficher("Jeudi")
    5 Afficher("Vendredi")
    6 Afficher("Samedi")
    7 Afficher("Dimanche")
    Afficher("Erreur, nombre n'est pas entre 1 et 7")
Fin
```
# Exercice 8

Énoncé: Écrire un algorithme qui lit trois nombres au clavier a, b et c et affiche le plus petit parmi ces trois
nombres.
```
Pseudo-Code

Début
     Variables:
     a,b,c: Réels
    Afficher("Entrez un premier nombre: ")
    Lire(a)
    Afficher("Entrez un deuxième nombre: ")
    Lire(b)
    Afficher("Entrez un troisième nombre: ")
    Lire(c)
    Si a < b alors
        Si a < c alors
            Afficher("Le plus petit nombre est: ", a)
        Fin si
    Fin si
    Si b < a alors
        Si b < c alors
            Afficher("Le plus petit nombre est: ", b)
        Fin si
    Fin si
    Si c < a alors
        Si c < b alors
            Afficher("Le plus petit nombre est: ", a)
        Fin si
    Fin si
    Afficher("Tout les nombres sont égaux.")
Fin
```
