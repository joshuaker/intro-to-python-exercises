if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

students = {}
with open(f'{student_info}') as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        students[parts[0]] = f'{parts[1]} {parts[2]}'

completed = {}
with open(f'{exercise_data}') as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        completed[parts[0]] = 0
        for i in range(1,8):
            completed[parts[0]] += int(parts[i])

for pic, name in students.items():
    if pic in completed:
        completions = completed[pic]
        print(f'{name} {completions}')