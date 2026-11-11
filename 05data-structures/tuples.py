# Tuples in Python
# A tuple is a built-in, immutable sequence data structure used to store collections of items.
# Core characteristics of Python tuples:
# 1. Immutable    : Elements cannot be changed, added, or removed after creation.
# 2. Ordered      : Elements maintain their defined insertion sequence (accessed via 0-based index).
# 3. Duplicates   : Can contain duplicate values.
# 4. Heterogeneous: Can store elements of mixed data types (int, float, bool, str, functions, None, etc.).


# --- 1. Creating Tuples & The Single-Element Quirk ---
# Tuples are defined using parentheses () or comma-separated values

# Heterogeneous collection with duplicates:
# Note: print() returns None, which is stored as a valid object in the tuple
a = (1, 2, 3, 4, 5, 5, 6.5, print(), "hello")
print("Tuple a:", a)

# Single-element tuple quirk:
# Parentheses around a single value without a comma are treated as standard math grouping.
# A trailing comma is REQUIRED to define a single-element tuple:
not_a_tuple = (1)   # Evaluates to an int (1)
n = (1,)            # Evaluates to a tuple with one element
print("\nType of (1)  :", type(not_a_tuple))  # <class 'int'>
print("Type of (1,) :", type(n))            # <class 'tuple'>


# --- 2. Immutability: What Makes Tuples Special ---
# Tuples cannot be modified after creation. Attempting to assign or delete raises a TypeError:
# a[0] = 99  # TypeError: 'tuple' object does not support item assignment
# del a[0]   # TypeError: 'tuple' object doesn't support item deletion
# Why use tuples over lists?
# - Data Integrity : Guarantees that data cannot be accidentally modified (e.g. coordinates, config settings).
# - Performance    : Memory-efficient and slightly faster allocation/iteration than lists.
# - Dictionary Keys: Tuples can be used as dictionary keys (if elements are hashable), unlike lists.


# --- 3. Iterating Over a Tuple ---
# Approach 1: Index-based iteration using len() and range()
# Useful when the index position is needed
print("\n--- Iteration using Indices ---")
for i in range(len(a)):
    print(f"Index {i} -> Value: {a[i]}")

# Approach 2: Direct value iteration (Pythonic & idiomatic)
# Preferred when you only need the element values
print("\n--- Iteration directly over Values ---")
for item in a:
    print(item)


# --- 4. Built-in Tuple Methods ---
# Because tuples are immutable, they provide only TWO built-in methods: .index() and .count()

# .index(x): Returns the index of the FIRST occurrence of value 'x'
index = a.index(5)
print("\nFirst index of 5:", index)

# .count(x): Returns the total number of times value 'x' appears in the tuple
count = a.count(5)
print("Count of 5:", count)


# --- 5. Tuple Packing and Unpacking ---
# Packing: Assigning multiple comma-separated values into a single tuple
# Unpacking: Extracting elements from a tuple directly into individual variables
w, x, y, z = (1, 2, 3, 4)
print(f"\nUnpacked variables -> w: {w}, x: {x}, y: {y}, z: {z}")

# Pythonic variable swap using tuple unpacking:
val1, val2 = 10, 20
val1, val2 = val2, val1
print(f"After swap -> val1: {val1}, val2: {val2}")


# --- 6. Slicing & Common Operations ---
nums = (10, 20, 30, 40, 50, 60)

# Slicing: tuple[start : stop : step] (produces a new tuple)
print("\nSlice [1:4]:", nums[1:4])          # (20, 30, 40)
print("Reversed slice [::-1]:", nums[::-1]) # (60, 50, 40, 30, 20, 10)

# Concatenation (+) and Repetition (*):
t1 = (1, 2)
t2 = (3, 4)
print("Concatenation (t1 + t2):", t1 + t2)  # (1, 2, 3, 4)
print("Repetition (t1 * 3):", t1 * 3)        # (1, 2, 1, 2, 1, 2)

# Converting between List and Tuple:
converted_list = list(nums)   # Create a mutable copy
converted_list.append(70)     # Modify list
updated_tuple = tuple(converted_list)
print("Updated tuple via list conversion:", updated_tuple)
