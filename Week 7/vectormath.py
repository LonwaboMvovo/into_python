# Basic vector calculations in 3 dimensions: addition, dot product and normalization
# Lonwabo Mvovo
# 23/05/2020

# Import 'sqrt' (square-root) function from the math library
from math import sqrt

# Start an infinite while loop that breaks when the user inputs 3 space separated numbers for vector A
while True:
    # Enter a try block
    try:
        # Set 'vector_a' to a tuple of integers or floats inputed by the user for vector A
        vector_a = tuple(int(num) if num.isdigit() else float(num) for num in input("Enter vector A:\n").split())
        # Assert that the length of 'vector_a' is 3 to insure that the user inputed 3 numbers
        assert len(vector_a) == 3
        # Break from the infinite loop
        break
    # Enter a try block that prints an invalid input message for when the user does not input 3 space separated numbers for vector A
    except: print('Please enter 3 space separated numbers for vector A.')

# Start an infinite while loop that breaks when the user inputs 3 space separated numbers for vector B
while True:
    # Enter a try block
    try:
        # Set 'vector_b' to a tuple of integers or floats inputed by the user for vector B
        vector_b = tuple(int(num) if num.isdigit() else float(num) for num in input("Enter vector B:\n").split())
        # Assert that the length of 'vector_b' is 3 to insure that the user inputed 3 numbers
        assert len(vector_b) == 3
        # Break from the infinite loop
        break
    # Enter a try block that prints an invalid input message for when the user does not input 3 space separated numbers for vector B
    except: print('Please enter 3 space separated numbers for vector B.')

# Print the sum of the vectors A and B
print('A+B =', [sum(xy) for xy in zip(vector_a, vector_b)])
# Print the dot product of the vectors A and B
print('A.B =', sum(x * y for x, y in zip(vector_a, vector_b)))
# Print the norm of vector A
print('|A| =', round(sqrt(sum([x ** 2 for x in vector_a])), 2))
# Print the norm of vector B
print('|B| =', round(sqrt(sum([y ** 2 for y in vector_b])), 2))