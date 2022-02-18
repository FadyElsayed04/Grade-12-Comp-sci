# Name: Fady Elsayed
# Date: sept 22 2021
# File Name: 1.8 3.py
# Description: A Program for fibonacci seq, based on mny didgets the user entered.
# Test Cases: 0, 1, 5, 10, 50.

# Process: Creats function for fibonacci, based on mny didgets the user entered.
def fibonacci(terms):
    num1 = 1
    num2 = 1
    count = 0
    nums = []

    if terms <= 0:
       print("Invalid, please enter a positive number.")
       
    else:
       print("\nFibonacci sequence:")

       while count < terms:
           
           if count >= 0:
              nums.append(num1)
              
           num3 = num1 + num2
           num1 = num2
           num2 = num3
           count += 1
          
    print(nums)

# Input: Asks user how many didgits he wants of the fibonacci seq.
terms = int(input("How many digits do you want?: "))

# Main Program
fibonacci(terms)
