# Copy here code of line function from previous exercise and use it in your solution
def line(integer, string):
    if string != '':
        print(string[0] * integer)
    else:
        print('*' * integer)

def shape(triangle_base, tri_string, rect_height, rect_string):
    count = 1
    while count <= triangle_base:
        line(count, tri_string)
        count += 1
    
    while rect_height > 0:
        line(triangle_base, rect_string)
        rect_height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")