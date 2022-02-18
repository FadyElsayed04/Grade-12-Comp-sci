# Name: Fady Elsayed
# Date: oct 21st 2021
# File Name: 3.2 comprehension.py
# Description: prints out a 5x8 table filled with 1s using comprehension.


# Program: Nicely prints 5x8 table of 1s.
def comprehension(table):
    try:
        new_table = [i for i in table if i == 1]
        for i in range(8):
            print(*new_table)
    except:
        return("Error")


# Program: Creates main program.
def main():
    table = [1, 2, 3, 1, 1, 1, 5, 32, "sdd", 3, 1, 34, 56]
    comprehension(table)

# Main Program.
main()
