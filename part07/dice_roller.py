# Write your solution here
# transitive dice; single dice rolling, and double dice rolling and scoring
from random import shuffle
def roll(die:str):
    A = [3,3,3,3,3,6]
    B = [2,2,2,5,5,5]
    C = [1,4,4,4,4,4]

    if die == 'A':
        die = A
    elif die == 'B':
        die = B
    else:
        die = C
    shuffle(die)

    return die[0]

def play(die1: str, 
         die2: str, 
         times: int
         ):
    A = [3,3,3,3,3,6]
    B = [2,2,2,5,5,5]
    C = [1,4,4,4,4,4]

    if die1 == 'A':
        die1 = A
    elif die1 == 'B':
        die1 = B
    else:
        die1 = C

    if die2 == 'A':
        die2 = A
    elif die2 == 'B':
        die2 = B
    else:
        die2 = C

    die1_nums = []
    die2_nums = []

    while times > 0:
        shuffle(die1)
        die1_nums.append(int(die1[0]))
        shuffle(die2)
        die2_nums.append(int(die2[0]))
        times -= 1

    die1_wins = 0
    die2_wins = 0
    ties = 0

    for i in range(len(die1_nums)):
        if die1_nums[i] == die2_nums[i]:
            ties += 1
        elif die1_nums[i] > die2_nums[i]:
            die1_wins += 1
        else:
            die2_wins += 1
    
    return die1_wins, die2_wins, ties
