

## Pseudo-Code & Analyse

## Analyse

Données:
- % des rabais.
- Montant de l'achat.
- % des taxes.

Sorties:
- Message du Montant Achat.
- Message du Montant Rabais.
- Message du Montant des taxes.
- Message du Montant Total.

Variables
##################################################################################
# Nom Variable___#_Description_______________________# Type_#_Variable/Constante #
# TAUX_TAXE      | taux de taxe                      | Réel | Constante          #
# montant_achat  | montant du client                 | Réel | Variable           #
# montant_rabais | montant du rabais                 | Réel | Variable           #
# montant_total  | montant après taxe et rabais      | Réel | Variable           #
# reponse        | Variable de contrôle de continuer | Char | Variable           #
# continuer      | Variable de contrôle de boucle    | Bool | Variable           #
##################################################################################

## Pseudo-Code

Début
     Variables
     TAUX_TAXE, montant, montant_rabais, montant_total, montant_taxe: Réels
     reponse: Char
     continuer: Bool

    TAUX_TAXE <--- 0.15

    Tant que continuer == True alors
        montant_rabais <--- 0
        Afficher("Entrez le montant de l'achat du client: ")
        Lire(montant)
        Si montant >= 100 et montant <= 250 alors
            montant_rabais <--- montant * 0.05
        Fin Si
        Si montant > 250 et montant <= 500 alors
            montant_rabais <--- montant * 0.1
        Fin Si
        Si montant > 500 alors
            montant_rabais <--- montant * 0.2
        Fin Si
        montant_taxe <--- (montant - montant_rabais) * TAUX_TAXE
        montant_total <--- (montant - montant_rabais) + montant_taxe

        Afficher("Montant de l'achat: ", montant)
        Afficher("Rabais de l'achat: -", montant_rabais)
        Afficher("Taxes:              ", montant_taxe)
        Afficher("Montant total:      ", montant_total)

        Afficher("Continuer? n/N pour sortir: ")
        Lire(reponse)
        Si reponse == 'n' ou reponse == 'N' alors
            continuer <--- False
        Fin Si
    Fin tant que
    Afficher("Sortie du programme.....")
Fin