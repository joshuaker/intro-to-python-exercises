# Write your solution here


def double_items(numbers: list):
    numbers_copy = numbers[:]
    # numbers_copy = numbers just sets the reference to the same thing, so modifying
    # numbers_copy will also modify numbers.
    # numbers_copy = numbers [:] sets a new variable equal to the slice of numbers
    
    for i in range(len(numbers_copy)):
        numbers_copy[i] *= 2
    return numbers_copy

if __name__ == '__main__':
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
