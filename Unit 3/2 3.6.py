# Name: Fady Elsayed
# Date: nov 4th 2021
# File Name: 2 3.6.py
# Description: A program that checks a list of words and checks
# if each word is a palindrome. 

# Process: Checks if words are a palindrome.
def isPalindrome(sentence):
    words = sentence.split()

# Process: Checks if words are a palindrome.
for w in words:
        if w == w[::-1]:
            print(w, "is a palindrome.")
            
        else:
            pass

# Program: Creates main program.
def main():

# Input: Asks user for input.
    sentence = input("Enter a sentence: ")
    isPalindrome(sentence)

# Main Program.
main()
