# Python Best Practices

# Following best practices leads to clean, maintainable, and professional code.

print("=== Python Best Practices - Comprehensive Guide ===\n")

# 1. Code Readability & Style (PEP 8)
print("=== 1. Follow PEP 8 Style Guide ===")
print("""
- Use 4 spaces for indentation (never tabs)
- Limit lines to 79 characters
- Use snake_case for variables and functions
- Use CamelCase for class names
- Add spaces around operators: a = b + c
- Import at the top of the file
""")

# Example of clean code
def calculate_circle_area(radius: float) -> float:
    """Calculate area of a circle given radius."""
    import math
    return math.pi * radius ** 2

print("Clean function example area (r=5):", round(calculate_circle_area(5), 2))

# 2. Meaningful Naming
print("\n=== 2. Meaningful Naming ===")
print("""
Bad:  x = 42
Good: user_age = 42

Bad:  def calc(a, b)
Good: def calculate_total_price(items, tax_rate)
""")

# 3. Functions & Modularity
print("\n=== 3. Write Small, Focused Functions ===")

def is_valid_email(email: str) -> bool:
    """Check if email format is valid."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

print("Is valid email?", is_valid_email("test@example.com"))

# 4. Error Handling
print("\n=== 4. Proper Error Handling ===")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None

print("Safe divide result:", safe_divide(10, 2))

# 5. Documentation
print("\n=== 5. Documentation Best Practices ===")
print("""
- Write docstrings for modules, classes, and functions
- Use type hints (Python 3.5+)
- Keep comments updated and meaningful
- Maintain a README.md for projects
""")

# 6. Other Important Practices
print("\n=== 6. Additional Best Practices ===")
print("""
• Use virtual environments for every project
• Write tests (unittest or pytest)
• Version control with Git
• Follow DRY (Don't Repeat Yourself)
• Use list/dict comprehensions wisely
• Prefer built-in functions and standard library
• Keep dependencies minimal
• Write defensive code
""")

# 7. Final Project Tip
print("\n=== Final Advice for This Repository ===")
print("""
Congratulations on completing Python Fundamentals!

Next Steps:
1. Build real projects
2. Contribute to open source
3. Learn frameworks (Django/Flask/FastAPI)
4. Study data structures & algorithms
5. Practice on LeetCode / HackerRank
""")

print("\n=== Write code that is not only correct but also clean and maintainable! ===")