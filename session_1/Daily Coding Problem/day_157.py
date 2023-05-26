'''
Daily Coding Problem #158 Given a string
determine whether any permutation of it is a palindrome
'''

def rearrange_palindrome(sentence: str) -> bool:
    ''' Find if a string is a palindrome permutation '''
    characters = []
    occurrences = []
    for character in sentence:
        characters.append(character)
    for character in characters:
        occurrences.append(characters.count(character))
    i = 0
    for k in occurrences:
        if k == 1:
            i += 1
        if i > 1:
            return False
    return True

print(rearrange_palindrome(input('Enter a sentence: ')))
