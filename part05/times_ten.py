# Write your solution here
# keys = numbers between range, inclusive
# values = key * 10

def times_ten(
    start_index: int,
    end_index: int
    ):
    dictionary = {}
    for i in range(start_index, end_index+1):
        dictionary[i] = i*10

    return dictionary
