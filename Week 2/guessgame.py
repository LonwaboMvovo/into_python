# Guessing game
# Lonwabo Mvovo
# 13/05/2020

# Set the secret word to 'Zaio'
secret_word = 'Zaio'

# Set initial number of guesses to 1
num_guesses = 1

# Set the guess limit to 3
guess_limit = 3

# Infinite loop that breaks when the user is out of guesses or the secret word is guessed correctly
while True:
    # Check if the user is not out of guess by checking that num_guesses is greater than guess_limit
    if num_guesses > guess_limit:
        # Print losing message that shows what the secret word was
        print(f'\nOut of guesses the secret word was "{secret_word}"')
        # Break out of while loop
        break
    
    # Set the user guess to a capitalized input
    user_guess = input('\nGuess the secret word: ').capitalize()

    # Check if the user guessed the secret word correctly by checking if user_guess is equal to secret_word
    if user_guess == secret_word:
        # Print winning message that shows the secret word they guessed correctly and shows the number of guesses it took with the right grammar
        print(f'\nWell done you guessed the secret word {secret_word} and it took you {num_guesses} {"guess" if num_guesses == 1 else "guesses"}')
        # Break out of while loop
        break
    
    # Add 1 to the number of guesses the user has made
    num_guesses += 1