''' Find the smallest distance between two any given words in a words list '''

def find_distance(word_one: str, word_two: str, sentence: str) -> int:
    ''' Finds the distance between two words in a sentence '''
    words = sentence.split(' ')
    distance = []
    for word in words:
        if word == word_one:
    return None

print(find_distance('hello', 'world', 'dog cat hello cat dog dog hello cat world'))
