# Datatypes in Python

# --- Python Primitive / Built-in Data Types ---
# int     => Whole numbers (e.g., 12, -5, 1000)
# float   => Decimal / floating-point numbers (e.g., 13.5, 3.14)
# complex => Numbers with real and imaginary parts (uses 'j', e.g., 19j)
# str     => Textual data enclosed in single or double quotes (e.g., "sans")
# bool    => Boolean values (True or False)
# None    => Represents absence of value (equivalent to null in JS/Java)

# Variable declarations with representative datatypes:

# Integer datatype
a = 12

# String datatype
b = "sans"

# Boolean datatype
c = True

# Float datatype
d = 13.5

# Complex datatype (real part: 0.0, imag part: 19.0)
e = 19j

# --- Type checking and conversion ---

# type() function returns the data type of a variable
# Output: <class 'int'>
print(type(a))

# str() function explicitly converts/casts the integer into a string ("12")
# Output: 12
print(str(a))

# 'a' is still an int — conversion returns a new string, it does NOT mutate the original variable
# Output: <class 'int'>
print(type(a))

# Example of converting string to int, and float to int:
num_str = "100"
num_int = int(num_str)  # Converts string "100" to integer 100

# Output: 100
print(num_int)

# Output: <class 'int'>
print(type(num_int))

# Converting float to int (truncates decimal part, does not round):
# Output: 13
print(int(d))