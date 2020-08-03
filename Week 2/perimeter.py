# Works out the total fence required to fence off perimeter of given diagram, as well as the cost of the fence
# Lonwabo Mvovo
# 13/05/2020

# Infinite loop that breaks if user enters a real number
while True:
    try:
        # Set width 1 to user input
        w1 = int(input('Enter width 1 (in metres): '))
        # Break loop
        break
    # Error message if real number is not entered
    except: print("Please enter a real number.")

# Infinite loop that breaks if user enters a real number
while True:
    try:
        # Set height 1 to user input
        h1 = int(input('Enter height 1 (in metres): '))
        break
    # Error message if real number is not entered
    except: print("Please enter a real number.")

# Infinite loop that breaks if user enters a real number
while True:
    try:
        # Set width 2 to user input
        w2 = int(input('Enter width 2 (in metres): '))
        break
    # Error message if real number is not entered
    except: print("Please enter a real number.")

# Infinite loop that breaks if user enters a real number
while True:
    try:
        # Set height 2 to user input
        h2 = int(input('Enter height 2 (in metres): '))
        break
    # Error message if real number is not entered
    except: print("Please enter a real number.")

# Infinite loop that breaks if user enters a real number
while True:
    try:
        # Set price per metre to user input
        ppm = int(input('Enter price per metre (in Rands): '))
        break
    # Error message if real number is not entered
    except: print("Please enter a real number.")

# Calculate perimeter of given shape
perimeter = w1 * 2 + h1 * 2 + w2 * 2

# Print fence required message
print(f'The total fence required = {perimeter} metres')
# Print total price message 
print(f'The total price = R {perimeter * ppm}')