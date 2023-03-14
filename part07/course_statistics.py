# Write your solution here

import urllib.request
import json
from math import floor

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    courses = json.loads(my_request.read()) #need the .read()
    #format = [dictionary, dictionary, dictionary]
    answer = []
    for course in courses:
        if course['enabled'] == True:
    # wanted information (fullName, name, year, sum of values listed in exercises)

            fullName = course['fullName']
            name = course['name']
            year = course['year']
            e_sum = sum(course['exercises'])

            answer.append((fullName, name, year, e_sum))

    return answer

def retrieve_course(course_name:str):
    my_request = urllib.request.urlopen(f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats')
    course = json.loads(my_request.read()) 
    #format is {0:{}, 1:{}, 2:{}, 3:{}}

    weeks = len(course)
    max_students = 0
    hours = 0 #total hours over all weeks
    exercises = 0


    for week in course: #need to access dictionary inside value, therefore course[week] for first dict, then ['name'] for second dict
        students = course[week]['students']
        if students > max_students:
            max_students = students
        
        hours += course[week]['hour_total']

        exercises += course[week]['exercise_total']

    hours_average = floor(hours/max_students)
    exercise_average = floor(exercises/max_students)
    #need floor() to round down to closest integer

    answer = {
            'weeks': weeks, 
            'students': max_students, 
            'hours': hours, 
            "hours_average": hours_average, 
            'exercises': exercises, 
            'exercises_average': exercise_average
            }
    
    return answer