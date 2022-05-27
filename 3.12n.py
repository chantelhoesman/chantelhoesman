# find which season by entering month and day

input_month = input()
input_day = int(input())

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'March']

seasons = spring + summer + autumn + winter

dates1 = {20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}
dates2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

dates3 = {21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}
dates4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

dates5 = {22, 23, 24, 25, 26, 27, 28, 29, 30}
dates6 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

dates7 = {20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}
dates8 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}

# Validate if the input is valid
if input_month not in seasons or (input_day not in range(1, 31)):
    print('Invalid')

# check the month and day for right time of year
if (input_month == 'March') and (input_day in dates1):
    print('Spring')
elif (input_month == 'June') and (input_day in dates2):
    print('Spring')
elif input_month == 'April':
    print('Spring')
elif input_month == 'May':
    print('Spring')
if (input_month == 'June') and (input_day in dates3):
    print('Summer')
elif (input_month in 'September') and (input_day in dates4):
    print('Summer')
elif input_month == 'July' and (0 < input_day <= 31):
    print('Summer')
elif input_month == 'August' and (0 < input_day <= 31):
    print('Summer')
if (input_month == 'September') and (input_day in dates5):
    print('Autumn')
elif (input_month == 'December') and (input_day in dates6):
    print('Autumn')
elif input_month == 'October' and (0 < input_day <= 31):
    print('Autumn')
elif input_month == 'November' and (0 < input_day <= 30):
    print('Autumn')
if input_month == 'December' and (input_day in dates7):
    print('Winter')
elif input_month == 'March' and (input_day in dates8):
    print('Winter')
elif input_month == 'January' and (0 < input_day <= 31):
    print('Winter')
elif input_month == 'February' and (0 < input_day <= 28):
    print('Winter')