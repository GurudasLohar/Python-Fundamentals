# Tuples

# Tuples are immutable, ordered collections. They are faster than lists
# and commonly used for fixed data.

# Creating tuples
coords = (10, 20, 30)
person = ("Developer", 25, "Engineer")
single = (5,)                    # Note the comma! Without it, it's just int
empty = ()

print("=== Original Tuples ===")
print("coords:", coords)
print("person:", person)
print("single:", single, type(single))
print("empty :", empty, type(empty))

# 1. Accessing Elements
print("\n=== Accessing ===")
print("First element :", coords[0])
print("Last element  :", coords[-1])
print("Slice [1:3]   :", coords[1:3])

# 2. Tuple Unpacking (Very Powerful)
print("\n=== Tuple Unpacking ===")
x, y, z = coords
print(f"Unpacked: x={x}, y={y}, z={z}")

# Extended unpacking
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# 3. Tuple Methods (Limited because immutable)
print("\n=== Tuple Methods ===")
print("Count of 10 in coords:", coords.count(10))
print("Index of 20         :", coords.index(20))

# 4. Immutability Demonstration
print("\n=== Immutability ===")
print("Tuples cannot be modified directly (no append, remove, etc.)")
# coords[0] = 99   # This would raise TypeError

# 5. Why use Tuples?
print("\n=== Advantages of Tuples ===")
print("- Faster than lists")
print("- Can be used as dictionary keys (hashable)")
print("- Safe from accidental modification")
print("- Good for returning multiple values from functions")

# Example: Returning multiple values
def get_user_info():
    return ("Bob", 30, "bob@example.com")

name, age, email = get_user_info()
print(f"User: {name}, Age: {age}, Email: {email}")

# 6. Tuple vs List Performance (Conceptual)
print("\n=== Tuple vs List ===")
print("Tuples are immutable → more memory efficient & faster for read-only data")

# Bonus: Nested Tuples
location = ((40.7128, -74.0060), "New York")
print("\nNested tuple (lat, lon):", location[0])

print("\n=== Tuples are excellent for fixed, related data! ===")