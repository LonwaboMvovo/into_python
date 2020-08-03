# Determines the day that January 1st will be on for each year in a user inputed range of years using Gaus's formula
# Lonwabo Mvovo
# 13/05/2020

# Set 'days' variable to a list of the days of the week in the order used by Gaus's formula
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Start infinite loop that breaks when user inputs an 4 digit integer for year 1
while True:
    # Enter try block
    try:
        # Set 'first_year' to a user inputed integer for the first year
        first_year = int(input('Enter the first year:\n'))
        # Assert that 'first_year' is a 4 digit number
        assert len(str(first_year)) == 4
        # Break infinite loop
        break
    # Enter exccept block that prints error message for when user doesn't input an 4 digit integer for year 1
    except: print('Please enter a four digit number representing a valid fist year.')

# Start infinite loop that breaks when user inputs an 4 digit integer for year 2
while True:
    # Enter try block
    try:
        # Set 'second_year' to a user inputed integer for the second year
        second_year = int(input('Enter the second year:\n'))
        # Assert that 'second_year' is a 4 digit number
        assert len(str(second_year)) == 4
        # Break infinite loop
        break
    # Enter exccept block that prints error message for when user doesn't input an 4 digit integer for year 2
    except: print('Please enter a four digit number representing a valid second year.')

# Start for loop with range of the absolute difference between the years that will print message for each year
for i in range(abs(second_year - first_year) + 1):
    # Set 'year' of current iteration to the first year minus the iteration index if 'second_year' is lower than 'first_year' otherwise first year plus the iteration index
    year = first_year - i if second_year < first_year else first_year + i
    # Gaus's formula to calculate a number that relates to the day that January 1st will be on
    day_number = (1 + (year - 1) % 4 * 5 + (year - 1) % 100 * 4 + (year - 1) % 400 * 6) % 7
    # Print a message that tells the user which day January 1st falls on for 'year' of current iteration
    print(f'The 1st of January {year} falls on a {days[day_number]}')