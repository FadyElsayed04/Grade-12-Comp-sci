# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 2abcd.py
# Description: A Program that sums up ur marks, checks the lowest and highest
# mark, and has error checking and self ending option.
# Test Cases: I used: 25, 50, 75, 80, 100.

# Process: Sets values for variables.
sum = 0
highest = 0
lowest = 100
loop = True
count = 0
# Output: prints title and command.
print("This program will add marks until -1 is given")

# Process: Loops untill -1 is entered and changes variables
# for highest and lowest mark.
while loop == True:
    try:
        num = int(input("Enter number: "))
        if num != -1:
            if num <= 100 and num >= 0:
                count = count + 1
                sum = sum + num
                if num <= lowest:
                    lowest = num
                if num >= highest:
                    highest = num
            else:
                print("Please enter a number from 0-100")
        else:
            loop = False
    except:
        print("\nPlease try again.")
# Ouput: Prints the sum of the marks, the lowest mark, and the highest marks.
print("The sum is", sum)
print("The lowest mark is", lowest)
print("The highest mark is", highest)
print("The average is", (sum / count))
