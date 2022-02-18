# Name: Fady Elsayed
# Date: Nov 1st 2021
# File Name: Unit 3.2 Assessment.py
# Description: A program that displays a multiplication times table to the user
# and does a multiplication question from the user.
# Test cases: 1, 3, 4, 5, 8, 10, hi, hello, 0, -5, -9

# Program: Creates program to display the multiplication times table.
def table(row, col):
    """ Creates program to display the multiplication times table.

        Arg:
        row(int), col(int): The amount of rows and colulmns in the table.

        Return:
        value(list): 2d list of multiplication table.
    """
# Process: Creates empty list.
    value = []

# Process: Creates table with 2d lists.    
    for i in range(1, row + 1):
        list_one = []
        
        for n in range(1, col + 1):
            list_one.append(i * n)
            
        value.append(list_one)
        
# Output: returns 2d list.
    return value
    
# Creates main program:
def main():
    """ Creates main program to display a multiplication times table to the
    user, and do a multiplication question from the user.

    """
    
# Input: Asks user amount of rows and colulmns in table and error checks.
    valid = False
    while valid == False:
        try:
            row = int(input("Enter the # of rows: "))
            
            if row < 1:
                raise Exception
            
            valid = True
            
        except:
            print("\nERROR\n")
        
    valid2 = False
    while valid2 == False:
        try:
            col = int(input("Enter the # of colulmns: "))
            
            if col < 1:
                raise Exception
            
            valid2 = True
            
        except:
            print("\nERROR\n")
        

# Process: Prints multiplication table.
    print()
    value = table(row, col)
    
    for i in range(len(value)):
        x = value[i]
        print(*x)

# Input: Asks user for 2 numbers to multiply and error checks.
    valid3 = False
    while valid3 == False:
        try:
            num1 = int(input("\nEnter number 1: "))
            
            if num1 < 1 or num1 > row:
                raise Exception
            
            valid3 = True
            
        except:
            print("\nERROR")
            
    valid4 = False
    while valid4 == False:
        try:
            num2 = int(input("Enter number 2: "))
            
            if num2 < 1 or num2 > col:
                raise Exception
            
            valid4 = True
            
        except:
            print("\nERROR")            

# Output: Prints the output for users multiplication.    
    print("\n"+ str(num1), "x", num2, "=", (value[num1 - 1][num2 - 1]))

# Main Program:
main()
