# Name: Fady Elsayed
# Date: sept 24 2021
# File Name: Unit 1 Assessment.py
# Description: A Gussesing game agasint a random generated number from 1-100.
# Diffrent modes with difffrent amount of guesses allowed and an play
# again feature.
# Test Cases: 1, 5, 6, 29, 96, 29, 49, yes, no, Easy, Medium, Hard,
# hello, x, 500, 200, -30, -20.

# Process: Imports random.
import random

# Process: sets value to variable.
loop = True

# Process: Checks user input for errors.
try:

# Process: Loops entire program for play again feature. 
    while loop == True:

# Process: gets random number for user to guess.
        cpu = random.randint(1,100)
        
# Process: sets value to variable.
        count = 0
        user = False
        mode = "None"
# Output: Prints random number for testing.
        print(cpu)
        
# Output: Prints the header.
        print("\nThe Guessing Game!")
        print("\nYou will be given a certain amount of guesses based on the \
mode you select, with each guess you will be told if your guess was higher or\
 lower than the random number.")
        
# Input: loops and asks user which mode the user would want to play.
        while mode != "Easy" and mode != "Medium" and mode != "Hard":
            mode = input("\nPlease enter the mode you like to play on \
'Easy', 'Medium', 'Hard': ")
            
# process: Sets limit to amount of guesses.
        if mode == "Easy":
            limit = 15
        if mode == "Medium":
            limit = 10
        if mode == "Hard":
            limit = 5
            
# output: Prints amount of guesses and intructions.
        print("You get", limit, "guesses")
        print("\nPlease guess a number from 1 to 100. ")

# Process: loops code to limit amount.
        if user != True:
            for i in range(limit):
                
# Input: Asks user to enter guess.
                guess = int(input("\nPlease enter your guess: "))
                
# Process: Checks if guess is vaild and adds count if the guess is valid.
                if guess <= 100 and guess >= 1:
                    count = count + 1

# Output: If user guessed correctly loop is broken and prints
# how many guesses it took for user to win.
                    if guess == cpu:
                        print("You won with:", count, "guess(es)!")
                        play_again = input("\nwould you like to play again? \
'yes'/'no': ")

# Process: checks if user wants to play again and runs code as so.
                        if play_again == "no":
                            print("\nGoodbye.")
                            loop = False

                        if play_again == "yes":
                            count = 0
                            cpu = random.randint(1,100)
                            print(cpu)
                            
# Process: Error checks users input.
                        while play_again != "yes" and play_again != "no":
                                play_again = input("\nIncorect input, would you \
like to play again? 'yes'/'no': ")

# Process: Checks if guess is too high or too low and prints message acordingly.
                    elif guess != cpu:
                        if guess > cpu:
                            print("Your guess is too high.")
                        if guess < cpu:
                            print("Your guess is too low.")

# Process: Checks if the user has reached the limit of guesses.
                    if count == limit:

# Input: Asks user if user wants to play again and prints message accordingly.
                        play_again = input("\nYou ran out of guesses would you \
like to play again? 'yes'/'no': ")
                        
                        if play_again == "no":
                            print("\nGoodbye.")
                            loop = False

# Process: Error checks users input.
                        while play_again != "yes" and play_again != "no":
                            play_again = input("\nIncorect input, would you \
like to play again? 'yes'/'no': ")
                            
                else:
                   print("Please enter a number from 1 to 100.")
                   
# Process: If users input is incorect program prints message.
except:
    print("Incorect input. Please restart.")
