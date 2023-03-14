# Write your solution here
phone_book = {}

while True:

    command = int(input('command(1 search,2 add, 3 quit): '))

    if command == 1:
        name = input('name: ')
        if not name in phone_book:
            print('no number')
        else:
            for number in phone_book[name]:
                print(number)
    elif command == 2:
        name = input('name: ')
        number = input('number: ')
        if not name in phone_book:
            phone_book[name] = []
            phone_book[name].append(number)
        else:
            phone_book[name].append(number)
        print('ok!')
    elif command == 3:
        print('quitting...')
        break



