# Write your solution here
def list_of_stars(a):
    for item in a:
        print('*' * item)

if __name__ == '__main__':
    list_of_stars([3, 7, 1, 1, 2])