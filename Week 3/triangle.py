# Calculates the area of a triangle from user inputed sides using Heron's formula
# Lonwabo Mvovo
# 14/05/2020

# import the sqrt function from the math library
from math import sqrt

# Start infinite loop that breaks when a valid input for side a is entered
while True:
    # Enter a try block
    try:
        # Set side a to an evaluated user inputed
        a = eval(input('Enter the length of the first side: '))
        # Break from loop
        break
    # Enter except block that prints error message for when a real number is not entered for side a
    except ValueError: print('Please enter a Real number for the length of the first side')
# Start infinite loop that breaks when a valid input for side b is entered
while True:
    # Enter a try block
    try:
        # Set side b to an evaluated user inputed
        b = eval(input('Enter the length of the second side: '))
        # Break from loop
        break
    # Enter except block that prints error message for when a real number is not entered for side b
    except ValueError: print('Please enter a Real number for the length of the second side')
# Start infinite loop that breaks when a valid input for side c is entered
while True:
    # Enter a try block
    try:
        # Set side c to an evaluated user inputed
        c = eval(input('Enter the length of the third side: '))
        # Break from loop
        break
    # Enter except block that prints error message for when a real number is not entered for side c
    except ValueError: print('Please enter a Real number for the length of the third side')

# Assign half of the triangles perimeter to a variable 'hp'
hp = (a + b + c) / 2

# Calculate the area of triangle with Heron's formula and assign this to variable 'area'
area = sqrt(hp * (hp - a) * (hp - b) * (hp-c))

# Print out the sides used in calcuation and the area of the triangle
print(f'The area of the triangle with sides of length {a} and {b} and {c} is {area}.')