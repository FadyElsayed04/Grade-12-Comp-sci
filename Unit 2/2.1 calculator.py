# Name: Fady Elsayed
# Date: oct 4th 2021
# File Name: 2.1 calculator
# Description: Uses the users input do run a calculator program.
# Test cases: 1, 3, 5, 6, 7, 20, 31, yes, no.


# Program: asks user for input from options. 
def options():
    print("Please pick an option.\n\nOption 1 - add\nOption\
2 - subtract\nOption 3 - multiply\nOption 4 - divide\nOption 5 - quit program")    
    while True:
        try:
            global option
            option = int(input("\nOption: "))
    
            while option != 1 and option != 2 and option != 3 and option != 4\
                  and option != 5:
                raise Exception
            
# Process: If user input is 5 quits program.
            if option == 5:
                print("Goodbye.")
                
            break
        
# Process: Prints if user input is invaild.
        except:
            print("\n\nIncorrect input!")
            print("Please pick either '1', '2', '3', '4', '5'.")
            
# Program: asks user for numbers for calculations.             
def numbers():
    while option != 5:
        try:
            global num1, num2
            
# Process: Asks user for numbers.
            num1 = float(input("Please enter one number: "))
            num2 = float(input("Please enter another number: "))
            break
        
# Process: Prints if user input is invaild.        
        except:
            print("\nIncorrect input!")

# Program: Does calculation based on inputs and prints.             
def calculation():
    while option != 5:
        if option == 1:
            result = num1 + num2
        elif option == 2:
            result = num1 - num2            
        elif option == 3:
            result = num1 * num2            
        elif option == 4:
            result = num1 / num2
        print("The result is", result)
        break

# Program: Asks user to try again and prints msg accordingly.               
def try_again():
    while option != 5:
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
        options()
        numbers()
        calculation()
        loop = try_again()


# Main program.
main()
