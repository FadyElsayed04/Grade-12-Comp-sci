# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1h 3.3.py
# Description: Counts the number of capitals and lowercases.

count_low = 0
count_high = 0

# Input: Asks user for input.
word = input("Enter a string: ")

for x in word:
    if x.islower():
        count_low += 1

    if x.isupper():
        count_high += 1

# Output: Prints the number of capitals and lowercases.
print("Capital:", count_high, "Lowercase:", count_low)
