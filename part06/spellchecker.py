# write your solution here
# take input an split it on the white spaces
# this becomes a list of individual words
# check if words in wordlist.txt (which you do by reading the wordlist.txt)
#wordlist.txt has each word on an individual line.
# compile a new list

dictionary = []
with open("wordlist.txt") as new_file:
    for line in new_file:
        line = line.strip()
        dictionary.append(line)

sentence = input('Write text:')

parts = sentence.split(' ')
answer = ''
for word in parts:
    if word.lower() in dictionary:
        answer += f'{word} '
    else:
        answer += f'*{word}* '

print(answer)