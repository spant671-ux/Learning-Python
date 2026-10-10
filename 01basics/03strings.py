# Strings in Python
# Strings are immutable sequences of Unicode characters.
# In Python 3, all strings are stored in Unicode (CPython dynamically uses 1, 2, or 4 bytes per character based on the highest code point).

# ord() returns the integer Unicode code point of a character
# Output: 65
print(ord("A"))

# chr() converts an integer code point back to its corresponding character
# Output: A
print(chr(65))


# --- String Indexing ---
# Positive index: Starts from 0 (left-to-right)
# Negative index: Starts from -1 (right-to-left / from the end)

a = "Sans"

# Accessing the last character using negative index (-1)
# Output: s
print(a[-1])


# --- String Slicing ---
# Syntax: string[start : stop : step]
# - start : starting index (inclusive, defaults to 0)
# - stop  : ending index (exclusive, defaults to string length)
# - step  : step size / stride (defaults to 1)

a = "hello sans"

# Extracts characters from index 0 to 4 (5 is excluded) with step 1
# Output: hello
print(a[0:5:1])

# Slices from index 0 to the end with default step 1
# Output: hello sans
print(a[0::])

# Omitting start, stop, and step creates a copy of the whole string
# Output: hello sans
print(a[::])

# Handy slicing trick: Reversing a string with step -1
# Output: snas olleh
# print(a[::-1])