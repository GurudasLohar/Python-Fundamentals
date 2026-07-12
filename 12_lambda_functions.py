# Lambda Functions

# ============================================================
# Lambda Function Syntax
# ============================================================
#
# lambda parameters: expression
#
# Components:
# 1. lambda            -> Keyword used to define a lambda function.
# 2. parameters        -> Inputs to the function (optional).
# 3. expression        -> Single expression that is evaluated and returned.
# 
# Note: Unlike a normal function, a lambda function does not use the return keyword. The result of the expression is returned automatically.
# ============================================================

# Anonymous functions => An anonymous function is a function without a name.
add = lambda x, y: x + y
print(add(5, 3))

# Both functions behave the same way.
# def add(x, y):
#    return x + y

# With map, filter
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(squares)
print(evens)


#| Feature               | `def` Function                  | `lambda` Function                         |
# | --------------------- | ------------------------------- | ----------------------------------------- |
# | Keyword               | `def`                           | `lambda`                                  |
# | Function Name         | Required                        | Anonymous (can be assigned to a variable) |
# | Number of Expressions | Multiple                        | Only one expression                       |
# | `return` Keyword      | Required (if returning a value) | Automatic                                 |
# | Best For              | Complex functions               | Small, simple functions                   |
