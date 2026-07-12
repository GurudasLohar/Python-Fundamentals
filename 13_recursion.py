# Recursion
# Recursion => where a function calls itself until it reaches a stopping condition.


# def function_name(parameters):
#    # Base case
#    if stopping_condition:
#        return value
#
#    # Recursive case
#    return function_name(smaller_problem)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

# Fibonacci
# Fibonacci sequence => series of numbers where each number is the sum of the previous two numbers
# Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(f"Fib(6): {fib(6)}")