# ==================== Exercise 01: Python Calculator ====================

"""
Exercise Objective:
- Build a console-based arithmetic calculator using conditional flow control (if / elif / else).
- Key Concepts:
    - String equality checking for valid arithmetic operators (+, -, *, /).
    - Floating-point numeric conversions with float(input()) to support decimal inputs.
    - Output formatting with round() to round results to the nearest integer.
    - Fallback error handling using an 'else' block for unrecognized operators.
"""

# ==================== 1. Calculator Inputs ====================
# Accepts arithmetic operator string and two numeric operands (floats).
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# ==================== 2. Operation Dispatching & Evaluation ====================
# Evaluates which arithmetic branch to execute based on the entered operator.

# Addition branch
if operator == "+":
    result = num1 + num2
    print(round(result))

# Subtraction branch
elif operator == "-":
    result = num1 - num2
    print(round(result))

# Multiplication branch
elif operator == "*":
    result = num1 * num2
    print(round(result))

# Division branch
elif operator == "/":
    result = num1 / num2
    print(round(result))

# Fallback branch: Executes if the user enters an unsupported operator symbol.
else:
    print(f"{operator} is not a valid operator.")

