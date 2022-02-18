# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1b 3.4.py
# Description: Counts the number of double vowels.

# Input: Asks user for input.
user = input("Enter a string: ")
count = 0
letter2 = ""

for letter in user:
    if letter in ("aeiouAEIOU") and letter2 in ("aeiouAEIOU"):
        count += 1
        
    letter2 = letter

# Output: Prints amount of double vowels.
print(count, "double vowels")
