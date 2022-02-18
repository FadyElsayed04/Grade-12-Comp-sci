# Name: Fady Elsayed
# Date: nov 3nd 2021
# File Name: 1d 3.5.py
# Description: Prints string without a's.

# Input: Asks user for input.
user = input("Enter a string with A's and B's: ")
stop = False
count = 0

for letter in user:
    if stop == False:
        if letter.upper() in "AB":
            if letter.upper() in "A":
                count += 1
            
        else:
            print("Contains more than As and Bs.")
            stop = True
            
    if count % 2 == 0:
        new = user.lstrip("Aa")
        
    else:
        new = user
        
if stop == False:
    
# Output: Prints string without a's. 
    print(new)
