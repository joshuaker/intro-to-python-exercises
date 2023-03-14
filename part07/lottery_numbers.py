# Write your solution here
from random import randint
def lottery_numbers(amount: int, 
                    lower: int, 
                    upper: int):
    # quantity
    # bounds
    # can't use sample because possible for sample size to be larger than population
    draw = []
    count = amount
    while count > 0:
        x = randint(lower,upper)
        if not x in draw:
            draw.append(x)
        else:
            continue
        count -= 1
    draw.sort()
    return draw
