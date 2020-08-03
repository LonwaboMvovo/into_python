# Prints out numbers starting from a number inputed by user to that number + 41 over 6 rows
# Lonwabo Mvovo
# 16/05/2020

# Start an infinite while loop that breaks when user enters an integer between -6 and 2
while True:
    # Enter a try block
    try:
        # Set 'n' to a user inputed integer representing the start number
        n = int(input('Enter the start number: '))
        # Assert that 'n' is between -6 and 2. If it is continue otherwise throw an error
        assert -6 < n < 2
        # Break the infinite loop
        break
    # Enter an except block that prints an error message for when user does not enter an integer between -6 and 2
    except: print('Please enter an integer between -6 and 2')

# Set 'grid_elements' to a list of all the integers starting from 'n' to 'n' + 41
grid_elements = [*range(n, n + 42)]

# Set 'grid_rows' to a list of lists (rows) with 7 elements from 'grid_elements' starting from the iterations index, separating each element with a space and right-justfying them over 2 digits
grid_rows = [' '.join(f'{num:>2}' for num in grid_elements[row_index * 7: row_index * 7 + 7]) for row_index in range(6)]

# Print all elements in 'grid_rows' (which are rows of numbers) on separate lines and adding no space after the last row is entered
print(*grid_rows, sep='\n', end='')