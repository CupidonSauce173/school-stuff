'''
Écrire un algorithme qui permet de déterminer le montant à payer pour une clôture
en métal à placer tout autour d’un terrain rectangulaire
 '''

 # ---- Variables
 # ---- longueur, largeur, perimetre, prix, cout : réels
 # ---- limite_1, limite_2, limite_3 : réels
 # ---- rabais_1, rabais_2, rabais_3 : réels
 # ---- continuer : bool

print("* ------------------------------------- *")
print("* Calcul du coût de la clôture en métal *")
print("* ------------------------------------- *")

# ---- Saisie et initialisations des données
prix = 50
limite_1 = 1000
limite_2 = 2000
limite_3 = 7000
rabais_1 = 5
rabais_2 = 10
rabais_3 = 15

# ---- Boucle pour l'entrer de données.
continuer = True
while continuer:
    try:
        longueur = float(input("Saisir la longueur du rectangle: "))
        largeur = float(input("Saisir la largeur du rectangle: "))
    except ValueError:
        print("Rentrez des nombres, pas des lettres ou des charactères spéciaux.")
    else:
        continuer = False

# ---- Traitements
perimetre = 2 * (largeur + longueur)
cout = perimetre * prix

if cout > limite_3:
    cout = cout - cout * (rabais_3 / 100)
elif cout > limite_2:
    cout = cout - cout * (rabais_2 / 100)
elif cout > limite_1:
    cout = cout - cout * (rabais_1 / 100)
print(f"Le coût de la clôture en métal est de {cout}$")
