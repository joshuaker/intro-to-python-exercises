# Write your solution here
def spruce(number):
    white_space_count = number - 1
    spruce_count = 0
    left = (white_space_count * ' ') + '*' + ('*' * spruce_count)
    
    print('a spruce!')
    
    while white_space_count >= 0:
        print((white_space_count * ' ') + '*' + ('*' * spruce_count))
        white_space_count -= 1
        spruce_count += 2
    
    print((number - 1)*' ' + '*')

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    print()
    spruce(3)