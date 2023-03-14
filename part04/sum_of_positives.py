# Write your solution here

def sum_of_positives(list_of_integers):
    list_of_pos = []
    for i in list_of_integers:
        if i > 0:
            list_of_pos.append(i)
    return sum(list_of_pos)

if __name__ == "__main__":
    print(sum_of_positives([1, -2, 3, -4, 5]))