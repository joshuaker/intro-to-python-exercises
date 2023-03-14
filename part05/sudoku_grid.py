# Write your solution here
# does not take row_no or column_no because you want to check every single one
def sudoku_grid_correct(sudoku: list):
    #row check
    rows = [0,1,2,3,4,5,6,7,8,]

    for row_no in rows:
        for element in sudoku[row_no]:
            if element != 0:
                check = sudoku[row_no].count(element)
                if check > 1:
                    return False

    #column check
    columns = [0,1,2,3,4,5,6,7,8]
    for column_no in columns:
        column_list = []
        for row in sudoku:
            #one element in each row
            column_list.append(row[column_no])

        for item in column_list:
            if item != 0 and column_list.count(item) > 1:
                return False

    #cubes check
    cubes = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3] , [6, 6]]
    for item in cubes: #accessing small lists ie. [0,0]
        numbers_check = []
        x = item[0]
        y = item[1]
        for row_num in range(x, x+3):
            for column_num in range(y, y+3):
                number = sudoku[row_num][column_num]
                if number > 0 and number in numbers_check:
                    return False
                numbers_check.append(number)
    
    return True    
