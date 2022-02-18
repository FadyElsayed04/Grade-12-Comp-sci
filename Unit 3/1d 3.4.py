# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1d 3.4.py
# Description: If string starts with "un" and ends with "ing".

# Input: Asks user for input.
user = input("Enter a string: ")

if user.lower().startswith("un") == True and \
   user.lower().endswith("ing") == True:

# Output: Prints True or False.
    print("True")

else:
    print("False")
