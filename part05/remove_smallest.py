# Write your solution here
def remove_smallest(numbers: list):
    #find and remove the smallest item
    # should not return value; directly modify the list
    ordered = numbers[:]
    ordered.sort()
    smallest = ordered[0]
    numbers.remove(smallest)


if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)