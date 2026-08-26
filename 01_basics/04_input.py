# ==================== User Input in Python ====================

"""
User Input Overview:
- input(prompt): Built-in function to accept user input from the console (stdin).
- Key Rule: input() ALWAYS returns data as a string (str), regardless of what the user types.
- Type Conversion: When expecting numeric input (like integers or floats), explicitly wrap input() with int() or float().
"""

# ==================== 1. String Input ====================
# Accepts text input from the user. Returns a string (str) by default.
name = input("Enter your name?: ")

# ==================== 2. Numeric Input with Typecasting ====================
# Wrapping input() inside int() explicitly converts the entered string into an integer.
# Without int(), performing arithmetic (age + 1) would raise a TypeError.
age = int(input("How old are you?: "))

# Incrementing numerical value (arithmetic addition)
age = age+1

# ==================== 3. Formatted Output ====================
print(f"Hello {name}!")
print("Hello Birthday!")
print(f"You are {age} years old.")