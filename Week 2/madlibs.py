# My version of the Madlibs Game
# Lonwabo Mvovo
# 13/05/2020

# Creates infinite while loop
while True:
    # Use try except to make sure 'one' or 'two' is entered
    try:
        # Get the group and make it lowercase just in case user does not enter it lowered
        group = input('\nWhich group are you in?(one or two) ').lower()
        assert group == 'one' or group == 'two'
        # Break the while loop
        break
    # Error message for when 'one' or 'two' is not chosen
    except: print("I don't think that group exists. Please enter either 'one' or 'two'")

# Get user input for an adjective
adjective = input('\nPlease enter an adjective: ')

# Get user input for an verb
verb = input('\nPlease enter an verb: ')

# Print the multiline madlib
print(f'''
Group {group} is the best!
I am {adjective} to start coding and 
I should {verb} in the next standup''')