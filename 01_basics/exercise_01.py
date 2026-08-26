# ==================== Exercise 01: Rectangle Area Calculator ====================

"""
Exercise Objective:
- Calculate the area of a rectangle using user-supplied length and breadth dimensions.
- Mathematical Formula: Area = length * breadth
- Key Concept: Using float(input()) to allow decimal input measurements (e.g., 5.5 cm).
"""

# ==================== 1. Dimension Inputs ====================
# float() ensures decimal values are preserved for accurate geometric calculation.
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))

# ==================== 2. Area Calculation ====================
area = length * breadth

# ==================== 3. Formatted Result Display ====================
# Formats and displays the calculated area with unit notation (cm²).
print(f"The area of the rectangle is {area}cm².")