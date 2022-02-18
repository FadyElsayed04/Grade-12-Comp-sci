# Name: Fady Elsayed
# Date: oct 21st 2021
# File Name: 3.2 print table.py
# Description: Uses the users to print it out nicely formatted.


# Program: Nicely prints 2d list given.
def print_table(table):    
    try:
        for i in range(len(table)):
            print(*table[i])
    
    except:
        return("Error")


# Program: Creates main program.
def main():
    table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_table(table)

# Main Program.
main()
