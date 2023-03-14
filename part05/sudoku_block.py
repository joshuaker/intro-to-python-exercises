# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    # do not follow rules of sudoku
    # every possible square is counted
    list = []
    i = 0
    j = 0
    while i < 3:
        while j < 3:
            list.append(sudoku[row_no + i][column_no + j])
            j += 1
        i += 1
        j = 0

    print('this is list', list)

    for item in list:
        if item != 0 and list.count(item) > 1:
            return False
    return True

