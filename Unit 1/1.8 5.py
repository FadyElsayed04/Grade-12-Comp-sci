# Name: Fady Elsayed
# Date: sept 22 2021
# File Name: 1.8 5.py
# Description: A Program to remove duplicates from list.

# Process: Creates function to remove duplicates.
def remove_duplicates(list_one):
    list_two = []

# Process: Loops to add 1 of every value from list 1 to list 2.
    for i in list_one:
        if i not in list_two:
            list_two.append(i)
            
# Process: Sorts list.
    list_two.sort()
    
# Process: Returns list 2.
    return list_two

# Main Program:
print(remove_duplicates([1, 2, 3, 3, 4, 2, 1, 5]))
        
