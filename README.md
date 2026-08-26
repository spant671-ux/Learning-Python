<div align="center">

# 🐍 Python Mastery & Learning Journey

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active%20learning-success.svg?style=for-the-badge&color=2ea44f)](https://github.com/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge)](https://github.com/)

<p align="center">
  <b>A curated, hands-on roadmap and codebase for mastering Python — from core fundamentals to advanced architectures.</b>
</p>

[📖 Overview](#-overview) •
[🗂️ Modules](#-repository-modules) •
[🚀 Quick Start](#-quick-start) •
[🗺️ Learning Path](#-learning-roadmap) •
[💡 Key Takeaways](#-key-takeaways)

---

</div>

## 📖 Overview

Welcome to the **Learning-Python** repository! This project serves as a comprehensive, well-structured companion for building a rock-solid foundation in Python. It contains modular code samples, practical exercises, and reusable scripts organized by concept.

---

## 🗂️ Repository Modules

```text
📦 Learning-Python
 ┣ 📂 01_basics               # Fundamentals & Execution Model
 ┃ ┣ 📜 hello.py              # Print methods & standard output
 ┃ ┗ 📜 variables.py          # Variables, data types, f-strings & conditionals
 ┣ 📂 02_data_types           # (Upcoming) Numbers, Strings, Lists, Dictionaries
 ┣ 📂 03_conditionals        # (Upcoming) Flow control & Pattern Matching
 ┣ 📂 04_loops               # (Upcoming) Iterations & Comprehensions
 ┣ 📂 05_functions           # (Upcoming) Closures, Scopes, *args & **kwargs
 ┣ 📂 06_oop                 # (Upcoming) Object-Oriented Architecture
 ┗ 📜 README.md              # Project Documentation & Guide
```

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have **Python 3.10+** installed:

```bash
python --version
```

### 2. Clone & Explore

```bash
# Clone the repository
git clone https://github.com/your-username/Learning-Python.git

# Navigate into the project
cd Learning-Python
```

### 3. Run Samples

```bash
# Run print basics
python 01_basics/hello.py

# Run variables, data types, f-strings & conditionals
python 01_basics/variables.py
```

---

## 🗺️ Learning Roadmap

| Module | Status | Core Concepts Covered | Folder |
| :--- | :---: | :--- | :---: |
| **01. Basics** | 🟢 `Completed` | Syntax, `print()`, Variables, Data Types (`str`, `int`, `float`, `bool`), `f-strings`, `if-else` | [`01_basics/`](./01_basics) |
| **02. Data Types & Collections** | 🟡 `In Progress` | Strings in-depth, Lists, Tuples, Sets, Dictionaries, Mutability | `02_data_types/` |
| **03. Conditionals & Logic** | ⚪ `Planned` | If-Elif-Else, Logical Operators (`and`, `or`, `not`), Match-Case | `03_conditionals/` |
| **04. Loops & Iteration** | ⚪ `Planned` | `for`, `while`, `break`, `continue`, List Comprehensions | `04_loops/` |
| **05. Functions & Scopes** | ⚪ `Planned` | `def`, Return values, Default args, `*args`, `**kwargs`, LEGB Scope | `05_functions/` |
| **06. Object-Oriented Programming** | ⚪ `Planned` | Classes, Objects, `__init__`, Inheritance, Encapsulation | `06_oop/` |
| **07. Functional & Decorators** | ⚪ `Planned` | Lambdas, `map`/`filter`, Decorators, Generators (`yield`) | `07_decorators/` |
| **08. Error & File Handling** | ⚪ `Planned` | `try-except-finally`, `with` statement, File I/O | `08_error_handling/` |
| **09. Practical Mini-Projects** | ⚪ `Planned` | CLI Tools, Automation Scripts, Mini-Apps | `09_projects/` |

---

## 💡 Key Takeaways & Quick Reference

<details open>
<summary><b>Quick Reference: Variables & Data Types (01_basics)</b></summary>
<br>

| Concept | Description | Example Syntax |
| :--- | :--- | :--- |
| **`print()`** | Outputs text or values to console | `print("Hello World")` |
| **Variable** | Named container in memory (dynamically typed) | `age = 25` |
| **`str` (String)** | Text enclosed in `'...'` or `"..."` | `name = "santosh"` |
| **`int` (Integer)** | Whole numbers (+, -, 0) with no decimal | `quantity = 3` |
| **`float` (Float)** | Numbers containing a decimal point | `price = 10.99` |
| **`bool` (Boolean)** | Binary truth values (`True` or `False`) | `is_student = False` |
| **`f-string`** | Formatted string for variable interpolation | `f"Hello {name}, age: {age}"` |
| **`if-else`** | Conditional branching (uses 4-space indent) | `if is_online: print("Online")` |

</details>

<details>
<summary><b>🔍 Behind the Scenes: Python Execution & <code>__pycache__</code></b></summary>
<br>

- Python compiles source code (`.py`) into bytecode (`.pyc`) stored inside `__pycache__` for imported modules to accelerate startup.
- Python's Virtual Machine (PVM) interprets and executes this bytecode.
- Top-level scripts execute directly, while imported modules leverage bytecode caching.

</details>

---

## 🛠️ Built With

- **Language:** [Python 3](https://www.python.org/)
- **Editor / IDE:** VS Code / Antigravity IDE
- **Version Control:** Git & GitHub

---

<div align="center">

<sub>Crafted with passion for clean code & continuous learning. ⭐ Star this repo if you find it helpful!</sub>

</div>
