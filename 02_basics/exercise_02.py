# ==================== Exercise 02: Circle Area Calculator ====================

"""
Exercise Objective:
- Calculate the area of a circle given its radius.
- Mathematical Formula: Area = π * r²
- Key Concepts:
    - math.pi for π constant
    - pow(radius, 2) for exponentiation
    - round(area, 2) for clean decimal presentation
"""

import math

# Accepts radius dimension as float to allow decimal precision
radius = float(input("Enter the radius of the circle: "))

# Area formula: π * r²
area = math.pi * pow(radius, 2)

# Output rounded to 2 decimal places with cm² unit
print(f"The area is of the circle is {round(area, 2)}cm².")