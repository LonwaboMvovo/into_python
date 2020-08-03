# Creates an acronym for a title inputed by the user without the words that the user chooses to ignore
# Lonwabo Mvovo
# 23/05/2020

# Set 'ignored_words' to a list of user inputed comma separated words that are converted to lowercase letters and all spaces are removed
ignored_words = input('Enter words to be ignored separated by commas:\n').lower().replace(' ', '').split(',')
# Set 'phrase' to a user inputed title that is converted into lowercase letters and then made into a list
phrase = input('Enter a title to generate its acronym:\n').lower().split()

# Print the acronym of the title inputed by the user without the words in the 'ignored_words' list
print('The acronym is:', "".join(word[0].upper() for word in phrase if word not in ignored_words))