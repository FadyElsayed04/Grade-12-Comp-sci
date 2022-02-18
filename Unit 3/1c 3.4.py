# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1c 3.4.py
# Description: Counts the number of uppercase vowels.

# Input: Asks user for input.
user = input("Enter a string: ")
count = 0
for letter in user:
    if letter.isupper() == True and letter in ("aeiouAEIOU"):
        count += 1

# Output: Prints amount of uppercase vowels.
print(count, "uppercase vowels")
