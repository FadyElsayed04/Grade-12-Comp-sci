# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1b 3.3.py
# Description: Prints every other letter of a word.

# Input: Asks user for input.
user = input("Enter a word: ")

# Output: Prints every other letter of a word.
for i in range(len(user)):
    if i % 2 == 0:
        print(user[i])
    
