# Write your solution here
count = int(input('How many items: '))
list = []

while count > 0:
    n = 1
    item = int(input(f'Item {n}: '))
    list.append(item)
    n += 1
    count -= 1

print(list)