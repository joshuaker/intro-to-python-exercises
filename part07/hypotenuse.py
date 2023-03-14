# Write your solution here
import math
def hypotenuse(
        leg1: float,
        leg2: float
    ):
    # a2 + b2 = c2

    c = leg1**2 + leg2**2
    return math.sqrt(c)