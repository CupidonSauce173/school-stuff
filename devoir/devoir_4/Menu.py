"""
-----------------------------------------------------------------------------------------------
#
# Programme	: Menu.py
# Auteur 	: Antoine Langevin
# Date de dernière modification : D2022

# Objectif :
#   Offre différentes fonctionnalités pour le menu du MEV.
#   --> Savoir si une lst_articles est vide.
#   --> Chercher un article dans la lst_articles.
#   --> Ajouter un article dans la lst_articles.
#   --> Afficher la facture.
#   --> Afficher un sommaire de la facture.
#   --> Calculer l'item ayant la plus grande quantité
#   --> Calculer l'item ayant la plus faible quantité
#   --> Afficher le menu principal.
#   --> Retirer un article de la lst_articles.
#   --> Créer un nouvel article (list).
#   --> Modifier la quantité acheté d'un article.
#   --> Trier la lst_articles par ID d'article en ordre croissant.

#
--------------------------------------------------------------------------------------------------
"""
#pylint:disable=line-too-long
import sys
import Valider_Nombre_A22 as saisir_func

HIGHEST_INT = sys.maxsize
TAUX_TPS    = 0.05
TAUX_TVQ    = 0.09975

#...........................................................................................................................
def is_empty(lst_articles: list) -> bool:
    """
    Lis la liste des articles et calcule si elle est vide.

    Paramètres :
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : True si elle est vide et False si elle n'ai pas vide.
    """

    if len(lst_articles) <= 0:
        return True
    # end if
    return False

#...........................................................................................................................
def chercher_article(lst_articles: list, target_id: int) -> int:
    """
    Recherche un article dans la liste d'articles donné et retourne
    son id si il est déjà dans la liste.

    Paramètres :
    lst_articles : Liste actuelle des articles de la facture.
    target_id     : L'indice (Id) de l'article à chercher dans la liste "articles".

    Retourne : L'indice (Id) de l'article s'il est trouvé dans la liste.
    """
    for article in lst_articles:
        if article[0] == target_id:
            return target_id
        # end if
    # end for
    return -1

#...........................................................................................................................
def ajouter_article(lst_articles: list) -> None:
    """
    Ajoute un article dans la liste d'articles fournie, utilisant
    la méthode 'chercher_article()' pour vérifier si l'article n'est
    pas déjà dans la liste.

    Paramètres :
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : None
    """
    new_article_id = saisir_func.saisir_entier_mini("Id: ", 0)
    if chercher_article(lst_articles, new_article_id) == -1:
        lst_articles.append(create_new_article(new_article_id))
    else:
        print(f"L'article {new_article_id} est déjà dans la liste.")
    # end if

#...........................................................................................................................
def afficher_facture(lst_articles: list, nom: str, prenom: str) -> None:
    """
    Afficher la facture comportant le nom et prénom du client,
    le nombre d'articles achetés, le montant total hors taxe de
    la facture de ce client, le montant total de la TPS et de la TVQ
    (séparé) et montant total toutes taxes comprises de la facture.

    Paramètres :
    lst_articles : Liste actuelle des articles de la facture.
    nom          : Le nom du client.
    prenom       : Le prénom du client.

    Retourne : None
    """
    print("Facture")
    print(f"Nom: {nom} Prénom: {prenom}")
    # Pré-traitements
    nbre_articles = 0
    prix_hors_taxes = 0
    prix_total = 0
    total_tps = 0
    total_tvq = 0
    # [id, nom, prix u, quantité]
    print("-------------------")
    for elem in lst_articles:
        montant_hors_taxes = round(elem[2] * elem[3], 2)
        prix_tps = round(montant_hors_taxes * TAUX_TPS, 2)
        prix_tvq = round(montant_hors_taxes * TAUX_TVQ, 2)
        total_article = round(montant_hors_taxes + prix_tps + prix_tvq, 2)
        nbre_articles += elem[3]
        prix_hors_taxes += montant_hors_taxes
        prix_total += total_article
        total_tps += prix_tps
        total_tvq += prix_tvq

        print(f"Article {elem[0]}")
        print(f"Prix unitaire: {elem[2]}$")
        print(f"Désignation: {elem[1]}")
        print(f"Quantité: {elem[3]}")
        print(f"Montant Hors Taxes: {montant_hors_taxes}$")
        print(f"TPS: {prix_tps}$")
        print(f"TVQ: {prix_tvq}$")
        print(f"Prix Total: {total_article}$")
        print("-------------------")
    # end for
    print(f"Nombre d'articles achetés: {nbre_articles}")
    print(f"Montant Sans Taxes: {prix_hors_taxes}$")
    print(f"TPS: {total_tps}$")
    print(f"TVQ: {total_tvq}$")
    print(f"Montant Avec TTC: {prix_total}$")

#...........................................................................................................................
def afficher_sommaire(lst_articles: list) -> None:
    """
    Affiche le sommaire des articles achetés par le client avec
    un simple print(). Si la liste est vide, un message indiquant
    qu'il n'y a aucun article va être affiché.

    Paramètres:
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : None
    """
    if len(lst_articles) == 0:
        print("La liste des articles est vide.")
        return None
    # end if
    print(lst_articles)
    return None
#...........................................................................................................................
def quantite_maximale(lst_articles: list) -> int:
    """
    Lit et retourne l'article le plus acheté dans la facture
    du client avec la liste des articles.

    Paramètres :
    lst_articles: Liste actuelle des articles de la facture.

    Retourne : La quantité la plus haute dans la liste d'articles fournie.
    """
    if len(lst_articles) == 0:
        print("La liste est vide.")
        return 0
    # end if
    current_highest = 0
    for article in lst_articles:
        if article[3] > current_highest:
            current_highest = article[3]
        # end if
    # end for
    return current_highest

#...........................................................................................................................
def quantite_minimale(lst_articles: list) -> int:
    """
    Lit et retourne l'article le moins acheté dans la facture
    du client avec la liste des articles.

    Paramètres :
    lst_articles: Liste actuelle des articles de la facture.

    Retourne : La quantité la plus basse dans la liste d'articles fournie.
    """

    if len(lst_articles) == 0:
        print("La liste est vide.")
        return 0
    # end if
    current_smallest = HIGHEST_INT
    for article in lst_articles:
        if article[3] < current_smallest:
            current_smallest = article[3]
        # end if
    # end for
    return current_smallest

#...........................................................................................................................
def menu_selection_page() -> int:
    """
    Afficher le menu du programme et invite l'utilisateur à entrer un entier
    entre 1 et 9. Fait appel à la méthode saisir_entier mini_maxi de
    la classe Valider_Nombre_A22.

    Retourne: l'entier saisi par l'utilisateur qui est >= p_mini et <= p_maxi .
    """
    msg = f"""
    {'-' * 40}
    [1]. Afficher la facture détaillée
    [2]. Ajouter un article à la facture
    [3]. Supprimer un article de la facture
    [4]. Modifier la quantité d'un article
    [5]. Trier la facture par numéro d'article
    [6]. Afficher les articles les plus achetés (quantité maximale)
    [7]. Afficher les articles les moins achetés (quantité minimale)
    [8]. Afficher sommairement la facture
    [9]. Quitter
    {'-' * 40}
    """
    print(msg)
    return saisir_func.saisir_entier_mini_maxi("Saisir Votre choix parmi [1..9]: ", 1, 9)

#...........................................................................................................................
def create_new_article(article_id: int) -> list:
    """
    Lit et retourne une liste contenant un nouvel article.

    Méthode qui fait appel à saisir_entier et saisir_entier_mini de
    la classe Valider_Nombre_A22.py

    Paramètres :
    article_id : L'indice (ID) du nouvel article.

    Retourne : Une liste contenant le nouvel article.
    """
    return [
        article_id,
        input("Nom article:"),
        saisir_func.saisir_reel_mini("Prix: ", 0),
        saisir_func.saisir_entier_mini("Quantité: ", 1)
    ]

#...........................................................................................................................
def delete_article(lst_articles: list) -> None:
    """
    Lit et supprime un article (par Id) de la liste des articles fournie.
    Sinon, afficher un message d'erreur.

    Paramètres :
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : None.
    """

    target_id = saisir_func.saisir_entier("Indice de l'article: ")
    target_id = chercher_article(lst_articles, target_id)
    if target_id == -1:
        print("L'article n'a pas été trouvé.")
    else:
        i = 0
        for article in lst_articles:
            if article[0] == target_id:
                lst_articles.pop(i)
                return None
            # end if
            i += 1
        # end for
    # end if

#...........................................................................................................................
def edit_article_quantity(lst_articles: list) -> None:
    """
    Lis l'indice de l'article à modifier, la nouvelle quantité et
    cherche l'article dans la liste, si trouvé, la quantité va être
    modifié, sinon, un message d'erreur va apparaître.

    Paramètres:
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : None.
    """

    target_id = saisir_func.saisir_entier_mini("Indice de l'article: ", 0)
    target_id = chercher_article(lst_articles, target_id)
    if target_id == -1:
        print("L'article n'a pas été trouvé.")
    else:
        i = 0
        for article in lst_articles:
            if article[0] == target_id:
                lst_articles[i][3] = saisir_func.saisir_entier_mini("Nouvelle Quantité: ", 1)
            # end if
            i += 1
        # end for
    # end if

#...........................................................................................................................
def order_lst_articles(lst_articles: list) -> None:
    """
    Trie la liste des articles par ordre croissant des numérros des articles.
    Va créer une liste tempéraire, la recopier dans lst_articles et l'inverser.
    Paramètres:
    lst_articles : Liste actuelle des articles de la facture.

    Retourne : None.
    """
    temp_lst = []
    while len(lst_articles) > 0:
        current_smallest = [[HIGHEST_INT], 0]
        i = 0
        for article in lst_articles:
            if article[0] < current_smallest[0][0]:
                current_smallest = [article, i]
            # end if
            i += 1
        # end for
        temp_lst.append(current_smallest[0])
        lst_articles.pop(current_smallest[1])
    # end while
    for temp_article in temp_lst:
        lst_articles.append(temp_article)
    # end for
