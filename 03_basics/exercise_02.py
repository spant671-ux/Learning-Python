# ==================== Exercise 02: Weight Converter ====================

"""
Exercise Objective:
- Convert weight values bidirectionally between Kilograms (K) and Pounds (L).
- Conversion Formulas:
    - Kilograms (K) -> Pounds (Lbs): weight * 2.205
    - Pounds (L) -> Kilograms (Kgs): weight / 2.205
- Key Concepts:
    - float(input()) for numeric weight magnitude.
    - String equality comparison for unit selection.
    - Dynamic variable mutation and output formatting with round(weight, 1).
"""

# ==================== 1. Weight & Unit Inputs ====================
# Accepts numeric weight (float) and target unit indicator (str: 'K' or 'L').
weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

# ==================== 2. Conversion Logic & Unit Updates ====================
# Converts Kilograms to Pounds
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."

# Converts Pounds to Kilograms
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs."

# Invalid unit fallback
else:
    print(f"{unit} was not valid!")

# ==================== 3. Converted Weight Display ====================
print(f"Your weight is {round(weight, 1)} {unit}")