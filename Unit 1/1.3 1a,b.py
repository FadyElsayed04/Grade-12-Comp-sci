# Name: Fady Elsayed
# Date: sept 10 2021
# File Name: 1.3 1ab.py
# Description: rolls and prints two separate dice and one large dice.

import random

# Process: Sets value for dice.
sum_of_dice = random.randint(2,12)

# Process: Sets value for dice 1 and two.
dice_one = random.randint(1,6)
dice_two = random.randint(1,6)

# Process: calculates values for dice.
dice_total = dice_one + dice_two

# Output: prints values for dice.
print(sum_of_dice)
print(dice_total)
