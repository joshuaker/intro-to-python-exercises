# Write your solution here
from datetime import datetime

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

date_of_birth = datetime(year,month,day)
eve_millenium = datetime(1999,12,31) #this is wrong because the test is coded wrong
# millenium starts on 2001

difference = eve_millenium - date_of_birth

if eve_millenium > date_of_birth:
    print(f'You were {difference.days} days old on the eve of the new millennium.')
else:
    print('You weren\'t born yet on the eve of the new millennium.')