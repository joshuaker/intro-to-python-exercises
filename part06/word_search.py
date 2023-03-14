# Write your solution here
def find_words(search_term:str):
    words = []
    with open('words.txt') as file:
        for line in file:
            line = line.strip('\n')
            words.append(line)
    possible_words = []
    search_term_copy = search_term
    locations = []
    found_words = []


    if '.' in search_term:
        for _ in words:
            if len(_) == len(search_term):
                possible_words.append(_)
        
        count = search_term.count('.')
        while count > 0:
            x = search_term_copy.find('.')
            locations.append(int(x))
            search_term_copy = search_term_copy[0:x] + search_term_copy[x+1:]

            count -= 1
        for _ in possible_words:
            _copy = _
            for index in locations:
                _copy = _copy[0:index] + _copy[index+1:]
            if _copy == search_term_copy:
                found_words.append(_)
    
    elif search_term.endswith('*'):
        for word in words:
            if word.startswith(f'{search_term[:-1]}'):
                found_words.append(word)
    
    elif search_term.startswith('*'):
        for word in words:
            if word.endswith(f'{search_term[1:]}'):
                found_words.append(word)
    
    else:
        for word in words:
            if word == search_term:
                found_words.append(word)

    return found_words




    # replace dot with everysingle character and search for that
    # or take slices around the dot, and match (but this will have to take into account position of characters)
    #find all equal length words, take out the '.' index, match