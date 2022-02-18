# Name: Fady Elsayed
# Date: Oct 20th 2021
# File Name: 3.1 Birthday Paradox.py
# Description: A Program that runs simulations of people with the same birthday in the same class.
# Test Cases: 0, 1, 5, 10, 50, yes, no, as, 1000, 2000, -5.

# Program: Creates program to get user input for students.      
def get_students():
    """Asks user for amount of students.
    
        Returns:
           students(int): Number of students.
    """

    loop = True
    
    while loop:
        try:
            students = int(input("Please enter amount of students: "))
            
            if students < 1 or students > 100:
                raise Exception
            
            return students
            loop = False
            
        except:
            print("Error. Please enter an interger from 1 to 100.\n")
            
# Program: Creates program to get user input for simulation count.      
def get_simulations():
    """Asks user for amount of simulations
    
        Returns:
           simulations(int): Number of simulations.
    """

    loop = True
    
    while loop:
        try:
            simulations = int(input("Please enter amount of simulations: "))
            
            if simulations < 1 or simulations > 1000:
                raise Exception
            
            return simulations
            loop = False
            
        except:
            print("Error. Please enter an interger from 1 to 1000.\n")
            
# Program: Creates program to generate random birthdays.      
def get_birthdays(students):
    """Returns a list of n integers randomly chosen between 1 and 365.
    
	 Args:
           students(int): Amount of students.
           Assumption: n >= 0
    
	 Returns:
           birthdays(list): List of n integers between 1-365.
    """

    import random
    birthdays = []

    for n in range(students):
        random_birthday = random.randint(1, 365)
        birthdays.append(random_birthday)
        
    return birthdays

# Program: Creates program to find duplicates.          
def find_dup(birthdays):
    """Returns a list with the duplicate birthdays.
    
	 Args:
           birthdays(list): list of birthdays.
           Assumption: n >= 0
    
	 Returns:
           duplicate_list(list): List with the duplicate birthdays.
    """
    
    duplicate_list = []
    
    for i in birthdays:
        if birthdays.count(i) > 1:
            find_dup = i, birthdays.count(i)
            duplicate_list.append(find_dup)
            
    return duplicate_list

# Program: Creates program to remove duplicates.          
def remove_duplicates(list_one):
    """Removes duplicate values in duplicate list.
    
	 Args:
           list_one(list): List to remove duplicates out of.
           Assumption: n >= 0
    
	 Returns:
           list_two(list): List of duplicate birthdays without double birthdays.
    """
    
    list_two = []

    for i in list_one:
        if i not in list_two:
            list_two.append(i)
            
    list_two.sort()
    return list_two

# Program: Creates program to ask if user wants the duplicate birthdays. 
def show_dup():
    """Returns True or False if user wants to see birthdays.
    
	 Returns:
           True, False
    """
    
    while True:
        show_birthdays = input("\nwould you like to see the duplicate \
birthdays? 'yes'/'no': ")
            
        while show_birthdays != "yes" and show_birthdays != "no":
            show_birthdays = input("\nIncorect input, would you like to see \
the duplicate birthdays? 'yes'/'no': ")
                    
        if show_birthdays == "no":
            return False
        
        elif show_birthdays == "yes":
            print("\n")
            return True
        
# Program: Asks user to try again and prints msg accordingly.               
def try_again():
    """Asks user to try again.
    
	 Returns:
           True, False
    """
    
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
        
# Program: Creates main program.
def main():
    """Runs Algorithm to complete program. 
    
    """
    
    loop = True
    while loop:
        count = 0
        simulations = get_simulations()
        students = get_students()
        show = show_dup()
        
        for i in range(simulations):
            birthdays = get_birthdays(students)
            duplicate_list = find_dup(birthdays)
            
            if remove_duplicates(duplicate_list) != []:
                count += 1
                
            if show == True:
                for i in (remove_duplicates(duplicate_list)):
                    print(i[1], "people have the same birthday on day", \
                          str(i[0])+ ".")
                    
        print("\nOut of", simulations, "simulations.\n"\
+ str(count), "times there were at least one duplicate birthday. \
\nTherefore there is a", str(count / 10) + "% chance to have a \
duplicate birthday with", students, "students.")
        loop = try_again()

# Main program.
main()
