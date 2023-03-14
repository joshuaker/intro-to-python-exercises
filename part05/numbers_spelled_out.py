# Write your solution here

def dict_of_numbers():
    numbers = {}
    digits = {0:'zero', 1: 'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    tens = {1:'ten',2: 'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    teens = {10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}

    # i // 10 determines the tens position
    # i - i//10*10 determines the digit position of i>9
    for i in range(100):
        if i//10 > 1:
            if (i - (i//10)*10) != 0:  # for tens with digit != 0
                numbers[i] = f'{tens[i//10]}-{digits[(i - (i//10)*10)]}'
            else:
                numbers[i] = tens[i//10] #for the tens with digit = 0
        elif i//10 == 1:
            numbers[i] = teens[i]
        elif i < 10:
            numbers[i] = digits[i]

    return numbers

if __name__ == '__main__':
    numbers = dict_of_numbers()
    print(numbers[2])
    print(numbers[11])
    print(numbers[45])
    print(numbers[99])
    print(numbers[0])