# Write your solution here

def all_the_longest(string_list):
    long_list = []
    longest = string_list[0]

    for item in string_list:
        if len(item) > len(longest):
            longest = item
            long_list = []
            long_list.append(item)
        elif len(item) == len(longest):
            long_list.append(item)
    
    return long_list