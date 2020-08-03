# Calendar functions that determine if given year is a leap year,
# convert month number to month name, returns the number of days in a month within a specific year, 
# returns the first day of a given year and returns the first day of a given month within a given year
# Lonwabo Mvovo
# 18/05/2020

# Define function 'is_leap_year' that returns true if the year given as an argument is a leap year otherwise will return false
def is_leap_year(year):
    # Check if 'year' is divisible by 4 completely and is not divisible by 100 completely
    if (year % 4 == 0 and year % 100 != 0
        or
        # Check if 'year' is divisible by 400 completely
        year % 400 == 0):
        # If either of the conditions are true, return 'True' which means the year inputed is a leap year
        return True
    # Since none of ther conditions are true, return 'False' which means the year inputed is not a leap year
    return False


# Define function 'month_name' that returns name of the month when the number of the month is given as an argument
def month_name(number):
    # Return the name of the month by using the months index from a list of all the months in order
    return [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'][number - 1] # Index is 'number - 1' because lists index from 0


# Define function 'days_in_month' that returns the number of days in a specific month (given as the functions first argument) and year (given as the functions second argument)
def days_in_month(month_number, year): 
    # Check if 'month_number' is 2 (means the month is February). If it is then return 29 if the year is a leap year (check by calling 'is_leap_year'), otherwise return 28
    if month_number == 2: return 29 if is_leap_year(year) else 28
    # Check if 'month_number' is less than 8 and odd or 'month_number' is greater than 7 and even. These conditions are true if the month has 31 days, so if either condition is true return 31
    if month_number < 8 and month_number % 2 != 0 or month_number > 7 and month_number % 2 == 0: return 31 
    # Since none of the above mentioned conditions are true, the month has 30 days so the function must return 30
    return 30

# Define function 'first_day_of_year' that returns the day as a number that January 1st will be on from a year (given as an argument) will be on
def first_day_of_year(year):
    # Return day using Gaus's formula
    return (1 + (year - 1) % 4 * 5 + (year - 1) % 100 * 4 + (year - 1) % 400 * 6) % 7


# Define function 'first_day_of_month' that returns the day as a number that the 1st of a month (given as the functions first argument) will be on from a year (given as the functions second argument) will be on
def first_day_of_month(month_number, year):
    # Set 'month_start_day' to the day that January 1st will be on
    month_start_day = first_day_of_year(year)
    # Start a for loop with as many iterations as the month's number minus 1
    for i in range(1, month_number):
        # Check if 'i' is 2 (means the month is February). If it is then update 'month_start_day' to the remainder of dividing the previous value of 'month_start_day' plus 29 if the year is a leap year (check by calling 'is_leap_year'), otherwise plus 28 by 7 (number of days per week)
        if i == 2: month_start_day = (month_start_day + 29) % 7 if is_leap_year(year) else (month_start_day + 28) % 7
        # Check if 'i' is less than 8 and odd or 'i' is greater than 7 and even. These conditions are true if the month at the current iteration has 31 days, so if either condition is true update 'month_start_day' to the remainder of dividing the previous value of 'month_start_day' plus 31 by 7 (number of days per week)
        elif i < 8 and i % 2 != 0 or i > 7 and i % 2 == 0: month_start_day = (month_start_day + 31) % 7
        # Since none of the above mentioned conditions are true, the month has 30 days so update 'month_start_day' to the remainder of dividing the previous value of 'month_start_day' plus 30 by 7 (number of days per week)
        else: month_start_day = (month_start_day + 30) % 7
    # Return 'month_start_day' which will be the day as a number that the 1st of a month will be on
    return month_start_day


# # Set variable 'days_of_the_week' to a list of all the days of the week in the order that is used by the functions
# days_of_the_week = [
#     'Sunday',
#     'Monday',
#     'Tuesday',
#     'Wednesday',
#     'Thursday',
#     'Friday',
#     'Saturday']

# # Start an infinite while loop
# while True:
#     # Enter a try block
#     try:
#         # Set variable 'chosen_option' to an integer inputed by the user that corresponds with the option they would like to try
#         chosen_option = int(input('''Choose from the following options:
# 0. quit
# 1. Test is_leap_year().
# 2. Test month_name().
# 3. Test days_in_month().
# 4. Test first_day_of_year().
# 5. Test first_day_of_month().
# '''))
#         # Assert that 'chosen_option' is greater than or equal to 0 and less than 6. If it is continue, otherwise throw an error
#         assert 0 <= chosen_option < 6
#         # Check if 'chosen_option' is 0. If it is it means the user would like to quit so break from infinite loop
#         if chosen_option == 0: break
#         # Otherwise check if 'chosen_option' is 1. If it is it means the user would like to test 'is_leap_year' so run this code
#         elif chosen_option == 1:
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'ily_arg' to a 4 digit integer inputed by the user which will be the argument used when calling 'is_leap_year'
#                     ily_arg = int(input('Enter the year (4 digits):\n'))
#                     # Assert that 'ily_arg' has 4 digits by checking its length. If it does continue, otherwise throw an error
#                     assert len(str(ily_arg)) == 4
#                     # Since the user has inputed a valid year, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid year
#                 except: print('Please enter a four digit number representing a valid year.')
#             # Check if calling 'is_leap_year' with 'ily_arg' as the argument is true. If it is print leap year message
#             if is_leap_year(ily_arg): print(f'The year {ily_arg} is a leap year.')
#             # Since calling 'is_leap_year' with 'ily_arg' as the argument is false print not leap year message
#             else: print(f'The year {ily_arg} is not a leap year.')
#         # Otherwise check if 'chosen_option' is 2. If it is it means the user would like to test 'month_name' so run this code
#         elif chosen_option == 2:
#             # Print all the month's numbers and corresponding names in separate messages
#             for i in range(1, 13): print(f'Month number {i} is {month_name(i)}.')
#         # Otherwise check if 'chosen_option' is 3. If it is it means the user would like to test 'days_in_month' so run this code
#         elif chosen_option == 3:
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'dim_arg_1' to an integer inputed by the user which will be the first argument used when calling 'days_in_month'
#                     dim_arg_1 = int(input('Enter the month (1 - 12):\n'))
#                     # Assert that 'dim_arg_1' is greater than to 0 and less than 13. If it is continue, otherwise throw an error
#                     assert 0 < dim_arg_1 < 13
#                     # Since the user has inputed a valid number for month, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid number for month
#                 except: print('Please enter the month as a number from 1-12. 1 = January, 2 = February, ..., 12 = December.')
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'dim_arg_2' to a 4 digit integer inputed by the user which will be the second argument used when calling 'days_in_month'
#                     dim_arg_2 = int(input('Enter the year (4 digits):\n'))
#                     # Assert that 'dim_arg_2' has 4 digits by checking its length. If it does continue, otherwise throw an error
#                     assert len(str(dim_arg_2)) == 4
#                     # Since the user has inputed a valid year, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid year
#                 except: print('Please enter a four digit number representing a valid year.')
#             # Print a message that informs user how many days the month inputed has in the year inputed
#             print(f'In the year {dim_arg_2}, {month_name(dim_arg_1)} lasts {days_in_month(dim_arg_1, dim_arg_2)} days.')
#         # Otherwise check if 'chosen_option' is 4. If it is it means the user would like to test 'first_day_of_year' so run this code
#         elif chosen_option == 4:
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'fdoy_arg' to a 4 digit integer inputed by the user which will be the argument used when calling 'first_day_of_year'
#                     fdoy_arg = int(input('Enter the year (4 digits):\n'))
#                     # Assert that 'fdoy_arg' has 4 digits by checking its length. If it does continue, otherwise throw an error
#                     assert len(str(fdoy_arg)) == 4
#                     # Since the user has inputed a valid year, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid year
#                 except: print('Please enter a four digit number representing a valid year.')
#             # Print a message that informs the user which day the first of January will fall on
#             print(f'The year {fdoy_arg} will start on a {days_of_the_week[first_day_of_year(fdoy_arg)]}.')
#         # Since 'chosen_option' is not any of the other options, it is 5. This means the user would like to test 'first_day_of_month' so run this code
#         else:
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'fdom_arg_1' to an integer inputed by the user which will be the first argument used when calling 'first_day_of_month'
#                     fdom_arg_1 = int(input('Enter the month (1 - 12):\n'))
#                     # Assert that 'fdom_arg_1' is greater than to 0 and less than 13. If it is continue, otherwise throw an error
#                     assert 0 < fdom_arg_1 < 13
#                     # Since the user has inputed a valid number for month, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid number for month
#                 except: print('Please enter the month as a number from 1-12. 1 = January, 2 = February, ..., 12 = December.')
#             # Start an infinite while loop
#             while True:
#                 # Enter a try block
#                 try:
#                     # Set 'fdom_arg_2' to a 4 digit integer inputed by the user which will be the second argument used when calling 'first_day_of_month'
#                     fdom_arg_2 = int(input('Enter the year (4 digits):\n'))
#                     # Assert that 'fdom_arg_2' has 4 digits by checking its length. If it does continue, otherwise throw an error
#                     assert len(str(fdom_arg_2)) == 4
#                     # Since the user has inputed a valid year, break from the infinite loop
#                     break
#                 # Enter except block that prints an error message if the user does not enter a valid year
#                 except: print('Please enter a four digit number representing a valid year.')
#             # Print a message that informs the user which day the first of the month inputed will fall on in the year inputed
#             print(f'In the year {fdom_arg_2}, the first of {month_name(fdom_arg_1)} falls on a {days_of_the_week[first_day_of_month(fdom_arg_1, fdom_arg_2)]}.')
#     # Enter except block that prints an error message if the user does not enter a option
#     except: print('Please enter a number from 0 - 5 that corresponds with the option you would like to try.')

# 1. 
# So the first function they want us to make is "is_leap_year()" which takes a year given as a parameter and will return True if the year is a leap year and 
# False if the year is not a leap year

# 2. 
# So with the 'month_name' function they want us to return the name for the month when they give the number of the month which will be the parameter 'number'. So for example if the number is 5 your function must return May. For this one you can use a list that has all the month names in their order like 'month_list = ["January", "February", ..., "December"]' so that you can do something like: return month_list[number] and this will return the name

# 3.
# For the 'days_in_month' function they are going to give 2 parameters: month_number (representing the number of the month ex 3 is March) and year (representing the year you must check for).You must return a number indincating how many days in that month. All the other months will not change how many days there is no matter the yearbut Feb changes from 28 to 29 if it is a leap year so you must return a differenct number for Feb depending if the year is a leap year or not. For this one you can also use a list with all the number of days of each month in order but then use an if statement if 'month_number' is 2 to check if it is a leap year.

# 4.
# For the 'first_day_of_year' this one we have basically already done because in week 3 we did the 'firstday' assignment so you must just use that equation to return the first day of the year.

# 5.
# For the 'first_day_of_month' this one is a bit tricky but it uses functions you have done. So they want you to return the number of day (ex 1 is Monday and 6 is Saturday) and they are going to give 2 parameters: month_number (representing the number of the month ex 3 is March) and year (representing the year you must check for).For example let's say 'month_number' is 6 and 'year' is 2020What I did was using 'first_day_of_year' you will get a start number representing the firstday of the year and for this example it will be 3 so now we know in 2020 January starts on a wednesday.Then one by one we add the number of days per month using 'days_in_month' so we will get 3 + 31 (Days in Jan) + 29 (Feb: because 2020 is a leap year) + 31 (Mar) + 30 (Apr) + 31 (May) = 155. Then we must divide this number by 7 (because there are 7 days in a week) and the remainder will be the first day of June in 2020. In python we can use the modulus operator to get remainder's so 155 % 7 = 1. Therefore June in 2020 starts on Monday which is what you must return