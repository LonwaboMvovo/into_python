# Calculator that can perform all basic operations
# Lonwabo Mvovo
# 13/05/2020

# Calculator function
def better_calculator():
    # Infinite loop that only breaks if a real number is entered for the first number
    while True:
        try:
            # Set the first number
            num1 = float(input('Fist Number: '))
            break
        except ValueError:
            print('Please enter a real number')

    # Infinite loop that only breaks if a basic operator is entered
    while True:
        try:
            # Set the operator
            operator = input('\nOperator: ')
            assert operator == '+' or operator == '-' or operator == '*' or operator == '/'
            break
        except:
            print('Please enter a basic operator')

    # Infinite loop that only breaks if a real number is entered for the second number
    while True:
        try:
            # Set the second number
            num2 = float(input('\nSecond Number: '))
            break
        except ValueError:
            print('Please enter a real number')
    
    # Check if operator is add and if true add the numbers
    if operator == '+': return num1 + num2

    # Check if operator is subtract and if true return the second number subtracted from the first
    elif operator == '-': return num1 - num2

    # Check if operator is multiply and if true return the multiplication of the numbers
    elif operator == '*': return num1 * num2

    # The only operator left is divide so check if the denomenator is zero and if true return error message
    elif num2 == 0: return 'Math ERROR. Cannot divide by zero'

    # Operator is divide and the second number is not equal to zero so return the first number divided by the second
    else: return num1 / num2


# Print the answer
print('\n' + str(better_calculator()))