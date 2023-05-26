

repetitions = int(input('Nombres de répétitions: '))
multiplicator = int(input('Multiplicateur: '))
i = 0
print('| x | ' + str(multiplicator) + ' |')
while i < repetitions:
    print('| ' + str(i) + ' | ' + str(i * multiplicator) + ' |')
    i += 1