MAX = 6
budgets = []

# Entrées des budgets
for i in range ( MAX ):
    budgets += [int(input())]
# end for

# Calculs et sortie. À faire
moyenne = (budgets[0] + budgets[1]) / 2
print(moyenne)
