# Write your solution here
#search based on name, preparation times, or ingredients used
# read recipes from submitted file

# first line = name
# second line = integer (prep in minutes)
# remaining = ingredients, divided by line
# if not last recipe, end = \n ; if last recipe, end = ''

# take all recipes; split by \n
# dictionary (name: int, ['','',''])


def read_file(filename):
    recipe_dictionary = {}
    with open(f"{filename}") as new_file:
        bigstring = new_file.read()
        biglist = bigstring.split('\n\n')
        for _ in biglist:
            
            parts = _.split('\n')
            #how to strip the last '' 
            recipe_dictionary[parts[0].lower()] = [int(parts[1]), parts[2:]]

    return recipe_dictionary


def search_by_name(
        filename: str,
        word: str
        ):
    recipe_dictionary = read_file(filename)
    recipes = []
    for key, value in recipe_dictionary.items():
        if word in key:
            recipes.append(key.capitalize())
    return recipes

def search_by_time(
        filename: str,
        prep_time: int
        ):
    #find all recipes with prep_time at most the number given
    # return recipes in list with prep time appended
    recipe_dictionary = read_file(filename)
    recipe_and_preptime = []
    for key, value in recipe_dictionary.items():
        time = recipe_dictionary[key][0]
        if prep_time >= time:
            recipe_and_preptime.append(f'{key.capitalize()}, preparation time {time} min')
    return recipe_and_preptime

def search_by_ingredient(
        filename: str,
        ingredient: str
        ):
    #find recipes whose ingredients contain the given search string
    #return same as search_by_time

    recipe_dictionary = read_file(filename)
    recipe_and_preptime = []
    for key, value in recipe_dictionary.items():
        time = recipe_dictionary[key][0]
        ingredients = recipe_dictionary[key][1]
        if ingredient in ingredients:
            recipe_and_preptime.append(f'{key.capitalize()}, preparation time {time} min')
    return recipe_and_preptime

if __name__ == "__main__":
    recipe_dictionary = read_file('recipes1.txt')

    print(recipe_dictionary)
    #for key,value in recipe_dictionary.items():
    if 'Pancakes'.lower() in recipe_dictionary:
        print('found')
    
    found_recipes = search_by_name('recipes1.txt', 'cake')
    print(found_recipes)

    found_recipes = search_by_time('recipes1.txt', 20)
    print(found_recipes)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    print(found_recipes)
