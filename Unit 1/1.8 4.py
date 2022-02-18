# Name: Fady Elsayed
# Date: sept 22 2021
# File Name: 1.8 4.py
# Description: A Program for cumulative summing of lists
# Test Cases: 0, 1, 5, 10, 50.

# Process: Creates function.
def cumulative_sum(n):
        list_one = []
        list_two = []
        sum_list = 0

# Process: Loops n amount.
        for i in range(1, n + 1):
            list_one.append(i)
            sum_list += i
            list_two.append(sum_list)

# Output: returns lists.
        return list_one, list_two

# Input: asks user for input.
num = int(input("Please enter a number: "))

# Main Program:
print(cumulative_sum(num))
