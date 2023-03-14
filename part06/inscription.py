# Write your solution here
name = input('Whom should I sign this to:')
location = input('Where should I save it:')

with open(location, 'w') as new_file:
    new_file.write(f'Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team')