import math

# Working with Strings:
def make_exited(word):
    return word.upper() + '!!!'

first_greeting = 'Hello World'
exited_first_greeting = make_exited(first_greeting)
# print(exited_first_greeting)

# print('''
# ****************************
# *                          *
# *                          *
# *                          *
# *                          *
# ****************************
# ''')

def name_age_msg(name,age):
    pass
    # print(f"There once was a man named {name},\nhe was {age} years old.\nHe really liked the name {name},\nbut didn't like being {age}.")


character_name = 'Lonwabo'
character_age = 19
name_age_msg(character_name,character_age)

num = 1434343434342423431.999999999999999
# print(num)

phrase = 'BaBOOon academy'
# print(phrase.upper())
# print(phrase.capitalize())
# print(phrase.lower().islower())
# print(phrase[0])
# print(phrase , 'is not cool')
# print('%s' % (phrase))
# print('hello freaks')
# print(phrase.index('OO'))
# print(phrase.replace('BaBOOon', 'Giraffe'))
# print('hello', 'world', sep='<->', end='\n******')
# print('me', 67, end='')
# print('hello')

array = [1,2,3]
# print(len(array))

# Working with Numbers:
# print(5.66666666666666666666666)
# print(0.1 + 0.2)
# print(0.7777777777777777777777777777777777)
# print(-0.7777777777777777777777777777777777)
# print(0.2 + 0.2)
# print(format(0.1, '.60f'))
my_num = 16
# print(type(str(my_num)))
# print(type(my_num))
# print(abs(-my_num))
# print(pow(12, 2))
# print(max(3,64,346,1,3))
# print(min(array))
# print(round(6.6, 0))
# print(int(6.6))

# print(math.factorial(5))
# print(math.floor(6.7))
# print(math.floor(-6.7))
# print(math.ceil(6.7))
# print(math.trunc(-6.7))
# print(math.trunc(6.7))
# print(math.floor(-0.1))
# print(math.ceil(-0.9))
# print(math.sqrt(121))

# print(isinstance(False, bool))

# Getting input from user:
# name = input('Enter your name: ').capitalize()
# age = input('Enter your age: ')
# print('Hello', name, 'I didn\'t know you were', age, 'years old')

# Building a calculator:
# num1 = float(input("Calculator\nFirst number: "))
# num2 = float(input("Second number: "))
# ans = num1 + num2
# print(ans)

# Madlibs Game:
# colour = input('Colour: ').lower()
# plural_noun = input('Plural Noun: ').capitalize()
# celebrity = input('Celebrity: ').capitalize()

# print(f'''
# Roses are {colour}
# {plural_noun} are blue
# I love {celebrity}''')

# print('Roses are ' + colour)
# print(plural_noun + ' are blue')
# print('I love ' + celebrity)

friends = ['Joe', 'Brendan', 'Theo', 'Bryan', 'Kat', 'Chin', 'Andrew']
friends[-1] = 'Bobby'
# print(friends)
# print(f'My first friend was {friends[0]}')
# print(friends[-1::-1])

# List Functions:
# lucky_numbers = [2, 16, 116, 44,4]
# lucky_numbers.sort()
# print(lucky_numbers)
# lucky_numbers.reverse()
# print(lucky_numbers)
# lucky_numbers2 = lucky_numbers.copy()
# lucky_numbers.pop()
# print(lucky_numbers)
# print(lucky_numbers2)
# friends.extend(lucky_numbers)
# print(friends)
# friends.append('whoop')
# print(friends)
# friends.insert(2, 'Rudy')
# friends.insert(2, 'Rudy')
# print(friends)
# friends.remove('Joe')
# print(friends)
# print(friends.pop())
# print(friends)
# print('Rudy' in friends)
# print(friends.count('Rudy'))
# print(friends.index('Rudy'))
# friends.sort()
# print(friends)
# friends.clear()
# print(friends)

# Tuples:
my_tuple = (1,2,3)
# print(my_tuple)

# Functions: 
def greet():
    person_name = input('What\'s your name: ').capitalize()
    age = input('What\'s your age: ')
    return f'Hello {person_name}\nYou are {age} years old'


# print(greet())

def cubed_num(num): return num ** 3


# print(cubed_num(5))

# If Statements:
is_male = False
is_tall = True

# if is_male and is_tall: print('You are a tall male')
# elif is_male and not is_tall: print('You are not a tall male')
# elif not is_male and is_tall: print('You are not a male, but you are tall')
# else: print('You are not a tall male')

# Comparisons:
def max_num(list_of_numbers):
    highest = list_of_numbers[0]
    for num in list_of_numbers[1:]:
        if num > highest: highest = num
    return highest


# print(max_num([1,4,64,2,6,-9]))

# Building a better calcultator:
def better_calculator():
    while True:
        try:
            num1 = float(input('Fist Number: '))
            break
        except ValueError:
            print('Please enter a real number')
    while True:
        try:
            operator = input('Operator: ')
            assert operator == '+' or operator == '-' or operator == '*' or operator == '/'
            break
        except:
            print('Please enter a basic operator')
    while True:
        try:
            num2 = float(input('Second Number: '))
            break
        except ValueError:
            print('Please enter a real number')
    
    if operator == '+': return num1 + num2
    elif operator == '-': return num1 - num2
    elif operator == '*': return num1 * num2
    elif num2 == 0: return 'Cannot divide by zero'
    else: return num1 / num2


# print(better_calculator())

# Dictionaries:

months = {
    'jan': 'January',
    'feb': 'February',
    'mar': 'March',
    'apr': 'April',
    'may': 'May',
    'jun': 'June',
    'jul': 'July',
    'aug': 'August',
    'sep': 'September',
    'oct': 'October',
    'nov': 'November',
    'dec': 'December'
}

# print(months['nov'])
# print(months.get('1', 'Not a valid month'))

# While loop:
i = 1
while i <= 10:
    # print(i)
    i += 1
# print('done')

# Guessing game:
secret_word = 'Hello'
num_guesses = 1
guess_limit = 3

# while True:
#     if num_guesses > guess_limit:
#         print(f'\nOut of guesses the secret word was "{secret_word}"')
#         break

#     user_guess = input('\nWhat do you think my secret word is? ').capitalize()
#     if user_guess == secret_word:
#         print(f'\nWell done you guessed my word {secret_word} and it took you {num_guesses} {"guess" if num_guesses == 1 else "guesses"}')
#         break
#     else:
#         print('That is not the secret word!')
#     num_guesses += 1

# print('\nGame over!!!')

# # For Loops:
# for letter in 'Malumz on deckz':
#     print(letter)

# podcasts = ['JRE', 'Bad Friends', 'KATS']
# for podcast in podcasts:
#     print(podcast)

# for i in range(4):
#     print(i)

# Exponent Power:
# print(4 ** 2)
# print(pow(4,2))

def raise_to_pow(number, power):
    ans = 1
    if power < 0:
        for _ in range(0,power,-1): ans *= number
        return 1 / ans
    else:
        for _ in range(power): ans *= number
        return ans


print(raise_to_pow(0,2))