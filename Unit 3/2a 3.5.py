# Name: Fady Elsayed
# Date: nov 3nd 2021
# File Name: 2a 3.5.py
# Description: Prints table.


# Input: Asks user for input.
row = int(input("Enter the # of rows: "))
col = int(input("Enter the # of columns: "))


# Output: Prints table. 
print("{0:>3s}{1:>3s}".format("*", "|"), end="")

for i in range (1, row + 1):
    print("{0:4d}".format(i), end="")
    
print("\n" + "--" * (row * 2 + 4))
    
for i in range (1, col + 1):
    print("{0:>3d}{1:>3s}".format(i, "|"),end="")
        
    for n in range (1, row + 1):
        num = i * n
        print("{0:4d}".format(num),end="")
            
    print("")
