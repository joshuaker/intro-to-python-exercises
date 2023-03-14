# Write your solution here
#The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.
#All words should begin with the string specified by the second argument.

from random import sample
# sample provides unique 
# sample raises valueError when not enough population
def words(n: int, 
          beginning: str
          ):
    
    dict_list = []
    with open('words.txt') as file:
        for line in file:
            line = line.strip('\n')
            dict_list.append(line)
    
    possible_words = []
    for word in dict_list:
        if word.startswith(beginning):
            possible_words.append(word)
    

    return sample(possible_words,n)
