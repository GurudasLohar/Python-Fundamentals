# JSON Handling in Python

# JSON (JavaScript Object Notation) is a lightweight data interchange format.
# Python's json module makes it easy to work with JSON data.

import json
import os

print("=== JSON Handling in Python - Enhanced Guide ===\n")

# 1. Basic JSON Operations
print("=== 1. Python dict → JSON ===")

data = {
    "name": "Developer",
    "age": 28,
    "is_student": False,
    "skills": ["Python", "SQL", "Machine Learning"],
    "address": {
        "city": "Mumbai",
        "country": "India"
    },
    "scores": [95, 87, 92]
}

# Convert dict to JSON string
json_str = json.dumps(data, indent=2)
print("JSON String:\n", json_str)

# 2. JSON String → Python dict
print("\n=== 2. JSON String → Python Object ===")
parsed_data = json.loads(json_str)
print("Name :", parsed_data["name"])
print("Skills:", parsed_data["skills"])

# 3. Working with JSON Files
print("\n=== 3. Reading & Writing JSON Files ===")

# Write to file
with open("user_data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Data saved to 'user_data.json'")

# Read from file
with open("user_data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("Loaded from file - Name:", loaded_data["name"])

# 4. Advanced Options
print("\n=== 4. Advanced JSON Options ===")

# Custom encoding for non-serializable objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def person_encoder(obj):
    if isinstance(obj, Person):
        return {"__type__": "Person", "name": obj.name, "age": obj.age}
    raise TypeError("Object is not JSON serializable")

p = Person("Tester", 35)
print(json.dumps(p, default=person_encoder, indent=2))

# 5. Error Handling
print("\n=== 5. Error Handling ===")

invalid_json = '{"name": "Developer", "age": 28'   # Missing closing brace

try:
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print("JSON Decode Error:", e)

# 6. Best Practices
print("\n=== 6. Best Practices ===")
print("""
1. Always specify encoding='utf-8' when working with files
2. Use indent for readability in development
3. Handle JSONDecodeError gracefully
4. Use json.dumps() with default= for custom objects
5. Consider orjson or ujson for high-performance needs
""")

print("\n=== JSON is the standard for data exchange in web and APIs! ===")
print("Files created: user_data.json")