# Write your solution here
def points(points_list):
    # processing inputs; valid input is either combination of two integers or blank line
    # first number exam points; second number exercises completed
    # find the whitespace, slice 
        # question: does this work for integers? A: no

    # take points_list and split it into exam points and exercises completed
    exam_points = []
    exercises_completed = []

    for item in points_list:
        index = item.find(' ')
        exam_points.append(item[0:index])
        exercises_completed.append(item[index+1:])

    return exam_points, exercises_completed
    # exam_points and exercises_completed are lists of strings

def string_to_int(
    exam_points, 
    exercises_completed
    ):

    #first need to convert the string form of input into a list of numbers
    
    string_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100']
    numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    exam_points_int = []
    exercises_completed_int = []
    # length of number_list is 101, because you have 0

    for item in exam_points:
        index = string_list.index(item)
        x = numbers_list[index]
        exam_points_int.append(x)
    
    for item in exercises_completed:
        index = string_list.index(item)
        x = numbers_list[index]
        exercises_completed_int.append(x)

    return exam_points_int, exercises_completed_int

def statistics(
    exam_points_int,
    exercises_completed_int
    ):
    
    # breakpoint for exam points; 10
    # need to add exam_points and exercises_copmleted together
    #need to transform exercised_completed into exercise points

    # exercise points is 10% rounded down
    exercise_points = []
    for item in exercises_completed_int:
        e_points = item // 10
        exercise_points.append(e_points)

    points = []
    
    grade = []
    
    # by index i, i+= 1, add numbers together; if number in threshold = grade, if exam_points less, 0
    i = 0
    while i < len(exam_points_int):
        if exam_points_int[i] < 10:
            grade.append(0)
            points.append(exam_points_int[i] + exercise_points[i])
            i += 1
        else:
            total_points = exam_points_int[i] + exercise_points[i]
            points.append(total_points)

            if 0 <= total_points and total_points <= 14:
                grade.append(0)
            elif 15 <= total_points and total_points <= 17:
                grade.append(1)
            elif 18 <= total_points and total_points <= 20:
                grade.append(2)
            elif 21 <= total_points and total_points <= 23:
                grade.append(3)
            elif 24 <= total_points and total_points <= 27:
                grade.append(4)
            elif 28 <= total_points and total_points <= 30:
                grade.append(5)
            
            i += 1

    #using grade list
    number_of_entries = len(points)
    points_sum = sum(points)
    average = points_sum/number_of_entries #points average points average not grade average

    fails = grade.count(0)
    pass_percentage = ( (number_of_entries - fails) / number_of_entries ) * 100 #pass percentage

    return grade, average, pass_percentage

def stars(
    grade
    ):
    grade_5 = 0
    grade_4 = 0
    grade_3 = 0
    grade_2 = 0
    grade_1 = 0
    grade_0 = 0

    for item in grade:
        if item == 5:
            grade_5 += 1
        elif item == 4:
            grade_4 += 1
        elif item == 3:
            grade_3 += 1
        elif item == 2:
            grade_2 += 1
        elif item == 1:
            grade_1 += 1
        elif item == 0:
            grade_0 += 1
    
    print(f'''Grade distribution:
  5: {'*' * grade_5}
  4: {'*' * grade_4}
  3: {'*' * grade_3}
  2: {'*' * grade_2}
  1: {'*' * grade_1}
  0: {'*' * grade_0}''')


points_list = []
while True:
    points_query = input('Exam points and exercises completed:')
    if points_query == '':
        break
    else:
        points_list.append(points_query)

exam_points, exercises_completed = points(points_list)

exam_points_int, exercises_completed_int = string_to_int(exam_points, exercises_completed)

grade, average, pass_percentage = statistics(exam_points_int, exercises_completed_int)

print(f'''Statistics:
Points average: {average}
Pass percentage: {pass_percentage:.1f}''')
stars(grade)
