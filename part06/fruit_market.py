# write your solution here
def read_fruits():
    fruit_dictionary = {}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(';')
            
            fruit = parts[0]
            price = parts[1]
            fruit_dictionary[fruit] = float(price)
    return fruit_dictionary

