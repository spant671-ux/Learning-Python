# ==================== Exercise 02: Shopping Cart Total Calculator ====================

"""
Exercise Objective:
- Build an interactive shopping cart receipt calculator.
- Mathematical Formula: Total = price * quantity
- Key Concept: Handling heterogeneous input types:
    - String (str) for item name
    - Floating-point (float) for unit price
    - Integer (int) for item count
"""

# ==================== 1. Shopping Inputs ====================
# Accepts item description as string (str)
item = input("What item would you like to buy?: ")

# Converts price to float to support cents/decimals (e.g., 4.99)
price = float(input("What is the price?: "))

# Converts quantity to integer (int) since items are counted in whole units
quantity = int(input("How many items would you like?: "))

# ==================== 2. Total Calculation ====================
total = price * quantity

# ==================== 3. Receipt Output ====================
print(f"You have bought {quantity}x {item}/s.")
print(f"Your total is ${total}.")