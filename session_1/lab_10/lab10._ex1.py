'''
Programme qui lit des chaînes de caractères et affiche la taille. Pour terminer l'utilisateur
donne la chaîne vide
'''
print('*** Taille de chaînes de caractères ***')
MESSAGE = 'Entrez la chaîne: '
userInput = input(MESSAGE)
while userInput != '':
    print(f"Taille de la chaîne: {str(len(userInput))}")
    userInput = input(MESSAGE)
# end while
print('*** Fin du programme ***')
