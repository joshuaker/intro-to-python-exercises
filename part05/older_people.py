# Write your solution here
def older_people(
    people: list,
    year: int
    ):
    new_list = []
    for item in people:
        if item[1] < year:
            new_list.append(item[0])
    return new_list