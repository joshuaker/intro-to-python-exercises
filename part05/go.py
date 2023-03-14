# Write your solution here
def who_won(game_board: list):
    #for any size game board

    empty = 0
    player_1 = 0
    player_2 = 0

    for row in game_board:
        empty += row.count(0)
        player_1 += row.count(1)
        player_2 += row.count(2)
    
    if player_1 > player_2:
        return 1
    elif player_1 < player_2:
        return 2
    else:
        return 0