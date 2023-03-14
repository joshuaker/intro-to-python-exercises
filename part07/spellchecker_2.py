# Write your solution here
from difflib import get_close_matches

word_list = []
with open('wordlist.txt') as file:
    for line in file:
        line = line.strip('\n')
        word_list.append(line)

text = input('write text: ')
words = text.split(' ')

return_string = ''
suggestions = {}
for word in words:
    if word.lower() in word_list:
        return_string += f'{word} '
    else:
        return_string += f'*{word}* '
        suggestions[word] = get_close_matches(word, word_list) # returns a list

print(return_string)
print('suggestions: ')
for key, value in suggestions.items():
    suggestions = ','.join(value)
    print(f'{key}: {suggestions}')