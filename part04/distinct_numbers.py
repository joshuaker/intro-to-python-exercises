# Write your solution here
def distinct_numbers(int_list):
    new_list = []
    for item in int_list:
        if new_list.count(item) == 0:
            new_list.append(item)
    return sorted(new_list)

    # for items in list, count new_list for item; if count == 0: append.