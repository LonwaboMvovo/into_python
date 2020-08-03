# Prints a sequence of 7 numbers, starting from a value entered by the user
# Lonwabo Mvovo
# 15/05/2020

# Start an infinite while loop that breaks when user enters an integer between -6 and 93 (not inclusive)
while True:
    # Enter a try block
    try:
        # Set 'n' to a user inputed integer representing the start number
        n = int(input('Enter the start number: '))
        # Assert that 'n' is between -6 and 93 (not inclusive). If it is continue otherwise throw an error
        assert -6 < n < 93
        # Break infinite loop
        break
    # Enter an except block that prints an error message for when user doesn't enter an integer between -6 and 93 (not inclusive)
    except: print('Please enter an integer within the range (-6, 93)')

# Set 'row' to 7 numbers starting from 'n' using the splat operator
row = [*range(n, n + 7)]

# Print out the elements of 'row', separating each element with a space, right-justfying them, filling the optional digit with a space and no space after the last field is entered
print(' '.join(f'{x:>2}' for x in row), end='')