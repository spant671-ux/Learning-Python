# File Handling in Python
# File handling enables programs to read from and write to external files on disk,
# allowing data to persist even after the Python program finishes execution.
#
# Core File Access Modes:
# 'r'  : Read (default) - Opens file for reading; raises FileNotFoundError if absent.
# 'w'  : Write          - Opens file for writing; creates file if missing, OVERWRITES if exists.
# 'a'  : Append         - Opens file for writing; creates file if missing, APPENDS to end.
# 'r+' : Read + Write   - File pointer at beginning; does not truncate.
# 'w+' : Write + Read   - Truncates existing file or creates new file.
# 'a+' : Append + Read  - Appends to end; creates file if missing.
# 'b'  : Binary Mode    - e.g., 'rb', 'wb' for images, audio, and non-text files.


# --- 1. Opening and Reading a File ---
# Default mode is 'r' (read mode).
# Use a raw string r'...' or forward slashes to prevent escape character issues in Windows paths.

p = open(r'main.py', 'r')
# .read() loads the entire file content into a single string:
content = p.read()
print("--- Content of main.py ---")
print(content[:100] + "...\n")  # Printing first 100 characters preview
p.close()  # Always close file streams to free OS resources!


# --- 2. Writing to a File ('w' mode) ---
# WARNING: 'w' mode overwrites (truncates) any existing content in the file!
# If the file does not exist, Python creates it automatically.

w = open("file.txt", "w")
w.write("Hello, this is a file created by 'w' mode and written via .write().\n")
w.close()
print("Written initial text to file.txt successfully.")


# --- 3. Appending to a File ('a' mode) ---
# 'a' mode preserves existing content and adds new text to the end of the file.

r = open("file.txt", "a")
r.write("And now I am appending some additional content inside the file.\n")
r.close()
print("Appended content to file.txt successfully.")


# --- 4. Different Ways to Read Files ---
# Reading line-by-line vs reading all lines at once:

f = open("file.txt", "r")

# A. .read(): Reads entire file into one string
# full_text = f.read()

# B. .readline(): Reads one line at a time (moves file pointer forward)
first_line = f.readline()
print("\nFirst line using .readline():", first_line.strip())

# C. Iterating directly over the file object (Memory-efficient for huge files):
print("\nRemaining lines via direct iteration:")
for line in f:
    print(">", line.strip())

f.close()


# --- 5. The Pythonic Best Practice: The 'with' Statement ---
# Using a Context Manager ('with open(...) as file:') guarantees that
# the file is AUTOMATICALLY closed, even if an error or exception occurs inside the block.
# No manual .close() required!

print("\n--- Reading using 'with' Context Manager ---")
with open("file.txt", "r") as file:
    data = file.read()
    print(data)

# Checking if the file is closed:
print("Is file closed outside 'with' block?", file.closed)  # Output: True


# --- 6. Writing Multiple Lines with .writelines() ---
lines_to_add = [
    "Line 1: Learning Python with Sheryians\n",
    "Line 2: File Handling is easy\n",
    "Line 3: Always prefer 'with' statement\n"
]

with open("sample.txt", "w") as f:
    f.writelines(lines_to_add)

print("\nsample.txt created with multiple lines via .writelines().")
