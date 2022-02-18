# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 2e.py
# Description: Uses the users input and check which number is larger.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

# Input: Asks user for input.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# Process: calculates and prints which number is larger.
if num1 > num2:
  print(num1, "is larger than", num2)

elif num2 > num1:
  print(num2, "is larger than", num1)
else:
  print("numbers are the same.")
