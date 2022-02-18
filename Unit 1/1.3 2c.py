# Name: Fady Elsayed
# Date: sept 10 2021
# File Name: 1.3 2c.py
# Description: randomly selects two letters from my name and checks if they are
# the same.


import random

# Process sets value for letter one and letter two.
letter_one = random.choice("FADY")
letter_two = random.choice("FADY")

# Output prints the letters selected and checks if they are the same.
print(letter_one)
print(letter_two)

if letter_one == letter_two:
    print("they are the same")
