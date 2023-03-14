# Write your solution here
#ddmmyyXyyyz, where ddmmyy contains the date of birth, X is the marker for century, yyy is the personal identifier and z is a control character.
#The first half of the code is a valid, existing date in the format ddmmyy.
#The century marker is either + (1800s), - (1900s) or A (2000s).
#The control character is valid.
from datetime import datetime

def is_it_valid(pic: str):
    control = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    if len(pic) != 11: #if pic incorrect length
        return False
    
    if pic[6] not in ['-','+','A']: #check century marker
        #print('error A')
        return False
    
    date = int(pic[0:2])
    month = int(pic[2:4])
    year = 0000
    if pic[6] == '+':
        year = int(f'18{pic[4:6]}')
    elif pic[6] == '-':
        year = int(f'19{pic[4:6]}')
    else:
        year = int(f'20{pic[4:6]}')

    if not 1 <= date <= 31: #check valid date
        #print('error date')
        return False
    if not 1 <= month <= 12: #check valid month
        #print('error month')
        return False
    
    try:
        dob = datetime(year, month, date) #year, month, date
    except:
        return False
    
    if dob > datetime.now(): # if person is born in the future
        #print('error B')
        return False
    
    control_character = control[int(f'{pic[0:6]}{pic[-4:-1]}')%31]
    if pic[-1] != control_character:
        #print('error C')
        return False
    
    return True

