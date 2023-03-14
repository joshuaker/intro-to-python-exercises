# Write your solution here
def find_movies(
    database:list,
    search_term:str
    ):
    #capitalization irrelevant

    new_list = []

    for dictionary in database:
        if search_term in dictionary["name"].lower():
            new_list.append(dictionary)
        
    return new_list
