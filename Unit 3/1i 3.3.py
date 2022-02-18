# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1i 3.3.py
# Description: Counts the number of numbers and letters.

count_nums = 0
count_letters = 0

# Input: Asks user for input.
word = input("Enter a string: ")

for x in word:
    if x.isdigit():
        count_nums += 1

    elif x.isalpha():
        count_letters += 1

    else:
        pass

# Output: Prints the number of numbers and letters.
print("Numbers:", count_nums, "Letters:", count_letters)
