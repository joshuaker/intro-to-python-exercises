# Write your solution here
def no_shouting(str_list):
    new_list = []
    for item in str_list:
        if not item.isupper():
            new_list.append(item)
    return new_list
    
if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    print(no_shouting(my_list))