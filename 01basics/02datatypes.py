# --- Datatypes ---
# Python has several built-in data types including int, str, float, complex, and boolean.

# Variable declarations with representative datatypes:

# Integer datatype
a = 12

# String datatype
b = "sans"

# Boolean datatype
c = True

# Float datatype
d = 13.5

# Complex datatype
e = 19j

# --- Type Checking and Conversion ---
# Using the 'type()' function to check data types:

# Output: <class 'int'>
print(type(a))

# Using 'str()' function to convert integer 'a' to a string
# Note: This returns a new string object and doesn't change the original variable 'a' in place.
print(str(a))

# Output: <class 'int'> (Since 'a' is still an integer)
print(type(a))