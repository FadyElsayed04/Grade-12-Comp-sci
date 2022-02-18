# Name: Fady Elsayed
# Date: nov 3nd 2021
# File Name: 2b 3.5.py
# Description: Prints table.

# Input: Asks user for input.
ferr = int(input("Temp in Fahrenheit: "))
speed = int(input("Wind speed in mph: "))

row = 50
col = 60

# Output: Prints table. 
print("{0:>3s}{1:>2s}".format("*", "|"), end="")

for i in range (0, row + 1, 5):
    print("{0:7d}".format(i), end="")
    
print("\n" + "-" * (row * 2 - 18))
    
for i in range (-20, col + 1, 10):
    print("{0:>3d}{1:>2s}".format(i, "|"), end="")
        
    for n in range (0, row + 1, 5):
        num = 35.74 + 0.621 * i - 35.75 * (n ** 0.16) + 0.4275 * i * (n ** 0.16)
        print("{0:>7.2f}".format(num), end="")
            
    print("")
