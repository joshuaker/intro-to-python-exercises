# Write your solution here
import csv
from datetime import datetime, timedelta

def final_points():
    #if multiple submissions; submission with highest point is valid
    #dictionary format
    #if over three hour time, ignored

    start_times = {}
    #desired format is start_times['name'] : datetime(... hh,mm)
    with open("start_times.csv") as file:
        content = csv.reader(file, delimiter = ';') 
        #content format is ['name', 'hh:mm']
        for line in content:
            x = line[1].split(':')
            time_format = datetime(2000, 1, 1, int(x[0]),int(x[1]))
            start_times[line[0]] = time_format
    submissions = {}
    #desired format is submissions[name] : [tasks[task]: ..., tasks[task]: ...]
    valid_time = timedelta(hours = 3)
    #task[tasks]: [(points, h:mm), (points, h:mm)]
    with open("submissions.csv") as file:
        content = csv.reader(file, delimiter = ';')
        #content format is [name,task,points,hh:mm]
        for line in content:
            name = line[0]
            task = int(line[1])
            points = int(line[2])
            x = line[3].split(':')
            end_time_format = datetime(2000, 1, 1, int(x[0]),int(x[1])) #submission time
            
            #i want only valid time submissions; if not valid, ignore (continue) to next line
            if end_time_format-start_times[name] > valid_time:
                continue
            
            if name not in submissions:
                submissions[name] = [[task, points]]
            else:
                submissions[name].append([task,points])                

    best_grades = {}
    # submissions format is name : [ (task#, points), (task#, points)]
    for key, value in submissions.items():
        total_points = []
        for i in range(1,9): #because no exercise 0
            max = 0
            for item in value: #item = individual task submissions pairs [task no., points]
                if item[0] == i:
                    if item[1] > max:
                        max = item[1]
            total_points.append(max)
        best_grades[key] = sum(total_points)

    return best_grades

