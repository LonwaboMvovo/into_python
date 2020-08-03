# Simple arithmetic functions for the Bukiyip language
# Lonwabo Mvovo
# 19/05/2020

# Define 'bukiyip_to_decimal' which returns a decimal (base-10) number when a bukiyip (base-3) number taken as a parameter is given
def bukiyip_to_decimal(a):
    # Convert 'a' into a list of strings because an integer is given as an argument
    a = list(str(a))
    # Return the decimal number by summing 3 to the power of a numbers iteration index for all the numbers in list 'a' starting from the end
    return sum([int(a[-i - 1]) * 3 ** i for i in range(len(a))])


# Define 'decimal_to_bukiyip' which returns a bukiyip (base-3) number when a decimal (base-10) number taken as a parameter is given
def decimal_to_bukiyip(a):
    # Set 'buk_num' to an empty list which will represent the bukiyip (base-3) number
    buk_num = []
    # Start an infinite while loop that breaks when the floor division of 'a' by 3 equals 0
    while True:
        # Insert the remainder received from dividing 'a' by 3 converted to a string to the begining of 'buk_num'
        buk_num.insert(0, str(a % 3))
        # Check if the floor division of 'a' by 3 equals 0 and if it is break from the infinite loop
        if a // 3 == 0: break
        # Update 'a' to the floor division of itself by 3
        a //= 3
    # Return a joined string of values from 'buk_num'
    return ''.join(buk_num)


# Define 'bukiyip_add' which returns the sum of two bukiyip (base-3) numbers taken as parameters, as a bukiyip number
def bukiyip_add(a, b):
    # Return the sum (converted to a bukiyip number by calling 'decimal_to_bukiyip') of 'a' and 'b' (converted to decimal numbers by calling 'bukiyip_to_decimal') 
    return decimal_to_bukiyip(bukiyip_to_decimal(a) + bukiyip_to_decimal(b))


# Define 'bukiyip_add' which returns the multiplication of two bukiyip (base-3) numbers taken as parameters, as a bukiyip number
def bukiyip_multiply(a, b):
    # Return the multiplication (converted to a bukiyip number by calling 'decimal_to_bukiyip') of 'a' and 'b' (converted to decimal numbers by calling 'bukiyip_to_decimal') 
    return decimal_to_bukiyip(bukiyip_to_decimal(a) * bukiyip_to_decimal(b))

# # Define 'bukiyip_program' which does not return anything but uses recursion to keep asking for commands until the user opts to quit
# def bukiyip_program():
#     # Start infinite while loop that breaks when the user inputs a valid command
#     while True:
#         # Enter a try block
#         try:
#             # Set 'command' to a list consisting of integers if the value is a digit or otherwise lowercase letters from a user input split into a list
#             command = [int(com) if com.isdigit() else com.lower() for com in input('Enter a command:\n').split()]
#             # Assert that the command is valid by calling 'valid_command' with the command as the argument. If it is continue otherwise throw an error
#             assert valid_command(command)
#             # Break the infinite loop
#             break
#         # Enter a try block that tells user the command is invalid and explains how to input valid commands if an error is thrown
#         except: print('''
# Invalid command!

# Available commands:
# d <number> : convert given decimal number to base-3.
# b <number> : convert given base-3 number to decimal.
# a <number> <number> : add the given base-3 numbers.
# m <number> <number> : multiply the given base-3 numbers.
# q : quit
# ''')
#     # Check if the command is 'q' which means the user would like to quit. If it is return from this function to get out of the recursion
#     if command == ['q']: return
#     # Otherwise check if the command is 'd' which means the user would like to convert a decimal number to bukiyip. If it is print the value from calling 'decimal_to_bukiyip' with the bukiyip number as an argument
#     elif command[0] == 'd': print(decimal_to_bukiyip(command[1]))
#     # Otherwise check if the command is 'b' which means the user would like to convert a bukiyip number to decimal. If it is print the value from calling 'bukiyip_to_decimal' with the decimal number as an argument
#     elif command[0] == 'b': print(bukiyip_to_decimal(command[1]))
#     # Otherwise check if the command is 'a' which means the user would like to add two bukiyip numbers. If it is print the value from calling 'bukiyip_add' with the bukiyip numbers as arguments
#     elif command[0] == 'a': print(bukiyip_add(command[1], command[2]))
#     # Since none of the above conditions are true it means the user would like to multiply two bukiyip numbers. If it is print the value from calling 'bukiyip_multiply' with the bukiyip numbers as arguments
#     else: print(bukiyip_multiply(command[1], command[2]))
#     # Since the user does not want to quit and their command has been fulfilled then call 'bukiyip_program'. This makes 'bukiyip_program' a recursive function
#     bukiyip_program()


# # Print Welcome message and instructions that explain how to input commands
# print('''**** Bukiyip test program ****
# Available commands:
# d <number> : convert given decimal number to base-3.
# b <number> : convert given base-3 number to decimal.
# a <number> <number> : add the given base-3 numbers.
# m <number> <number> : multiply the given base-3 numbers.
# q : quit
# ''')
# # Call 'bukiyip_program' to start the Bukiyip test program
# bukiyip_program()