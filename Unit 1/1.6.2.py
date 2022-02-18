# Name: Fady Elsayed
# Date: sept 21 2021
# File Name: 1.6 2.py
# Description: A Program that calculates the volume and area of a sphere
# Test Cases: 0, 1, 4, 10.4, 100.344.
import math

# Process: creats function to calculate the volume of the sphere.
def volume_sphere(r):
    volume = 4/3 * math.pi * r ** 3
    return round(volume, 2)

# Process: creats function to calculate the area of the sphere.
def area_sphere(r):
    area = 4 * math.pi * r ** 2
    return round(area, 2)


# Main Program:
print(volume_sphere(100.344), area_sphere(100.344))
