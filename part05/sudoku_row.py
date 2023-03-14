# Write your solution here
def row_correct(sudoku: list, row_no: int):
    # row_no is specific row index
    # check if specific row contains at most 1-9 unique

    for element in sudoku[row_no]:
        if element != 0:
            check = sudoku[row_no].count(element)
            if check > 1:
                return False
    return True
