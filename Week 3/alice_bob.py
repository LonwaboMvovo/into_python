# Solving Compare the Triplets problem from hackerrank
# Lonwabo Mvovo
# 13/05/2020
# Mood: Exited that we're coding

# Define 'compareTriplets' so that it takes two parameters 'a' and 'b' that represent Alice's and Bob's points and returns a tuple of their compare points
def compareTriplets(a, b):
    # Set variable 'alice_compare_points' to the sum of the list of compare points she gets if she scored higher than bob in that category
    alice_compare_points = sum([1 for i in range(len(a)) if a[i] > b[i]])
    # Set variable 'bob_compare_points' to the sum of the list of compare points he gets if he scored higher than Alice in that category
    bob_compare_points = sum([1 for i in range(len(a)) if a[i] < b[i]])
    # Return a tuple of their compare points
    return alice_compare_points, bob_compare_points


# Start an infinite while loop that breaks when user enters 3 space-separated integers
while True:
    # Enter try block
    try:
        # Set 'a_list' to a list of 3 space-separated integers representing Alice's points if they are within 0 and 101 in each category inputed by the user
        a_list = [int(a_num) for a_num in input().split() if 0 < int(a_num) < 101]
        # Assert that the length of 'a_list' is 3 in order to check that the user inputed 3 numbers. If true continue otherwise throw an error
        assert len(a_list) == 3
        # Break the infinite loop
        break
    # Enter except block that prints error message for when user does not enter 3 space-separated integers for Alice's points
    except: print("Please enter 3 space-separated integers [1, 100] for Alices's points")

while True:
    # Enter try block
    try:
        # Set 'b_list' to a list of 3 space-separated integers representing Bob's points if they are within 0 and 101 in each category inputed by the user
        b_list = [int(b_num) for b_num in input().split() if 0 < int(b_num) < 101]
        # Assert that the length of 'b_list' is 3 in order to check that the user inputed 3 numbers. If true continue otherwise throw an error
        assert len(b_list) == 3
        # Break the infinite loop
        break
    # Enter except block that prints error message for when user does not enter 3 space-separated integers for Bob's points
    except: print("Please enter 3 space-separated integers [1, 100] for Bob's points")

# Print the values recieved from calling 'compareTriplets' with 'a_list' and 'b_list' as arguments which will be the scores of their compare points with Alice's score first and Bob's second
print(*compareTriplets(a_list, b_list))