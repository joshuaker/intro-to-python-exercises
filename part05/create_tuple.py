# Write your solution here
def create_tuple(
    x: int,
    y: int,
    z: int
    ):
    list = [x,y,z]
    list.sort()
    return (list[0],list[-1],sum(list))