# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1c 3.3.py
# Description: Prints longest word.

# Input: Asks user for input.
while True:
    try:
        n = int(input("How many words would you like to enter: "))
        if n > 0:
            break
        
        else:
            raise Exception
        
    except Exception:
        print("invalid input.")

longest = ""
smallest = ""

# Input: Asks user for input.
for i in range(n):
    user = input("Enter a word: ")

    if len(user) > len(longest):
        longest = user

# Output: Prints longest word.
print("The longest word is:", longest)
