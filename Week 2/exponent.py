# Exponent function that will take a number and raise it to another number
# Lonwabo Mvovo
# 13/05/2020

# The function that will raise number to another taking two parameter
def raise_to_power(number, power):
    # Set initial answer to 1 in case the 'power' is 1 and there is no loop
    ans = 1

    # Check if a negetive power is givin so that a range decreasing negatively can be made
    if power < 0:
        # Multiply 'ans' by the 'number' within negative range of power
        for _ in range(0,power,-1): ans *= number
        # Return 1 over the 'ans' because power is negative
        return 1 / ans

    # Therefore power is greater than or equal to zero

    # Multiply 'ans' by the 'number' within range of power
    for _ in range(power): ans *= number
    # Return the 'ans'
    return ans


# Print the answer from raising 4 to 4
print(raise_to_power(4,4))