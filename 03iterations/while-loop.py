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


# --- 3. Practice: Reverse a Number Mathematically ---
# Shifts existing reversed digits to the left (rev * 10),
# then adds the newly extracted last digit (a % 10).

a = int(input("Give a number: "))
rev = 0
while a > 0:
    rev = rev * 10 + a % 10 
    a = a // 10 
print(rev)


# --- 4. Practice: Palindrome Number Check ---
# A number is a palindrome if it equals its reversed value (e.g., 121, 1331).
# We preserve 'a' in 'copy' because 'a' reduces to 0 during the loop.

a = int(input("Give a number: "))
copy = a
rev = 0
while a > 0:
    rev = rev * 10 + a % 10 
    a = a // 10 
if copy == rev:
    print("Palindrome")
else:
    print("Not Palindrome")


# --- 5. Project: Number Guessing Game (while True & break) ---
# Generates a random secret number between 1 and 11.
# Uses an infinite loop (while True) and exits via 'break' upon a correct guess.

import random
num = random.randint(1, 11)
tries = 0

while True:
    guess = int(input("Pick a random number: "))
    if guess == num: 
        tries += 1
        print(f"You guessed the correct value in {tries} tries!")
        break
    elif num < guess: 
        tries += 1 
        print("Go a little lower!")
    elif num > guess: 
        tries += 1
        print("Go a little higher!")
    else: 
        tries += 1
        print("Your guess isnt right!")