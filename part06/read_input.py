# Write your solution here
def read_input(string:str,
            lower_bound:int,
            upper_bound:int
               ):
    while True:
        try:
            num = int(input(string))
            if lower_bound < num < upper_bound: #python
                return num
        except:
            pass
        print(f'You must type in an integer between {lower_bound} and {upper_bound}')
