# Comments in Python

# Single-line comment: Starts with '#' and is ignored by Python
# This is a single line comment.

# Multi-line comment: Python doesn't have a /* */ syntax like JS or Java.
# Triple quotes (""" or ''') create multiline strings; when not assigned to a variable, they act as comments.
"""This is a
Multi-Line Comment."""


# Variables
# Python is dynamically typed — variable types are inferred at runtime without declaration.

# Integer variable
a = 18

# String variable
b = "Hello"

# --- Rules for naming variables ---

# 1. Dont use number at start (must begin with a letter or underscore):
# 1a = 18          # SyntaxError: invalid decimal literal

# 2. Dont use space in variables (use snake_case instead):
# my var = "sans"  # SyntaxError: invalid syntax

# 3. Shouldnt use spcl characters in variable (@, $, %, -, etc.):
# my-var = "sans"  # SyntaxError: cannot assign to expression
# user$ = 100      # SyntaxError: invalid syntax

# 4. Variable names are case-sensitive:
# age, Age, and AGE are treated as three separate variables

# 5. Cannot use Python reserved keywords (like if, for, while, class, def, return)