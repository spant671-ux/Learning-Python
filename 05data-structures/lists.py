# Lists in Python
# A list is a built-in, versatile data structure used to store collections of items.
# Core characteristics of Python lists:
# 1. Mutable      : Elements can be added, updated, or removed in-place.
# 2. Ordered      : Elements maintain their defined insertion sequence (accessed via 0-based index).
# 3. Duplicates   : Can contain duplicate values.
# 4. Heterogeneous: Can store elements of mixed data types (int, float, bool, str, functions, etc.).


# --- 1. Creating and Modifying Lists ---
# Lists are defined using square brackets []

a = [1, 2, 3, 4.3, 5, True, "Hello", 2]

# Mutability: Modifying an element directly at index 0
a[0] = 99
print("Mutated list a:", a)


# --- 2. Iterating Over a List ---
b = [1, 2, 3, 4.3, 5, 6]

# Approach 1: Index-based iteration using range() and len()
# Useful when the index position is required during traversal
print("\n--- Iteration using Indices ---")
for i in range(len(b)):
    print(f"Index {i} -> Value: {b[i]}")

# Approach 2: Direct value iteration (Pythonic & idiomatic)
# Preferred when you only need the element values
print("\n--- Iteration directly over Values ---")
for item in b:
    print(item)


# --- 3. Functions vs Methods in Python ---
# Function: Standalone callable (e.g., len(l), dir(l), type(l))
# Method  : Function bound to an object, invoked via dot notation (e.g., l.append(), l.insert())
# dir(list) displays all attributes and methods available on list objects:
# print(dir(list))

l = [1, 2, 3, 4, 5]
print("\nInitial list l:", l)

# .append(x): Adds a single item 'x' to the end of the list
l.append(6)
l.append(7)
print("After append(6) & append(7):", l)

# .insert(index, x): Inserts item 'x' at the specified index position (shifts remaining items right)
l.insert(2, 21)
print("After insert(2, 21):", l)

# .extend(iterable): Appends all items from an iterable/list to the end of the list
l.extend([9, 10, 11])
print("After extend([9, 10, 11]):", l)

# .remove(x): Removes the first occurrence of value 'x' (raises ValueError if value is not present)
l.remove(1)
print("After remove(1):", l)


# --- 4. Practice Problems & Algorithmic Patterns ---

# Problem 1: Filter positive and negative numbers from a list
a = [6, -89, 9, 2, -98, -6]

print("\nPositive numbers:")
for i in a:
    if i >= 0:
        print(i, end=" ")
print()

print("Negative numbers:")
for i in a:
    if i < 0:
        print(i, end=" ")
print()


# Problem 2: Calculate the sum and arithmetic mean of list elements
b = [2, 4, 6, 8, 10]
total = 0
for i in b:
    total = total + i

mean = total / len(b)
print(f"\nSum: {total}, Mean: {mean}")


# Problem 3: Find the greatest number in a list and its index
c = [1, 2, 32, 444, 56, 999]
greatest = c[0]
index = 0

for i in range(len(c)):
    if c[i] > greatest:
        greatest = c[i]
        index = i

print(f"\nGreatest number in list c is {greatest} at index {index}.")


# Problem 4: Find the greatest and second greatest numbers without sorting
d = [1, 2, 3, 4, 66, 88, 999, 98, 2]
greatest = d[0]
sec_greatest = d[0]

for i in range(len(d)):
    if d[i] > greatest:
        sec_greatest = greatest  # Previous greatest becomes second greatest
        greatest = d[i]          # Update new greatest
    elif d[i] > sec_greatest:
        sec_greatest = d[i]      # Update second greatest if greater than current second

print(f"\nIn list d -> Greatest: {greatest}, Second Greatest: {sec_greatest}")


# Problem 5: Check if a list is sorted in ascending order (using for...else)
# The 'else' block executes only if the loop completes without encountering a 'break'
e = [33, 99, 1, 2, 34, 5]

for i in range(len(e) - 1):
    if e[i] < e[i + 1]:
        continue
    else:
        print("\nYour list is not sorted!")
        break
else:
    print("\nYour list is sorted!")