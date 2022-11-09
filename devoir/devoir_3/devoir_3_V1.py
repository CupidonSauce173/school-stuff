'''
Author: Antoine Langevin
Description: Application de gestion de la facturation des commmandes des clients.
'''


'''
Notes

- Lire le nombre de clients par table
- Lire les prix des mets commandés
- Lire le pourboire offert par chacun des clients de la table
- Calculer sa facture détaillée et cela pour chaque client de chacune des tables du restaurant
- Une facture par table (uniquement le montant total payé par tous les clients de chacune des tables)

Informations

- Prix de l'entrée choisie
- Prix du plat principal choisi
- Prix du dessert choisi
- Prix de la boisson choisie
- La taux de taxe applicable
- Le taux du pourboire (taxable)
- Le nombre de client sur une table
- Pourcentage minimum pour pourboire == 10%

Informations à afficher
- Le sous-total (avant taxe & pourboire)
- Montant du pourboire
- Montant de la taxe
- Montant total à payer
- Montant à retourner au client s'il y a lieu

'''
import datetime

# Initialisation des variables de contrôle
status = True # contrôle de la boucle
TAUX_TAXE = 0.15
facture_id = 0
nbre_table = 0

while status:
    NBRE_CLIENTS = int(input('Nombre de client sur la table: '))
    if NBRE_CLIENTS > 0:
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
                if entree < 0 or plat_p < 0 \
                    or dessert < 0 or boisson < 0:
                    print('Informations non valide, recommencez')
                else:
                    not_finished = False
                # Fin si
            # Fin while

            sous_total = round(entree + plat_p + dessert + boisson, 2)
            print(f"Sous-total: {sous_total}$")

            # Init & validation pourboire
            pourboire = int(input("Pourboire (minimum 10%): "))
            if pourboire < 10:
                pourboire = 10
            # Fin si
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
            dateData = datetime.datetime.now()
            print(f"Facture NO:{facture_id}".center(36))
            print('Reçu'.center(36))
            print(
                f"{'Entrée:':<21}{'{0:.2f}'.format(entree):>15}",
                f"\n{'Plat Principal:':<21}{'{0:.2f}'.format(plat_p):>15}",
                f"\n{'Dessert:':<21}{'{0:.2f}'.format(dessert):>15}",
                f"\n{'Boisson:':<21}{'{0:.2f}'.format(boisson):>15}", end='\n\n')
            print(f"{'SOUS-TOTAL':<21}{'{0:.2f}'.format(sous_total):>15}")
            print(
                f"{f' {sous_total} Pourboire({pourboire})%':<21}{'{0:.2f}'.format(prix_pourboire):>15}",
                f"\n{f' {round(sous_total + pourboire, 2)} TAXES({TAUX_TAXE * 100})%':<21}{'{0:.2f}'.format(prix_taxe):>15}"
                f"\n{'TOTAL':<21}{'{0:.2f}'.format(total):>15}",
                f"\n{'PAYÉ':<21}{'-{0:.2f}'.format(payee):>15}"
            )
            if monnaie != 0:
                print(f"\n{'MONNAIE':<21}{'{0:.2f}'.format(monnaie):>15}", end='\n')
            # Fin si
            print("Au plaisir de vous revoir!".center(36), end='\n')
            print('*** COPIE DU CLIENT ***'.center(36))
            print(f"{f'{dateData.day}/{dateData.month}/{dateData.year}':<21}{f'{dateData.hour}:{dateData.minute}':>15}", end='\n\n\n')

            # Incrementation
            total_table += total
            facture_id += 1
        # Fin for
        print(f"TABLES: {nbre_table}")
        print(f"Total: {total_table}$")
        nbre_table += 1
    else:
        print('Information non valide.')
    #Fin si
    status = input('Continuer? y/Y: ') in ['y', 'Y']