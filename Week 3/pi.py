# Calculates the value of Pi using a formula and also computes and displays the area of a circle with radius entered by the user
# Lonwabo Mvovo
# 15/05/2020

# Import the sqrt function from the math library
from math import sqrt

# Set 'term_numerator' initially to the first term's numerator in the forumula
term_numerator = sqrt(2)
# Set 'ans' initially to the first term in the formula
ans = term_numerator / 2

# Start infinite loop that will keep updating 'ans' to the multiplication of itself and the next term until the size of the next term is 1
while True:
    # Update the 'term_numerator' to the square root of 2 plus the previous numerator
    term_numerator = sqrt(2 + term_numerator)
    # Set 'term' to the term's numerator divided by 2
    term = term_numerator / 2
    # Check if the size of the term is 1 and if it is break the infinite loop
    if term == 1: break
    # Update 'ans' to the multiplication of itself and 'term' since it is not equal to 1 
    ans *= term

# Set 'pi_approx' to what the approximation of pi will be from using the given formula
pi_approx = 2 / ans

# Start infinite loop that will break when a positive real number is inputed by the user for the radius of a circle
while True:
    # Enter try block
    try:
        # Print the approximation of pi rounded to 3 decimal places and set 'radius' to a float inputed by the user
        radius = float(input(f'Approximation of pi: {round(pi_approx, 3)} Enter the radius:\n'))
        # Break the infinite loop
        break
    # Enter except block that prints out an error message for when user does not enter a positive real number
    except ValueError: print('Please enter a positive Real number [0, ∞) for the radius')

# Set 'area' to the area of a circle with a radius inputed by the user rounded to 3 decimal places
area = round(pi_approx * radius ** 2, 3)

# Print area message 
print(f'Area: {area}')