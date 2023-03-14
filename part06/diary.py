# Write your solution here
while True:
    diary = ''
    with open('diary.txt') as file:
        diary = file.read()

    print('1 - add an entry, 2 - read entries, 0 - quit')
    func = input('Function: ')

    if func == '0':
        print('Bye now!')
        break

    if func== '2':
        print(f'''Entries:{diary}''')
    if func == '1':
        entry = input('Diary entry: ')
        diary += f'\n{entry}'

        with open('diary.txt', 'w') as file:
            for _ in diary:
                file.write(_)
        print('Diary saved')

