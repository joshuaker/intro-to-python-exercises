# Write your solution here
import csv
from datetime import datetime, timedelta
def cheaters():
    start_times = {}
    with open('start_times.csv') as file:
        content = csv.reader(file, delimiter = ';')
        for line in content:
            start_times[line[0]] = line[1]
    task_handin = {}
    with open('submissions.csv') as new_file:
        for line in csv.reader(new_file, delimiter=';'):
            if line[0] not in task_handin:
                task_handin[line[0]] = [line[3]] #this will always replace the last value;
            else:
                task_handin[line[0]].append(line[3])

    #print(task_handin)
    year = 2000
    time_limit = timedelta(hours=3)
    cheaters = []
    # transform string hour:minute into datetime, then compare timedelta for greater than 3 hours
    for name, time in task_handin.items(): 
        start_time_list = start_times[name].split(':')
        start_time = datetime(2000, 1, 1, int(start_time_list[0]), int(start_time_list[1]))
        
        for item in time:
            parts = item.split(':')
            end_time = datetime(2000, 1, 1, int(parts[0]),int(parts[1]))

            if end_time - start_time > time_limit: 
                if name not in cheaters: #unique names
                    cheaters.append(name)
    
    return cheaters

