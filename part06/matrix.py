# write your solution here
def read_matrix():
    with open("matrix.txt") as new_file:
        matrix = []
        for line in new_file:
            rows = []
            items = line.split(",")
            for item in items:
                rows.append(int(item))
            matrix.append(rows)
    return matrix

def row_sums():
    matrix = read_matrix()
    sums = []
    for list in matrix:
        sums.append(sum(list))
    return sums

def combine(read_matrix):
    big_list = []
    for row in read_matrix:
        big_list += row
    return big_list

def matrix_sum():
    big_list = combine(read_matrix())
    return sum(big_list)

def matrix_max():
    big_list = combine(read_matrix())
    return max(big_list)