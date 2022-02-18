# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1e 3.4.py
# Description: prints all non-letters.

# Input: Asks user for input.
user = input("Enter a string: ")
for letter in user:
    if letter.isalpha() == False:

# Output: Prints string without letters.
        print(letter, end="")
