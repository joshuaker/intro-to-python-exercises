# Write your solution here
""" import copy
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku_copy = copy.deepcopy(sudoku)
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy
 """

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_list = []
    for item in sudoku:
        new_list.append(item[:])
    
    print(id(new_list[0][0]), id(sudoku[0:0]))
    

copy_and_add([[1,2],[1,2]], 0, 0, 0)