<div align="center">

# 🐍 Python Mastery & Learning Journey

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-active%20learning-success.svg?style=for-the-badge&color=2ea44f)](https://github.com/)
[![License](https://img.shields.io/badge/license-MIT-informational.svg?style=for-the-badge)](LICENSE)
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
 ┃ ┣ 📜 hello.py              # Print methods & first function definitions
 ┃ ┗ 📜 import.py             # Module system, __pycache__, and import mechanics
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
# Test execution of basics
python 01_basics/hello.py

# Test module imports
python 01_basics/import.py
```

---

## 🗺️ Learning Roadmap

| Module | Status | Core Concepts Covered | Folder |
| :--- | :---: | :--- | :---: |
| **01. Basics** | 🟢 `Completed` | Syntax, Print, Functions, Mutable/Immutable overview, Imports | [`01_basics/`](./01_basics) |
| **02. Data Types & Memory** | 🟡 `In Progress` | Numbers, Strings, Lists, Tuples, Dicts, Memory References | `02_data_types/` |
| **03. Conditionals & Logic** | ⚪ `Planned` | If-Elif-Else, Ternary Operators, Structural Pattern Matching | `03_conditionals/` |
| **04. Loops & Iteration** | ⚪ `Planned` | `for`, `while`, Loop else, List/Dict/Set Comprehensions | `04_loops/` |
| **05. Functions & Scopes** | ⚪ `Planned` | `*args`, `**kwargs`, Lambda, Closures, LEGB Rule | `05_functions/` |
| **06. Object-Oriented Programming** | ⚪ `Planned` | Classes, Objects, Inheritance, Dunder Methods, Encapsulation | `06_oop/` |
| **07. Functional & Decorators** | ⚪ `Planned` | First-class functions, Custom Decorators, Generators | `07_decorators/` |
| **08. Error & File Handling** | ⚪ `Planned` | `try-except-finally`, Context Managers (`with`), Custom Errors | `08_error_handling/` |
| **09. Practical Mini-Projects** | ⚪ `Planned` | CLI Tools, Automation Scripts, API Integrations | `09_projects/` |

---

## 💡 Key Takeaways & Notes

<details>
<summary><b>🔍 Behind the Scenes: Python Execution & <code>__pycache__</code></b></summary>
<br>

- Python compiles source code (`.py`) into bytecode (`.pyc`) stored inside the `__pycache__` folder for imported modules to speed up subsequent loads.
- Python's Virtual Machine (PVM) executes this bytecode line-by-line.
- Top-level scripts run directly, but imported modules benefit from bytecode caching.

</details>

<details>
<summary><b>📦 Python Import System</b></summary>
<br>

- Using `from module import function` brings specific attributes into the current namespace.
- Any top-level code inside the imported module executes once upon initial import.

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
