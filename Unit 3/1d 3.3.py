# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1d 3.3.py
# Description: Counts number of letters.

# Input: Asks user for input.
while True:
    try:
        n = int(input("How many words would you like to enter: "))
        if n > 0:
            break
        else:
            raise Exception

    except Exception:
        print("Invalid input.")

for i in range(n):
    count = 0
    
# Input: Asks user for input.
    word = input("Enter a word: ")

    for letters in word:
        count+= 1

# Output: Prints number of letters.
    print(word, "has", count, "letters.")
