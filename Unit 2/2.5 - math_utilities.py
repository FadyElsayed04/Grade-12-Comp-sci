import math

# Program: Finds the diagonals.
def num_diag(num):
    """Determine the number of diagonals in an num-sided polygon.

    
    Args:
        num(int): The number of sides of the polygon.
        Assummptions: num > 2
    
    Returns:
    x(int): Number of diagonal.
    """

    x = num *(num - 3)/2
    return x


# Program: Finds the sum of cubes in n.
def sum_cubes(num):
    """Determine the sum of cubes in num.
    
    Args:
        num(int): The total range for the sum of cubes.
        Assummptions: num > 0
    
    Returns:
    total_sum(int): The total sum of cubes.
    """

    total_sum = 0
    for i in range(1, num + 1):   
        total_sum += i ** 3
        
    return total_sum


# Program: Finds sum of first n odd numbers.
def sum_odd(num):
    """Determine the sum of odd numbers in num.
    
    Args:
        num(int): The total range for odd numbers.
        Assummptions: num != 0
    
    Returns:
    total_sum(int): The total sum of odd numbers.
    """

    total_sum = 0
    for i in range(1, num + 1):
        total_sum += 2 * i - 1
        
    return total_sum


# Program: Finds sum of first n even numbers.
def sum_even(num):
    """Determine the sum of even numbers in num.
    
    Args:
        num(int): The total range for even numbers.
        Assummptions: num != 0
    
    Returns:
    total_sum(int): The total sum of even numbers.
    """

    total_sum = 0
    for i in range(1, num + 1):
        total_sum += 2 * i
        
    return total_sum


# Program: Approximates value of pi.
def approximate_pi(num):
    """Approximates value of pi.
    
    Args:
        num(int): The total amount of tests to approximates pi.
        Assummptions: num > 0
    
    Returns:
    pi_aprox(float): Approximates value of pi..
    """

    pi_aprox = 0
    for i in range(0, num):      
        if i == 0:
            pi = 4 / (i + 1)
            
        elif i % 2 != 0:
            pi = - 4 / (i * 2 + 1)
            
        elif i % 2 == 0:
            pi = 4 / (i * 2 + 1)
            
        pi_aprox += pi
        
    return pi_aprox


# Program: Finds factors of n.
def find_factors(num):
    """Finds the factors of n.
    
    Args:
        num(int): Value to find factor of.
        Assummptions: num > 0
    
    Returns:
    factors(int): Factors of num.
    """

    factors = []
    
    for i in range(1, num + 1):
        
        if num % i == 0:
            factors.append(i)
            
    return factors


# Program: Finds factorial of n.
def factorial(num):
    """Finds the factorial of n.
    
    Args:
        num(int): Value to find factorial of
        Assummptions: num > 0
    
    Returns:
    factorial(int): factorial of num.
    """

    factorial = 1
    
    for i in range(1, num + 1):
        factorial = factorial * i
        
    return factorial


# Program: Checks if value is even.
def is_even(num):
    """Finds if n is even.
    
    Args:
        num(int): Value to find if it is even.
        Assummptions: num != 0
    
    Returns:
    True or False 
    """
    
    if num % 2 == 0:
        return True
    
    else:
        return False

    
# Program: Finding prime numbers until n.
def is_prime(num):
    """Finds if n is prime.
    
    Args:
        num(int): Value to find if it is prime.
        Assummptions: num != 0
    
    Returns:
    True or False 
    """

    if num == 1:
        return False
    
    elif num == 2:
        return True
    
    else:
        for i in range(2, num):
            
            if num % i == 0:
                return False
            
    return True


# Program: Test cases.
def main():
    """Tests functions
    
    Returns:
    value, True or False 
    """
    
# num_diag() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(num_diag(test))           # 0, -1, -1, 0, 2, 5, 35, 1175, 4850
        
# sum_of_cubes() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sum_cubes(test))          # 0, 1, 9, 36, 100, 225, 3025,
                                           # 1625625, 25502500

# sum_odd() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sum_odd(test))            # 0, 1, 4, 9, 16, 25, 100, 2500, 10000
        
# sum_even() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sum_even(test))           # 0, 2, 6, 12, 20, 30, 110, 2550, 10100

# approximate_pi() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(approximate_pi(test))     # 0, 4.0, 2.666666666666667,
                                        # 3.466666666666667,
                                        # 2.8952380952380956,
                                        # 3.3396825396825403,
                                        # 3.0418396189294032,
                                        # 3.121594652591011,
                                        # 3.1315929035585537

# find_factors() test cases
    for test in [1, 2, 3, 8, 10, 12, 17, 36]:
        print(find_factors(test))       # [1],  [1, 2],  [1, 3],
                                        # [1, 2, 4, 8], [1, 2, 5, 10],
                                        # [1, 2, 3, 4, 6, 12], [1, 17],
                                        # [1, 2, 3, 4, 6, 9, 12, 18, 36]

# factorial() test cases
    for test in [1, 2, 3, 5, 10, 11, 25]:
        print(factorial(test))          # 1, 2, 6, 120,  3628800,
                                        # 39916800,
                                        # 15511210043330985984000000

# is_even() test cases
    for test in [1, 2, 3, 4, 7, 9, 38, 107]:
        print(is_even(test))            # False, True, False, True, False, False, True, False
    
# is_prime() test cases
    for test in [1, 2, 5, 3, 7, 23, 38, 59]:
        print(is_prime(test))           # False, True, True, True, True, True, False, True


# Main program
if __name__ == "__main__":
    main()
