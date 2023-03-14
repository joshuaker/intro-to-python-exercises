# Copy here code of line function from previous exercise
def line(integer, string):
    if string != '':
        print(string[0] * integer)
    else:
        print('*' * integer)

def triangle(size):
    # You should call function line here with proper parameters
    count = 1
    while count <= size:
        line(count, "#")
        count += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
    print()
    triangle(3)