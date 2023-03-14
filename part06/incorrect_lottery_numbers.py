# Write your solution here

# week #
# seven integers
# integer between 1 and 39
# same number appears twice
def filter_incorrect():
    correct = []
    with open('lottery_numbers.csv') as file:
        for line in file:
            line_copy = line
            line = line.strip('\n')
            parts = line.split(';')
            header = parts[0]
            numbers = parts[1].split(',')

            if len(numbers) != 7: #check number of int
                continue

            try:
                header = int(header[5:]) #check the numbers after 'week '
            except:
                continue

            try:
                repeat_check = []
                for i in numbers: 
                    x = int(i) #check if int
                    if not 0 < x < 40: #check if in range
                        raise ValueError
                    if x in repeat_check: #check if repeat
                        raise ValueError
                    repeat_check.append(x)
            except:
                continue
            
            correct.append(line_copy)

    with open('correct_numbers.csv', 'w') as file:
        for item in correct:
            file.write(item)