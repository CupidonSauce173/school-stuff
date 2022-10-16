''' Author: Antoine Langevin Date: 2022-10-12, Update: 2022-10-12. 
 Programme pour calculer le montant total à payer pour des clients. '''

# ---- Variables
# ---- montant_achat, montant_taxe, montant_rabais, montant_total, TAUX_TAXE: Réels
# ---- continuer: Bool
# ---- montant_achat: Str

print("* ----- Calculer Le Coût Total À Payer Pour Des Clients ----- *")
print("\n")

# Initialisation
TAUX_TAXE = 0.15
continuer = True

# Traitement
while continuer:
    montant_rabais = 0
    rabais_type = "00%"
    try:
        montant_achat = float(input("Entrez le montant de l'achat du client: "))
    except ValueError:
        print("Entrez un nombre, pas des charactères spéciaux ou des lettres.")
    else:
        if 250 >= montant_achat >= 100:
            montant_rabais = montant_achat * 0.05
            rabais_type = "05%"
        elif 500 >= montant_achat > 250:
            montant_rabais = montant_achat * 0.1
            rabais_type = "10%"
        elif montant_achat > 500:
            rabais_type = "20%"
            montant_rabais = montant_achat * 0.2
        
        montant_taxes = (montant_achat - montant_rabais) * TAUX_TAXE
        montant_total = (montant_achat - montant_rabais) + montant_taxes

        # Donner un bon format aux valeurs. N'est pas nécessaire au programme, uniquement pour du visuel.
        montant_achat = "{:.2f}".format(montant_achat)
        montant_rabais = "{:.2f}".format(montant_rabais)
        montant_taxes = "{:.2f}".format(montant_taxes)
        montant_total = "{:.2f}".format(montant_total)

        # Afficher le reçu.
        print("\n")
        print("* ----- Reçu client ----- *")
        print(f"* Montant Achat:    {montant_achat}$")
        print(f"* Économies ({rabais_type}):  -{montant_rabais}$")
        print(f"* Taxes (15%):       {montant_taxes}$")
        print(f"* Montant total:    {montant_total}$")
        print("* ------------------------*")
        print("\n")

        if input("Continuer? n/N pour sortir: ") in ('n','N'):
            continuer = False
            print("Sortie du programme...")