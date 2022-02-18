# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 3.py
# Description: A program that displays the Fibonacci sequence depending on
# the given value.
# Test cases: I used the numbers: 7, 8, 12.

# Input: Asks user for number of digits wanted.
terms = int(input("How many digits do you want?: "))

# Process: Set variables for the first two numbers, and count.
num1 = 1
num2 = 1
count = 0

# Process: Determine if the number of digits is valid.
if terms <= 0:
   print("Invalid, please enter a positive number.")
else:
   print("\nFibonacci sequence:")


   while count < terms:
# Output: Prints Fibonacci sequence and changes variables.
       if count >= 0:
          print(num1)
       num3 = num1 + num2
       num1 = num2
       num2 = num3
       count += 1
