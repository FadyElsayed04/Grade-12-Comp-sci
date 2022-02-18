# Name: Fady Elsayed
# Date: sept 21 2021
# File Name: 1.6 1.py
# Description: A Program that calculaates the sum of the first n cubes.
# Test Cases: 0, 1, 5, 10, 50.

# Process: creats function to calculate the sum of the first n cubes.
def sum_cubes(n):
    cubes = 0
    for i in range(1, n + 1):
        cubes =+ cubes + i ** 3
    print(cubes)

# Main Program:
sum_cubes(50)
