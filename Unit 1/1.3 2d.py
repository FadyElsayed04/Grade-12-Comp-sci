# Name: Fady Elsayed
# Date: sept 10 2021
# File Name: 1.3 2d.py
# Description: checks if random 3 letters are vowels.

import random

# Process: Sets random letter to variables.
letter1 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter2 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letter3 = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
num = 0

# Output: prints variable values.
print("The letters are:", letter1, letter2, letter3)

# Process: Checks if letters are vowels.
if letter1 == "A" or letter1 == "E" or letter1 == "I" or letter1 \
   == "O" or letter1 == "U":
    num += 1
    
if letter2 == "A" or letter2 == "E" or letter2 == "I" or letter2 \
   == "O" or letter2 == "U":
    num += 1

if letter3 == "A" or letter3 == "E" or letter3 == "I" or letter3 \
   == "O" or letter3 == "U":
    num += 1
    
if num == 2:

# Output: prints if there are two letters that are vowels.
    print("\nThere are exactly two letters are vowels.")
