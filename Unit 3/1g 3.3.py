# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1g 3.3.py
# Description: Determines the number of non alphanumeric characters.

count = 0

# Input: Asks user for input.
word = input("Enter a string: ")

for value in word:
    if value.isalpha() == False and value.isdigit() == False:
        count += 1
    else:
        pass

# Output: Prints the number of non alphanumeric characters.
print(count, "non-alphanumeric characters.")
