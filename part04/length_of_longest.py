# Write your solution here
def length_of_longest(string_list):
    best = string_list[0]

    for item in string_list:
        if len(item) > len(best):
            best = item
    
    return len(best)