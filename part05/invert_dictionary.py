# Write your solution here
import copy
def invert(dictionary: dict):
    # values become keys and keys become values
    dictionary_copy = copy.deepcopy(dictionary)
    dictionary.clear()

    for key, value in dictionary_copy.items():
        dictionary[value] = key
        
