# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.1 4.py
# Description: Uses the users input and calculates the amount of
# pizza slices per child.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

import math

# Input: Asks user for input.
people_num = int(input("Please enter the amount of children at the birthday party :"))
pizza_num = int(input("Please enter the amount of pizza ordered :"))

# Process: calculates the amount of pizzer per child.
pizza_slices = pizza_num * 12
pizza_per = pizza_slices // people_num
pizza_left = pizza_slices % people_num

# Output: the amount of pizzer per child.
print("Everyone will get", pizza_per, "pizza slices.")
print("There will be", pizza_left, "Pizza slices left.")
