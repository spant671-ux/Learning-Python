# ==================== Conditionals (if / elif / else) ====================

"""
Conditional Statements Overview:
- Used to execute specific blocks of code based on whether a condition evaluates to True or False.
- Keywords:
    - if: Evaluates the initial condition.
    - elif (else if): Evaluates subsequent conditions ONLY if preceding conditions were False.
    - else: Default fallback executed when none of the preceding conditions were met.
- Key Rules:
    - Evaluation Order Matters: Conditions are checked top-to-bottom; the first matching True block executes, skipping all remaining branches.
    - Indentation: Python uses standard 4-space indentation to define the code block for each branch.
    - Equality Check: Use '==' for comparison (equality check), not '=' (assignment).
"""

# ==================== 1. Multi-Condition Numeric Range Checking ====================
# Condition order is critical: Checking 'age > 100' must precede 'age >= 18',
# otherwise a 105-year-old would match 'age >= 18' first and trigger the wrong branch.
age = int(input("Enter your age: "))

if age > 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up.")
elif age < 0:
    print("You haven't been born yet.")
# Note on order: If placed after 'age >= 18', 'age > 100' would become unreachable dead code.
# elif age > 100:
#     print("You are too old to sign up.")
else: 
    print("You must be 18+ to sign up.")


# ==================== 2. String Equality Comparison ====================
# Compares user string input using the '==' equality operator (case-sensitive).
response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food.")
else:
    print("No food for you.")


# ==================== 3. Input Validation (Empty String Check) ====================
# Checks if the user pressed Enter without typing any characters (empty string "").
name = input("Enter your name: ")

if name == "":
    print("You didn't enter a name.")
else:
    print(f"Hello {name}")


# ==================== 4. Direct Boolean Flag Evaluation ====================
# When a variable holds a boolean (True/False), it can be evaluated directly without '== True'.

# Example A: for_sale evaluates to True -> 'if' block executes
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item isn't for sale.")

# Example B: online evaluates to False -> 'else' block executes
online = False

if online:
    print("The user is online.")
else:
    print("The user is offline.")


