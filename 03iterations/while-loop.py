# While Loops in Python

# --- 1. Basic while Loop ---
# Repeats a block of code as long as the test condition remains True.
# Key components:
#   1. Initialization: Setting up a starting value (a = 1)
#   2. Condition: Checked before each iteration (a <= 30)
#   3. Update: Modifying the counter (a = a + 1) to avoid an infinite loop

a = 1
while a <= 30:
    print(a)
    a = a + 1
# --- 2. Practice: Extracting Digits of a Number in Reverse ---
# Uses modulo (% 10) to extract the last digit,
# and integer/floor division (// 10) to strip off the last digit.
# Continues until no digits remain (a becomes 0).

a = int(input("Give a number: "))
while a > 0:
    print(a % 10)   # Extracts the last digit
    a = a // 10     # Removes the last digit

a = int(input("Give a number: "))
rev = 0
while a > 0:
    rev = rev*10 + a % 10 
    a = a // 10 
print(rev)


a = int(input("Give a number: "))
copy = a
rev = 0
while a > 0:
    rev = rev*10 + a % 10 
    a = a // 10 
if copy == rev: print("Palindrome")
else: print("Not Palindrome")
