# Sets

# Sets are unordered, mutable collections of **unique** elements.
# Very fast for membership testing and mathematical set operations.

# Creating sets
unique = {1, 2, 2, 3, 4, 4, 5}          # Duplicates are automatically removed
print("Original set:", unique)

# From list
fruits = set(["apple", "banana", "apple", "cherry"])
print("From list :", fruits)

empty_set = set()                        # Not {} (that's a dict)
print("Empty set type:", type(empty_set))

# 1. Adding & Removing Elements
print("\n=== Adding & Removing ===")
fruits.add("date")
print("After add('date'):", fruits)

fruits.update(["elderberry", "fig"])
print("After update():", fruits)

fruits.remove("banana")                  # Raises KeyError if not found
print("After remove('banana'):", fruits)

fruits.discard("mango")                  # No error if not found
print("After discard('mango'):", fruits)

popped = fruits.pop()                    # Removes and returns arbitrary element
print(f"Popped element: {popped}")

# 2. Set Operations (Mathematical)
print("\n=== Set Operations ===")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union (a | b)        :", set_a | set_b)
print("Intersection (a & b)  :", set_a & set_b)
print("Difference (a - b)    :", set_a - set_b)
print("Symmetric Difference  :", set_a ^ set_b)

# Using methods
print("Union method         :", set_a.union(set_b))
print("Intersection method  :", set_a.intersection(set_b))

# 3. Membership Testing (Very Fast!)
print("\n=== Membership Testing ===")
print("3 in set_a :", 3 in set_a)
print("10 in set_a:", 10 in set_a)

# 4. Other Useful Methods
print("\n=== Other Methods ===")
print("Length of set_a    :", len(set_a))
print("Is subset          :", {1,2}.issubset(set_a))
print("Is superset        :", set_a.issuperset({3,4}))

# 5. Set Comprehension
print("\n=== Set Comprehension ===")
squares = {x**2 for x in range(10)}
print("Squares set:", squares)

# 6. When to Use Sets?
print("\n=== When to Use Sets? ===")
print("- Remove duplicates from a list")
print("- Fast membership testing (O(1) average)")
print("- Mathematical set operations")
print("- Finding unique items")

# Practical Example: Remove duplicates from list
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = list(set(data))
print("\nRemoved duplicates:", unique_data)

print("\n=== Sets are perfect for uniqueness and fast lookups! ===")