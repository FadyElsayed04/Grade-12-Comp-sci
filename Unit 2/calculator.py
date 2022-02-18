# Name: Fady Elsayed
# Date: oct 18th 2021
# File Name: calculator.py
# Description: Uses the users input do run a calculator program. The user is
# asked to pick from options aswell as entering values.
# Test cases: 1, 3, 5, 6, 7, 20, 31, yes, no.

# Process: Imports modules.
import operations 
import input_utilities

# Program: Prints meanu.
def print_menu():
    """
    Prints meanu.
    """
    
    print("Welcome to the Calculator Program\n")
    print("Your options are:\n")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit Calculator\n")

# Program: Does calculation depending on option and values picked.

def do_calculation(choice):
    num1 = input_utilities.get_num()
    num2 = input_utilities.get_num()
    """
    Does calculations based on choice picked
    
    Args:
        choice(int): The option the user picked.
        Assummptions: choice > 0 and choice < 6
    
    Returns:
    result(int): The result of the calculation.
    """
    
    if choice == 1:
        result = operations.add(num1, num2)
        
    elif choice == 2:
        result = operations.subtract(num1, num2)
        
    elif choice == 3:
        result = operations.multiply(num1, num2)
        
    elif choice == 4:
        result = operations.divide(num1, num2)
        
    print("The result is", result,"\n\n---------------------------------------\
-----------------------------------------\n")

# Program: Creates main funtion.            
def main():
    while True:
        print_menu()
        choice = input_utilities.get_option(5)
        
        if choice == 5:
            break
            
        else:
            do_calculation(choice)

    print("Thank you. Goodbye!")

# Main program.
main()
