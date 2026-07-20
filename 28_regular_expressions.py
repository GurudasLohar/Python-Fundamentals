# Regular Expressions (Regex) in Python

# Regular Expressions are used for pattern matching, searching, and manipulating text.

import re

print("=== Regular Expressions (Regex) - Enhanced Guide ===\n")

text = """
Contact us at support@example.com or sales@company.org.
Phone numbers: 123-456-7890, (555) 123-4567, 9876543210
Dates: 2025-07-20, 12/25/2024
"""

# 1. Basic Functions
print("=== 1. Basic Regex Functions ===")

# search() - finds first match
match = re.search(r'\S+@\S+', text)
print("First email found:", match.group() if match else "None")

# findall() - finds all matches
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print("All emails     :", emails)

phones = re.findall(r'\d{3}-\d{3}-\d{4}|\(\d{3}\)\s?\d{3}-\d{4}', text)
print("Phone numbers  :", phones)

# 2. Common Patterns
print("\n=== 2. Common Regex Patterns ===")

patterns = {
    "Email"         : r'[\w\.-]+@[\w\.-]+',
    "Phone (basic)" : r'\d{3}-\d{3}-\d{4}',
    "Date (YYYY-MM-DD)": r'\d{4}-\d{2}-\d{2}',
    "URL"           : r'https?://[\w\.-]+',
    "Word"          : r'\b\w+\b',
}

for name, pattern in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{name:15}: {matches}")

# 3. Character Classes & Quantifiers
print("\n=== 3. Character Classes & Quantifiers ===")

sample = "abc123 def456 xyz789"

print("Digits          :", re.findall(r'\d+', sample))
print("Non-digits      :", re.findall(r'\D+', sample))
print("Word characters :", re.findall(r'\w+', sample))
print("Exactly 3 digits:", re.findall(r'\b\d{3}\b', sample))

# 4. Groups & Named Groups
print("\n=== 4. Grouping ===")

date_str = "2025-07-20"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
if match:
    print("Year :", match.group(1))
    print("Month:", match.group(2))
    print("Day  :", match.group(3))

# Named groups
match = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', date_str)
if match:
    print("Named groups:", match.groupdict())

# 5. Substitution (replace)
print("\n=== 5. Substitution ===")
email_text = "Contact support@oldcompany.com"
new_text = re.sub(r'[\w\.-]+@[\w\.-]+', 'new@company.com', email_text)
print("After replacement:", new_text)

# 6. Flags
print("\n=== 6. Flags ===")
text_case = "Python python PYTHON"
print("Case-sensitive  :", re.findall(r'python', text_case))
print("Case-insensitive:", re.findall(r'python', text_case, re.IGNORECASE))

# 7. Best Practices
print("\n=== Best Practices ===")
print("""
1. Use raw strings (r'pattern') to avoid escaping issues
2. Compile patterns if using them multiple times: re.compile()
3. Be specific with patterns (avoid .*)
4. Use online tools like regex101.com for testing
5. Consider readability vs complexity
""")

print("\n=== Regular Expressions are extremely powerful for text processing! ===")
print("Use them wisely — sometimes simple string methods are better.")