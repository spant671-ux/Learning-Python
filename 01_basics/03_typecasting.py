# ==================== Type Casting (Type Conversion) ====================

"""
Type Casting Overview:
- The process of converting the value of one data type into another.
- Two forms in Python:
  1. Implicit Conversion: Handled automatically by Python (e.g., int + float -> float).
  2. Explicit Conversion: Done manually using built-in constructors (str(), int(), float(), bool()).
"""

# Initial variable declarations with original types:
name = "santosh pant"  # str
age = 21               # int
gpa = 8.9              # float
is_student = True      # bool


# ==================== 1. Integer to String Conversion ====================
# str() constructor converts numerical data to string representation.
age = str(age)

# String Concatenation: Since 'age' is now a string ("21"), the '+' operator performs string concatenation rather than numeric addition.
age += "1"

# Expected Output: "211" (not 22)
print(age)


# ==================== 2. String to Boolean Conversion ====================
# bool() constructor converts values to True or False based on Truthy/Falsy evaluation.
# In Python:
# - Falsy values: Empty string (""), 0, 0.0, None, False, empty sequences ([], {}, ()).
# - Truthy values: Any non-empty string ("santosh pant"), non-zero numbers, populated collections.

# Since 'name' is a non-empty string, bool(name) evaluates to True.
name = bool(name)

# Expected Output: True
print(name)