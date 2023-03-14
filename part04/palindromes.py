# Write your solution here
def palindromes(word):
    list = []
    reversed_list = []

    for i in range(0, len(word), 1):
        list.append(word[i])
        
    for i in range(len(word)-1, -1, -1):
        reversed_list.append(word[i])

    return list == reversed_list

while True:
    word = input('Please type in a palindrome: ')

    if palindromes(word) == True:
        print(f'{word} is a palindrome!')
        break
    else:
        print('''that wasn't a palindrome''')



# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
