# CSV Handling in Python

# CSV (Comma-Separated Values) is a common format for tabular data.

import csv
import os

print("=== CSV Handling in Python - Enhanced Guide ===\n")

# 1. Writing CSV Files
print("=== 1. Writing CSV ===")

data = [
    ["Name", "Age", "City", "Salary"],
    ["Developer", 28, "New Delhi", 75000],
    ["Tester", 34, "Mumbai", 82000],
    ["Engineer", 25, "Chennai", 68000],
    ["Analyst", 31, "Bangalore", 91000]
]

with open("employees.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV file 'employees.csv' written successfully.")

# 2. Reading CSV Files
print("\n=== 2. Reading CSV ===")

with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 3. Using DictReader / DictWriter
print("\n=== 3. DictReader & DictWriter ===")

# Reading as dictionaries
with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Name: {row['Name']}, City: {row['City']}, Salary: {row['Salary']}")

# Writing using DictWriter
fieldnames = ["Name", "Department", "Score"]
new_data = [
    {"Name": "Eve", "Department": "HR", "Score": 95},
    {"Name": "Frank", "Department": "IT", "Score": 88}
]

with open("performance.csv", "w", newline='', encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_data)

print("performance.csv written using DictWriter.")

# 4. Advanced: Handling Large Files & Different Delimiters
print("\n=== 4. Advanced CSV Features ===")

# Reading large files line by line
print("Reading first few rows efficiently:")
with open("employees.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i >= 3:
            break
        print(row)

# Using different delimiters (e.g., tab-separated)
print("\nNote: You can use delimiter='\\t' for TSV files.")

# 5. Best Practices
print("\n=== 5. Best Practices ===")
print("""
1. Always use newline='' when opening CSV files
2. Specify encoding='utf-8'
3. Use DictReader/DictWriter for better readability
4. Handle large files with streaming (avoid loading everything into memory)
5. Validate data before writing
""")

print("\n=== CSV is widely used for data export/import in business and analytics! ===")
print("Files created: employees.csv, performance.csv")