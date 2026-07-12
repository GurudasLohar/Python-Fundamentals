# Functions

# ============================================================
# Function Syntax
# ============================================================
#
# def function_name(parameters):
#     """
#     Optional Docstring => Describes what the function does.
#     """
#     # Function body
#     statement1
#     statement2
#     ...
#     return value
#
# Components:
# 1. def               -> Keyword used to define a function.
# 2. function_name     -> Name of the function.
# 3. parameters        -> Inputs to the function (optional).
# 4. Docstring         -> Optional documentation for the function.
# 5. Function body     -> Statements that perform the task.
# 6. return            -> Returns a value to the caller (optional).
# ============================================================


def greet(name="World"):
    """Greet function with default parameter"""
    return f"Hello, {name}!"

print(greet())
print(greet("Shyam"))


# Variable length arguments
# *args stores all positional values as a tuple: (10, 20, 30) (Accepts any number of positional arguments.)

def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))



# Keyword arguments
# **kwargs stores all keyword arguments as a dictionary: {'name': 'Ram', 'age': 30} (Accepts any number of keyword arguments.)

def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(name="Ram", age=30)