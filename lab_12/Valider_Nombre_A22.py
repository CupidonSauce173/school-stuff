"""
-----------------------------------------------------------------------------------------------
#
# Programme	: Valider_Nombre_A22.py
# Auteur 	: Samira Bennis
# Date de dernière modification : 2022-12-06

# Patchnote
#   --> Inconsistence du code fixé.
#   --> Pylint check passé.

# Objectif :
#   offre différentes fonctions obligeant l'utilisateur à saisir ce qui suit :
#   --> un nombre quelconque
#   --> un nombre entier quelconque
#   --> un nombre entier supérieur ou égal à un nombre passé en paramètre
#   --> un nombre entier inférieur ou égal à un nombre passé en paramètre
#   --> un nombre entier compris entre 2 nombres passés en paramètre (inclusivement)

#   --> un nombre réel quelconque
#   --> un nombre réel supérieur ou égal à un nombre passé en paramètre
#   --> un nombre réel compris entre 2 nombres passés en paramètre (inclusivement)

#
--------------------------------------------------------------------------------------------------
"""

#............................................................................
def saisir_entier(p_message: str) -> int:
    """
    Lit et retourne un entier

    invite l'utilisateur à saisir un entier et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un entier.

    Paramètre :
    p_message : chaîne de caractères invitant l'utilisateur à saisir

    Retour : l'entier saisi par l'utilisateur


    """

    while True:
        try:
            return int(input(p_message))
        except ValueError:
            print('==> Erreur de saisie, saisir un entier, réessayer \n')
    #end while

#............................................................................
def saisir_reel(p_message: str) -> float:
    """
    Lit et retourne le nombre saisi par l'utilisateur

    invite l'utilisateur à saisir une valeur numérique et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un nombre.

    Paramètre :
    p_message : chaîne de caractères invitant l'utilisateur à saisir un nombre

    Retour : le nombre saisi par l'utilisateur
    """
    bon = False
    while not bon:
        try:
            un_nombre = float(input(p_message))
            bon = True
        except ValueError:
            print('==> Erreur de saisie, saisir un nombre(entier ou réel), réessayer \n')
    #end while
    return un_nombre

#............................................................................
def saisir_entier_mini(p_message: str, p_mini: int) -> int:
    """
    Lit et retourne un entier qui est >= p_mini

    invite l'utilisateur à saisir un entier et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un entier qui est >= p_mini.

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_mini    : nombre entier avec lequel on compare le nombre saisi

    Retour : l'entier saisi par l'utilisateur qui est >= p_mini
    """
    while True:
        try:
            un_nombre = int(input(p_message))
            if un_nombre >= p_mini :
                return un_nombre
            # end if
            print('==>', p_message, "doit être un entier >= ", p_mini, "réessayer \n")
        except ValueError:
            print("==> Erreur de saisie, saisir un entier >= ", p_mini, "réessayer \n")
    #end while

#............................................................................
def saisir_un_nombre(p_message: str) -> tuple:
    """
    Lit et retourne le nombre saisi par l'utilisateur

    invite l'utilisateur à saisir une valeur numérique et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un nombre.

    Paramètre :
    p_message : chaîne de caractères invitant l'utilisateur à saisir un nombre

    Retour : un tuple composé du nombre saisi par l'utilisateur et
    une chaine de caractères contenant le type (int ou float)

    [ Exemples (6, "int") ou (7.1, "float") ]
    """
    while True:
        un_nombre = input(p_message)
        try:
            if int(un_nombre):
                return un_nombre, "int"
            if float(un_nombre):
                return un_nombre, "float"
            #end if
        except ValueError:
            print('==> Attention : Erreur de saisie, saisir \
                un nombre (entier ou réel), réessayer \n')
    #end while

#............................................................................
def saisir_entier_maxi(p_message: str, p_maxi: int) -> int:
    """
    Lit et retourne un entier qui est <= p_maxi

    invite l'utilisateur à saisir un entier et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un entier qui est <= p_maxi.

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_maxi    : nombre entier avec lequel on compare le nombre saisi

    Retour : l'entier saisi par l'utilisateur qui est <= p_maxi
    """
    while True:
        try:
            un_nombre = int(input(p_message))
            if un_nombre <= p_maxi :
                return un_nombre
            # end if
            print('==>', p_message, "doit être un entier <= ", p_maxi, "réessayer \n")
        except ValueError:
            print("==> Erreur de saisie, saisir un entier <= ", p_maxi, "réessayer \n")
    #end while

#............................................................................
def saisir_reel_mini(p_message: str, p_mini: float) -> float:
    """
    Lit et retourne un entier qui est >= p_mini

    invite l'utilisateur à saisir un nombre et
    le réinvite à ressaisir tant que l'utilisateur ne saisit pas un nombre qui est >= p_mini.

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_mini    : valeur numérique avec lequel on compare le nombre saisi

    Retour : le nombre saisi par l'utilisateur qui est >= p_mini
    """
    while True:
        try:
            un_nombre = float(input(p_message))
            if un_nombre >= p_mini :
                return un_nombre
            # end if
            print('==>', p_message, "doit être un réel >= ", p_mini, "réessayer \n")
        except ValueError:
            print("==> Erreur de saisie, saisir un réel >= ", p_mini, "réessayer \n")
    #end while

#............................................................................
def saisir_reel_maxi(p_message: str, p_maxi: float) -> float:
    """
    Lit et retourne un nombre qui est <= p_maxi

    invite l'utilisateur à saisir un nombre et le réinvite à ressaisir
    tant que l'utilisateur ne saisit pas un nombre qui est <= p_maxi.

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_maxi    : valeur numérique avec lequel on compare le nombre saisi

    Retour : le nombre saisi par l'utilisateur qui est <= p_maxi
    """
    while True:
        try:
            un_nombre = float(input(p_message))
            if un_nombre <= p_maxi :
                return un_nombre
            #end if
            print('==>', p_message, "doit être un réel <= ", p_maxi, "réessayer \n")
        except ValueError:
            print("==> Erreur de saisie, saisir un réel <= ", p_maxi, "réessayer \n")
    #end while

#............................................................................
def saisir_reel_mini_maxi(p_message: str, p_mini: float, p_maxi: float) -> float:
    """
    Lit et retourne un nombre qui est >= p_mini et <= p_maxi

    invite l'utilisateur à saisir un nombre et le réinvite à ressaisir
    tant que l'utilisateur ne saisit pas un nombre qui est >= p_mini et <= p_maxi

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_maxi    : valeur numérique avec lequel on compare le nombre saisi
    p_mini    : valeur numérique avec lequel on compare le nombre saisi

    Retour : le nombre saisi par l'utilisateur qui est >= p_mini et <= p_maxi
    """
    while True:
        try:
            un_nombre = float(input(p_message))
            if un_nombre >= p_mini and un_nombre <= p_maxi:
                return un_nombre
            # end if
            print('==>', p_message, "(doit être un réel compris entre", \
                p_mini, "et", p_maxi, ") réessayer \n")
        except ValueError:
            print("==> Erreur de saisie (doit être un réel compris entre", \
                p_mini, "et", p_maxi, ") réessayer \n")
    #end while
#............................................................................

def saisir_entier_mini_maxi(p_message: str, p_mini: int, p_maxi: int) -> int:
    """
    Lit et retourne un entier qui est >= p_mini et <= p_maxi

    invite l'utilisateur à saisir un entier et le réinvite à ressaisir
    tant que l'utilisateur ne saisit pas un entier qui est >= p_mini et <= p_maxi

    Paramètres :
    p_message : chaîne de caractères invitant l'utilisateur à saisir
    p_maxi    : entier avec lequel on compare l'entier saisi
    p_mini    : entier avec lequel on compare l'entier saisi

    Retour : l'entier saisi par l'utilisateur qui est >= p_mini et <= p_maxi
    """
    while True:
        try:
            un_nombre = int(input(p_message))
            if un_nombre >= p_mini and un_nombre <= p_maxi:
                return un_nombre
            #end if
            print('==>', p_message, "(doit être un entier compris entre", \
                p_mini, "et", p_maxi, ") réessayer \n")
        except ValueError:
            print("==> Erreur de saisie, (doit être un entier compris entre", \
                p_mini, "et", p_maxi, ") réessayer \n")
    #end while
#............................................................................
