# Functions in Python
# A function is a reusable block of code that executes only when called.
# Helps organize code into modular, maintainable, and DRY (Don't Repeat Yourself) components.

# Built-in function: Pre-defined by Python (e.g., print(), len(), type(), input())
print("Hello World")


# --- 1. Defining and Calling a User-Defined Function ---
# Use the 'def' keyword followed by function name and parentheses ():
def greet():
    print("Hello")

# Calling / invoking the function
# Output: Hello
greet()


# --- 2. Parameters vs Arguments ---
# Parameter : Variable listed inside parentheses in the function definition (e.g., 'name')
# Argument  : Actual value sent to the function when it is called (e.g., "Sans")

def hello(name):
    print(f"Hello {name}!")

# Output: Hello Sans!
hello("Sans")

# Function with multiple parameters:
def sum(a, b):
    print(f"The sum of {a} and {b} is {a+b}")

# Output: The sum of 9 and 1 is 10
sum(9, 1)

# Output: The sum of 13 and 23 is 36
sum(13, 23)


# --- 3. Types of Arguments ---

# A. Positional Arguments: Arguments matched to parameters based on position/order
def wish(name, age):
    print(f"Your name is {name} and your age is {age}.")

# Positional: "Sans" -> name, 21 -> age
wish("Sans", 21)

# B. Keyword Arguments: Passed by parameter name; order does not matter
wish(age = 21, name = "Sans")

# C. Default Arguments: Provides a fallback value if argument is omitted in the call
# Note: Default parameters must always follow non-default parameters
def diff(a, b = 45):
    print(f"The difference between {b} and {a} is {b-a}.")

# 'b' defaults to 45: 45 - 12 = 33
diff(12)


# --- 4. Function Logic Example: Palindrome Checker ---
# Encapsulates reusable algorithmic logic inside a function
def palindrome(str):
    rev = ""
    for i in range(len(str)-1, -1, -1):
        rev = rev + str[i]

    if rev == str:
        print(f"{str} is a palindrome!")
    else:
        print(f"{str} is not palindrome!")

# Output: racecar is a palindrome!
palindrome("racecar")

# Output: hello is not palindrome!
palindrome("hello")


# --- 5. The 'return' Statement ---
# Sends a value back to the caller and terminates function execution.
# If no return statement is specified, Python functions return 'None' by default.
def ask():
    return "Hello! How are You?"

# Output: Hello! How are You?
print(ask())