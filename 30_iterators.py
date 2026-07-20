# Iterators and Iterables in Python

# Iterables: Objects that can return an iterator (lists, tuples, strings, etc.)
# Iterators: Objects that implement __iter__() and __next__()

print("=== Iterators and Iterables - Deep Dive ===\n")

# 1. Basic Usage
print("=== 1. Built-in Iterators ===")

numbers = [1, 2, 3, 4, 5]
it = iter(numbers)

print("Next item:", next(it))
print("Next item:", next(it))

# Using for loop (automatically uses iterator)
print("Using for loop:")
for num in numbers:
    print(num, end=' ')
print()

# 2. Custom Iterator Class
print("\n=== 2. Custom Iterator ===")

class Counter:
    """Iterator that counts from low to high"""
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Using the custom iterator
print("Counter from 1 to 5:")
for num in Counter(1, 5):
    print(num, end=' ')
print()

# 3. Generator vs Iterator
print("\n=== 3. Generators (Easy way to create Iterators) ===")

def my_generator(n):
    for i in range(n):
        yield i * i          # yield makes it a generator

print("Generator squares:")
for sq in my_generator(6):
    print(sq, end=' ')
print()

# Generator Expression
gen_exp = (x**2 for x in range(10))
print("Generator expression (first 5):", [next(gen_exp) for _ in range(5)])

# 4. Iterable vs Iterator
print("\n=== 4. Iterable vs Iterator ===")
lst = [10, 20, 30]
print("List is iterable:", hasattr(lst, '__iter__'))
print("List is iterator:", hasattr(lst, '__next__'))

it = iter(lst)
print("Iterator from list is iterator:", hasattr(it, '__next__'))

# 5. Practical Use Cases
print("\n=== 5. Practical Examples ===")

# Infinite Iterator
class InfiniteCounter:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        return self.num

# Limited usage
print("First 5 from infinite counter:")
counter = InfiniteCounter()
for i, val in enumerate(counter):
    print(val, end=' ')
    if i >= 4:
        break
print()

# 6. Best Practices & Tips
print("\n=== Best Practices ===")
print("""
1. Use generators for memory efficiency
2. Prefer built-in functions (range, enumerate, zip)
3. Implement __iter__ and __next__ for custom iterators
4. Always raise StopIteration when exhausted
5. Use itertools for advanced iterator tools
""")

print("\n=== Iterators are fundamental to Python's 'for' loops and memory-efficient programming! ===")