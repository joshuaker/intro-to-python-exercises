# Write your solution here
def most_common_character(string):
    '''string argument
    freturns character with most occurences
    if there are equal number many, return first in string
    '''

    count = 0
    char = ''

    for character in string:
        if string.count(character) > count:
            count = string.count(character)
            char = character
    return char
