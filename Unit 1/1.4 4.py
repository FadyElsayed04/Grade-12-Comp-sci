# Name: Fady Elsayed
# Date: sept 20 2021
# File Name: 1.4 4.py
# Description: A Program that determines the largest 2 positive integers.
# entered the user
# Test Cases: I used: 25, 50, 75, 80, 100, -30.

# Process: Sets values for variables.
loop = True
first_largest = 0
second_largest = 0
# Process: Loops untill a negative value is entered and saves any values
# that are larger than the second or first largest values.
while loop == True:
    try:
        num = int(input("Enter number: "))
        if num >= 0:
            if num > first_largest:
                second_largest = first_largest  
                first_largest = num
            elif num > second_largest:
                second_largest = num  
        else:
            loop = False
    except:
        print("\nPlease try again.")        

# Ouput: Prints the largest and second largest numbers.
print("The largest number is", first_largest)
print("The second largest number is", second_largest)
