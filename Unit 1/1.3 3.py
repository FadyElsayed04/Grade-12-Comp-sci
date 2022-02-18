# Name: Fady Elsayed
# Date: sept 10 2021
# File Name: 1.3 3.py
# Description: A Program to play rock paper scissors with a cpu.
# Test cases: r, p, s

import random

# Process: selects random value to cpu.
cpu = random.choice("rps")

# Input: Asks user for input.
player = str(input("\nRock, Paper, or Scissors? (r,p,s): "))
       
# Process: checks who won rock paper scissors and prints winner.
if player == "s" and cpu == "p":
    print("\nYou win, I chose:", cpu)
        
elif player == "p" and cpu == "r":
    print("\nYou win, I chose:", cpu)
        
elif player == "r" and cpu == "s":
    print("\nYou win, I chose:", cpu)
        
elif player == cpu:
    print("\nWe tied! I chose:", cpu)

elif cpu == "s" and player == "p":
    print("\nYou lost, I chose:", cpu)
        
elif cpu == "p" and player == "r":
    print("\nYou lost, I chose:", cpu)
        
elif cpu == "r" and player == "s":
    print("\nYou lost, I chose:", cpu)
