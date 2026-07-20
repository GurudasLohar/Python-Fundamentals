# Python Coding Standards (PEP 8)

# PEP 8 is the official style guide for Python code.

print("=== PEP 8 - Python Coding Standards ===\n")

# 1. Imports
print("=== 1. Imports (at the top) ===")
import os
import sys
from datetime import datetime

# Standard library → Third-party → Local imports
# Use blank lines to separate groups

# 2. Naming Conventions
print("\n=== 2. Naming Conventions ===")
print("""
Variables & Functions: snake_case
Constants: UPPER_CASE
Classes: CamelCase
Private attributes: _single_leading_underscore
Protected: _single (convention)
""")

# Good examples
user_name = "Alice"
max_connections = 100
MAX_RETRIES = 3

class UserProfile:
    def __init__(self, username):
        self.username = username
        self._email = None   # Private by convention

# 3. Code Layout
print("\n=== 3. Code Layout Best Practices ===")
print("""
- 4 spaces indentation
- Line length ≤ 79 characters
- Two blank lines between top-level functions/classes
- One blank line between methods
- Spaces around operators: x = a + b
- No spaces inside parentheses: func(arg)
""")

# 4. Function Definition Example
def calculate_total(items: list, tax_rate: float = 0.08) -> float:
    """Calculate total price including tax."""
    subtotal = sum(items)
    return subtotal + (subtotal * tax_rate)

print("Total with tax:", round(calculate_total([100, 200, 50]), 2))

# 5. Comments & Docstrings
print("\n=== 5. Documentation ===")
print("""
Use docstrings for modules, classes, and functions.
Inline comments should be used sparingly.
""")

# 6. Other PEP 8 Rules
print("\n=== 6. Key PEP 8 Rules ===")
print("""
• Avoid wildcard imports: from module import *
• Use 'is' for None / singletons, '==' for values
• Prefer comprehensions for simple loops
• Use 'with' for resource management
• Avoid deep nesting (max 3-4 levels)
""")

# 7. Tools for Checking PEP 8
print("\n=== 7. Tools to Enforce Standards ===")
print("""
- pycodestyle (formerly pep8)
- black (auto formatter)
- flake8 (linting)
- pylint
- VS Code + Python extension (shows issues in real-time)
""")

print("\n=== Writing clean, consistent code makes you a better developer! ===")
print("Always aim for readability — code is read more than it is written.")