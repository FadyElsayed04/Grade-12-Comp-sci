# Name: Fady Elsayed
# Date: nov 2nd 2021
# File Name: 1g 3.4.py
# Description: Prints if string is a pandigital.

# Input: Asks user for input.
user = input("Enter a positive number: ")
count = 0

for i in range(1, len(user) + 1):
    if str(i) in (user):
        count += 1
        
    else:
        i = len(user) + 2
        count = "Not a pandigital"
        
# Output: Prints if string is a pandigital.        
print(count)
