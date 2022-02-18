# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 2d.py
# Description: Uses the users input prints multiples of the given numbers.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

# Input: Asks for users input for num 1 num 2 and num 3.
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))
num3 = int(input("Please enter a number: "))

# Process: Checks if any of the users input are a multiple of another,
# and prints if so.
if num1 % num2 == 0:
  print(num1, "is a multiple of", num2)
        
elif num2 % num1 == 0:
  print(num2, "is a multiple of", num1)
  
elif num1 % num3 == 0:
  print(num1, "is a multiple of", num3)
  
elif num3 % num1 == 0:
  print(num3, "is a multiple of", num1)
  
elif num2 % num3 == 0:
  print(num2, "is a multiple of", num3)
  
elif num3 % num2 == 0:
  print(num3, "is a multiple of", num2)

# Output: prints if there are no multiples.
else:
  print("no numbers are multiples with other numbers.")
