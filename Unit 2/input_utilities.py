#input_utilities.py

# Program: Asks user for positive interger.
def get_positive_int():
    """
    Asks user for positive interger.

    Returns:
        num(int): The number the user enters.
        flag(bool): True or False.
    """
    
    while True:
        try:
            num = int(input("Enter a value: "))
            flag = num > 0
            return num, flag
            break
            
        except Exception:
            print("enter a positive integer greater than 0.")

# Program: Asks user to pick option out of n options.    
def get_option(n):
    """
    Asks user to pick option.

    Args:
        n(int):  The number of options the user has to pick from.			         choose from.
        Assummptions: n >= 1

    Returns:
        option(int): User's option.
    """
    
    while True:
        try:
            option = int(input("Choose your option: "))
            
            if option in range(1, n + 1):
                return option
                break
            
            else:
                print("Need to enter a value between 1 and", n, "to \
continue!\n")

        except:
            print ("Need to enter a value between 1 and", n, "to continue!\n")

# Program: Asks user for interger.
def get_int(choice):
    """
    Asks user to enter an interger.

    Returns:
        option(int): User's int.
    """
    
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
            break
        
        except:
            print("Need to a number to continue!")

# Program: Asks user for float.            
def get_num():
    """
    Asks user to enter an float.

    Returns:
        option(int): User's float.
    """
    
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
            break
        
        except:
            print("Need to a number to continue!")

