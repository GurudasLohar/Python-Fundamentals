# Exception Handling in Python

# Exception handling allows your program to gracefully handle runtime errors

print("=== Basic Exception Handling ===")

# 1. Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. Handling multiple exceptions
try:
    num = int(input("Enter a number: "))  # Try running with non-number input
    result = 100 / num
except ValueError:
    print("Please enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:                    # Catch-all (use sparingly)
    print(f"Unexpected error: {e}")

# 3. else and finally
try:
    file = open("sample.txt", "r", encoding="utf-8")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
    print("First 100 chars:", content[:100] if content else "Empty")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("Finally block: File closed (if opened)")

# 4. Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print("Validation error:", e)

# 5. Custom Exceptions
class InsufficientFundsError(Exception):
    """Custom exception for banking scenarios"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds! Balance: {balance}, Tried to withdraw: {amount}")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except InsufficientFundsError as e:
    print(e)

# 6. Best Practices
print("\n=== Exception Handling Best Practices ===")
print("""
1. Be specific with exception types (avoid bare 'except:')
2. Use finally for cleanup (files, connections)
3. Don't suppress exceptions silently
4. Use custom exceptions for domain-specific errors
5. Keep try blocks as small as possible
6. Log exceptions in production code
""")

# Practical Example: Robust File Processing
print("\n=== Practical Example ===")
def safe_read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
        return None
    except Exception as e:
        print(f"Unexpected error reading '{filename}': {e}")
        return None

content = safe_read_file("nonexistent.txt")
print("Safe read result:", content is not None)

print("\n=== Exception Handling makes your code robust and production-ready! ===")