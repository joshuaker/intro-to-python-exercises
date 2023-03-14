# Write your solution here
my_list = []
ordered = []

while True:
    item = int(input('New item: '))

    if item == 0:
        print('Bye!')
        break

    my_list.append(item)
    ordered = sorted(my_list)

    print(f'The list now: {my_list}')
    print(f'The list in order: {ordered}')
