'''
Author: Antoine Langevin 
Last Update: 2022-11-09

Description: Programme calculant le coût total par client d'un séjour à un restaurant,
calcule le total de la table et affiche le total quand tout les clients ont payés.


Les méthodes dans la classe Client ont leur propre exception handler pour recommencer à 
taper le moins possible des informations en double. 
'''

# Début
# Initisalisation des variables globales
TAUX_TAXE = 0.15

#region class-client
class Client:
    ''' Classe qui forme le client sur une table.'''
    prix_plat = 0
    prix_dessert = 0
    prix_entree = 0
    prix_boisson = 0
    pourboire = 10
    sous_total = 0
    prix_total = 0
    taxe = 0

    def init_prix(self) -> None:
        ''' Initisaliser les prix des plats. '''
        status = True
        while status:
            try:
                print('>> Prix Principaux << ')
                self.prix_entree = float(input('Entrée: '))
                self.prix_plat = float(input('Plat Principal: '))
                self.prix_dessert = float(input('Dessert: '))
                self.prix_boisson = float(input('Boisson: '))
                print('>> Autres Charges << ')
                self.pourboire = int(input('Pourboire en %: '))
            except ValueError:
                print('Prix incorrect(s).')
            else:
                status = False
        # Fin while

    def validate_informations(self) -> bool:
        ''' Valider si les informations client sont correct. '''
        passed = True
        try:
            if self.prix_plat < 0 or self.prix_dessert < 0 \
                    or self.prix_entree < 0 or self.prix_boisson < 0 \
                    or self.pourboire < 0:
                passed = False
            # Fin si
        except ValueError:
            print("La valeur n'est pas valide.")
            passed = False
        finally:
            if not passed:
                if input("Les prix n'ont pas pu être validés, \
                    voulez-vous refaire les prix? y/Y pour continuer: ") in ['y', 'Y']:
                    self.init_prix()
                    self.validate_informations()
        return passed

    def calculer_sous_total(self) -> float:
        ''' Calculer le sous-total avant pourboire et taxe. '''
        self.sous_total = round(self.prix_plat + self.prix_dessert + \
            self.prix_entree + self.prix_boisson, 2)
        return self.sous_total

    def calculer_total(self) -> float:
        ''' Calculer le prix total de la part du client.'''
        if self.pourboire > 10:
            self.prix_total = self.sous_total * (self.pourboire / 100) \
                + self.sous_total
        # Fin si
        self.taxe = (self.prix_total * TAUX_TAXE)
        self.prix_total = self.taxe + self.prix_total
        return round(self.prix_total, 2)
    
    def payage(self, total: int) -> float:
        ''' Payer le montant de la facture'''
        status = True
        while status:
            try:
                montant_paye = float(input('Montant payé par le client: '))
                while montant_paye < total:
                    print(f'Montant Restant ({round(total - montant_paye, 2)})')
                    montant_paye += float(input('Entrer un montant: '))
                # Fin while
            except ValueError:
                print('Montant incorrect.')
            else:
                status = False
        # Fin while
        return round(montant_paye, 2)
#endregion class-client

#region main-script
continuer = True
table_nbr = 1
while continuer:
    client = Client()
    try:
        # Initialisation des variables de contrôle
        total_table = 0
        for i in range(int(input('Combien de clients sur cette table?: '))):
            print(f'\n---- Client #{i} ----')
            client.init_prix()
            # Traîtement de la facture
            if not client.validate_informations():
                continue
            # Fin si
            # Init sous_total (sans taxe) && total (avec taxe & pourboire)
            sous_total = client.calculer_sous_total()
            total = client.calculer_total()

            # Paiement de la facture
            print('Total:', total)
            montant_paye = client.payage(total)

            # Affichage de la facture
            print('\n---- Reçu ----')
            print(f"Sous-total:    {'{0:.2f}'.format(sous_total)}$")
            print(f"Pourboire:     {'{0:.2f}'.format(client.sous_total * (client.pourboire / 100))}$")
            print(f"Taxe:          {'{0:.2f}'.format(client.taxe)}$")
            print(f"Montant Total: {'{0:.2f}'.format(total)}$")
            print(f"Monnaie:      {'{0:.2f}'.format(round(total - montant_paye, 2))}$")

            # Incrementation du total de la table et de la variable de contrôle.
            total_table += client.prix_total
            i += 1
        # Fin for
        print(f'\n\n---- Table #{table_nbr} ----')
        print(f"Total payé: {'{0:.2f}'.format(total_table)}")
    except ValueError:
        print('Rentrez des informations valides.')
    else:
        continuer = input('Continuer? n/N pour sortir: ') not in ('n','N')
# Fin while
# Fin
#endregion main-script
