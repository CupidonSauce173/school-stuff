'''
Author: Antoine Langevin & Achram Yvan
lastUpdate: 2022-11-16
2022-11-09 -> Création du programme
2022-11-16 ->
- Création variable MIN_POURBOIRE (10).
- Équivalent du tableau d'environnement.
- Création de boucles de prévention de perte de données.
Description: Application de gestion de la facturation des commmandes des clients.
'''
# pylint: disable=C0103
from datetime import datetime

# Initialisation des variables de contrôle
status = True # contrôle de la boucle
TAUX_TAXE = 0.15
MIN_POURBOIRE = 10
facture_id = 0
nbre_table = 0

while status:
    try:
        nbre_clients = int(input('Nombre de client sur la table: '))
    except ValueError:
        print("Nombre de client invalide; entrez un entier positif uniquement.")
    else:
        if nbre_clients < 0:
            print('Information non valide; Entrez un nombre positif.')
        else:
            total_table = 0
            for i in range(nbre_clients):
                print(f"Traitement client: {i}")
                # Init sous_total
                not_finished = True
                while not_finished:
                    try:
                        entree = float(input("Prix de l'entrée: "))
                        plat_p = float(input('Prix du plat principal: '))
                        dessert = float(input('Prix du dessert: '))
                        boisson = float(input('Prix de la boisson: '))
                        if entree < 0 or plat_p < 0 or dessert < 0 or boisson < 0:
                            print('Entrez des prix valide et positif uniquement.')
                        else:
                            not_finished = False
                        # End if
                    except ValueError:
                        print("Entrez des prix valide et positif uniquement.")
                    # End try-except
                # End while

                sous_total = round(entree + plat_p + dessert + boisson, 2)
                print(f"Sous-total: {sous_total}$")

                # Init & validation pourboire
                not_finished = True
                while not_finished:
                    try:
                        pourboire = int(input("Pourboire (minimum 10%): "))
                    except ValueError:
                        print("Valeur invalide; Entrez un entier uniquement.")
                    else:
                        not_finished = False
                    # End try-except
                # End while
                pourboire = max(pourboire, MIN_POURBOIRE)
                # Init total
                prix_pourboire = round((sous_total * pourboire) / 100, 2)
                prix_taxe = round((sous_total + prix_pourboire) * TAUX_TAXE, 2)
                total = round(sous_total + prix_pourboire + prix_taxe, 2)

                # Payage de la facture
                print(f"À payer: {total}")

                payee = float(input('Montant payé par le client: '))
                while payee < total:
                    try:
                        print('Montant trop petit.')
                        payee = float(input('Montant payé par le client: '))
                    except ValueError:
                        print("Montant invalide; Entrez une valeur Float ou Int uniquement.")
                    # End try-except
                # End while
                monnaie = round(total - payee, 2)
                print(f'Monnaie: {monnaie}', end='\n\n')

                # Facture détaillée pour le client
                dateData = datetime.now()
                print(f"Facture NO:{facture_id}".center(37))
                print('Reçu'.center(37))
                print(
                    f"{'Entrée:':<21}{f'{entree:.2f}':>16}",
                    f"\n{'Plat Principal:':<21}{f'{plat_p:.2f}':>16}",
                    f"\n{'Dessert:':<21}{f'{dessert:.2f}':>16}",
                    f"\n{'Boisson:':<21}{f'{boisson:.2f}':>16}", end='\n\n')
                print(f"{'SOUS-TOTAL':<21}{f'{sous_total:.2f}':>16}")
                print(
                    f"{f' {sous_total} Pourboire({pourboire})%':<21}{f'{prix_pourboire:.2f}':>16}",
                    f"\n{f' {round(sous_total + prix_pourboire, 2)} TAXES({TAUX_TAXE * 100})%':<21}{f'{prix_taxe:.2f}':>16}" # pylint: disable=line-too-long
                    f"\n{'TOTAL':<21}{f'{total:.2f}':>16}",
                    f"\n{'PAYÉ':<21}{f'-{payee:.2f}':>16}"
                )
                if monnaie != 0:
                    print(f"\n{'MONNAIE':<21}{f'{monnaie:.2f}':>16}", end='\n')
                # End if
                print('Au plaisir de vous revoir!'.center(37), end='\n')
                print('*** COPIE DU CLIENT ***'.center(37))
                print(f"{f'{dateData.day}/{dateData.month}/{dateData.year}':<21}{f'{dateData.hour}:{dateData.minute}':>16}" # pylint: disable=line-too-long
                    , end='\n\n\n')
                total_table += total
                facture_id += 1
            # End for
            nbre_table += 1
            print(f"TABLES: {nbre_table}")
            print(f"Total: {total_table}$")
        # End if
        status = input('Continuer? y/Y: ') in ['y', 'Y']

    # End try-except
# End while

# pylint: disable=W0105
'''
Note: Les variables pour le prix des items, pourboire, nbre_clients et toutes variables étant dans la boucle principal (status) ne sont pas des constantes.
La valeur des variables change avec le temps (sur une nouvelle table). Uniquement MIN_POURBOIRE et TAUX_TAXE ne changent sous aucun cas.

Description             Nom de la variable  Type     Rôle         Nature
Variable de contrôle    status              booléen  entrée       variable
de la boucle.
Variable de contrôle    not_finished        booléen  calculée     variable
de la boucle. (entrées)
Taux des taxes.         TAUX_TAXE           réel     donnée fixe  constante
Minimum du pourboire.   MIN_POURBOIRE       entier   donnée fixe  constante
Prix de l'entrée.       entree              réel     entrée       variable
Prix du plat principal. plat_p              réel     entrée       variable
Prix du dessert.        dessert             réel     entrée       variable
Prix de la boisson.     boisson             réel     entrée       variable
Prix du pourboire.      prix_pourboire      réel     calculée     variable
Prix de la taxe.        prix_taxe           réel     calculée     variable
Sous total de           sous_total          réel     calculée     variable 
la facture.
Total de la facture.    total               réel     calculée     variable
Montant payé par        payee               réel     entrée       variable
le client.
Monnaie à redonner      monnaie             réel     calculée     variable
au client.
L'ID de la facture.     facture_id          entier   calculée     variable
Le nombre de table      nbre_table          entier   calculée     variable
facturé.
Variable de contrôle    i                   entier   calculée     variable
de la boucle.
Nombre de client sur    nbre_clients        entier   entrée       variable
la table.
Pourcentage du          pourboire           entier   entrée       variable
pourboire donné.
'''