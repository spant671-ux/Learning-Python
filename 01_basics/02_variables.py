# ==================== Variables & Fundamental Data Types ====================

"""
Python Variables & Type System Overview:
- Variables in Python are references (labels) bound to objects stored in memory.
- Dynamically Typed: You do not need to explicitly declare variable types; Python infers them at runtime.
- Strongly Typed: Python prevents unintended operations between incompatible types (e.g., adding string to number).
- Naming Conventions: Use snake_case for variable names (PEP 8 standard).
"""

# ==================== 1. Strings (str) ====================
# Strings are immutable sequences of Unicode characters enclosed in single ('...') or double ("...") quotes.
first_name = "santosh"
food = "pizza"
email = "bro123@fake.com"

# Formatted String Literals (f-strings):
# Introduced in Python 3.6 (PEP 498). Expressions inside curly braces { } are evaluated at runtime.
# Expected Output: Hello santosh
print(f"Hello {first_name}")

# Expected Output: You like pizza
print(f"You like {food}")

# Expected Output: Your email is bro123@fake.com
print(f"Your email is {email}")


# ==================== 2. Integers (int) ====================
# Integers represent whole numbers (positive, negative, or zero) with arbitrary precision (no fixed 32/64-bit overflow limit).
age = 25
quantity = 3
num_of_students = 30

# Expected Output: You are 25 years old.
print(f"You are {age} years old.")

# Expected Output: You are buying 3 items.
print(f"You are buying {quantity} items.")

# Expected Output: Your class has 30 students.
print(f"Your class has {num_of_students} students.")


# ==================== 3. Floating-Point Numbers (float) ====================
# Floats represent real numbers with a decimal point, implemented using C doubles (64-bit IEEE 754 standard).
price = 10.99
gpa = 8.9
distance = 5.5

# Expected Output: The price is $10.99.
print(f"The price is ${price}.")

# Expected Output: Your gpa is 8.9.
print(f"Your gpa is {gpa}.")

# Expected Output: You ran 5.5 kms.
print(f"You ran {distance} kms.")


# ==================== 4. Booleans (bool) & Conditionals ====================
# Booleans represent binary truth values: True or False (Case-sensitive; internally subclasses of int where True == 1, False == 0).
# Control Flow: Python uses indentation (standard 4 spaces) instead of curly braces {} to define code blocks.

# Example 1: is_student evaluates to False -> else block executes
is_student = False
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")

# Example 2: for_sale evaluates to True -> if block executes
for_sale = True
if for_sale:
    print("That item is for sale.")
else:
    print("This item isn't available.")

# Example 3: is_online evaluates to True -> if block executes
is_online = True
if is_online:
    print("You are online.")
else:
    print("You are offline.")


