# Write your solution here
def same_chars(string, ind1, ind2):
    if ind1 >= len(string) or ind2 >= len(string):
        return False
    elif string[ind1:ind1+1] == string[ind2:ind2+1]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))