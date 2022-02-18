# Name: Fady Elsayed
# Date: nov 1st 2021
# File Name: 1e 3.3.py
# Description: Determines if a word is a palindrome.


word_list = []

# Input: Asks user for input.
user = input("Enter a word: ")

for letters in user:
    word_list.append(letters)

# Output: Prints if palindrome or not.
if word_list == word_list[::-1]:
    print("palindrome.")

else:
    print("regular word.")
