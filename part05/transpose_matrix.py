# Write your solution here
# transpose a matrix; flip it on its diagonal. the rows become the columns and vice versa
import copy

def transpose(matrix:list):
    matrix_copy = copy.deepcopy(matrix)
    # need copy to preserve all numbers

    j = 0
    while j < (len(matrix)):
        for i in range(len(matrix)):
            matrix[i][j] = matrix_copy[j][i]
        j += 1



if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose(matrix)
    print(matrix)