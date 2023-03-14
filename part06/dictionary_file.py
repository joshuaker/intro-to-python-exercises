# Write your solution here
# three functions: 1 add, 2 search, 3 quit. no function for word not found
# finnish - english dictionary
# all entries written in a file called dictionary.txt;
# func 2 also provides words that contains searchterm

dictionary = {}
with open('dictionary.txt') as file:
    for line in file:
        line = line.strip('\n')
        parts = line.split(';')
        dictionary[parts[0]] = parts[1]

def write():
    with open('dictionary.txt', 'w') as file:
        for key, value in dictionary.items():
            file.write(f'{key};{value}\n')


while True:
    print('1 - Add word, 2- Search, 3 - Quit')
    func = int(input('Function: '))

    # add Finnish and English terms
    if func == 1:
        finnish = input('The word in Finnish: ')
        english = input('The word in English: ')

        dictionary[finnish] = english
        write()
        print('Dictionary entry added')

    if func == 2:
        search_term = input('Search term: ')
        for key, value in dictionary.items():
            if search_term in value:
                print(f'{key} - {value}')
            if search_term in key:
                print(f'{key} - {value}')
    
    if func == 3:
        print('Bye!')
        break
# the test 