# Exception Handling in Python
# Exception handling allows programs to handle runtime errors gracefully without crashing.

# --- 1. Errors vs Exceptions ---
# - Errors (Compile/Parsing Time): Cannot be handled programmatically; must be fixed in code.
#   * SyntaxError      : Code violates Python grammar rules (e.g., missing closing parenthesis)
#   * IndentationError : Incorrect or missing code indentation
#   * TabError         : Inconsistent use of tabs and spaces in indentation
# - Exceptions (Runtime): Logical errors occurring during program execution (e.g. ZeroDivisionError, TypeError, ValueError).

# SyntaxError example:
# print("Hello World"

# IndentationError example:
# a = 12
# if a == 12:
# print("Hello")


# --- 2. Unhandled Exception Demonstration ---
# Without try-except, dividing by 0 crashes the script and terminates execution immediately:
# a = int(input("Tell your number: "))
# print(10/a)   # Raises ZeroDivisionError if a == 0
# print("Okay I have run the division!")


# --- 3. The try-except Block ---
# Code that might raise an exception is placed inside 'try'.
# If an exception occurs, the 'except' block catches it and execution continues safely.

a = int(input("Tell your number: "))

try:
    print(10 / a)
except Exception as err:
    # Catches any standard exception and stores error details in 'err'
    print(f"Sorry there is an error as {err}.")

print("Okay I have done the division!")


# --- 4. The Complete try-except-else-finally Suite ---
# - try     : Code to attempt
# - except  : Runs ONLY IF an exception occurs in the try block
# - else    : Runs ONLY IF NO exception occurs in the try block
# - finally : ALWAYS runs regardless of whether an exception occurred or was handled (ideal for cleanup)

b = input("Enter a word: ")

try: 
    print(10 / b)   # Raises TypeError because dividing int by str is invalid
except Exception as err:
    print(f"Sorry there is an error as {err}.")
else: 
    print("There is no exceptions!")
finally: 
    print("I will run no matter what!")

print("Done!")


# --- 5. Raising Custom Exceptions with 'raise' ---
# Use the 'raise' keyword to manually trigger an exception when custom business rules fail.

age = int(input("Tell your age: "))

try:
    if age < 10 or age > 18:
        # Manually raising a ValueError with a custom error message
        raise ValueError("Your age must be between 10 and 18.")
    else:
        print("Welcome to the class!")
except Exception as err:
    print(f"An error occured as {err}.")

print("The class will start soon.")
