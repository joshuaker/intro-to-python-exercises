# Write your solution here
def everything_reversed(str_list):
    '''
    str_list = list of strings
    return = new_list
    function = reverse the strings, reverse the order of index
    '''
    new_list = []

    for item in str_list:
        # do 2 things, reverse the string itself, and then reverse the order in the list
        new_list.append(item[::-1])
    
    return new_list[::-1]

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
