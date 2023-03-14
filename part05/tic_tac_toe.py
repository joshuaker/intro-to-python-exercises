# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    # x = column; y = row
    # pieces = strings; '', 'X' = p1, 'O' = p2
    # function returns True if space was empty and was successfully replaced; otherwise False (if coordinates aren't valid or occupied)
    # game_board = [['','',''],['','',''],['','','']]

    # start with return False if coordinates aren't valid:
    if not 0 <= x < 3:
        return False
    if not 0 <= y < 3:
        return False
    if game_board[y][x] != '':
        return False
    elif game_board[y][x] == '':
        game_board[y][x] = piece
        return True
    

if __name__ == '__main__':
    game_board = [['', '', ''], ['', '', ''], ['', '', 'O']]
    print(play_turn(game_board, 1, 1, 'O'))
    print(game_board)
