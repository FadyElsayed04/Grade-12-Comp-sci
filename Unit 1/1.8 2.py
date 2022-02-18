# Name: Fady Elsayed
# Date: sept 22 2021
# File Name: 1.8 2.py
# Description: A Program that checks if the list is in the correct sorted order.
# Test Cases: 0, 1, 5, 10, 50.

# Process: Creates two lists.
nums = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
nums_sorted = sorted(nums)

# Checks if list is sorted and prints.
def is_descending(num):
    
    if nums_sorted == nums:
        print("it's in correct order")
        
    else:
        print("it's not correct order")
        
# Main Program:
is_descending()
