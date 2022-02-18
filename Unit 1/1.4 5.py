# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 5.py
# Description: A Program that lists all the factors of a random number from
# 1 - 100 and loops until the user enters no

# Process: Sets Values for variables and imports random.
import random
play_again = "Yes"

# Process: While loop to loop the game.
while play_again == "Yes":
    num = random.randint(1,101)
# Output: Prints the factors.
    print ("The factors for {} are: ".format(num))
    
    for i in range (1, num+1):
        if num % i == 0:
            print (i)
            
# Process: asks user to play again.
    play_again = input("Do you want to play again? Please enter 'Yes' \
or 'No': ")
    
    while play_again != "Yes" and play_again != "No":
       play_again = input("Do you want to play again? Please enter 'Yes' \
or 'No': ") 
