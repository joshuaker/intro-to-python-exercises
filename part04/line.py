# Write your solution here
def line(integer, string):
    if string != '':
        print(string[0] * integer)
    else:
        print('*' * integer)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")
    line(10, '')