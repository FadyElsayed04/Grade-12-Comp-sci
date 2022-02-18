# Name: Fady Elsayed
# Date: oct 4th 2021
# File Name: 2.1 Using functions
# Description: Checks if users input is prime or not.
# Test cases: 1, 3, 5, 6, 7, 20, 31, yes, no.

# Program: asks user for input. 
def user_input():
    while True:
        try:
            user = int(input("Please enter a number: "))
            
            if user < 1:
                raise Exception
            
            return user
            break
        
        except:
            print("\nIncorrect input!")

# Program: checks if number is prime and returns true or false accordingly.
def prime(n):
    print("\n" + str(n))
    
    n = (n == 2 or n == 3 or n == 5 or n == 7 or n == 7 or n == 13 or \
         (n % 5 != 0 and n % 2 != 0 and n % 3 != 0 and n % 13 !=0 and \
          n % 7 !=0))

    print(n)

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
        user = user_input()
        
        for n in range(1, user + 1):
            prime(n)
            
        loop = try_again()


# Main program.        
main()
