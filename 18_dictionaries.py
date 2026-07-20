# Dictionaries

# Dictionaries are mutable, unordered (insertion ordered since Python 3.7+)
# key-value pairs. Keys must be immutable (hashable).

# Creating dictionaries
person = {
    "name": "Develoeper",
    "age": 25,
    "skills": ["Python", "SQL", "AWS"],
    "active": True
}

print("=== Original Dictionary ===")
print(person)
print(f"Number of items: {len(person)}")

# 1. Accessing Values
print("\n=== Accessing Values ===")
print("Name:", person["name"])
print("Age :", person.get("age"))           # Safer, returns None if key missing
print("City:", person.get("city", "Not Found"))  # Default value

# 2. Adding & Updating
print("\n=== Adding & Updating ===")
person["city"] = "New York"
person["age"] = 26                          # Update existing
print("After updates:", person)

# 3. Removing Items
print("\n=== Removing Items ===")
removed = person.pop("active")              # Remove and return value
print(f"Removed 'active': {removed}")
print("After pop():", person)

del person["city"]                          # Delete by key
print("After del city:", person)

# 4. Dictionary Views
print("\n=== Dictionary Views ===")
print("Keys   :", list(person.keys()))
print("Values :", list(person.values()))
print("Items  :", list(person.items()))

# 5. Looping
print("\n=== Looping ===")
for key in person:
    print(f"{key}: {person[key]}")

print("\nBetter way:")
for key, value in person.items():
    print(f"{key:10} : {value}")

# 6. Dictionary Methods
print("\n=== Useful Methods ===")
print("Has key 'name'?", "name" in person)
print("Has key 'salary'?", person.get("salary") is not None)

# Merge dictionaries (Python 3.9+)
extra = {"salary": 75000, "department": "Engineering"}
person.update(extra)
print("After update():", person)

# 7. Dictionary Comprehension
print("\n=== Dictionary Comprehension ===")
squares = {x: x**2 for x in range(6)}
print("Squares dict:", squares)

# Filter example
filtered = {k: v for k, v in person.items() if isinstance(v, (int, str))}
print("Filtered dict:", filtered)

# 8. Nested Dictionaries
print("\n=== Nested Dictionaries ===")
company = {
    "name": "TechCorp",
    "employees": {
        "emp1": {"name": "Ram", "role": "Developer"},
        "emp2": {"name": "Shyam", "role": "Manager"}
    }
}
print("Employee 1 role:", company["employees"]["emp1"]["role"])

# 9. When to Use Dictionaries?
print("\n=== When to Use Dictionaries? ===")
print("- Fast lookup by key (O(1) average)")
print("- Representing structured data (JSON-like)")
print("- Counting frequencies")
print("- Configuration settings")

# Practical Example: Word frequency
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print("Word frequency:", freq)

print("\n=== Dictionaries are one of Python's most powerful data structures! ===")