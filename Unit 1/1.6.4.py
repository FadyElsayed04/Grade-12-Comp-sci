# Name: Fady Elsayed
# Date: sept 21 2021
# File Name: 1.6 4.py
# Description: A Program that approximates pi.
# Test Cases: 3, 10, 100, 1000

# Process: creates function to approximates pi.
def approximate_pi(n):
    pi_aprox = 0
    for i in range(0, n):
        print(i)
        
        if i == 0:
            pi = 4/(i + 1)
            
        if i % 2 != 0:
            pi = -4/(i * 2 + 1)
            
        if i % 2 == 0:
            pi = 4/(i * 2 + 1)
            
        pi_aprox = pi_aprox + pi
        
    return(pi_aprox)

# Main Program:
print(approximate_pi(1000))
