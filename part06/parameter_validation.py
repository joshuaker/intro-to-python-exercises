# Write your solution here
def new_person(name:str,
               age: int):
    #creates and returns tuple containing data in arguments
    # name, age
    if len(name) == 0 or ' ' not in name or len(name) > 40 or age < 0 or age > 150: #raising error on invalid parameters
        raise ValueError
    return (name,age)