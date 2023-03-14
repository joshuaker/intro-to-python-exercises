# Write your solution here
list = []
count = 0

while True:
    word = input('Word: ')

    if word in list:
        print(f'You typed in {count} different words')
        break

    list.append(word)
    count += 1