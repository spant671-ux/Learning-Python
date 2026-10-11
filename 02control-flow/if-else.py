# Conditional Statements (Control Flow) in Python

# --- 1. The 'if' Statement ---
# Executes the indented block ONLY if the condition evaluates to True.
# Indentation (4 spaces) defines the code block in Python (replaces {} in C/Java/JS).

a = 13

# Condition is True (13 > 10) -> code block executes
if a > 10:
    print("Greater than 10")


# --- 2. The 'if-else' Statement ---
# Provides two mutually exclusive paths:
# Runs 'if' block when condition is True; runs 'else' block when False.

# 13 > 14 is False -> 'if' block is skipped, 'else' block executes
if a > 14:
    print("Greater than 10")
else:
    print("Smaller than 10")

# Example: Decision making using integer input
money = int(input("Please give me money: "))
if money > 10:
    print("Will buy expensive!")
else:
    print("Buy Cheap!")


# --- 3. The 'if-elif-else' Ladder ---
# Tests multiple conditions in order. Executes the FIRST condition that evaluates to True,
# then skips the rest. 'else' acts as a default fallback if none match.

if money == 10:
    print("Buy Cheap!")
elif money == 20:
    print("Buy in Moderate amount!")
else:
    print("Will buy expensive!")


# --- 4. Short-Hand if-else (One-Line Syntax) ---
# Allows writing compact condition checks on a single line.
# Note: Without typecasting, input() returns strings (compared lexicographically).
x = input("Give first number X: ")
y = input("Give second number Y: ")

if x > y: print("X is the greater number!")
else: print("Y is the greater number!")


# --- 5. String Comparison with if-elif-else ---
gender = input("What is your gender? (male/female): ")

if gender == "male":
    print("Welcome Sir!")
elif gender == "female":
    print("Welcome Ma'am!")
else:
    print("Please provide a valid gender!")
