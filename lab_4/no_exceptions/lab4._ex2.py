''' Calcule et afficher la somme des nombres pairs de 1 à 1000. '''

i = 1
somme = 0
while i <= 1000:
    if i % 2 == 0:
        somme += i
    i += 1
print(somme)