# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1k 3.3.py
# Description: Counts the average number of capital letters.

while True:
    try:
        
# Input: Asks user for input.
        n = int(input("How many words would you like to enter: "))
        if n > 0:
            break

        else:
            raise Exception
        
    except Exception:
        print("Invalid input.")

count_caps = 0

for i in range(n):
    
# Input: Asks user for input.
    word = input("Enter a string: ")

    for letters in word:
        if letters.isupper():
            count_caps += 1
            
        else:
            pass
        

average_caps = count_caps / n

# Output: Prints the average number of capital letters.
print("Average", average_caps, "capitals per word.")

