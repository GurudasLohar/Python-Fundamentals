# Context Managers in Python

# Context Managers allow you to allocate and release resources precisely
# using the 'with' statement. They are most commonly used for file handling,
# database connections, locks, etc.

print("=== Context Managers in Python - Deep Dive ===\n")

# 1. Using Built-in Context Managers
print("=== 1. Built-in Examples ===")

# File handling (most common)
with open("context_example.txt", "w", encoding="utf-8") as f:
    f.write("Hello from context manager!\n")
    f.write("This file will be automatically closed.")

print("File written and automatically closed.\n")

# 2. Creating Context Manager using Class
print("=== 2. Class-based Context Manager ===")

class MyContextManager:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Entering context: {self.name}")
        return self   # Value returned to 'as' variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Exiting context: {self.name}")
        if exc_type:
            print(f"Exception occurred: {exc_type.__name__}")
        return False   # Do not suppress exception

# Using the class-based context manager
with MyContextManager("Database Connection") as cm:
    print("Inside context manager")
    print(f"Name: {cm.name}")

# 3. Context Manager using @contextmanager Decorator
print("\n=== 3. @contextmanager Decorator (from contextlib) ===")

from contextlib import contextmanager

@contextmanager
def timer_context(name):
    start = time.time()
    print(f"Starting {name}...")
    try:
        yield "Timer Active"      # Value passed to 'as' variable
    finally:
        end = time.time()
        print(f"{name} completed in {end - start:.4f} seconds")

import time

with timer_context("Long Operation") as status:
    print(f"Status: {status}")
    time.sleep(0.5)
    print("Processing...")

# 4. Multiple Context Managers
print("\n=== 4. Multiple Context Managers ===")

with open("file1.txt", "w") as f1, open("file2.txt", "w") as f2:
    f1.write("Data for file 1")
    f2.write("Data for file 2")
print("Both files closed automatically.")

# 5. Real-World Use Cases
print("\n=== 5. Common Use Cases ===")
print("""
- File I/O
- Database connections
- Network sockets
- Thread locks / Semaphores
- Temporary directory management
- Database transactions
""")

# 6. Best Practices
print("\n=== Best Practices ===")
print("""
1. Use 'with' statement whenever possible
2. Always clean up resources in __exit__ / finally
3. Use @contextmanager for simple cases
4. Make context managers reusable
5. Handle exceptions appropriately in __exit__
""")

print("\n=== Context Managers make resource management safe and elegant in Python! ===")