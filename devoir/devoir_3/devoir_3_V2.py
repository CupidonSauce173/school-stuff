''' Antoine Langevin '''
# Initisalisation
TAUX_TAXE = 0.15

class Client:

    prix_plat = 0
    prix_dessert = 0
    prix_entree = 0
    prix_boisson = 0
    pourboire = 10
    sous_total = 0
    prix_total = 0
    taxe = 0

    def validate_informations(self):
        ''' Valider si les informations client sont correct. '''
        try:
            if self.prix_plat < 0 or self.prix_dessert < 0 \
                    or self.prix_entree < 0 or self.prix_boisson < 0 \
                    or self.pourboire < 0:
                return False
            return True
        except ValueError:
            print("La valeur n'est pas un float ou un int.")
            return False

    def calculer_sous_total(self):
        ''' Calculer le sous-total avant pourboire et taxe. '''
        self.sous_total = round(self.prix_plat + self.prix_dessert + \
            self.prix_entree + self.prix_boisson, 2)
        return self.sous_total

    def calculer_total(self):
        ''' Calculer le prix total de la part du client.'''
        if self.pourboire > 10:
            self.prix_total = round(client.sous_total * (client.pourboire / 100), 2) \
                + self.sous_total
        self.taxe = round((self.prix_total * TAUX_TAXE), 2)
        self.prix_total = self.taxe + self.prix_total
        return self.prix_total


continuer = True
table_nbr = 1

while continuer:
    client = Client()
    try:
        # Initialisation des variables de contrôle
        nbr_clients = int(input('Combien de clients sur cette table?: '))
        i = 0
        total_table = 0
        while i < nbr_clients:
            print(f'\n---- Client #{i} ----')
            print('>> Prix Principaux << ')
            client.prix_entree = float(input('Entrée: '))
            client.prix_plat = float(input('Plat Principal: '))
            client.prix_dessert = float(input('Dessert: '))
            client.prix_boisson = float(input('Boisson: '))
            print('>> Autres Charges << ')
            client.pourboire = int(input('Pourboire en %: '))

            # Traîtement de la facture
            if not client.validate_informations():
                continue

            sous_total = client.calculer_sous_total()
            total = client.calculer_total()

            # Paiement de la facture
            print('Total:', total)
            montant_paye = float(input('Montant payé par le client: '))
            while montant_paye < total:
                print(f'Montant Restant ({total - montant_paye})')
                montant_paye += float(input('Entrer un montant: '))

            # Affichage de la facture
            print('\n---- Reçu ----')
            print('Sous-total:', sous_total)
            print(f'Pourboire ({client.pourboire}%):', \
                round(client.sous_total * (client.pourboire / 100), 2))
            print('Taxe:', client.taxe)
            print('Montant total:', total)
            print('Monnaie:', round(total - montant_paye, 2))
            total_table += client.prix_total
            i += 1
        print(f'\n\n---- Table #{table_nbr} ----')
        print(total_table)
        print('Total payé:', total)

    except ValueError:
        print('Rentrer des informations valide.')
    else:
        continuer = input('Continuer? n/N pour sortir: ') not in ('n','N')
