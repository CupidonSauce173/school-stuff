''' Daily Coding Problem #159 Finding First Reccurring Problem '''

from ctypes import Union

def find_reccurring(sentence: str) -> Union(chr, None):
    ''' Returns the first reccurring character in a string. '''
    recorded = []
    for character in sentence:
        for rec_character in recorded:
            if rec_character == character:
                return character
        recorded.append(character)
    return None

output = find_reccurring(input('Enter string: '))
print(output)
