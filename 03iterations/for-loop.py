# For Loops & Iterations in Python

# --- 1. The range() Function ---
# Syntax: range(start, stop, step)
# - start: Starting integer (inclusive, default: 0)
# - stop:  Stopping integer (exclusive — loop stops before reaching this value)
# - step:  Increment / decrement value (default: 1)

# Example: Iterating from 1 to 20 (step +1)
# for i in range(1, 21, 1):
#     print(i)

# Example: Iterating from 20 to 50
# for i in range(20, 51, 1):
#     print(i)

# Example: Reverse iteration / countdown using negative step (-1)
# Counts down from 16 to 1
# for i in range(16, 0, -1):
#     print(i)

# Example: Reverse iteration with negative numbers (-3 down to -15)
# for i in range(-3, -16, -1):
#     print(i)


# --- 2. Real-World Application: Multiplication Table ---
# Generates the multiplication table of 'n' from n*1 to n*10 using step=n
# n = int(input("What number's table do you want?: "))
# for i in range(n, (n * 10) + 1, n):
#     print(i)


# --- 3. Iterating Over Strings ---

# Approach A: Index-based iteration using len() and range()
# a = "Hello World"
# print("Length of string:", len(a))
# for i in range(len(a)):
#     print(a[i])

# Approach B: Direct character iteration (Pythonic way — cleaner and preferred)
# x = "My name is Sans"
# for char in x:
#     print(char)


# --- 4. Loop Control Statements: break and continue ---

# 'break' terminates the loop completely when condition is met
# Prints 1 through 14, terminates upon reaching 15
# for i in range(1, 21):
#     if i == 15:
#         break
#     print(i)

# 'continue' skips only the current iteration and jumps to the next
# Prints 1 through 20, skipping 6
# for i in range(1, 21):
#     if i == 6:
#         continue
#     print(i)


# --- 5. The for...else Construct ---
# Python-unique feature: The 'else' block runs ONLY IF the loop terminates normally
# (i.e. completes all iterations without encountering a 'break' statement).

# for i in range(1, 21):
#     if i == 15:
#         print("Break statement is executed!")
#         break
#     print(i)
# else:
#     # Will NOT execute here because loop was terminated by 'break'
#     print("Break statement isnt executed!")

# n = int(input("Tell your number: "))
# for i in range(n):
#     print("Hello")

# n = int(input("Tell your number: "))
# for i in range(1, n+1, 1):
#     print(i)

# n = int(input("Tell your number: "))
# for i in range(n, 0, -1):
#     print(i)

# n = int(input("Tell the number for the table: "))
# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# n = int(input("Tell your number: "))
# sum = 0
# for i in range(1, n+1,):
#     sum = sum+i
# print(f"Sum of {n} digits is: {sum}")

# n = int(input("Enter your number: "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(f"Factorial of {n} is {fact}")

# n = int(input("Enter your number: "))
# even = 0
# odd = 0
# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#        odd = odd+i 
# print(f"Sum of even numbers is {even} and sum of odd numbers is {odd}.")

# n = int(input("Enter your number: "))

# for i in range(1, n+1):
#      if n%i == 0:
#           print(i)

# n = int(input("Check your number is perfect or not: "))
# sum = 0
# for i in range(1, n):
#     if n%i == 0:
#         sum = sum+i

# if sum == n:
#     print("Your number is perfect")
# else:
#     print("Not a perfect number")

