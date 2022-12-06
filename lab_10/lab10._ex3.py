'''
Un programme qui lit une phrase et qui l'affiche à l’envers. Utiliser une fois la boucle while et
une fois la boucle for.
'''

print("*** Affiche l'inversé d'une phrase ***")
userInput = input('Entrez une phrase: ')
inputList = userInput.split(' ')
reversedInput = []

print("-- WHILE LOOP --")
while len(inputList) > 0:
    reversedInput.append(inputList[-1])
    inputList.pop()
# end while
print("Résultat: " + " ".join(reversedInput))

print("-- FOR LOOP --")
inputList = userInput.split(' ')
reversedInput = []
for word in inputList:
    reversedInput.append(word)
# end while
reversedInput.reverse()
print("Résultat: " + " ".join(reversedInput))

print('*** Fin du programme ***')
