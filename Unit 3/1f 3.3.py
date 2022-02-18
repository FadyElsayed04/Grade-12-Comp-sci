# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1f 3.3.py
# Description: Determines if string is made of only numbers or only letters.

# Input: Asks user for input.
word = input("Enter a word: ")

# Output: Prints if there are only letters or numbers or both in
# the string entered.
if word.isalpha() == True:
    print("All letters.")

elif word.isdigit() == True:
    print("All numbers.")

else:
    print("Mixed.")
