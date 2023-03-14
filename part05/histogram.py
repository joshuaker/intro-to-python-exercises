# Write your solution here
def histogram(string:str):
    letters = {}

    for character in string:
        if not character in letters:
            letters[character] = 1
        else:
            letters[character] += 1
    
    for key, value in letters.items():
        print(key, '*'*value)
