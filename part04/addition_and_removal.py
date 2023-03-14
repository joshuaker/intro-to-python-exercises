# Write your solution here
list = []
count = 1

while True:

    print(f'The list is now {list}')
    func = input('a(d)d, (r)emove or e(x)it: ')
    if func == 'x':
        print('Bye!')
        break

    if func == 'd':
        list.append(count)
        count += 1
    
    if func == 'r':
        list.remove(count-1)
        count -= 1