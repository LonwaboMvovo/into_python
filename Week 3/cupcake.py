# Organised version of the cupcake assignment
# Lonwabo Mvovo
# 13/05/2020

# Print a welcome message
print('Welcome to the 30 Second Rule Expert')
# Print dashes for each character in the welcome message
print('------------------------------------')
# Print instructions for user on how to use the program
print('Answer the following questions by selecting from among the options.')
# Set variable 'r' to users response to the question 'Did anyone see you?'
r = input('Did anyone see you? (yes/no)\n')
# Check if the user's response was 'no' to the question 'Did anyone see you?' and if it is then run this code
if r == 'no':
    # Update variable 'r' to users response to the question 'Was it sticky?'
    r = input('Was it sticky? (yes/no)\n')
    # Check if the user's response was 'no' to the question 'Was it sticky?' and if it is then run this code
    if r == 'no':
        # Update variable 'r' to users response to the question 'Is it an Emausaurus?'
        r = input('Is it an Emausaurus? (yes/no)\n')
        # Check if the user's response was 'no' to the question 'Is it an Emausaurus?' and if it is then run this code
        if r == 'no':
            # Update variable 'r' to users response to the question 'Did the cat lick it?'
            r = input('Did the cat lick it? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Did the cat lick it?' and if it is then run this code
            if r == 'no':
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Did the cat lick it?' run this code
            else:
                # Update variable 'r' to users response to the question 'Is your cat healthy?'
                r = input('Is your cat healthy? (yes/no)\n')
                # Check if the user's response was 'no' to the question 'Is your cat healthy?' and if it is then run this code
                if r == 'no':
                    # Set variable 'decision' to a string with value 'Your call'
                    decision = 'Your call.'
                    # This is the end of a possible decision tree
                # Since user's response was not 'no' to the question 'Is your cat healthy?' run this code
                else:
                    # Set variable 'decision' to a string with value 'Eat it.'
                    decision = 'Eat it.'
                    # This is the end of a possible decision tree
        # Since user's response was not 'no' to the question 'Is it an Emausaurus?' run this code
        else:
            # Update variable 'r' to users response to the question 'Are you a Megalosaurus?'
            r = input('Are you a Megalosaurus? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Are you a Megalosaurus?' and if it is then run this code
            if r == 'no':
                # Set variable 'decision' to a string with value 'Don't eat it.'
                decision = "Don't eat it."
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Are you a Megalosaurus?' run this code
            else:
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
    # Since user's response was not 'no' to the question 'Was it sticky?' run this code
    else:
        # Update variable 'r' to users response to the question 'Is it a raw steak?'
        r = input('Is it a raw steak? (yes/no)\n')
        # Check if the user's response was 'no' to the question 'Is it a raw steak?' and if it is then run this code
        if r == 'no':
            # Update variable 'r' to users response to the question 'Did the cat lick it?'
            r = input('Did the cat lick it? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Did the cat lick it?' and if it is then run this code
            if r == 'no':
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Did the cat lick it?' run this code
            else:
                # Update variable 'r' to users response to the question 'Is your cat healthy?'
                r = input('Is your cat healthy? (yes/no)\n')
                # Check if the user's response was 'no' to the question 'Is your cat healthy?' and if it is then run this code
                if r == 'no':
                    # Set variable 'decision' to a string with value 'Your call.'
                    decision = 'Your call.'
                    # This is the end of a possible decision tree
                # Since user's response was not 'no' to the question 'Is your cat healthy?' run this code
                else:
                    # Set variable 'decision' to a string with value 'Eat it.'
                    decision = 'Eat it.'
                    # This is the end of a possible decision tree
        # Since user's response was not 'no' to the question 'Is it a raw steak?' run this code
        else:
            # Update variable 'r' to users response to the question 'Are you a puma?'
            r = input('Are you a puma? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Are you a puma?' and if it is then run this code
            if r=='no':
                # Set variable 'decision' to a string with value 'Don't eat it.'
                decision = "Don't eat it."
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Are you a puma?' run this code
            else:
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
# Since user's response was not 'no' to the question 'Did anyone see you?' run this code
else:
    # Update variable 'r' to users response to the question 'Was it a boss/lover/parent?'
    r = input('Was it a boss/lover/parent? (yes/no)\n')
    # Check if the user's response was 'no' to the question 'Was it a boss/lover/parent?' and if it is then run this code
    if r == 'no':
        # Set variable 'decision' to a string with value 'Eat it.'
        decision = 'Eat it.'
        # This is the end of a possible decision tree
    # Since user's response was not 'no' to the question 'Was it a boss/lover/parent?' run this code
    else:
        # Update variable 'r' to users response to the question 'Was it expensive?'
        r = input('Was it expensive? (yes/no)\n')
        # Check if the user's response was 'no' to the question 'Was it expensive?' and if it is then run this code
        if r=='no':
            # Update variable 'r' to users response to the question 'Is it chocolate?'
            r = input('Is it chocolate? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Is it chocolate?' and if it is then run this code
            if r == 'no':
                # Set variable 'decision' to a string with value 'Don't eat it.'
                decision="Don't eat it."
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Is it chocolate?' run this code
            else:
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
        # Since user's response was not 'no' to the question 'Was it expensive?' run this code
        else:
            # Update variable 'r' to users response to the question 'Can you cut off the part that touched the floor?'
            r = input('Can you cut off the part that touched the floor? (yes/no)\n')
            # Check if the user's response was 'no' to the question 'Can you cut off the part that touched the floor?' and if it is then run this code
            if r == 'no':
                # Set variable 'decision' to a string with value 'Your call.'
                decision = 'Your call.'
                # This is the end of a possible decision tree
            # Since user's response was not 'no' to the question 'Can you cut off the part that touched the floor?' run this code
            else:
                # Set variable 'decision' to a string with value 'Eat it.'
                decision = 'Eat it.'
                # This is the end of a possible decision tree
# Print decision message with the value of the 'decision' variable
print('Decision:', decision)