# ==================== Exercise 03: Hypotenuse Calculator (Pythagorean Theorem) ====================

"""
Exercise Objective:
- Calculate the hypotenuse (side c) of a right-angled triangle using the Pythagorean theorem.
- Mathematical Formula: c = √(a² + b²)
- Key Concepts:
    - User input with float typecasting
    - Combining math.sqrt() and pow() for compound algebraic evaluation
"""

import math

# Accepts lengths of triangle perpendicular sides (legs a and b)
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

# Pythagorean theorem: c = √(a² + b²)
c = math.sqrt(pow(a, 2) + pow(b, 2))

# Result display
print(f"Side c = {c}")