# Name: Fady Elsayed
# Date: nov 4th 2021
# File Name: 3 3.6.py
# Description: A Program to find the longest and shortest words.               

# Program: Creates function to find the longest and shortest words.
def shortest_longest(sentence):
    words = sentence.split()
 
# Process: Finds longest and shortest words.
    longest = max(words, x = len)
    shortest = min(words, x = len)

# Output: Prints the longest and shortest words.
    print("The longest word is", longest, "the length is"\
             , len(longest))
    
    print("The shortest word is", shortest, "the length is"\
             , len(shortest))

# Program: Creates main program.
def main():

# Input: Asks user for input.
    sentence = input("Enter a sentence: ")
    shortest_longest(sentence)

# Main Program.
main()
