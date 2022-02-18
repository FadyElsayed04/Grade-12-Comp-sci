# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1f 3.4.py
# Description: prints amount of "ana"s in string.

# Input: Asks user for input.
user = input("Enter a string: ")
lowered_user = user.lower()
count = 0

while "ana" in lowered_user:
    lowered_user = lowered_user.replace("ana", "a")
    count += 1

# Output: Prints amount of "ana"s in string.
print(user, "contains", count, "such substrings.")

