# Comprehensive Guide to Python Standard Library

# Python's "Batteries Included" philosophy means it comes with a rich set of
# high-quality modules ready to use without external installation.

print("=== Python Standard Library Overview ===\n")

# 1. Core Utility Modules
print("=== 1. Math & Random ===")
import math
import random

print(f"Pi: {math.pi:.4f}")
print(f"Square root of 64: {math.sqrt(64)}")
print(f"Random integer 1-100: {random.randint(1, 100)}")
print(f"Random choice: {random.choice(['Python', 'Java', 'JavaScript'])}")

# 2. Date and Time
print("\n=== 2. Datetime ===")
from datetime import datetime, timedelta, date

now = datetime.now()
print(f"Current datetime : {now}")
print(f"Formatted        : {now.strftime('%A, %B %d, %Y')}")
print(f"Date only        : {date.today()}")
print(f"Tomorrow         : {now + timedelta(days=1)}")

# 3. Operating System & Filesystem
print("\n=== 3. OS and Sys ===")
import os
import sys

print(f"Current directory: {os.getcwd()}")
print(f"Python version   : {sys.version.split()[0]}")
print(f"Platform         : {sys.platform}")
print(f"Python path      : {sys.executable}")

# 4. Collections - Advanced Data Structures
print("\n=== 4. Collections ===")
from collections import Counter, defaultdict, deque, namedtuple

# Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print("Word frequency:", Counter(words))

# defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
print("Defaultdict:", dict(dd))

# deque (fast append/pop from both ends)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", list(dq))

# 5. JSON & CSV
print("\n=== 5. JSON ===")
import json

data = {"name": "Developer", "age": 28, "skills": ["Python", "SQL"]}
json_str = json.dumps(data, indent=2)
print("JSON string:\n", json_str)

# 6. Itertools & Functools
print("\n=== 6. Itertools ===")
import itertools

print("Combinations of [1,2,3] taken 2 at a time:")
for combo in itertools.combinations([1, 2, 3], 2):
    print(combo)

# 7. Logging
print("\n=== 7. Logging ===")
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("This is an info message")
logging.warning("This is a warning!")

# 8. Other Important Modules
print("\n=== Other Essential Standard Library Modules ===")
print("""
• re              → Regular Expressions
• argparse        → Command-line argument parsing
• subprocess      → Run external commands
• threading / multiprocessing → Concurrency
• urllib.request  → HTTP requests
• zlib / gzip     → Compression
• pickle          → Object serialization
• copy            → Deep/shallow copy
• enum            → Enumerations
• statistics      → Statistical functions
""")

# 9. Best Practices
print("\n=== Best Practices with Standard Library ===")
print("""
1. Explore the library before installing third-party packages
2. Import only what you need (from module import specific)
3. Read the official documentation for each module
4. Use context managers (with statement) whenever possible
5. Prefer standard library over reinventing the wheel
""")

print("\n=== The Python Standard Library is vast and powerful! ===")
print("You can accomplish most common tasks without external dependencies.")
print("Explore more at: https://docs.python.org/3/library/")