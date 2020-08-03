# Generates an 8 character password that includes: 1 uppercase letter, 1 lowercase letter, 1 number and 1 special character
# Lonwabo Mvovo
# 14/05/2020

# Import the choice and shuffle functions from the random library/module in order to choose random characters for password and shuffle them
from random import choice, shuffle
# Import ascii_lowercase, ascii_uppercase, digits and punctuation variables from the string library/module
    # ascii_lowercase includes all the lowercase letters of the English alphabet
    # ascii_uppercase includes all the uppercase letters of the English alphabet
    # digits includes all the base-10 numbers
    # punctuation includes all the special characters
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


# Define function that will generate the password
def passwordGenerator():
    # Set variable 'all_chars' to all the characters that could be used in the password using the variables imported from 'string' library/module
    all_chars = ascii_lowercase + ascii_uppercase + digits + punctuation
    # Set the required length of the password (8 in this case) to a variable 'password_length'
    password_length = 8

    # Set variable 'password' initially to all the required characters
    password = [choice(ascii_uppercase), # Include uppercase letters
                choice(ascii_lowercase), # Include lowercase letters
                choice(digits), # Include base-10 numbers
                choice(punctuation)] # Include special characters

    # Add random characters from 'all_chars' to the password until it becomes the required length
    while len(password) < password_length: password.append(choice(all_chars))
    # Shuffle password randomly so that all passwords generated do not have a similar structure for some more safety
    shuffle(password)
    # Return a string of the generated password
    return ''.join(password)

# Print the generated password formed from calling the 'passwordGenerator' function
print(passwordGenerator())