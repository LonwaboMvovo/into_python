# Prints every 7th number on a new line in a range starting from a value between -6 and 2 entered by the user to that number plus 41 
# Lonwabo Mvovo
# 16/05/2020

# Start an infinite while loop that breaks when user enters an integer between -6 and 2
while True:
    # Enter a try block
    try:
        # Set 'n' to an integer inputed by the user representing the start number
        n = int(input('Enter a number: '))
        # Assert that 'n' is within -6 and 2. If it is continue otherwise throw an error
        assert -6 < n < 2
        # Break the infinite loop
        break
    # Enter an except block that prints an error message for when user does not enter an integer between -6 and 2
    except: print('Please enter an integer within range (-6, 2)')

# Set 'column' to a list of every 7th number in a range starting from 'n' to 'n' + 41
column = [*range(n, n + 42, 7)]

# Print out numbers in 'column' on different lines using field width of 2, right-justified and representing [d] as a space if needed
print('\n'.join(f'{y:>2}' for y in column), end='')