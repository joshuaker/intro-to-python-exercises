# wwite your solution here
if True:
    student_info = input('Student information: ')
    exercise_data = input('Exercises completed: ')
    exam_data = input('Exam points: ')
else: 
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        else:
            students[parts[0]] = f'{parts[1]} {parts[2]}'

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        else:
            total_completed = 0
            for i in range(1, len(parts)):
                total_completed += int(parts[i])
            exercises[parts[0]] = total_completed

exams = {}
with open(exam_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        else:
            exam_grade = 0
            for i in range(1, len(parts)):
                exam_grade += int(parts[i])
            exams[parts[0]] = exam_grade

# 40 exercises = 10 points
# 10$ of exercises = 1 point
#every 4 points (4,8,12,16,20,24,28,32,36,40) // 4 


for pic, name in students.items():
    exercise_points = exercises[pic]//4
    grade = 0
    limits = [15,18,21,24,28]

    while grade < 5 and (exercise_points + exams[pic]) >= limits[grade]:
        grade += 1
    if False:
        if exercise_points + exams[pic] <= 14:
            grade = 0
        elif 15 <= exercise_points + exams[pic] <= 17:
            grade = 1
        elif 18 <= exercise_points + exams[pic] <= 20:
            grade = 2
        elif 21 <= exercise_points + exams[pic] <= 23:
            grade = 3
        elif 24 <= exercise_points + exams[pic] <= 27:
            grade = 4
        elif 28 <= exercise_points + exams[pic]:
            grade = 5

    print(f'{name} {grade}')


