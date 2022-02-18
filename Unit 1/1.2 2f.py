# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 2f.py
# Description: Uses the users input and check which number is larger.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

# Input: Asks user for input.
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))

# Process: calcualtes and prints which number is larger.
if num1 > num2 and num1 > num3:
  print(num1, "is the largest.")

elif num2 > num1 and num2 > num3:
  print(num2, "is the largest.")

elif num3 > num1 and num3 > num2:
  print(num3, "is the largest.")
  
else:
  print("numbers are the same.")

