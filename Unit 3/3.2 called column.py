# Name: Fady Elsayed
# Date: oct 21st 2021
# File Name: 3.2 called column.py
# Description: Uses the users input to call a column.


# Program: Finds called column from users input. 
def called_column(table, c):
    """Finds and column and adds to list.

    Args:
        table(list): The list user wants column out of.
        c(int): The column user wants.
    
    Returns:
    column(list): list of column n from orginal list.
    """
    
    column = []
    try:
        
        if c >= 0 and c < len(table):
            for i in range(len(table)):
                column.append(table[i][c])

        return column
    
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
        print(called_column(test_list, i))     # [], [], [1, 4, 5], [3, 5, 3],
                                               # [2, 9, 1], [], []

# Main program
if __name__ == "__main__":
    main()
