# ==================== Exercise 01: Circle Circumference Calculator ====================

"""
Exercise Objective:
- Calculate the circumference of a circle given its radius.
- Mathematical Formula: Circumference = 2 * π * r
- Key Concepts:
    - Utilizing math.pi from the standard math module
    - Precision rounding using round(value, ndigits)
"""

import math

# Accepts radius dimension as float to allow decimal precision
radius = float(input("Enter the radius of the circle: "))

# Circumference formula: 2 * π * r
circumference = 2* math.pi* radius

# Output rounded to 2 decimal places with cm unit
print(f"The circumference is: {round(circumference, 2)}cm.")