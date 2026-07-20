# Decorators in Python

# Decorators are a powerful way to modify or extend the behavior of functions or classes.

import time
import functools

print("=== Decorators in Python - Deep Dive ===\n")

# 1. Basic Decorator
print("=== 1. Basic Function Decorator ===")

def timer(func):
    """Decorator that measures execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function(seconds=1):
    time.sleep(seconds)
    return "Done!"

print(slow_function(0.5))

# 2. Decorator with Arguments
print("\n=== 2. Decorator with Arguments ===")

def repeat(times=2):
    def decorator(func):
        @functools.wraps(func)   # Preserves original function metadata
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")
    return "Greeting done"

greet("Developer")

# 3. Class Decorator
print("\n=== 3. Class Decorator ===")

def add_method(cls):
    """Add a new method to a class"""
    def new_method(self):
        return f"New method called on {self}"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.new_method())

# 4. Multiple Decorators (Stacking)
print("\n=== 4. Stacking Decorators ===")

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper() if isinstance(result, str) else result
    return wrapper

@timer
@uppercase
def get_message():
    return "hello from decorators!"

print(get_message())

# 5. Real-World Use Cases
print("\n=== 5. Common Use Cases ===")
print("""
- Logging function calls
- Timing execution
- Authentication / Authorization
- Caching results (@lru_cache)
- Validation of input
- Retry logic on failure
""")

# Built-in decorator example
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\nFibonacci(35) with caching:", fibonacci(35))

# 6. Best Practices
print("\n=== Best Practices ===")
print("""
1. Always use @functools.wraps to preserve metadata
2. Keep decorators simple and single-purpose
3. Use classes for complex stateful decorators
4. Document your decorators well
""")

print("\n=== Decorators are one of Python's most elegant features for code reuse! ===")