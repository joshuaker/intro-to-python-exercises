# Write your solution here
def longest(strings: list):
    count = 0
    longest_string = ''

    for item in strings:
        if len(item) > count:
            count = len(item)
            longest_string = item
    
    return longest_string
