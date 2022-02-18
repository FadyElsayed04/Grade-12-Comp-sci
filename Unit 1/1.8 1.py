# Name: Fady Elsayed
# Date: sept 22 2021
# File Name: 1.8 1.py
# Description: A Program that calculaates the sum, max and min, the average
# and the number of even and odd numbers
# Test Cases: 0, 1, 5, 10, 50.


# Process: Sets values to variables.
num_list = []
even = 0
odd = 0

# Input: Asks user for input and adds to list.
for i in range(10):
    num = int(input("Please enter an interger: "))
    num_list.append(num)

# Process: Checks if the number is even or odd
    if num % 2 == 0:
        even += 1
        
    else:
        odd += 1

# Output: prints the sum, average, max, min, even amount, and the odd amount.
print("The sum of the numbers you entered are:", sum(num_list))
print("The average of the numbers you entered are:", sum(num_list) / 10)
print("The max number you entered is:", max(num_list))
print("The min number you entered is:", min(num_list))
print("The amount of even numbers you entered are:", even)
print("The amount of odd numbers you entered are:", odd)
