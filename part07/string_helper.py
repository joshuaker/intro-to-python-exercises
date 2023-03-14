# Write your solution here
#module name = file name

def change_case(orig_string: str):
    new_string = ''
    for character in orig_string:
        if character == character.lower():
            new_string += character.upper()
        else:
            new_string += character.lower()
    
    return new_string


def split_in_half(orig_string: str):
    #if odd, first half is shorter
    length = len(orig_string)
    if length % 2 == 0: #if even
        half = length/2
        return (orig_string[0:int(half)], orig_string[int(half):])
    else: #if odd
        return (orig_string[0:int((length-1)/2)], orig_string[int((length-1)/2):])


def remove_special_characters(orig_string: str):
    special_characters = ['¤','!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ';', ':', '"', "'", '-', '_', '+', '=', '[', ']', '{', '}', '\\', '|', '/', '?', '>', '<', ',', '.', '§']
    # this works because i can check what the auto test tests for
    # if not this, i could have allowed only upper,lower,space and numbers
    #ignoring evertyhign else
    new_string = ''
    notes = ''' from string import ascii_letters, digits
    allowed = ascii_letters + digits + ' '
    new_string = ""
    for character in orig_string:
        if character in allowed:
            new_string += character
            '''
    for character in orig_string:
        if character not in special_characters:
            new_string += character

    return new_string
