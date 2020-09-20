n = 0
while True:
    try:
        n = int(input('Please, Enter the Number of Month: '))
    except ValueError:
        print('That is not an integer, please enter a valid number within the range of 1 and 12')
    if n== 1:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 2:
        yr = int(input('Please, Which Year? \nEnter the Year Please: '))
        if yr % 4 == 0 and yr % 100 != 0:
            print('The number of month ', n, ' in the year ', yr, ' has 29 days in it (a leap year)')
        elif yr % 4 == 0 and yr % 100 == 0 and yr % 400 ==0:
            print('The number of month ', n, ' in the year ', yr, '  has 29 days in it (a leap year)')
        else:
            print('The number of month ', n, ' in the year ', yr, '  has 28 days in it (a common year)')
    elif n == 3:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 4:
        print('The number of month you Entered is ', n, ' which has 30 days in it')
    elif n == 5:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 6:
        print('The number of month you Entered is ', n, ' which has 30 days in it')
    elif n == 7:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 8:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 9:
        print('The number of month you Entered is ', n, ' which has 30 days in it')
    elif n == 10:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    elif n == 11:
        print('The number of month you Entered is ', n, ' which has 30 days in it')
    elif n == 12:
        print('The number of month you Entered is ', n, ' which has 31 days in it')
    else:
        print('Sorry! The number of the month must be an integer and in the range [1 to 12]')

# To exit the program press ctrl c