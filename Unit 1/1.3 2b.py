# Name: Fady Elsayed
# Date: sept 10 2021
# File Name: 1.3 2b.py
# Description: Uses the users input to add tax and calculate total price
# Test cases: 1, 3, 5, 6, 7, 20, 31.

import random

# Process sets value for tax.
tax = round(random.uniform(0.10, 0.20), 2)

# Input: Asks user for input.
price = float(input("Please enter the item price: "))

# Process calcuates cosr.
cost = price + (price * tax)

# Output: Prints tax and total price.
print("The tax is:", str(tax) + "%")
print("The price is: $" + str(cost))
