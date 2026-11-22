# Dictionaries in Python
# A dictionary is a built-in data structure used to store data in key-value pairs.
# Core characteristics of Python dictionaries:
# 1. Key-Value Mapping : Data is organized as {key: value} associations.
# 2. Hashable Keys     : Keys must be immutable and hashable (e.g., int, float, str, tuple). Mutable types (lists, dicts) CANNOT be keys.
# 3. Unique Keys       : Keys cannot be duplicated; assigning to an existing key overwrites its value.
# 4. Values are Free   : Values can be of ANY data type (mutable, immutable, duplicates allowed).
# 5. Mutable & Ordered : Dictionaries can be modified in-place and maintain insertion order (Python 3.7+).


# --- 1. Creating Dictionaries & Key Requirements ---
# User's initial dictionary:
# Dictionaries in Python
# A dictionary is a built-in data structure used to store data in key-value pairs.
# Core characteristics of Python dictionaries:
# 1. Key-Value Mapping : Data is organized as {key: value} associations.
# 2. Hashable Keys     : Keys must be immutable and hashable (e.g., int, float, str, tuple). Mutable types (lists, dicts) CANNOT be keys.
# 3. Unique Keys       : Keys cannot be duplicated; assigning to an existing key overwrites its value.
# 4. Values are Free   : Values can be of ANY data type (mutable, immutable, duplicates allowed).
# 5. Mutable & Ordered : Dictionaries can be modified in-place and maintain insertion order (Python 3.7+).


# --- 1. Creating Dictionaries & Key Requirements ---
# User's initial dictionary:
a = {
    1: "hello",
    2: 56
}
print("Dictionary a:", a)

# Valid vs Invalid Keys:
# Strings, integers, floats, and tuples are valid keys because they are immutable/hashable:
valid_dict = {
    "name": "Sans",
    42: "The answer",
    (1, 2): "Coordinate point"
}
print("\nValid keys dictionary:", valid_dict)

# Note: Mutable objects like lists cannot be keys:
# invalid_dict = {[1, 2]: "coords"}  # Raises TypeError: unhashable type: 'list'

# Creating empty dictionaries:
empty_dict1 = {}
empty_dict2 = dict()
print("Empty dict type:", type(empty_dict1))

# Duplicate key behavior (overwrites previous value):
dup_dict = {"fruit": "apple", "fruit": "banana"}
print("Duplicate key overwritten:", dup_dict)  # Output: {'fruit': 'banana'}


# --- 2. Accessing & Updating Values ---
# Approach A: Square bracket notation a[key]
print("\nAccessing key 1:", a[1])
# print(a[99])  # Raises KeyError if key does not exist!

# Approach B: .get(key, default) method (Safe access)
# Returns None (or custom default) instead of raising KeyError:
print("Safe access with .get(2):", a.get(2))
print("Non-existent key with default:", a.get(99, "Not Found"))

# Adding new key-value pairs:
a["role"] = "Developer"
print("\nAfter adding 'role':", a)

# Updating an existing key's value:
a[1] = "world"
print("After updating key 1:", a)

# Merging/updating with .update():
a.update({2: 99, "status": "active"})
print("After .update():", a)


# --- 3. Iterating Over a Dictionary ---
user_info = {
    "name": "Sans",
    "age": 21,
    "city": "Dehradun",
    "course": "Python"
}

print("\n--- Iterating over Keys (default) ---")
for key in user_info:
    print(f"Key: {key}")

print("\n--- Iterating over Values using .values() ---")
for val in user_info.values():
    print(f"Value: {val}")

print("\n--- Iterating over Key-Value Pairs using .items() ---")
# .items() returns tuples of (key, value) which can be unpacked cleanly:
for key, value in user_info.items():
    print(f"{key} -> {value}")


# --- 4. Deleting & Removing Elements ---
sample = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nInitial sample dictionary:", sample)

# del: Removes specific key (raises KeyError if key absent)
del sample["a"]
print("After del sample['a']:", sample)

# .pop(key, default): Removes key and returns its value
removed_val = sample.pop("b", "Default")
print(f"Removed value: {removed_val}, Dictionary: {sample}")

# .popitem(): Removes and returns the last inserted (key, value) pair (LIFO)
last_item = sample.popitem()
print(f"Popped last item: {last_item}, Dictionary: {sample}")

# .clear(): Empties the entire dictionary
sample.clear()
print("After .clear():", sample)  # Output: {}


# --- 5. Common Dictionary Patterns & Problem Solving ---

# Pattern 1: Fast Membership Testing (checks KEYS, not values, in O(1) time)
print("\nIs 'name' in user_info?", "name" in user_info)      # True
print("Is 'Sans' in user_info?", "Sans" in user_info)      # False (Sans is a value, not a key)

# Pattern 2: Word / Frequency Counter (Classic pattern using .get())
sentence = "apple banana apple orange banana apple"
frequency = {}

for word in sentence.split():
    # .get(word, 0) returns current count or 0 if seen for the first time
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord frequency counter:", frequency)


# --- 6. Nested Dictionaries ---
# Storing structured/hierarchical data:
student = {
    "id": 101,
    "name": "Sans",
    "academic": {
        "semester": 5,
        "gpa": 8.7,
        "subjects": ["Python", "DSA", "DBMS"]
    }
}

print("\nNested dictionary access:")
print("Student Name:", student["name"])
print("GPA:", student["academic"]["gpa"])
print("First Subject:", student["academic"]["subjects"][0])
print("Dictionary a:", a)

# Valid vs Invalid Keys:
# Strings, integers, floats, and tuples are valid keys because they are immutable/hashable:
valid_dict = {
    "name": "Sans",
    42: "The answer",
    (1, 2): "Coordinate point"
}
print("\nValid keys dictionary:", valid_dict)

# Note: Mutable objects like lists cannot be keys:
# invalid_dict = {[1, 2]: "coords"}  # Raises TypeError: unhashable type: 'list'

# Creating empty dictionaries:
empty_dict1 = {}
empty_dict2 = dict()
print("Empty dict type:", type(empty_dict1))

# Duplicate key behavior (overwrites previous value):
dup_dict = {"fruit": "apple", "fruit": "banana"}
print("Duplicate key overwritten:", dup_dict)  # Output: {'fruit': 'banana'}


# --- 2. Accessing & Updating Values ---
# Approach A: Square bracket notation a[key]
print("\nAccessing key 1:", a[1])
# print(a[99])  # Raises KeyError if key does not exist!

# Approach B: .get(key, default) method (Safe access)
# Returns None (or custom default) instead of raising KeyError:
print("Safe access with .get(2):", a.get(2))
print("Non-existent key with default:", a.get(99, "Not Found"))

# Adding new key-value pairs:
a["role"] = "Developer"
print("\nAfter adding 'role':", a)

# Updating an existing key's value:
a[1] = "world"
print("After updating key 1:", a)

# Merging/updating with .update():
a.update({2: 99, "status": "active"})
print("After .update():", a)


# --- 3. Iterating Over a Dictionary ---
user_info = {
    "name": "Sans",
    "age": 21,
    "city": "Dehradun",
    "course": "Python"
}

print("\n--- Iterating over Keys (default) ---")
for key in user_info:
    print(f"Key: {key}")

print("\n--- Iterating over Values using .values() ---")
for val in user_info.values():
    print(f"Value: {val}")

print("\n--- Iterating over Key-Value Pairs using .items() ---")
# .items() returns tuples of (key, value) which can be unpacked cleanly:
for key, value in user_info.items():
    print(f"{key} -> {value}")


# --- 4. Deleting & Removing Elements ---
sample = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print("\nInitial sample dictionary:", sample)

# del: Removes specific key (raises KeyError if key absent)
del sample["a"]
print("After del sample['a']:", sample)

# .pop(key, default): Removes key and returns its value
removed_val = sample.pop("b", "Default")
print(f"Removed value: {removed_val}, Dictionary: {sample}")

# .popitem(): Removes and returns the last inserted (key, value) pair (LIFO)
last_item = sample.popitem()
print(f"Popped last item: {last_item}, Dictionary: {sample}")

# .clear(): Empties the entire dictionary
sample.clear()
print("After .clear():", sample)  # Output: {}


# --- 5. Common Dictionary Patterns & Problem Solving ---

# Pattern 1: Fast Membership Testing (checks KEYS, not values, in O(1) time)
print("\nIs 'name' in user_info?", "name" in user_info)      # True
print("Is 'Sans' in user_info?", "Sans" in user_info)      # False (Sans is a value, not a key)

# Pattern 2: Word / Frequency Counter (Classic pattern using .get())
sentence = "apple banana apple orange banana apple"
frequency = {}

for word in sentence.split():
    # .get(word, 0) returns current count or 0 if seen for the first time
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord frequency counter:", frequency)


# --- 6. Nested Dictionaries ---
# Storing structured/hierarchical data:
student = {
    "id": 101,
    "name": "Sans",
    "academic": {
        "semester": 5,
        "gpa": 8.7,
        "subjects": ["Python", "DSA", "DBMS"]
    }
}

print("\nNested dictionary access:")
print("Student Name:", student["name"])
print("GPA:", student["academic"]["gpa"])
print("First Subject:", student["academic"]["subjects"][0])