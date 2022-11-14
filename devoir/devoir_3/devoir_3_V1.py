'''
Author: Antoine Langevin
lastUpdate: 2022-11-09
Description: Application de gestion de la facturation des commmandes des clients.
'''
# pylint: disable=C0103
from datetime import datetime

# Initialisation des variables de contrôle
status = True # contrôle de la boucle
TAUX_TAXE = 0.15
facture_id = 0
nbre_table = 0

while status:
    NBRE_CLIENTS = int(input('Nombre de client sur la table: '))
    if NBRE_CLIENTS < 0:
        print('Information non valide; Entrez un nombre positif.')
    else:
        total_table = 0
        for i in range(NBRE_CLIENTS):
            print(f"Traitement client: {i}")
            # Init sous_total
            not_finished = True
            while not_finished:
                entree = float(input("Prix de l'entrée: "))
                plat_p = float(input('Prix du plat principal: '))
                dessert = float(input('Prix du dessert: '))
                boisson = float(input('Prix de la boisson: '))
                if entree < 0 or plat_p < 0 or dessert < 0 or boisson < 0:
                    print('Informations non valide, recommencez')
                else:
                    not_finished = False
                # Fin si
            # Fin while

            sous_total = round(entree + plat_p + dessert + boisson, 2)
            print(f"Sous-total: {sous_total}$")

            # Init & validation pourboire
            pourboire = int(input("Pourboire (minimum 10%): "))
            pourboire = max(pourboire, 10)
            # Init total
            prix_pourboire = round((sous_total * pourboire) / 100, 2)
            prix_taxe = round((sous_total + prix_pourboire) * TAUX_TAXE, 2)
            total = sous_total + prix_pourboire + prix_taxe

            # Payage de la facture
            print(f"À payer: {total}")
            payee = float(input('Montant payé par le client: '))
            while payee < total:
                print('Montant trop petit.')
                payee = float(input('Montant payé par le client: '))
            # Fin while
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
            # Fin si
            print('Au plaisir de vous revoir!'.center(37), end='\n')
            print('*** COPIE DU CLIENT ***'.center(37))
            print(f"{f'{dateData.day}/{dateData.month}/{dateData.year}':<21}{f'{dateData.hour}:{dateData.minute}':>16}" # pylint: disable=line-too-long
                , end='\n\n\n')
            total_table += total
            facture_id += 1
        # Fin for
        nbre_table += 1
        print(f"TABLES: {nbre_table}")
        print(f"Total: {total_table}$")
    #Fin si
    status = input('Continuer? y/Y: ') in ['y', 'Y']
