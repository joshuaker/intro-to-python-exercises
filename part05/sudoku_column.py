# Write your solution here
def column_correct(sudoku: list, column_no: int):
    # check if every column is unique 1-9
    column_list = []
    for row in sudoku:
        #one element in each row
        column_list.append(row[column_no])

    print('This is columnlist:', column_list)
    for item in column_list:
        if item != 0 and column_list.count(item) > 1:
            return False
    
    return True
