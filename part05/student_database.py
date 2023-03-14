def add_student(
    students:dict,
    name:str
    ):
    students[name] = [] # list of courses
    
    return students

def print_student(
    students: dict,
    name: str
    ):
    
    if not name in students:
        print(f'{name}: no such person in the database')
    else:
        if students[name] == []:
            print(f'''{name}:\n no completed courses''')
        else:
            number = len(students[name])
            print(f'''{name}:\n {number} completed courses:''')
            grade_list = []
            for course_tuple in students[name]:
                x, y = course_tuple
                grade_list.append(y)
                print(f'''  {x} {y}''')
            gpa = sum(grade_list)/number
            print(f' average grade {gpa}')

def add_course(
    students:dict,
    name:str,
    course_data:tuple
    ):
    if course_data[1] == 0:
        return
    
    # students = {'Peter': [(course 1, grade),(course 2, grade)]}
    for person in students:
        list_of_courses = [] 
        list_of_grades = []
        for courses in students[name]:
            list_of_courses.append(courses[0]) #create helper list
            list_of_grades.append(courses[1])
            
        if course_data[0] in list_of_courses:
            index = list_of_courses.index(course_data[0])
            if course_data[1] > list_of_grades[index]:
                students[name].remove((list_of_courses[index], list_of_grades[index]))
                students[name].append(course_data)
        else:
            students[name].append(course_data)
    
def summary(
    students: dict
    ):
    #{name: [(),(),(),()], name2: [(),(),()]}

    course_lengths = []
    names_list = []
    gpa_list = []
    for names, courses_list in students.items():
        course_lengths.append(len(courses_list))
        names_list.append(names)

        grades = []
        for courses in courses_list:
            grades.append(courses[1])

        gpa_list.append(sum(grades)/len(courses_list))

    most_courses = max(course_lengths)
    most_index = course_lengths.index(most_courses)
    most_name = names_list[most_index]
    
    best_grade = max(gpa_list)
    best_index = gpa_list.index(best_grade)
    best_name = names_list[best_index]
    
    print(f'students {len(names_list)}')
    print(f'most courses completed {most_courses} {most_name}')
    print(f'best average grade {best_grade} {best_name}')

