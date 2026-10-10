# 🐍 Learning Python

A structured repository documenting my journey learning Python programming from the fundamentals to advanced concepts, with clean, concise, and educational code examples.

---

## 📂 Repository Structure

### 📁 `01basics` — Core Foundations
*   **`01comms-and-var.py`**:
    *   **Comments**: Single-line (`#`), multi-line string convention (`"""..."""`), and docstring overview.
    *   **Variables**: Dynamic typing, heap-allocated object references, and variable assignment.
    *   **Naming Rules & PEP 8**: Valid identifier rules, syntax error examples for invalid names (leading digits, spaces, special characters), case-sensitivity, and reserved keywords.
*   **`02datatypes.py`**:
    *   **Primitive & Built-in Types**: `int`, `float`, `complex` (using `j`), `str`, `bool`, and `None`.
    *   **Type Inspection**: Using `type()` to determine object class.
    *   **Type Conversion & Casting**: Explicit conversion with `str()`, `int()`, and `float()`, truncation behavior, and immutability of primitive types.
*   **`03strings.py`**:
    *   **Unicode Representation**: Character encoding and decoding using `ord()` and `chr()`.
    *   **String Indexing**: Zero-based positive indexing (left-to-right) and negative indexing (right-to-left from end).
    *   **String Slicing**: Slice syntax `[start : stop : step]`, default slice parameters, and string reversal using negative step (`[::-1]`).
*   **`04in-out.py`**:
    *   **Output with `print()`**: Multiple arguments with automatic space separation (`sep=" "`), newline ending behavior.
    *   **String Formatting**: Comma-separated output vs. modern Python 3.6+ f-strings (`f"{var}"`).
    *   **User Input with `input()`**: Reading terminal input, understanding that `input()` always returns a string (`str`), and typecasting input to numeric types (`int(input(...))`).
*   **`05operators.py`**:
    *   Arithmetic operators, comparison, logical, assignment, identity (`is`), and membership (`in`) operators *(in progress)*.

---

## 🛠️ How to Run Locally

1. **Prerequisites:** Make sure you have Python 3 installed. Check with:
   ```bash
   python --version
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/spant671-ux/Learning-Python.git
   ```

3. **Run any script directly in the terminal:**
   ```bash
   python 01basics/01comms-and-var.py
   python 01basics/02datatypes.py
   python 01basics/03strings.py
   python 01basics/04in-out.py
   ```

---

## 🚀 Learning Progress

*   [x] **Python Basics**: Comments, Variables & Naming Rules
*   [x] **Data Types & Type Casting**: Numbers, Booleans, Strings, `type()`
*   [x] **String Manipulation**: Indexing, Slicing, Unicode (`ord`/`chr`)
*   [x] **Input / Output**: `print()`, f-strings, `input()`
*   [ ] **Operators**: Arithmetic, Relational, Logical, Assignment, Bitwise
*   [ ] **Control Flow**: Conditionals (`if-elif-else`), Loops (`for`, `while`)
*   [ ] **Data Structures**: Lists, Tuples, Dictionaries, Sets
*   [ ] **Functions & Scopes**: Parameters, `*args`, `**kwargs`, Lambda functions
*   [ ] **Object-Oriented Programming (OOP)**: Classes, Objects, Inheritance, Magic Methods
