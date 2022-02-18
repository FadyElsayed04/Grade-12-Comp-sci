# Name: Fady Elsayed
# Date: nov 4th 2021
# File Name: 1 3.6.py
# Description: Counts words in a sentence that are only letters and numbers.

w = 0
n = 0

# Input: Asks user for input.
sentence = input("Enter a sentence: ")

# Process: splits the sentence to words in a list.
w = sentence.split()

# Process: Checks if the word is is all letters or numbers.
for word in w:
    if word.isalpha():
        w += 1
        
    elif word.isdigit():
        n += 1
        
    else:
        pass

# Output: Prints the number of words made of only letters and num.
print("Number of words made of only letters:", w)
print("Number of words made of only numbers:", n)
