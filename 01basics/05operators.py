# Operators in Python

# --- 1. Arithmetic Operators ---
# Follows standard operator precedence: PEMDAS / BODMAS
# +  => Addition
# -  => Subtraction
# *  => Multiplication
# /  => Float Division (always returns a float in Python 3)
# %  => Modulus (remainder)
# // => Floor Division (integer quotient, rounds down)
# ** => Exponentiation (power)

a = 12
b = 6

# Output: 18 (Addition)
print(a + b)

# Output: 6 (Subtraction)
print(a - b)

# Output: 72 (Multiplication)
print(a * b)

# Output: 2.0 (Division always returns a float)
print(a / b)

# Output: 0 (Modulus returns remainder: 12 % 6 is 0)
print(a % b)

# Output: 2 (Floor division truncates decimal to nearest integer)
print(a // b)

# Output: 2985984 (Exponentiation: 12 raised to power 6)
print(a ** b)


# --- 2. Assignment & Compound Assignment Operators ---
# Combines an arithmetic operation with assignment (=, +=, -=, *=, /=, //=, **=, %=)

# a += 20 is shorthand for a = a + 20 (12 + 20 = 32)
a += 20

# Output: 32
print(a)


# --- 3. Comparison (Relational) Operators ---
# Compares two values and always returns a boolean: True or False
# == (equal), != (not equal), > (greater), < (less), >= (greater equal), <= (less equal)

# Output: False (32 == 6 is False)
print(a == b)

# Output: True (32 != 6 is True)
print(a != b)


# --- 4. Logical Operators ---
# Used to combine conditional statements: and, or, not

# 'and' returns True only if BOTH conditions are True
# Output: True (True and True)
print(123 > 100 and 34 == 34)

# 'or' returns True if AT LEAST ONE condition is True
# Output: True (False or False or True)
print(123 < 100 or 45 == 55 or 91 > 80)

# 'not' reverses the boolean result (not True -> False)
# Output: False
print(not 12 == 12)
