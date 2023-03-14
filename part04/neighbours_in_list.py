# Write your solution here

def longest_series_of_neighbours(int_list):
    # for every consecutive integer, count grows by 1
    # return the length of longest consecutive count
    # count every consecutive series: if count > longest; longest = count

    # ie. [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
    # want to compare int_list[index] with int_list[index + 1]
    # while index + 1 is still indexable
    # therefore index + 1 < len(int_list)
    # because len(int_list) fulfills half_open slicing

    index = 0
    count = 1
    longest = 0
    
    while index + 1 < len(int_list):
        if int_list[index] == int_list[index + 1] + 1 or int_list[index] == int_list[index + 1] - 1:
            # if consecutive numbers are +- 1:
            count += 1
        else:
            count = 1
        if count > longest:
            longest = count
        index += 1

    return longest



    
if __name__ == "__main__":
    my_list = [1, 2, 3, 5, 6, 9, 10]
    
    print(longest_series_of_neighbours(my_list))
