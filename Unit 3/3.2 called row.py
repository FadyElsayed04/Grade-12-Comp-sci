# Name: Fady Elsayed
# Date: oct 21st 2021
# File Name: 3.2 called row.py
# Description: Uses the users input do find row.


# Program: Finds called row from users input. 
def called_row(table, r):
    """Finds and row and adds to list.

    Args:
        table(list): The list user wants row out of.
        r(int): The row user wants.
    
    Returns:
    row(list): list of row n from orginal list.
    """
    
    try:
        if r >= 0 and r < len(table):
            return(table[r])
    except:
        return("Error")


# Program: Test cases:
def main():
    """Tests functions.
    
    Returns:
    Values
    """
# called_row() test cases
    test_list = [[1, 3, 2, 3], [4, 5, 9, 6], [5, 3, 1, 1]]
    for i in range(-2, 5):
        print(called_row(test_list, i))     # None, None, [1, 3, 2, 3],
                                        #[4, 5, 9, 6], [5, 3, 1, 1], None, None

# Main program
if __name__ == "__main__":
    main()
