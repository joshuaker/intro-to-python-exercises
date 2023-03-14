# tee ratkaisu tänne

def ask_for_info():
    student_info = input('Student information:')
    exercise_info = input('Exercises completed:')
    exam_info = input('Exam points:')
    course_info = input('Course information:')
    return student_info, exercise_info, exam_info, course_info

def course_name(course_info):
    header_list = []
    with open(course_info) as file:
        for line in file:
            line = line.strip('\n')
            parts = line.split(': ')
            header_list.append(parts[1])
    
    course_header = (f'{header_list[0]}, {header_list[1]} credits')
    return course_header

def exam_points(exam_info):
    exam_dict = {}
    with open(exam_info) as file:
        for line in file:
            line = line.strip('\n')
            parts = line.split(';')
            if parts[0] == 'id': #skip header
                continue
            # only 3 exams
            int_list = [int(parts[1]),int(parts[2]),int(parts[3])]
            exam_dict[parts[0]] = [int_list, sum(int_list)]

    return exam_dict

def exercise_points(exercise_info):
    exercise_dict = {}
    with open(exercise_info) as file:
        for line in file:
            line = line.strip('\n')
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            int_list = []
            for item in parts:
                int_list.append(int(item))
            int_list = int_list[1:]

            exercise_dict[parts[0]] = [int_list, sum(int_list)//4]
 
    return exercise_dict

def name(student_info):
    name_dict = {}
    with open(student_info) as file:
        for line in file:
            line = line.strip('\n')
            parts = line.split(';')
            if parts[0] == 'id':
                continue

            name_dict[parts[0]] = f'{parts[1]} {parts[2]}'
    return name_dict

def grade(exercise_dict, exam_dict):
    total_points = {}
    grade_dict = {}

    for key, value in exam_dict.items():
        total_points[key] = exercise_dict[key][1] + exam_dict[key][1]
    
    for key, value in total_points.items():
        points = total_points[key]
        grade = 0
        if points < 15:
            grade = 0
        elif points < 18:
            grade = 1
        elif points < 21:
            grade = 2
        elif points < 24:
            grade = 3
        elif points < 28:
            grade = 4
        else:
            grade = 5
        
        grade_dict[key] = [points, grade]
    return grade_dict
    
def header_formatting():
    header = course_name(course_info)
    header_under = len(header)*'='

    return f'{header}\n{header_under}'

def test():
    student_info, exercise_info, exam_info, course_info = ask_for_info()
    exam_dict = exam_points(exam_info)
    exercise_dict = exercise_points(exercise_info)
    name_dict = name(student_info)
    grade_dict = grade(exercise_dict, exam_dict)
    course_header = course_name(course_info)
    header = header_formatting()

    full_dict = {}

    for key, value in grade_dict.items():
        full_dict[key] = [name_dict[key],sum(exercise_dict[key][0]),exercise_dict[key][1],exam_dict[key][1],grade_dict[key][0],grade_dict[key][1]]
        #pic = name;exercise numbers; exercise points; exam points; total points; grade

    with open('results.txt', 'w') as file:
        header = header_formatting()

        file.write(f'{header}\n')
        file.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade'}\n")
        for key, value in full_dict.items():
            file.write(f"{full_dict[key][0]:30}{full_dict[key][1]:<10}{full_dict[key][2]:<10}{full_dict[key][3]:<10}{full_dict[key][4]:<10}{full_dict[key][5]}\n")

    with open('results.csv', 'w') as file:
        for key, value in full_dict.items():
            file.write(f'{key};{full_dict[key][0]};{full_dict[key][5]}\n')

    print('Results written to files results.txt and results.csv')


test()