# File Handling

# Writing
# with open("sample.txt", "w") as f:
#     f.write("Hello Python File Handling!\n")
#     f.write("Line 2")

# # Reading
# with open("sample.txt", "r") as f:
#     content = f.read()
# print(content)

# Best practice: Always use 'with' statement (auto-closes file)

print("=== File Writing ===")
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello Python File Handling!\n")
    f.write("This is line 2.\n")
    f.writelines(["Line 3\n", "Line 4\n"])

print("File 'sample.txt' written successfully.\n")

# Reading
print("=== Reading Files ===")
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Full content:\n", content)

# Read line by line
print("\nReading line by line:")
with open("sample.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {line.strip()}")

# 1. Different File Modes
print("\n=== File Modes ===")
"""
'r'  - Read (default)
'w'  - Write (overwrites)
'a'  - Append
'r+' - Read & Write
'x'  - Create new file (fails if exists)
"""

# Append mode
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("This line was appended.\n")

print("Appended new line.\n")

# 2. Working with JSON
print("=== JSON Handling ===")
import json

data = {
    "name": "Developer",
    "age": 25,
    "skills": ["Python", "SQL"],
    "active": True
}

# Write JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("JSON file written.")

# Read JSON
with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
    print("Loaded JSON:", loaded)

# 3. Working with CSV
print("\n=== CSV Handling ===")
import csv

with open("data.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Tester", 25, "New Delhi"])
    writer.writerow(["Developer", 30, "Mumbai"])

print("CSV file written.")

# Read CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 4. Error Handling & Best Practices
print("\n=== Error Handling Example ===")
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found! Handled gracefully.")
except Exception as e:
    print(f"Error: {e}")

print("\n=== Key Takeaways ===")
print("- Always use 'with' statement")
print("- Specify encoding='utf-8'")
print("- Use appropriate modes")
print("- Handle exceptions")
print("- Use json/csv modules for structured data")

print("\nFiles created: sample.txt, data.json, data.csv")

