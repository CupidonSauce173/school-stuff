'''
Programme qui lit une chaîne et affiche le menu ci-dessus. Votre programme réaffiche le
menu et répond à l'option choisie tant que l'utilisateur n'a pas saisit la lettre t ou T. Il faut ignorer la
casse
'''

MENUSTRING = "• L : affiche la longueur de la chaîne\n\
• J : affiche la chaîne tout en majuscule\n\
• M : affiche la chaîne tout en minuscule\n\
• E : efface les espaces du début et de fin de chaînes\n\
• C : affiche le nombre d'occurrence d'un caractère donné par l’utilisateur dans la chaîne saisie\n\
• T : pour terminer"
CHOIX_MESSAGE = "Votre choix: "
INPUT_MESSAGE = 'Entrez une chaîne de caractères: '

print(MENUSTRING)
user_input = input(CHOIX_MESSAGE)
while user_input not in ('T', 't'):
    if user_input not in ('L', 'l', 'J', 'j', 'M', 'm', 'E', 'e', 'C', 'c'):
        print('Option non trouvée.')
    elif user_input in ('L', 'l'):
        print(f"Longueur de la chaîne: {len(input(INPUT_MESSAGE))}")
    elif user_input in ('J', 'j'):
        print(input(INPUT_MESSAGE).upper())
    elif user_input in ('M', 'm'):
        print(input(INPUT_MESSAGE).lower())
    elif user_input in ('E', 'e'):
        sentence = input(INPUT_MESSAGE)
        if sentence[0] == ' ':
            sentence = sentence[1:]
        # end if
        if sentence[-1] == ' ':
            sentence = sentence[:-1]
        # end if
        print(sentence)
    elif user_input in ('C', 'c'):
        target_string = input(INPUT_MESSAGE)
        target_char = input('Caractère à chercher: ')
        if len(target_char) != 1:
            print('Entrez uniquement un caractère.')
        else:
            print(f'Occurences de {target_char}: {target_string.count(target_char)}')
        # end if
    # end if
    print(MENUSTRING)
    user_input = input(CHOIX_MESSAGE)
# end while
print('*** Fin du programme ***')
