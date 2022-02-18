# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 6.py
# Description: A Program that counts even numbers odd numbers and sevens.
# Test Cases: 1, 4, 6, 8, 7, 14, 21, 9, 20.

# Input: Asks user for a positive integer.
try:
    num = int(input("Enter a positive integer: "))

        
# Process: setsa values to variables.
    count_even = 0
    count_odd = 0
    count_seven = 0

# Process: starts while loop.
    while num >= 1:
     digit = num % 10
     num = num // 10

    # Process: checks if the interger is even odd or seven.
     if digit % 2 == 0:
         count_even += 1
     elif digit % 1 == 0:
         count_odd += 1
     if digit % 7 == 0:
         count_seven += 1
     else:
         pass

# Output: Prints the evens odds and sevens.
     print(digit)
     
    print("evens:", count_even)
    print("odds:", count_odd)
    print("sevens:", count_seven)
    
except:
    print("\nPlease try again.")
