# Python Lists

# Lists are mutable, ordered, and allow duplicate elements

fruits = ["apple", "banana", "cherry", "apple"]

print("=== Original List ===")
print(fruits)
print(f"Length: {len(fruits)}")

# 1. Adding Elements
print("\n=== Adding Elements ===")
fruits.append("date")                    # Add to end
print("After append('date'):", fruits)

fruits.insert(1, "blueberry")            # Insert at index
print("After insert(1, 'blueberry'):", fruits)

fruits.extend(["elderberry", "fig"])     # Extend with another iterable
print("After extend():", fruits)

# 2. Removing Elements
print("\n=== Removing Elements ===")
fruits.remove("apple")                   # Remove first occurrence
print("After remove('apple'):", fruits)

popped = fruits.pop()                    # Remove and return last item
print(f"Popped item: {popped}")
print("After pop():", fruits)

fruits.pop(1)                            # Remove by index
print("After pop(1):", fruits)

# 3. Accessing & Slicing
print("\n=== Accessing & Slicing ===")
print("First element:", fruits[0])
print("Last element :", fruits[-1])
print("Slice [1:4]  :", fruits[1:4])
print("Reverse      :", fruits[::-1])

# 4. Searching & Counting
print("\n=== Searching ===")
print("Index of 'cherry':", fruits.index("cherry"))
print("Count of 'banana':", fruits.count("banana"))

# 5. Sorting & Reversing
print("\n=== Sorting & Reversing ===")
numbers = [5, 2, 9, 1, 5]
print("Original numbers:", numbers)

numbers.sort()                           # In-place sort
print("After sort():   ", numbers)

numbers.sort(reverse=True)
print("Descending sort:", numbers)

sorted_copy = sorted(numbers)            # Returns new sorted list
print("sorted() copy  :", sorted_copy)

fruits.reverse()                         # In-place reverse
print("Reversed fruits:", fruits)

# 6. Useful List Operations
print("\n=== Other Operations ===")
print("Sum of numbers :", sum(numbers))
print("Max number    :", max(numbers))
print("Min number    :", min(numbers))

# Membership test
print("'banana' in fruits:", "banana" in fruits)

# 7. List Comprehension (Powerful Feature)
print("\n=== List Comprehensions ===")
squares = [x**2 for x in range(10)]
print("Squares:", squares)

even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Bonus: Nested Lists (2D)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix[1][2]  :", matrix[1][2])

print("\n=== Lists are one of Python's most used data structures! ===")