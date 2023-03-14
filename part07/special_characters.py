# Write your solution here
import string

def separate_characters(my_string: str):
    a = ''
    b = ''
    c = ''
    for i in range(len(my_string)):
        if my_string[i] in string.ascii_letters:
            a += my_string[i]
        elif my_string[i] in string.punctuation:
            b += my_string[i]
        else:
            c += my_string[i]
    return a,b,c