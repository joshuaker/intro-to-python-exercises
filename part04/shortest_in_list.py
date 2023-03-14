# Write your solution here

def shortest(string_list):
    shortest = string_list[0]

    for item in string_list:
        if len(item) < len(shortest):
            shortest = item
    
    return shortest