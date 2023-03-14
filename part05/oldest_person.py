# Write your solution here
def oldest_person(people:list):
    #list of tuples
    # first element is name, second is year of birth
    list = []
    for item in people:
        list.append(item[1]) #this is second element, year of birth
    
    new_list = sorted(list)
    new_list[0] #this is the oldest year

    x = list.index(new_list[0]) #this is the index of oldest person

    return people[x][0]