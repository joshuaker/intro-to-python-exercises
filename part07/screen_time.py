# Write your solution here
from datetime import datetime, timedelta

filename = input('Filename: ')
start = input('Start date: ')
days = int(input('How many days: ')) #1 day = start and end on same day

while False:
    filename = 'first_of_may.txt'
    start = '1.5.2020'
    days = int('1')


date = datetime.strptime(start, "%d.%m.%Y")
end_date = date + timedelta((days)) - timedelta(1)

print('Please type in screen time in minutes on each day (TV computer mobile): ')
count = 0

total_minutes = 0
screen_time_txt = ''
while count < days:
    increment = timedelta(days = count)
    screen_time = input(f'Screen time {(date + increment).strftime("%d.%m.%Y")}: ')
    parts = screen_time.split(' ')
    for i in parts:
        total_minutes += int(i)
    
    screen_time_txt += f'{(date + increment).strftime("%d.%m.%Y")}: {parts[0]}/{parts[1]}/{parts[2]}\n'
    count += 1

with open(filename, 'w') as file:
        file.write(f'''Time period: {date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n''')
        file.write(f'Total minutes: {total_minutes}\n')
        file.write(f'Average minutes: {total_minutes/days}\n')
        file.write(screen_time_txt)
