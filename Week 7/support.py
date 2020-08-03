# Selects a response from a dictionary for user problems that match the dictionaries keywords to assist user with computer problems
# Lonwabo Mvovo
# 23/05/2020

# Import the randint function from the random library
from random import randint


# Define 'set_responses' which accepts a parameter 'problem' and returns a matching response from the given list when called otherwise prints a backup message
def set_responses(problem):
    # Set 'responses' to a dictionary of the possible responses indexed by keywords in their given order
    responses = {
        'Crashed' : 'Are the drivers up to date?',
        'Blue'    : 'Ah, the blue screen of death. And then what happened?',
        'Hacked'  : 'You should consider installing anti-virus software.',
        'Bluetooth' : 'Have you tried mouthwash?',
        'Windows'  : 'Ah, I think I see your problem. What version?',
        'Apple'    : 'You do mean the computer kind?',
        'Spam'     : 'You should see if your mail client can filter messages.',
        'Connection' : 'Contact Telkom.'
    }
    # Return a response from 'responses' if 'problem' matches a keyword otherwise print back-up message
    return responses.get(problem, 'Curious, tell me more.')


# Define 'welcome' which prints a welcome message when called
def welcome():
    # Welcome message
    print('Welcome to the automated technical support system.')
    print('Please describe your problem.')


# Define 'get_input' which returns a users input when called
def get_input():
    # Return a users input lowered which represents the problem the user is facing with their computer. The input is lowered so that we can check if the user would like to quit.
    return input().lower()


# Define 'main' which starts the program when called
def main():
    # Call 'welcome' to print the welcome messages
    welcome()
    # Set 'query' to the a user's input by calling 'get_input'
    query = get_input()
    # Start a while loop that will run as long as the user's input is not 'quit' which means they would like to quit the program
    while (not query=='quit'):
        # Print a response given by calling 'set_responses' with 'query' capitalized (needed because dictionary keys are capitalized) as an argument
        print(set_responses(query.capitalize()))
        # Update 'query' to another input from the user by calling 'get_input'
        query = get_input()    


# Check if the __name__ is '__main__' to ensure that 'main' is only called if it is and not when imported
if __name__ == '__main__': main()