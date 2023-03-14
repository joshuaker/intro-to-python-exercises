# Write your solution here
def print_sudoku(sudoku: list):
    for row in range(len(sudoku)):
        for i in range(len(sudoku[row])):
            if i == 2 or i == 5:
                if sudoku[row][i] == 0:
                    print('_  ', end='')
                else:
                    print(f'{str(sudoku[row][i])}  ', end='')
            else:
                if sudoku[row][i] == 0:
                    print('_ ', end='')
                else:
                    print(f'{str(sudoku[row][i])} ', end='')
        print()
        if row == 2 or row == 5:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    #row_no = sudoku[row_no]
    #column_no = sudoku[row_no][column_no]
    #number = variable

    sudoku[row_no][column_no] = number

if __name__ == '__main__':
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)

    print_sudoku(sudoku)