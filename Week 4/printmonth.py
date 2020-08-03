# Prints a calendar for a month entered by the user starting on a day the user also chooses
# Lonwabo Mvovo
# 16/05/2020

# Set 'months' to a dictionary of all the months with their corresponding number of days + 1 because later these numbers will be used with the range function and the range function does not include the last number.
months = {
    'January'  : 32,
    'February' : 29,
    'March'    : 32,
    'April'    : 31,
    'May'      : 32,
    'June'     : 31,
    'July'     : 32,
    'August'   : 32,
    'September': 31,
    'October'  : 32,
    'November' : 31,
    'December' : 32
}

# Set 'days' to a dictionary of all the possible start days with their corresponding blank spaces displayed on a calender before that day
days = {
    'Monday'   : 0,
    'Tuesday'  : 1,
    'Wednesday': 2,
    'Thursday' : 3,
    'Friday'   : 4,
    'Saturday' : 5,
    'Sunday'   : 6
}

# Start an infinite while loop that breaks when the user enters a valid month
while True:
    # Enter a try block
    try:
        # Set 'chosen_month' to a month inputed by the user and capitalized in case user types in a different case which won't match with a month in the 'months' dictionary
        chosen_month = input("Enter the month ('January', ..., 'December'):\n").capitalize()
        # Assert that the month inputed is valid by checking if it's in the 'months' dictionary. If it is continue, otherwise throw an error
        assert chosen_month in months
        # Break the infinite loop
        break
    # Enter an except block that prints an error message for when user does not input a valid month
    except: print('Please enter a month of the year from January to December')

# Start an infinite while loop that breaks when the user enters a valid start day
while True:
    # Enter a try block
    try:
        # Set 'start_day' to a day inputed by the user and capitalized in case user types in a different case which won't match with a day in the 'days' dictionary
        start_day = input("Enter the start day ('Monday', ..., 'Sunday'):\n").capitalize()
        # Assert that the day inputed is valid by checking if it's in the 'days' dictionary. If it is continue, otherwise throw an error
        assert start_day in days
        # Break the infinite loop
        break
    # Enter an except block that prints an error message for when user does not input a valid start day
    except: print('Please enter a day of the week from Monday to Sunday')

# Set 'calender_days' to a list of all the days in numbers starting from 1 to the number of days in the month the user has chosen
calender_days = [*range(1, months[chosen_month])]
# Set 'calender_spaces' to a list of all the spaces that should appear on the calender before the start day chosen by user
calender_spaces = [' ' for _ in range(days[start_day])]
# Add 'calender_spaces' to the beginning of 'calender_days'
calender_days = calender_spaces + calender_days
# Add spaces to fill up the displayed calendar to ensure that a 6 row by 7 column grid is printed
for _ in range(42 - len(calender_days)): calender_days.append(' ')
# Set 'calender_weeks' to a list of lists (the weeks) starting from the day in the week's iteration index to that day + 7, separating each element with a space and right-justfying them over 2 digits
calender_weeks = [' '.join(f'{day:>2}' for day in calender_days[week * 7:week * 7 + 7]) for week in range(6)]

# Print the abbreviation of each day of the week by slicing the days in the 'days' dictionary, separating the days with a space
print(*[d[:2] for d in days])
# Print the weeks of the calender on seperate lines and with no space after the end of the calendar
print(*calender_weeks, sep='\n', end='')