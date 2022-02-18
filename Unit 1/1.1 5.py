# Name: Fady Elsayed
# Date: sept 9 2021
# File Name: 1.1 5.py
# Description: Uses the users input to transform improper fractions to mixed.
# Test cases: 1, 3, 5, 6, 7, 20, 31.

# Input: Asks user for numrator and denominator.
num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))

# Process: calculates the mixed number and remainder.
mixed = num // den
remainder = num % den

# Prints: prints the mixed and remainder.
if mixed > 0:
    print(str(num) + "/" + str(den), "is equivalent to", str(mixed), "and", \
                        str(remainder) + "/" + str(den))
else:
    print(str(num) + "/" + str(den), "is equivalent to", \
          str(remainder) + "/" + str(den))
