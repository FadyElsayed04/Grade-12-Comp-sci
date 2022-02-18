# Name: Fady Elsayed
# Date: oct 4th 2021
# File Name: 2.1 SumEvenOdd
# Description: Uses the users input to print the sum of the first n intergers.
# Test cases: 1, 3, 5, 6, 7, 20, 31, yes, no.

# Program: calculations sum of even numbers.       
def sum_even(num):
    even = 0

    for i in range( 1,num + 1):
        even += 2 * i

    return even

# Program: calculations sum of odd numbers.   
def sum_odd(num):
    odd = 0

    for i in range( 1,num + 1):
        odd += 2 * i - 1

    return odd

# Program: asks user for positive numbers for calculations.             
def pos_input():
    while True:
        try:
            global num
            num = int(input("Please enter a value: "))
            
            if num < 0:
                raise Exception
            
            else:
                break
            
        except:
            print("\nPlease enter a positive integer")

# Program: Asks user to try again and prints msg accordingly.               
def try_again():
    while True:
        try_again = input("\nwould you like to try again? 'yes'/'no': ")
            
        while try_again != "yes" and try_again != "no":
            try_again = input("\nIncorect input, would you like to try \
again? 'yes'/'no': ")
                    
        if try_again == "no":
            print("\nGoodbye.")
            return False 
        elif try_again == "yes":
            print("\n")
            return True
    
# Program: Creates main funtion.        
def main():
    loop = True
    
    while loop:
        pos_input()
        sum_even(num)
        sum_odd(num)

        print("\nThe sum of the first", num, "even integers is: ", sum_even(num))
        print("The sum of the first", num, "odd integers is: ", sum_odd(num))
        loop = try_again()
        
# Main program.
main()
