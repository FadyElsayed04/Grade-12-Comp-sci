# Name: Fady Elsayed
# Date: Oct 20th 2021
# File Name: 3.1 Locker Problem.py
# Description: A Program that runs simulations of the locker problem.

# Creates main function to simulate Day 1 Locker Problem.
def main():
    """
    Simulation for locker problem.    
    """
    lockers = []
    open_lockers = []
    count_open = 0
    count_closed = 0
    
    for i in range(1000):
        lockers.append(False)


    for i in range(1,1001):
        for x in range(1,1000):
            if x % i == 0:
            
                if lockers[x] == True:
                    lockers[x] = False
                else:
                    lockers[x] = True

                 
    for i in range(len(lockers)):
        if lockers[i] == True:
            open_lockers.append(i)
            count_open += 1

    print("The locker that will remain open are:\n" + str(open_lockers))
    print("There are", count_open, "open lockers.")

# Main Program
main()
