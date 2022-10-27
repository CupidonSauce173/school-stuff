# Va afficher chaque charactère de la Str.
for cara in ' bon matin':
    print(cara)

# Va afficher i et s'il est pair ou impair.
for i in range(10):
    if i % 2 == 0: 
        print(i, 'nombre pair')
    else :
        print(i, 'nombre impair')


print('\n')
vitesse = float(input('Vitesse: '))
if vitesse > 100:
    print('Trop Rapide')
elif vitesse < 60:
    print('Trop lent')
else:
    print('Correct')
