# Name: Fady Elsayed
# Date: sept 21 2021
# File Name: 1.6 3.py
# Description: A Program that swaps two values.
# Test Cases: 3, 5, "Boo", "Hoo".

# Process: creats function to swap two values.
def swap(a , b):
    c = a
    a = b
    b = c
    return(a , b)

# Main Program:
print(swap(3 , 5))
