# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 5.py
# Description: Uses the users input with the quadratic equation and solves it.
# Test cases: 1, 3, 5, 6, 7.

# Process: Imports math and states title.
import math
print("The standard quadratic equation is ax**2 + bx + c.\n")

# Process: Asks for input for a, b, c values.
a = int(input("Enter a value for 'a': "))
b = int(input("Enter a value for 'b': "))
c = int(input("Enter a value for 'c': "))

# Process: calculates values.
quad_form_pos = (-b + (b**2 - (4 * a * c)) ** 0.5) / (2 * a)
quad_form_neg = (-b - (b**2 - (4 * a * c)) ** 0.5) / (2 * a)

# Output: prints quadratic positive value and negative value.
print()
print(quad_form_pos)
print(quad_form_neg)

