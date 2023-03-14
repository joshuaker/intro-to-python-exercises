# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        num_list = []
        for line in new_file:
            num_list.append(line)
        return int(max(num_list))