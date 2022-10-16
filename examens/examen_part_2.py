''' Programme pour calculer le coût total d'un séjour selon des forfaits et nombres de personnes. '''


# VERSION 1, BONUS 1

'''
Dans cette version, le programme va arrêter de 
s'executer si l'utilisateur rentrer des données invalides.
'''

# ---- Variables
# ---- personnes, sejour_dure: Entiers
# ---- cout_total, COUT_2_JOURS, COUT_3_JOURS, COUT_ACCOMP, RABAIS: Réels

print("* ---------------------------------------------- *")
print("* Calculer le coût total d'un séjour - VERSION 1 *")
print("* ---------------------------------------------- *")

# ---- Initialisation des constantes
COUT_2_JOURS = 160
COUT_3_JOURS = 230
COUT_ACCOMP = 7
RABAIS = 0.1

# ---- Entrée des données
personnes = int(input("Entrez le nombres de personnes dans le groupe: "))
sejour_dure = int(input('Entrez le nombre de jours de votre séjour (2 ou 3 jours): '))


# ---- Traitements

# Pour note, le \ permet de continuer la ligne de code sur une autre ligne.
if sejour_dure == 2:
    cout_total = (COUT_2_JOURS * personnes) + \
                 (COUT_ACCOMP * personnes) + \
                 (100 * personnes)
elif sejour_dure == 3:
    cout_total = (COUT_3_JOURS * personnes) + \
                 (COUT_ACCOMP * personnes) + \
                 (100 * personnes)

# le in (x,y,...) permet de regarder si la variable se trouve dans une liste, genre sejour_dure = 3, est-ce que c'est dans 2 ou 
# Ça permet de simplifier la comparaison if sejour_dure == 2 or sejour_dure == 3 
if sejour_dure in (2,3):
    if personnes > 5:
        cout_total = cout_total - (cout_total * RABAIS)
        print('Vous avez un rabais de 10%!')
    # print(f''),  le f permet de rajouter des variables entre les {}.
    # \n permet de sauter une ligne dans l'écrant.
    print(f'Le prix total du séjour va être de {cout_total}$ \n')
else:
    print('Choisissez un fortais entre 2 et 3 jours.')

input("Cliquez sur une touche pour continuer...")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# --------------------------------------------------------------------------

# VERSION 2, BONUS 1

'''
Dans cette version, le programme va attendre que 
l'utilisateur rentre des données valide pour rentrer dans la section de traitements.
'''

# ---- Variables
# ---- personnes, sejour_dure: Entiers
# ---- cout_total, COUT_2_JOURS, COUT_3_JOURS, COUT_ACCOMP, RABAIS: Réels

print("* ---------------------------------------------- *")
print("* Calculer le coût total d'un séjour VERSION - 2 *")
print("* ---------------------------------------------- *")

# ---- Initialisation des constantes
COUT_2_JOURS = 160
COUT_3_JOURS = 230
COUT_ACCOMP = 7
RABAIS = 0.1

# ---- Entrée des données
continuer = True

# On rentre dans une boucle qui va essayer la saisie de données, continuer est True et la boucle va continuer
# jusqu'à se que continuer devient False.
while continuer:
    # try va essayer un bloc de code et executer du code si une erreur occure.
    try:
        personnes = int(input("Entrez le nombres de personnes dans le groupe: "))
        sejour_dure = int(input('Entrez le nombre de jours de votre séjour (2 ou 3 jours): '))
    # except va catch les erreurs, ValueError est une erreur de quand l'utilisateur
    # essaie de rentrer "F" au lieu d'un int (dans le input)
    except ValueError:
        # Si ValueError est appelé, le code va executer ce code.
        print('Entrez des nombres entiers, pas des lettre ou charactères spéciaux.')
    else:
        # Si il n'y a aucune erreur, le programme va executer ce code.
        # Si sejour_dure est 2 ou 3, le code va assigner continuer à False.
        if sejour_dure in (2,3):
            # On assigne continuer à False pour que le while se termine.
            continuer = False
        else:
            # Sinon, on print un message et la boucle va continuer.
            print('Choisissez un fortais entre 2 et 3 jours.')

# ---- Traitements
if sejour_dure == 2:
    cout_total = (COUT_2_JOURS * personnes) + \
                 (COUT_ACCOMP * personnes) + \
                 (100 * personnes)
else:
    cout_total = (COUT_3_JOURS * personnes) + \
                 (COUT_ACCOMP * personnes) + \
                 (100 * personnes)

if personnes > 5:
    cout_total = cout_total - (cout_total * RABAIS)
    print('Vous avez un rabais de 10%!')
print(f'Le prix total du séjour va être de {cout_total}$ \n')

input("Cliquez sur une touche pour continuer...")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# --------------------------------------------------------------------------

# VERSION 1, BONUS 2

'''
Dans cette version, le programme va arrêter de 
s'executer si l'utilisateur rentrer des données invalides
et calculer le coût total pour chaque groupes.
'''

# ---- Variables
# ---- personnes, sejour_dure: Entiers
# ---- cout_total, COUT_2_JOURS, COUT_3_JOURS, COUT_ACCOMP, RABAIS: Réels

print("* ---------------------------------------------- *")
print("* Calculer le coût total d'un séjour (Multiple groupes) - VERSION 1 *")
print("* ---------------------------------------------- *")

# ---- Initialisation des constantes
COUT_2_JOURS = 160
COUT_3_JOURS = 230
COUT_ACCOMP = 7
RABAIS = 0.1
cout_total_groupes = 0

# ---- Entrée des données
groupes = int(input("Entrez le nombres de groupes à traiter: "))
i = 0
while i < groupes:
    personnes = int(input(f"Entrez le nombres de personnes dans le groupe {i + 1}: "))
    sejour_dure = int(input(f'Entrez le nombre de jours du séjour pour le groupe {i + 1} (2 ou 3 jours): '))
    # ---- Traitements
    if sejour_dure == 2:
        cout_total = (COUT_2_JOURS * personnes) + \
                     (COUT_ACCOMP * personnes) + \
                     (100 * personnes)
    elif sejour_dure == 3:
        cout_total = (COUT_3_JOURS * personnes) + \
                     (COUT_ACCOMP * personnes) + \
                     (100 * personnes)
    if sejour_dure in (2,3):
        if personnes > 5:
            cout_total = cout_total - (cout_total * RABAIS)
            print('Vous avez un rabais de 10%!')
        cout_total_groupes += cout_total
        print(f'Le prix total du séjour va être de {cout_total}$')
    else:
        print('Choisissez un fortais entre 2 et 3 jours.')
    i += 1
print(f"Le coût total pour tous les groupes va être de {cout_total_groupes}$ \n")

input("Cliquez sur une touche pour continuer...")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
# --------------------------------------------------------------------------

# VERSION 2, BONUS 2

'''
Dans cette version, le programme va attendre que 
l'utilisateur rentre des données valide pour rentrer dans la section de traitements
et va traiter un nombre x de groupes.
'''

# ---- Variables
# ---- personnes, sejour_dure: Entiers
# ---- cout_total, COUT_2_JOURS, COUT_3_JOURS, COUT_ACCOMP, RABAIS: Réels

print("* ---------------------------------------------- *")
print("* Calculer le coût total d'un séjour (Multiple groupes) - VERSION 2 *")
print("* ---------------------------------------------- *")

# ---- Initialisation des constantes
COUT_2_JOURS = 160
COUT_3_JOURS = 230
COUT_ACCOMP = 7
RABAIS = 0.1
cout_total_groupes = 0

# ---- Entrée des données
groupes = int(input("Entrez le nombres de groupes à traiter: "))
i = 0
while i < groupes:
    continuer = True
    while continuer:
        try:
            personnes = int(input(f"Entrez le nombres de personnes dans le groupe {i + 1}: "))
            sejour_dure = int(input(f'Entrez le nombre de jours du séjour pour le groupe {i + 1} (2 ou 3 jours): '))
        except ValueError:
            print('Entrez des nombres entiers, pas des lettre ou charactères spéciaux.')
        else:
            if sejour_dure in (2,3):
                continuer = False
            else:
                print('Choisissez un fortais entre 2 et 3 jours.')
    # ---- Traitements
    if sejour_dure == 2:
        cout_total = (COUT_2_JOURS * personnes) + \
                     (COUT_ACCOMP * personnes) + \
                     (100 * personnes)
    elif sejour_dure == 3:
        cout_total = (COUT_3_JOURS * personnes) + \
                     (COUT_ACCOMP * personnes) + \
                     (100 * personnes)
    if sejour_dure in (2,3):
        if personnes > 5:
            cout_total = cout_total - (cout_total * RABAIS)
            print('Vous avez un rabais de 10%!')
        cout_total_groupes += cout_total
        print(f'Le prix total du séjour va être de {cout_total}$')
    else:
        print('Choisissez un fortais entre 2 et 3 jours.')
    i += 1
print(f"Le coût total pour tous les groupes va être de {cout_total_groupes}$")
