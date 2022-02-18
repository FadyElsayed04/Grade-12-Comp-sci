# Name: Fady Elsayed
# Date: nov 3nd 2021
# File Name: 1b 3.5.py
# Description: Prints string without a's.

# Input: Asks user for input.
user = input("Enter a string with A's and B's: ")
stop = False

for letter in user:
    if stop == False:
        if letter.upper() in "AB":
            new = user.strip("Aa")
            
        else:
            print("Contains more than As and Bs.")
            stop = True

if stop == False:

# Output: Prints string without a's.    
    print(new)
