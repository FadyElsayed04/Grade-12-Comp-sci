# moreMath.py

# Program: Finds the sum of first n intergers.
def sumFirstInt(n):
    """Determine the sum of intergers in n.
    
    Args:
        n(int): The total range for the values.
        Assummptions: n >= 0
    
    Returns:
    total_sum(int): The total sum of squares.
    """
    
# process: Calculates and returns sum of first n intergers.
    total_sum = 0
    for i in range(1, n + 1):   
        total_sum += i
        
    return total_sum


# Program: Finds the sum of the first n triangulars.
def sumFirstTriangular(n):
    """Determine the sum of triangulars in n.
    
    Args:
        n(int): The total range for the values.
        Assummptions: n >= 0
    
    Returns:
    total_sum(int): The total sum of the first n triangulars.
    """
    
# process: Calculates and returns sum of first n triangulars.
    total_sum = 0
    triangulars = 0
    for i in range(0, n + 1):   
        triangulars += i 
        total_sum += triangulars
    return total_sum


# Program: Finds the sum of squares in n.
def sumFirstSquare(n):
    """Determine the sum of squares in n.
    
    Args:
        n(int): The total range for the sum of squares.
        Assummptions: n >= 0
    
    Returns:
    total_sum(int): The total sum of squares.
    """
    
# process: Calculates and returns sum of first n squares.
    total_sum = 0
    for i in range(1, n + 1):   
        total_sum += i ** 2
        
    return total_sum


# Program: Finds sum of first n odd numbers.
def sumFirstOdd(n):
    """Determine the sum of the first odd numbers in n.
    
    Args:
        n(int): The total range for first odd numbers.
        Assummptions: n >= 0
    
    Returns:
    total_sum(int): The total sum of the first n odd numbers.
    """

# process: Calculates and returns sum of the first n odd numbers.
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += 2 * i - 1
        
    return total_sum


# Program: Finds sum of first n even numbers.
def sumFirstEven(n):
    """Determine the sum of the first even numbers in n.
    
    Args:
        n(int): The total range for first even numbers.
        Assummptions: n >= 0
    
    Returns:
    total_sum(int): The total sum of the first n even numbers.
    """

# process: Calculates and returns sum of the first n even numbers.
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += 2 * i
        
    return total_sum


# Program: Finding composite numbers until n.
def isComposite(n):
    """Determines if n is composite.
    
    Args:
        num(int): The total range for to find if the values are composite.
        Assummptions: n != 0
    
    Returns:
    True or False 
    """
    
# process: Calculates and returns True or Flase if the n is composite or not.
    if n == 1:
        return True
    
    elif n == 2:
        return False
    
    else:
        for i in range(2, n):
            
            if n % i == 0:
                return True
            
    return False


# Program: Finding prime numbers until n.
def isPrime(n):
    """Determines if n is prime.
    
    Args:
        num(int): The total range for to find if the values are prime.
        Assummptions: n != 0
    
    Returns:
    True or False 
    """
    
# process: Calculates and returns True or Flase if the n is prime or not.
    if n == 1:
        return False
    
    elif n == 2:
        return True
    
    else:
        for i in range(2, n):
            
            if n % i == 0:
                return False
            
    return True



# Program: Test cases.
def main():
    """Tests functions.
    
    Returns:
    value, True or False 
    """
    
# sum_of_cubes() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sumFirstInt(test)) # 0, 1, 3, 6, 10, 15, 55, 1275, 5050
    print()       

# sum_of_cubes() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sumFirstSquare(test)) # 0, 1, 5, 14, 30, 55, 385, 42925, 338350
    print()                     

# sum_odd() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sumFirstOdd(test))    # 0, 1, 4, 9, 16, 25, 100, 2500, 10000
    print()
    
# sum_even() test cases
    for test in [0, 1, 2, 3, 4, 5, 10, 50, 100]:
        print(sumFirstEven(test))   # 0, 2, 6, 12, 20, 30, 110, 2550, 10100
    print()
    
# is_prime() test cases
    for test in [1, 2, 5, 3, 7, 23, 38, 59]:
        print(isPrime(test))    # False, True, True, True, True, True, False, 
    print()                     # True
    
# is_prime() test cases
    for test in [1, 2, 5, 3, 7, 23, 38, 59]:
        print(isComposite(test))    # True, False, False, False, False, False, 
    print()                         # True, False
    
# is_prime() test cases
    for test in [0, 1, 2, 3, 4, 5, 23, 38, 59]:
        print(sumFirstTriangular(test)) # 0, 1, 4, 10, 20, 35, 2300, 9880,
                                        # 35990


# Main program
if __name__ == "__main__":
    main()

