# Strings and String Methods

# Strings are immutable sequences of Unicode characters

s = "  Hello, Python Programming!  "

print("=== Original String ===")
print(repr(s))  # Shows whitespace
print(f"Length: {len(s)}")

# 1. Case Conversion
print("\n=== Case Conversion ===")
print("upper()     :", s.upper())
print("lower()     :", s.lower())
print("title()     :", s.title())
print("capitalize():", s.capitalize())
print("swapcase()  :", s.swapcase())

# 2. Stripping Whitespace
print("\n=== Stripping ===")
print("strip()     :", repr(s.strip()))
print("lstrip()    :", repr(s.lstrip()))
print("rstrip()    :", repr(s.rstrip()))

# 3. Searching & Checking
text = "Python is powerful and Python is popular"

print("\n=== Searching & Checking ===")
print("find('Python')     :", text.find("Python"))
print("find('Java')       :", text.find("Java"))        # -1 if not found
print("count('Python')    :", text.count("Python"))
print("startswith('Py')   :", text.startswith("Py"))
print("endswith('ar')     :", text.endswith("ar"))
print("'is' in text       :", "is" in text)

# 4. Replacing & Splitting
print("\n=== Replacing & Splitting ===")
print("replace()   :", text.replace("Python", "Java", 1))  # Replace once
print("split()     :", text.split())                     # On whitespace
print("split(',')  :", "apple,banana,cherry".split(","))

# 5. Joining
print("\n=== Joining ===")
words = ["Python", "is", "awesome"]
print("join()      :", " ".join(words))
print("-".join(words))

# 6. Alignment & Formatting
print("\n=== Alignment ===")
print("center(30)  :", repr("Python".center(30, "*")))
print("ljust(30)   :", "Python".ljust(30, "-"))
print("rjust(30)   :", "Python".rjust(30, "-"))

# 7. Character Type Checks
print("\n=== Character Checks ===")
print("123".isdigit())      # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True
print("hello".islower())    # True
print("   ".isspace())      # True

# 8. Modern Formatting
print("\n=== f-strings & Formatting ===")
name = "Developer"
age = 25
score = 98.75

print(f"Hello, {name}! You are {age} years old.")
print(f"Score: {score:.2f}")                    # 2 decimal places
print("Name: {}, Age: {}, Score: {:.1f}".format(name, age, score))

# Bonus: String Slicing
print("\n=== Slicing Examples ===")
lang = "Python"
print(lang[0:2])    # 'Py'
print(lang[-3:])    # 'hon'
print(lang[::-1])   # Reverse: 'nohtyP'

print("\n=== All done! Strings are powerful in Python ===")