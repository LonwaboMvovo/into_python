# Randomly selects a response from a list to assist user with computer problems
# Lonwabo Mvovo
# 23/05/2020

# Import the randint function from the random library
from random import randint


# Define 'random_response' which returns a random response from the given list when called
def random_response():
    # Set 'responses' to a list of the possible responses in their given order
    responses = [
        'Have you tried it on a different operating system?',
        'Did you reboot it?',
        'What colour is it?',
        'You should consider installing anti-virus software.',
        'Contact Telkom.',
        'I should get that looked at if I were you.'
    ]
    # Return a random response from the list
    return responses[randint(0, 5)]


# Define 'welcome' which prints a welcome message when called
def welcome():
    # Welcome message
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


# Define 'get_input' which returns a users input when called
def get_input():
    # Return a users input lowered which represents the problem the user is facing with their computer. It does not matter what the value of the user's input is because a random response will be given except for when the user would like to quit the program which is why the input is lowered so that we can check if the user would like to quit.
    return input().lower()


# Define 'main' which starts the program when called
def main():
    # Call 'welcome' to print the welcome messages
    welcome()
    # Set 'query' to the a user's input by calling 'get_input'
    query = get_input()
    # Start a while loop that will run as long as the user's input is not 'quit' which means they would like to quit the program
    while (not query=='quit'):
        # Print a random response by calling 'random_response'
        print(random_response())
        # Update 'query' to another input from the user by calling 'get_input'
        query = get_input()    


# Check if the __name__ is '__main__' to ensure that 'main' is only called if it is and not when imported
if __name__ == '__main__': main()