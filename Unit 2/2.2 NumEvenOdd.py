# Name: Fady Elsayed
# Date: oct 5th 2021
# File Name: 2.2 NumEvenOdd.py
# Description: generates a number 1-1000 n amount of times and counts how
# many times it was poitive or negative.
# Test cases: 1, 3, 5, 6, 7, 20, 31, yes, no.

import random

# Program: Checks if input is even or odd from a random number n amounr of \
times.
def random_even_or_odd():
    loop = True
    
    while loop == True:
        try:
            user = int(input("How many times would you like to run the \
simulation? "))

            while user <1:
                raise Exception
            
            odd = 0
            even = 0
            
            for i in range(user):
                num = random.randint(1,1000)
                
                if num % 2 == 0:
                    even += 1

                else:
                    odd += 1
                    
            print("\nThere were", even, "even numbers, and", odd, "odd \
numbers.")
            loop = False
            
        except:
            print("\nplease enter a interger from 1 to 100.\n")
            
# Program: Creates main funtion.        
def main():
    loop = True
    
    while loop == True:
        random_even_or_odd()
        try_again = input("\nwould you like to play again? 'yes'/'no': ")
        
        while try_again != "yes" and try_again != "no":
            try_again = input("\nIncorect input, would you like to try \
again? 'yes'/'no': ")
                
        if try_again == "no":
            print("\nGoodbye.")
            loop = False
                
        if try_again == "yes":
            print()

# Main program.
main()
