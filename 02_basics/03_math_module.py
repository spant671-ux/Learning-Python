# ==================== Python Math Module ====================

"""
Math Module Overview:
- The 'math' module provides access to underlying C mathematical library functions and constants.
- Must be imported via `import math` before use.
- Key Constants:
    - math.pi: Ratio of circle circumference to diameter (~3.141592653589793)
    - math.e: Euler's number / base of natural logarithm (~2.718281828459045)
- Key Functions:
    - math.sqrt(x): Returns the square root of x as a float.
    - math.ceil(x): Rounds a number UP to the nearest integer.
    - math.floor(x): Rounds a number DOWN to the nearest integer.
"""

import math

x = 9.1

# Mathematical constants:
# print(math.pi)
# print(math.e)

# Square root calculation (e.g., sqrt of 9.1 -> ~3.0166)
# result = math.sqrt(x)

# Ceiling: Rounds UP to the next integer (9.1 -> 10)
# result = math.ceil(x)

# Floor: Rounds DOWN to the previous integer (9.1 -> 9)
result = math.floor(x)

# Expected Output: 9
print(result)