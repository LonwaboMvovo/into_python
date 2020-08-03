# Tells user if the time they have inputed is valid or not
# Lonwabo Mvovo
# 14/05/2020

# Set the number of hours to a user inputed integer
hours = int(input('Enter the hours:\n'))
# Set the number of minutes to a user inputed integer
minutes = int(input('Enter the minutes:\n'))
# Set the number of seconds to a user inputed integer
seconds = int(input('Enter the seconds:\n'))

# Check if hours is between 0 and 23 (inclusive)
if (-1 < hours < 24 and
# Check if minutes is between 0 and 59 (inclusive)
    -1 < minutes < 60 and
# Check if seconds is between 0 and 59 (inclusive)
    -1 < seconds < 60):
# Print valid time message if all conditions are met
    print('Your time is valid.')
# If any of the conditions are not met print invalid time message 
else: print('Your time is invalid.')