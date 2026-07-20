# Generators in Python

# Generators are a simple and powerful way to create iterators.
# They allow you to declare a function that behaves like an iterator.

print("=== Generators in Python - Deep Dive ===\n")

# 1. Basic Generator Function
print("=== 1. Basic Generator ===")

def simple_generator():
    print("First yield")
    yield 1
    print("Second yield")
    yield 2
    print("Third yield")
    yield 3

gen = simple_generator()
print("Generator object:", gen)

print(next(gen))
print(next(gen))
print(next(gen))

# 2. Generator with loop
print("\n=== 2. Generator with Loop ===")

def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Blast off!"

print("Countdown:")
for value in countdown(5):
    print(value)

# 3. Generator Expression (Memory Efficient)
print("\n=== 3. Generator Expressions ===")

# List comprehension (stores everything in memory)
squares_list = [x**2 for x in range(10)]
print("List of squares (memory):", squares_list)

# Generator expression (lazy evaluation)
squares_gen = (x**2 for x in range(10))
print("Generator of squares:", squares_gen)

print("First 5 squares from generator:", [next(squares_gen) for _ in range(5)])

# 4. Practical Use Cases
print("\n=== 4. Real-World Examples ===")

# Reading large files line by line
def read_large_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.strip()

# Fibonacci generator (infinite, memory efficient)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("First 10 Fibonacci numbers:")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=' ')
print()

# 5. Advanced: Generator with send(), throw(), close()
print("\n=== 5. Advanced Generator Features ===")

def echo():
    print("Generator started")
    try:
        while True:
            value = yield
            print(f"Received: {value}")
    except GeneratorExit:
        print("Generator closed")

g = echo()
next(g)           # Prime the generator
g.send("Hello")
g.send("Python")
g.close()

# 6. Benefits of Generators
print("\n=== Why Use Generators? ===")
print("""
1. Memory efficiency (lazy evaluation)
2. Better performance for large/infinite sequences
3. Cleaner code than manual iterator classes
4. Can be paused and resumed
""")

print("\n=== Generators are one of Python's most elegant and powerful features! ===")