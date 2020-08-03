# Functions that convert English sentences into Pig-Latin and vice-versa
# Lonwabo Mvovo
# 22/05/2020

# Import 'ascii_lowercase' which contains all the lowercase letters from the string library
# from string import ascii_lowercase

# Define 'to_pig_latin' which takes an English sentence as a parameter and returns the sentence converted into Pig-Latin
def to_pig_latin(sentence):
    # Set 'vowels' to a string of all the vowels
    vowels = 'aeiou'
    # Set 'pig_latin_sentence' initially to an empty list
    pig_latin_sentence = []
    # Start a for loop for each word in the English sentence converted to a list
    for word in sentence.split():
        # Check if the first letter in the word is a vowel. If it is then add that word to 'pig_latin_sentence' with the letters 'way' attached
        if word[0] in vowels: pig_latin_sentence.append(word + 'way')
        # Otherwise
        else:
            # Start a for loop with the range starting from 1 to the length of the word
            for i in range(1, len(word)):
                # Check if the letter in the word for each iteration index is a vowel.
                if word[i] in vowels:
                    # Since it is convert that word into Pig-Latin and then add it to 'pig_latin_sentence' and then break from the for loop
                    pig_latin_sentence.append(word[i:] +'a' + word[:i] + 'ay')
                    break
                # Since there is no vowel in the word check if this is the last letter in the word
                if i + 1 == len(word):
                    # Append 'a' + the word + 'ay' because the word consists of consonants only
                    pig_latin_sentence.append('a' + word + 'ay')
    # Return all the words in 'pig_latin_sentence' joined with a space to make a sentence
    return ' '.join(pig_latin_sentence)


# Define 'to_english' which takes a Pig-Latin sentence as a parameter and returns the sentence converted into English
def to_english(sentence):
    # Set 'english_sentence' initially to an empty list
    english_sentence = []
    # Start a for loop for each word in the Pig-Latin sentence converted to a list
    for word in sentence.split():
        # Check if each word ends with way. If does then add that word without 'way' to 'english_sentence'
        if word.endswith('way'): english_sentence.append(word[:-3])
        # Otherwise
        else:
            # Start a for loop with the range starting from -3 to the negative of the length of the word with a step of -1 in order to count each letter backwards
            for i in range(-3, -len(word) - 1, -1):
                # Check if the letter in the word for each iteration index is 'a'.
                if word[i] == 'a':
                    # Since it is convert that word into English and then add it to 'english_sentence' and then break from the for loop
                    english_sentence.append(word[i+1:-2] + word[:i])
                    break
    # Return all the words in 'english_sentence' joined with a space to make a sentence
    return ' '.join(english_sentence)


# # Start an infinite while loop that breaks when the user inputs a valid language they would like to convert from
# while True:
#     # Enter a try block
#     try:
#         # Set 'language' to the language the user would like to convert from converted into lowercase letters in case user inputs in uppercase
#         language = input('(E)nglish or (P)ig Latin?\n').lower()
#         # Assert that 'language' is either 'e' or 'p'. If it is continue otherwise throw an error
#         assert language == 'e' or language == 'p'
#         # Break from the infinite loop
#         break
#     # Enter an except block that prints an invalid input message
#     except: print('Invalid input. Please either input "E" for English or "P" for Pig Latin.')

# # Start an infinite while loop that breaks when the user inputs a valid sentence only consisting of letters and spaces
# while True:
#     # Enter a try block
#     try:
#         # Set 'sentence' to the user's sentence for the language they have chosen converted into lowercase letters in case user inputs in uppercase
#         sentence = input(f'Enter {"an English" if language == "e" else "a Pig Latin"} sentence:\n').lower()
#         # Assert that the sentence only consists of letters and spaces
#         assert all(letter in ascii_lowercase for letter in sentence.replace(" ", ""))
#         # Break from the infinite loop
#         break
#     # Enter an except block that prints an invalid sentence message
#     except: print('Invalid input. Your sentence should only consist of letters.')

# # Print the user's sentence converted to either Enlish or Pig-Latin by calling 'to_pig_latin' or 'to_english' respectively with the sentence as an argument
# print('\nPig-Latin:\n' + to_pig_latin(sentence)) if language == 'e' else print('\nEnglish:\n' + to_english(sentence))

# # the quick black fox jumps over the lazy apple
# # eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway