# This code will show you the output of which season a month/day falls in.
input_month = input()
input_day = int(input())

spring = ['March', 'April', 'May', 'June']
summer = ['June', 'July', 'August', 'September']
autumn = ['September', 'October', 'November', 'December']
winter = ['December', 'January', 'March']

# check the month and day for right time of year
if (input_month == 'March') and (20 < input_day < 31):
    print('Spring')
elif (input_month == 'June') and (0 < input_day < 20):
    print('Spring')
elif (input_month == 'April') and (0 < input_day < 30):
    print('Spring')
elif (input_month == 'May') and (0 < input_day < 31):
    print('Spring')
if (input_month == 'June') and (0 < input_day < 20):
    print('Summer')
elif (input_month in 'September') and (0 < input_day < 21):
    print('Summer')
elif (input_month == 'July') and (0 < input_day <= 31):
    print('Summer')
elif (input_month == 'August') and (0 < input_day <= 31):
    print('Summer')
if (input_month == 'September') and (0 < input_day < 21):
    print('Autumn')
elif (input_month == 'December') and (0 < input_day < 20):
    print('Autumn')
elif (input_month == 'October') and (0 < input_day <= 31):
    print('Autumn')
elif (input_month == 'November') and (0 < input_day <= 30):
    print('Autumn')
if (input_month == 'December') and (20 < input_day < 31):
    print('Winter')
elif (input_month == 'March') and (0 < input_day < 19):
    print('Winter')
elif (input_month == 'January') and (0 < input_day <= 31):
    print('Winter')
elif (input_month == 'February') and (0 < input_day <= 28):
    print('Winter')
else:
    print('Invalid')
