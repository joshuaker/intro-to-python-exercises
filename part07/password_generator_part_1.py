# Write your solution here
from random import shuffle

def generate_password(length: int):
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shuffle(characters)
    password = ''
    for i in range(length):
        password += characters[i] #concatenate first i letters
    return password
