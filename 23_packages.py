# Packages

# A package is a way of organizing related Python modules into a directory hierarchy.
# It must contain a special file: __init__.py (can be empty or contain initialization code)

print("=== Understanding Python Packages ===")
print("""
Package Structure Example:
mypackage/
├── __init__.py          # Makes the directory a package
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
""")

# 1. Importing from Packages
print("\n=== Importing from Packages ===")
"""
Common import styles:

1. import mypackage.module1
2. from mypackage import module1
3. from mypackage.module1 import function_name
4. from mypackage.module1 import function_name as alias
"""

# Example using standard library packages
import os
import json
from datetime import datetime

print("Imported from packages:")
print("- os package")
print("- json package")
print("- datetime from datetime package")

# 2. __init__.py Role
print("\n=== Role of __init__.py ===")
print("""
- Marks directory as Python package
- Can contain package-level initialization code
- Can define __all__ list to control 'from package import *'
- Can expose public API by importing key functions/classes
""")

# 3. Creating a Simple Package (Demonstration)
print("\n=== Example Package Usage ===")
"""
To create your own package:
1. Create folder: myutils/
2. Add __init__.py inside it
3. Add helper.py with functions
4. Import: from myutils.helper import calculate
"""

# Practical demonstration with built-in packages
print("\n=== Working with Packages ===")

# OS package
print("Current directory:", os.getcwd())

# JSON package
data = {"name": "Developer", "age": 25}
json_str = json.dumps(data, indent=2)
print("JSON string from json package:\n", json_str)

# 4. Relative vs Absolute Imports
print("\n=== Import Types ===")
print("""
- Absolute: from mypackage.module1 import func
- Relative: from .module1 import func     (inside package)
""")

# 5. Installing and Using Third-party Packages
print("\n=== Third-party Packages ===")
print("""
Install via pip:
pip install requests numpy pandas

Usage:
import requests
response = requests.get('https://api.github.com')
""")

# 6. Namespace Packages (Advanced)
print("\n=== Namespace Packages (Python 3.3+) ===")
print("Packages without __init__.py - useful for large distributed projects.")

# 7. Best Practices for Packages
print("\n=== Best Practices for Packages ===")
print("""
1. Keep __init__.py clean (avoid heavy imports)
2. Use meaningful package and module names (lowercase)
3. Follow flat is better than nested when possible
4. Document your package with README and docstrings
5. Use setup.py or pyproject.toml for distributable packages
6. Expose only public API in __init__.py
""")

print("\n=== Packages are essential for building large, maintainable Python projects! ===")
print("They help avoid name collisions and improve code organization.")