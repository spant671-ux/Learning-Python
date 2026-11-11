# Sets in Python
# A set is a built-in data structure used to store collections of unique, unordered items.
# Core characteristics of Python sets:
# 1. Unordered    : Elements have no defined index or position (no indexing or slicing like a[0]).
# 2. Unique       : Duplicate values are automatically eliminated; every element is distinct.
# 3. Mutable      : The set itself can be modified (elements can be added or removed).
# 4. Hashable Only: Elements must be immutable and hashable (e.g., int, float, str, tuple).


# --- 1. Creating Sets & The Empty Set Quirk ---
# Sets are defined using curly braces {} with comma-separated values

a = {1, 2, 3, 4, 5, 6}
print("Set a:", a)

# Automatic duplicate removal:
duplicates_demo = {1, 2, 2, 3, 3, 3, 4}
print("Duplicates auto-removed:", duplicates_demo)  # Output: {1, 2, 3, 4}

# The Empty Set Quirk:
# Empty curly braces {} create an empty dictionary (dict), NOT a set!
# Always use the set() constructor to create an empty set:
empty_dict = {}
empty_set = set()
print("\nType of {}:", type(empty_dict))   # <class 'dict'>
print("Type of set():", type(empty_set))  # <class 'set'>


# --- 2. Hashing & Element Requirements ---
# Sets are implemented under the hood using Hash Tables.
# This gives sets an extremely fast average lookup/membership test time complexity of O(1).
# Any object added to a set must have a fixed hash value via the hash() function:

b = hash("hello")
print("\nHash of 'hello':", b)

c = hash((1, 2, 344))
print("Hash of tuple (1, 2, 344):", c)

# Note: Mutable objects (like lists or sets) cannot be hashed and cannot be elements of a set:
# invalid_set = {[1, 2], 3}  # Raises TypeError: unhashable type: 'list'


# --- 3. Iterating Over a Set & Membership Testing ---
# Because sets are unordered, they cannot be traversed by index.
# We iterate directly over the elements:

d = {1, 8, 6, 9, 2, 3, "hello", 4, 5, 7}

print("\n--- Iteration directly over Set elements ---")
for i in d:
    print(i, end=" ")
print()

# High-performance membership testing (O(1) average time):
if "hello" in d:
    print("'hello' exists in set d")


# --- 4. Modifying Sets: Methods & Removals ---
e = {1, 2, 3, 4, 5}
print("\nInitial set e:", e)

# .add(x): Adds a single new element
e.add(10)
print("After add(10):", e)

# .remove(x): Removes value 'x' (raises KeyError if value is not present)
e.remove(2)
print("After remove(2):", e)

# .discard(x): Removes value 'x' safely (does NOT raise an error if absent)
e.discard(99)  # Safe: element 99 does not exist, but no error thrown

# .pop(): Removes and returns an arbitrary element from the set
popped_item = e.pop()
print(f"Popped item: {popped_item}, set after pop():", e)

# .clear(): Removes all elements from the set
e.clear()
print("After clear():", e)  # Output: set()


# --- 5. Mathematical Set Operations ---
x = {1, 2, 3, 4, 5}
y = {4, 5, 6, 7, 8}

print(f"\nx = {x}")
print(f"y = {y}")

# A. Union (| or .union()): All unique elements from both sets
union_set = x | y
print("Union (x | y):", union_set)

# B. Intersection (& or .intersection()): Common elements present in both sets
intersection_set = x & y
print("Intersection (x & y):", intersection_set)

# C. Difference (- or .difference()): Elements present in x but NOT in y
diff_set = x - y
print("Difference (x - y):", diff_set)

# D. Symmetric Difference (^ or .symmetric_difference()): Elements in either set, but not in both
sym_diff = x ^ y
print("Symmetric Difference (x ^ y):", sym_diff)
