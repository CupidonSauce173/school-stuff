'''
Find the smallest number of squared intergers which sum to n
'''

# digital root is 1, 4, 7, or 9

def find_smallest_squared_int(nbr: int) -> int:
    ''' Find the smallest squared intergers which sum to n'''
    i = 0
    while nbr > 0:
        if nbr - 9 >= 0:
            nbr -= 9
            i += 1
        elif nbr - 7 >= 0:
            nbr -= 7
            i += 1
        elif nbr - 4 >= 0:
            nbr -= 4
            i += 1
        elif nbr - 1 >= 0:
            nbr -= 1
            i += 1
    return i

print(find_smallest_squared_int(int(input('Entrer un nombre entier: '))))
