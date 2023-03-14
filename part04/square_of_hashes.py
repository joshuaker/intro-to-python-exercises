# Copy here code of line function from previous exercise
def line(integer, string):
    if string != '':
        print(string[0] * integer)
    else:
        print('*' * integer)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    count = 0
    while count < size:
        line(size, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)