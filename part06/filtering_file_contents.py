# Write your solution here
def filter_solutions():
    with open('solutions.csv') as new_file:
        correct = []
        incorrect = []
        for line in new_file:
            parts = line[:-1].split(';')
            parts[2] = int(parts[2])
            ans = 0
            if '-' in parts[1]:
                numbers = parts[1].split('-')
                left = int(numbers[0])
                right = int(numbers[1])
                ans = left - right
            else:
                numbers = parts[1].split('+')
                left = int(numbers[0])
                right = int(numbers[1])
                ans = left + right
            
            if parts[2] == ans:
                correct.append(line)
            else:
                incorrect.append(line)

    with open('correct.csv', 'w') as file:
        for _ in correct:
            file.write(_)
    
    with open('incorrect.csv', 'w') as file:
        for _ in incorrect:
            file.write(_)