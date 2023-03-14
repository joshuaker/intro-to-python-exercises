# Write your solution here
def count_matching_elements(my_matrix:list, element:int):
    # count how many elements within matrix match the argument value

    element_count = 0

    for row in my_matrix:
        element_count += row.count(element)
    
    return element_count