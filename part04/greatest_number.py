# Write your solution here
def greatest_number(a, b, c):
    list = [a, b, c]
    list.sort()
    return list[-1]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(greatest_number(3, 4, 1))
    print(greatest_number(99, -4, 7))
    print(greatest_number(0, 0, 0))