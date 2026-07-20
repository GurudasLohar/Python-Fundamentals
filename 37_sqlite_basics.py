# SQLite Database in Python

# SQLite is a lightweight, serverless, embedded SQL database engine.

import sqlite3
import os

print("=== SQLite Database Basics - Enhanced Guide ===\n")

# 1. Connect to Database
print("=== 1. Creating/Connecting to Database ===")

# Connect (creates the file if it doesn't exist)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

print("Connected to SQLite database.")

# 2. Create Table
print("\n=== 2. Creating Tables ===")

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    salary REAL,
    hire_date TEXT
)
''')

print("Table 'employees' created or already exists.")

# 3. Insert Data
print("\n=== 3. Inserting Data ===")

employees_data = [
    ("Developer", 28, "Engineering", 75000, "2023-01-15"),
    ("Tester", 34, "Marketing", 82000, "2022-06-20"),
    ("Engineer", 25, "Engineering", 68000, "2024-03-10"),
    ("Analyst", 31, "HR", 91000, "2021-11-05")
]

cursor.executemany('''
INSERT INTO employees (name, age, department, salary, hire_date)
VALUES (?, ?, ?, ?, ?)
''', employees_data)

conn.commit()
print(f"Inserted {len(employees_data)} records.")

# 4. Querying Data
print("\n=== 4. Querying Data ===")

# Select all
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Query with conditions
print("\nEmployees in Engineering:")
cursor.execute("SELECT name, salary FROM employees WHERE department = ?", ("Engineering",))
for row in cursor.fetchall():
    print(row)

# Aggregate queries
cursor.execute("SELECT COUNT(*), AVG(salary) FROM employees")
count, avg_salary = cursor.fetchone()
print(f"Total employees: {count}, Average salary: ${avg_salary:.2f}")

# 5. Updating & Deleting
print("\n=== 5. Update & Delete ===")

# Update
cursor.execute("UPDATE employees SET salary = salary * 1.1 WHERE department = 'Engineering'")
conn.commit()
print("Updated salaries for Engineering department.")

# Delete
cursor.execute("DELETE FROM employees WHERE age < 26")
conn.commit()
print("Deleted employees younger than 26.")

# 6. Best Practices
print("\n=== 6. Best Practices ===")
print("""
1. Always use parameterized queries (?) to prevent SQL injection
2. Commit changes explicitly
3. Close connection when done
4. Use context managers for better resource management
5. Index columns used in WHERE clauses for performance
""")

# 7. Clean up
conn.close()
print("\nDatabase connection closed.")

print("\n=== SQLite is perfect for small to medium applications and embedded use cases! ===")
print("Database file created: company.db")