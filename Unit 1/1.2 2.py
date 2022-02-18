# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 2.py
# Description: Checks users number entered if it is odd
# or even, if its divisible by 4 or 9 and if its positive or negative.
# Test cases: 5, 7, 9, -32, 10.

# Process: Imports math.
import math

# Input: Asks user for input.
num = int(input("Please enter an interger :"))

# Process: Checks if users number is odd.
if num % 2 > 0:
    print("The number is odd")
else:
        print("The number is even")
        
# Process: Checks if users number is divisible by 4 or 9.   
if num % 4 <= 0:
    print("It is divisible by 4 or 9")
elif num % 9 <= 0:
    print("It is divisible by 4 or 9")
else:
    print("It is not divisible by 4 or 9")

# Process: Checks if users number is positive or negative.
if num == 0:
    print("The number is not positive or negative")
elif num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
