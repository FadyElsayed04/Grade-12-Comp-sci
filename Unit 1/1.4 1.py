# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 1.py
# Description: Program can give a factorial of any number.
# Test Cases: I used: 3, 4, 5.

while True:
    try:
    
# Input: gathers users number.
        num = int(input("Please enter a interger: "))

# Process: Sets factorial to 1.
        factorial = 1

# Process: Loops for loop to calculate factorial.
        for i in range(1, num + 1):
            factorial = factorial * i
        
# Output: Prints the factorial of the number the user has given.
        print(factorial)
        break
    except:
        print("\nPlease try again")
