# Write your solution here
# key = number; value = number factorial
# range of key = 1 to n inclusive

def factorials(n:int):
    dictionary = {}
    for i in range(1, n+1):
        dictionary[i] = get_factorial(i)

    return dictionary


def get_factorial(i):
    factorial = 1
    while i > 0:
        factorial *= i
        i -= 1
    return factorial
