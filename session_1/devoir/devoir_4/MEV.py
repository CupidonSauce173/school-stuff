"""
-----------------------------------------------------------------------------------------------
#
# Programme	: Menu.py
# Auteur 	: Antoine Langevin
# Date de dernière modification : D2022

# Objectif :
#   Execute le MEV.
#   --> Afficher le menu avec le module Menu.py
#   --> Prend le nom et prénom du client.
#   --> Selectionne la bonne fonctionnalité selon le choix de l'utilisateur.

#
--------------------------------------------------------------------------------------------------
"""

import Menu
# ------------------------------------------------------------------------------------------------

########################################
#### PARTIE PRINCIPALE DU PROGRAMME ####
############ Devoir 4 (MEV) ############
########################################

KEEP_RUNNING = True # Variable de contrôle de la boucle.

print("*** Informations Client ***")
nom = input("Nom: ")
prenom = input("Prénom: ")
lst_articles = []

while any(char.isdigit() for char in nom) or any(char.isdigit() for char in prenom):
    print("Informations incorrectes. Uniquement des charactères sont autorisés.")
    nom = input("Nom: ")
    prenom = input("Prénom: ")

nom = nom.capitalize()
prenom = prenom.capitalize()


while KEEP_RUNNING:
    choice = Menu.menu_selection_page()
    if choice == 1:
        Menu.afficher_facture(lst_articles, nom, prenom)
    elif choice == 2:
        Menu.ajouter_article(lst_articles)
    elif choice == 3:
        Menu.delete_article(lst_articles)
    elif choice == 4:
        Menu.edit_article_quantity(lst_articles)
    elif choice == 5:
        Menu.order_lst_articles(lst_articles)
    elif choice == 6:
        quantite_max = Menu.quantite_maximale(lst_articles)
        print(f"Plus haute quantité: {quantite_max}")
        for elem in lst_articles:
            if elem[3] == quantite_max:
                print(f"Article {elem[0]} {elem[1]}")
    elif choice == 7:
        quantite_min = Menu.quantite_minimale(lst_articles)
        print(f"Plus basse quantité: {quantite_min}")
        for elem in lst_articles:
            if elem[3] == quantite_min:
                print(f"Article {elem[0]} {elem[1]}")
    elif choice == 8:
        Menu.afficher_sommaire(lst_articles)
    elif choice == 9:
        KEEP_RUNNING = False
    # end if
# end while
# ------------------------------------------------------------------------------------------------
