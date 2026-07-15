# Modules

# Modules are .py files containing Python code (functions, classes, variables)
# They help organize code and promote reusability.

print("=== Built-in Modules ===")

# 1. Math Module
import math

print("Square root of 16 :", math.sqrt(16))
print("Pi value         :", math.pi)
print("Floor of 4.7     :", math.floor(4.7))
print("Ceil of 4.3      :", math.ceil(4.3))
print("Factorial of 5   :", math.factorial(5))

# 2. Random Module
import random

print("\n=== Random Module ===")
print("Random integer (1-100) :", random.randint(1, 100))
print("Random choice from list:", random.choice(["apple", "banana", "cherry"]))
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list         :", numbers)

# 3. Datetime Module
from datetime import datetime, timedelta

print("\n=== Datetime Module ===")
now = datetime.now()
print("Current date & time :", now)
print("Formatted date      :", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Date after 7 days   :", now + timedelta(days=7))

# 4. OS Module (Operating System)
import os

print("\n=== OS Module ===")
print("Current working directory:", os.getcwd())
print("List of files in dir     :", os.listdir()[:5])  # First 5 items

# 5. Creating and Importing Custom Modules
print("\n=== Custom Modules ===")
"""
To create a custom module:
1. Create a file named mymodule.py with:
   def greet(name):
       return f"Hello, {name}!"

2. Then import it:
   import mymodule
   print(mymodule.greet("Developer"))
"""

# Example of importing specific functions
from math import pi, sqrt as square_root

print(f"Imported pi: {pi}")
print(f"Square root using alias: {square_root(25)}")

# 6. Module Search Path
import sys
print("\n=== Module Search Path ===")
print("Python looks for modules in these paths:")
for path in sys.path[:5]:  # Show first few
    print(path)

# 7. Best Practices with Modules
print("\n=== Best Practices ===")
print("""
- Import at the top of the file
- Use meaningful import aliases (e.g., import numpy as np)
- Prefer 'from module import specific_function' sparingly
- Organize related code into modules and packages
- Use if __name__ == "__main__": for executable scripts
""")

# 8. if __name__ == "__main__" Demo
if __name__ == "__main__":
    print("\n=== This script is being run directly! ===")
    print("This block won't run if the file is imported as a module.")

print("\n=== Modules are the foundation of Python's reusability and ecosystem! ===")