# Input and Output (I/O) in Python

name = "sans"
age = 21

# --- Basic Output with print() ---
# print() displays output to the console. By default, it ends with a newline (\n).

# Output: sans
print(name)

# Output: 21
print(age)

# Multiple arguments separated by comma; print() inserts a space between them by default (sep=" ")
# Output: sans 21
print(name, age)


# --- String Formatting ---

# 1. Comma separation (converts arguments to strings and separates with spaces)
# Output: Hello my name is sans and my age is 21
print("Hello my name is", name, "and my age is", age)

# 2. f-strings (Formatted String Literals, Python 3.6+)
# Modern, recommended way to interpolate variables/expressions inside strings (like template literals in JS)
# Output: Hello my name is sans and my age is 21
print(f"Hello my name is {name} and my age is {age}")


# --- User Input with input() ---
# input() pauses execution and waits for input from the terminal.
# Note: input() ALWAYS returns user input as a string (str).

# Reading string input
name = input("What is your name?: ")

# Reading numeric input: Must explicitly typecast with int() or float()
age = int(input("What is your age?: "))

# Displays entered name
print(name)

# Output: <class 'int'> (Verifies the string input was converted to integer)
print(type(age))
