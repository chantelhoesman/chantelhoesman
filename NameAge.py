# This program will tell the year the user was born
user_name = input('What is your name: ')
user_age = input('How old are you: ')

# formula
user_year = 2022 - int(user_age)
print('Hello', user_name + '!', 'You were born in', str(user_year) + '.')


# To better run this program I would opt for a 3rd prompt asking the user the
# current year, so it can be used more than one year.

user_name = input('What is your name: ')
user_age = input('How old are you: ')
current_year = input('What is the current year: ')

# formula
user_year = int(current_year) - int(user_age)
print('Hello', user_name + '!', 'You were born in', str(user_year) + '.')
