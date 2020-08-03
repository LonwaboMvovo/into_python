# Finds all palindromic primes between two integers given by user
# Lonwabo Mvovo
# 27/05/2020

# From the 'math' library import the 'sqrt' and 'floor' function which will be used in the sieve of Eratosthenes algorithm to determine prime numbers up to an integer
from math import sqrt, floor

def soe_primes(start, end):
    '''return a list of all the prime numbers from a start point to an end point using the sieve of Eratosthenes (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)'''
    # Set 'list_of_primes' to a list with 'end' amount of values all initially set to 'True'
    list_of_primes = [True for _ in range(end)]
    # Start a for loop where i is a number from a range of integers starting from 2 to the square root of 'end' rounded down plus 1
    for i in range(2, floor(sqrt(end)) + 1):
        # Check if the number at this iteration is set to 'True' in 'list_of_primes' (meaning its a prime number) and if its not run this inner code
        if list_of_primes[i-2]:
            # Set each number that is a factor of this prime number to 'False' starting from this prime number squared up to 'end'
            for j in range(i**2, end + 1, i):
                list_of_primes[j-2] = False
    # Return all prime numbers between the start point ('start') and the end point ('end')
    return [i + 2 for i in range(len(list_of_primes)) if start < i + 2 < end and list_of_primes[i]]


# Start an infinite loop that breaks when the user enters a valid start point
while True:
    try:
        # Set the start point to a user inputed integer
        start_point = int(input('Enter the start point N:\n'))
        break
    # Error message incase user does not enter an integer for the start point
    except ValueError: print('Please enter an integer for the start point.')

# Start an infinite loop that breaks when the user enters a valid end point
while True:
    try:
        # Set the end point to a user inputed integer
        end_point = int(input('Enter the end point M:\n'))
        # Make sure that the user enters an integer that is greater than or equal to the start point
        assert end_point >= start_point
        break
    # Error message incase user does not enter an integer for the end point that is greater than or equal to the start point
    except: print('Please enter an integer for the end point that is greater than or equal to the start point.')

# Start a for loop where 'prime_num' is a prime number from the list of primes received from calling 'soe_primes' with 'start_point' and 'end_point' as arguments
for prime_num in soe_primes(start_point, end_point):
    # Print the prime number if it is a palindrome
    if prime_num == int(str(prime_num)[::-1]): print(prime_num)