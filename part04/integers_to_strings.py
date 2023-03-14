# Write your solution here

def formatted(float_list):
    new_list = []
    for item in float_list:
        new_list.append(f'{item:.2f}')
    return new_list