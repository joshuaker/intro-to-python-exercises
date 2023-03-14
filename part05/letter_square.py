alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
pairs = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
         8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
         15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 
         20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}


layer = int(input('Layers:'))
side = layer*2 -1
coordinates = []
co_pair = {} #(coordinate): letter

# outward layer inward by i += 1
i = 0
while layer - i > 0:
    for num in range(0+i,side-i): #columns
        co_pair[(i,num)] = pairs[(layer - i)] #top row
        co_pair[(num,i)] = pairs[(layer - i)] #first column
        co_pair[(side-1 -i,num)] = pairs[(layer - i)] #bottom row
        co_pair[(num, side-1-i)] = pairs[(layer - i)] #last column
    i += 1        

# creating matrix template, so that the coordinates[x][y] can work
for i in range(side):
    coordinates.append([])
    num = 0
    while num < side:
        coordinates[i].append('')
        num += 1

# taking {(0,0}:'letter'...) and putting it into a list matrix
for key, value in co_pair.items():
    x, y = key
    coordinates[x][y] = value

# taking list matrix and printing it (remember sudoku?)
for row in coordinates:
    for item in row:
        print(item, end='')
    print()
