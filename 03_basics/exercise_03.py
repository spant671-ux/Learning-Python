# ==================== Exercise 03: Temperature Converter ====================

"""
Exercise Objective:
- Convert temperature measurements bidirectionally between Celsius (C) and Fahrenheit (F).
- Conversion Formulas:
    - Celsius (C) -> Fahrenheit (F): (9 * temp) / 5 + 32
    - Fahrenheit (F) -> Celsius (C): (temp - 32) * 5 / 9
- Key Concepts:
    - String equality checking to select conversion formula.
    - Floating-point input parsing with float(input()).
    - Operator precedence and precision rounding with round(temp, 1).
    - Fallback error handling for unsupported unit strings.
"""

# ==================== 1. Temperature & Unit Inputs ====================
# Accepts scale unit indicator (str: 'C' or 'F') and numeric temperature (float).
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: "))

# ==================== 2. Conversion Logic & Output ====================
# Converts Celsius to Fahrenheit
if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheight is {temp}°F")

# Converts Fahrenheit to Celsius
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)

# Invalid unit fallback
else:
    print(f"{unit} is an invalid unit of measurement.")