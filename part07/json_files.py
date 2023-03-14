# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    
    info = json.loads(data)
    
    for person in info:
        hobby_str = ''
        for hobbies in person['hobbies']:
            hobby_str += f'{hobbies}, '
        hobby_str = hobby_str[:-2]
        # or, use .join() method
        # hobby_str = ', '.join(person['hobbies']) 
        # don't need to worry about slicing off last two ', ' because the joinery only 
        # applies between elements

        print(f'''{person['name']} {person['age']} years ({hobby_str})''')
    