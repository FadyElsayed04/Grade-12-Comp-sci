# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.1 3.py
# Description: Uses the users input and subs it in for x.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

import math

# Input: asks user for input.
x = int(input("Enter an interger: "))

# Process: calculates and prints the answer.
print(float(0.08 * (math.sqrt(x**2 - 8)) + 12) / (x + 4))

