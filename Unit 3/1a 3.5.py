# Name: Fady Elsayed
# Date: nov 3nd 2021
# File Name: 1a 3.5.py
# Description: Prints string formated.

# Input: Asks user for input.
user = input("Enter a string with 10 for fewer characters: ")

if len(user) <= 10:

# Output: Prints string formated.       
    print(user.rjust(20))
    print(user.ljust(20))
    print(user.center(20))
    
else:
    print("Error")
