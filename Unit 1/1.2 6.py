# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.2 6.py
# Description: Uses the users input to transform improper fractions to mixed.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

# Process: Sets value for variable.
bonus = 10

# Process: Asks user for input.
sold_cones = int(input("How many cones did Ian sell?: "))

# Process: Calculates bonus for Ian.
if sold_cones <= 150:
  print("No bonus.")

if sold_cones > 150:
    
    bonus = bonus + (sold_cones - 150) * 0.1
    if sold_cones > 250:

        bonus = bonus + (sold_cones - 250) * 0.25
        if sold_cones > 350:

            bonus = bonus + (sold_cones - 350) * 0.35
            
# Output: Prints bouns.
    print("bonus is $" + str(bonus))
    
