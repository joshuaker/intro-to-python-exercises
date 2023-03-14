# Write your solution here
def store_personal_data(person: tuple):
    #name; age; height (str; int; float)
    #peoples.csv

    data = []
    with open('people.csv') as new_file:
        for line in new_file:
            data.append(line)
    
    x = ''
    for item in person:
        x += f'{item};'
    data.append(f'{x[:-1]}\n')

    with open('people.csv', 'w') as new_file:
        for item in data:
            new_file.write(item[:-1])

